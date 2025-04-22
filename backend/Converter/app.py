from flask import Flask, request, send_file, jsonify
import os
import subprocess
import tempfile

app = Flask(__name__)

@app.route('/compile', methods=['POST'])
def compile_latex():
    try:
        # Get LaTeX code from the request payload
        latex_code = request.json.get('latex_code')
        if not latex_code:
            return jsonify({"error": "No LaTeX code provided"}), 400

        # Create a temporary directory to store the .tex and .pdf files
        with tempfile.TemporaryDirectory() as temp_dir:
            tex_file_path = os.path.join(temp_dir, "document.tex")
            pdf_file_path = os.path.join(temp_dir, "document.pdf")

            # Write the LaTeX code to a .tex file
            with open(tex_file_path, 'w') as tex_file:
                tex_file.write(latex_code)

            # Run pdflatex to compile the .tex file into a PDF
            result = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "-output-directory", temp_dir, tex_file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            # Check if the compilation was successful
            if result.returncode != 0:
                return jsonify({
                    "error": "Failed to compile LaTeX",
                    "details": result.stderr.decode()
                }), 500

            # Log warnings (if any) for debugging purposes
            warnings = result.stderr.decode()
            if warnings:
                print("Warnings during compilation:", warnings)

            # Send the generated PDF as a response
            return send_file(pdf_file_path, as_attachment=True, download_name="document.pdf")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)