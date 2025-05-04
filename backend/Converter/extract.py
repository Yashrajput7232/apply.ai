import requests

# Define the API endpoint
url = "http://localhost:6000/extract-text"

# Path to the PDF file
pdf_file_path = "/workspaces/apply.ai/backend/Converter/output.pdf"

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