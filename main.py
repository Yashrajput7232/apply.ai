from flask import Flask, request, jsonify
import os ,sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Resume-Talior')))
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Cover-letter-email-generator')))

from backend.Resume_tailor.ResumeTailorAgent import ResumeTailorAgent
import  backend.Cover_letter_email_generator.agent as Coverletter_agent

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_documents():
    try:
        data = request.get_json()
        if not data or 'job_description' not in data or 'resume_path' not in data:
            return jsonify({"error": "Invalid input. Provide 'job_description' and 'resume_path'."}), 400

        job_description = data['job_description']
        resume_path = data['resume_path']

        # Generate tailored resume
        resume_agent = ResumeTailorAgent()
        resume_agent.read_resume(resume_path)
        resume_agent.store_memory('job_description', job_description)
        tailored_resume = resume_agent.generate_tailored_resume()

        # Generate tailored cover letter
        tailored_cover_letter = Coverletter_agent.generate_cover_letter(job_description, resume_agent.retrieve_memory('resume'))

        return jsonify({
            "resume": tailored_resume,
            "cover_letter": tailored_cover_letter
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)