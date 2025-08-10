# import requests
# from flask import Flask, request, jsonify, send_file
# from ResumeTailorAgent import ResumeTailorAgent
# import tempfile

# app = Flask(__name__)
# resume_tailor_agent = ResumeTailorAgent()


# @app.route('/generate_tailored_resume', methods=['POST'])
# def generate_tailored_resume():
#     try:
#         job_description = request.json.get('job_description')
#         resume = request.json.get('resume')

#         if not job_description or not resume:
#             return jsonify({'error': 'job_description and resume are required'}), 400

#         resume_tailor_agent.store_memory('job_description', job_description)
#         resume_tailor_agent.store_memory('resume', resume)

#         # Try up to 2 attempts: original, then fix if error
#         for attempt in range(2):
#             tailored_resume_path = resume_tailor_agent.generate_tailored_resume()
#             if not tailored_resume_path:
#                 return jsonify({'error': 'Failed to generate tailored resume'}), 500

#             with open(tailored_resume_path, 'r', encoding='utf-8') as file:
#                 tailored_resume = file.read()
#                 response = requests.post(
#                     'https://latex-api-xx5f.onrender.com/compile',
#                     json={'latex_code': tailored_resume},
#                     headers={'Content-Type': 'application/json'}
#                 )
#             # Check if the response is a PDF or an error
#             print(response)
#             # If PDF generation is successful, return the PDF
#             if response.status_code == 200 and response.headers.get('Content-Type', '').startswith('application/pdf'):
#                 with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
#                     temp_pdf.write(response.content)
#                     temp_pdf_path = temp_pdf.name
#                 return send_file(temp_pdf_path, as_attachment=True, download_name="tailored_resume.pdf")

#             # If first attempt failed, ask LLM to fix LaTeX and retry
#             if attempt == 0:
#                 error_message = response.json().get('error', response.text)
#                 # Call LLM to fix LaTeX (assume a method exists)
#                 fixed_latex = resume_tailor_agent.fix_latex_with_llm(tailored_resume, error_message)
#                 # Overwrite the LaTeX file with the fixed version
#                 with open(tailored_resume_path, 'w', encoding='utf-8') as file:
#                     file.write(fixed_latex)
#             else:
#                 # On second failure, return error details
#                 return jsonify({
#                     'error': 'Failed to compile LaTeX after retry',
#                     'details': response.json() if response.headers.get('Content-Type') == 'application/json' else response.text
#                 }), 500

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)



import requests
import os
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from ResumeTailorAgent import ResumeTailorAgent
import tempfile
import io
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

resume_tailor_agent = ResumeTailorAgent()


@app.route('/generate_tailored_resume', methods=['POST'])
def generate_tailored_resume():
    try:
        job_description = request.json.get('job_description')
        resume = request.json.get('resume')

        if not job_description or not resume:
            return jsonify({'error': 'job_description and resume are required'}), 400

        # Store inputs in memory for the agent
        resume_tailor_agent.store_memory('job_description', job_description)
        resume_tailor_agent.store_memory('resume', resume)

        # Generate initial LaTeX code
        tailored_resume_path = resume_tailor_agent.generate_tailored_resume()
        if not tailored_resume_path:
            return jsonify({'error': 'Failed to generate tailored resume'}), 500

        with open(tailored_resume_path, 'r', encoding='utf-8') as file:
            latex_code = file.read()

        # Try compiling up to 2 times (original, then fixed)
        for attempt in range(2):
            response = requests.post(
                'https://latex-api-xx5f.onrender.com/compile',
                json={'latex_code': latex_code},
                headers={'Content-Type': 'application/json'}
            )

            # If PDF generation is successful, return it
            if response.status_code == 200 and response.headers.get('Content-Type', '').startswith('application/pdf'):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                    temp_pdf.write(response.content)
                    temp_pdf_path = temp_pdf.name
                return send_file(temp_pdf_path, as_attachment=True, download_name="tailored_resume.pdf")

            # On first failure, fix LaTeX with LLM and retry
            if attempt == 0:
                try:
                    error_message = response.json().get('error', response.text)
                except ValueError:
                    error_message = response.text
                latex_code = resume_tailor_agent.fix_latex_with_llm(latex_code, error_message)
            else:
                # Second failure — return error details
                try:
                    details = response.json() if response.headers.get('Content-Type', '').startswith('application/json') else response.text
                except ValueError:
                    details = response.text
                return jsonify({
                    'error': 'Failed to compile LaTeX after retry',
                    'details': details
                }), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate_cover_letter', methods=['POST'])
def generate_cover_letter():
    try:
        job_description = request.json.get('job_description')
        resume = request.json.get('resume')

        if not job_description or not resume:
            return jsonify({'error': 'job_description and resume are required'}), 400

        # Step 1: Generate cover letter LaTeX file
        tex_file_path = resume_tailor_agent.call_llm_for_cover_letter(job_description, resume)

        # Step 2: Read LaTeX content from file
        with open(tex_file_path, 'r', encoding='utf-8') as f:
            latex_code = f.read()

        # Step 3: Compile LaTeX to PDF (max 2 attempts)
        for attempt in range(2):
            response = requests.post(
                'https://latex-api-xx5f.onrender.com/compile',
                json={'latex_code': latex_code},
                headers={'Content-Type': 'application/json'}
            )

            if response.status_code == 200 and response.headers.get('Content-Type', '').startswith('application/pdf'):
                # Save PDF to temp file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                    temp_pdf.write(response.content)
                    temp_pdf_path = temp_pdf.name
                return send_file(temp_pdf_path, as_attachment=True, download_name="cover_letter.pdf")

            # Retry with fixed LaTeX if first attempt fails
            if attempt == 0:
                try:
                    error_message = response.json().get('error', response.text)
                except ValueError:
                    error_message = response.text
                latex_code = resume_tailor_agent.fix_latex_with_llm(latex_code, error_message)
            else:
                try:
                    details = response.json() if response.headers.get('Content-Type', '').startswith('application/json') else response.text
                except ValueError:
                    details = response.text
                return jsonify({
                    'error': 'Failed to compile LaTeX after retry',
                    'details': details
                }), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
