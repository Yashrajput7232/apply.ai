from flask import Flask, request, send_file, jsonify
import os
import subprocess
import tempfile
from PyPDF2 import PdfReader

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route('/compile', methods=['POST'])
def compile_latex():
    try:
        latex_code = request.json.get('latex_code')
        if not latex_code:
            return jsonify({"error": "No LaTeX code provided"}), 400

        with tempfile.TemporaryDirectory() as temp_dir:
            tex_file_path = os.path.join(temp_dir, "document.tex")
            pdf_file_path = os.path.join(temp_dir, "document.pdf")
            log_file_path = os.path.join(temp_dir, "document.log")

            # Write LaTeX code to file
            with open(tex_file_path, 'w', encoding='utf-8') as tex_file:
                tex_file.write(latex_code)

            # Run pdflatex using TeX Live
            result = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "-output-directory", temp_dir, tex_file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result.returncode != 0:
                # Try to get log content
                log_content = ""
                if os.path.exists(log_file_path):
                    with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as log_file:
                        log_content = log_file.read()
                return jsonify({
                    "error": "LaTeX compilation failed",
                    "stdout": result.stdout.decode(errors="ignore"),
                    "stderr": result.stderr.decode(errors="ignore"),
                    "log": log_content
                }), 500

            return send_file(pdf_file_path, as_attachment=True, download_name="document.pdf")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/extract-text', methods=['POST'])
def extract_text_from_pdf():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400

        pdf_file = request.files['file']

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            pdf_file.save(temp_pdf.name)
            temp_pdf_path = temp_pdf.name

        reader = PdfReader(temp_pdf_path)
        extracted_text = ""
        for page in reader.pages:
            extracted_text += page.extract_text() + "\n"

        os.remove(temp_pdf_path)

        return jsonify({"text": extracted_text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
