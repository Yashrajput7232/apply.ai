from flask import Flask, request, jsonify
from Resume_tailor.ResumeTailorAgent import ResumeTailorAgent

app = Flask(__name__)
resume_tailor_agent = ResumeTailorAgent()

@app.route('/upload_resume', methods=['POST'])
def upload_resume():
    try:
        resume_path = request.json.get('resume_path')
        if not resume_path:
            return jsonify({'error': 'resume_path is required'}), 400
        response = resume_tailor_agent.read_resume(resume_path)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/upload_job_description', methods=['POST'])
def upload_job_description():
    try:
        job_description_path = request.json.get('job_description_path')
        if not job_description_path:
            return jsonify({'error': 'job_description_path is required'}), 400
        response = resume_tailor_agent.read_job_description(job_description_path)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate_tailored_resume', methods=['GET'])
def generate_tailored_resume():
    try:
        tailored_resume = resume_tailor_agent.generate_tailored_resume()
        return jsonify({'tailored_resume': tailored_resume}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)