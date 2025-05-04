import requests
from flask import Flask, request, jsonify, send_file
from ResumeTailorAgent import ResumeTailorAgent
import tempfile
import os

app = Flask(__name__)
resume_tailor_agent = ResumeTailorAgent()

@app.route('/generate_tailored_resume', methods=['POST'])
def generate_tailored_resume():
    try:
        # Get job description and instructions from the request payload
        job_description = request.json.get('job_description')
        resume = request.json.get('resume')

        if not job_description or not resume:
            return jsonify({'error': 'job_description and resume are required'}), 400

        # Store job description and instructions in memory
        resume_tailor_agent.store_memory('job_description', job_description)
        resume_tailor_agent.store_memory('resume', resume)

        # Generate the tailored LaTeX resume
        tailored_resume_path = resume_tailor_agent.generate_tailored_resume()
        if not tailored_resume_path:
            return jsonify({'error': 'Failed to generate tailored resume'}), 500
        
        # Read the tailored LaTeX resume from the file
        with open(tailored_resume_path, 'r', encoding='utf-8') as file:
            tailored_resume = file.read()
            response = requests.post(
                'https://latex-api-xx5f.onrender.com/compile',
                json={'latex_code': tailored_resume},
                headers={'Content-Type': 'application/json'}
            )

            # if response.status_code != 200:
            #     return jsonify({
            #         'error': 'Failed to compile LaTeX',
            #         'details': response.json() if response.headers.get('Content-Type') == 'application/json' else response.text
            #     }), 500

            # Save the compiled PDF to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                temp_pdf.write(response.content)
                temp_pdf_path = temp_pdf.name

            # Send the compiled PDF as a downloadable response
            return send_file(temp_pdf_path, as_attachment=True, download_name="tailored_resume.pdf")

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    # finally:
    #     # Clean up the temporary file if it exists
    #     if 'temp_pdf_path' in locals() and os.path.exists(temp_pdf_path):
    #         os.remove(temp_pdf_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)