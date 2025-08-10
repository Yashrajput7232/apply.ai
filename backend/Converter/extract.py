import requests

# Define the API endpoint
url = "https://latex-pdf-compiler.onrender.com/extract-text"

# Path to the PDF file
# pdf_file_path = "output.pdf"
pdf_file_path = "backend/Resume_tailor/TEST Resume.pdf"

# Make the POST request
with open(pdf_file_path, "rb") as pdf_file:
    files = {"file": pdf_file}
    response = requests.post(url, files=files)

# Check the response
if response.status_code == 200:
    print("Extracted Text:")
    print(response.json()["text"])
else:
    print(f"Failed to extract text. Status code: {response.status_code}")
    print("Response:", response.json())