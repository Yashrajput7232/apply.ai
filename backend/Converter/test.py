import requests

# Read the LaTeX file
latex_file_path = "/workspaces/apply.ai/backend/Resume_tailor/files/TailoredResume.tex"
latex_code = ""
with open(latex_file_path, 'r') as file:
    latex_code = file.read()

# Print the LaTeX code to verify
print("LaTeX Code:")
print(latex_code)

# Define the API endpoint and payload
# url = "http://localhost:5000/compile"
url = "https://latex-api-xx5f.onrender.com/compile"
payload = {"latex_code": latex_code}

# Send the POST request
response = requests.post(url, json=payload)

# Save the PDF if the request is successful
if response.status_code == 200:
    with open("output.pdf", "wb") as pdf_file:
        pdf_file.write(response.content)
    print("PDF saved as output.pdf")
else:
    print("Error:", response.json())