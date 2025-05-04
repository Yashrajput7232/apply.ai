import json
# from pylatex import Document
import os
import json
import subprocess
class Utility:

    @staticmethod
    def fileReader(file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"No such file: '{file_path}'")
        with open(file_path,'r',encoding='utf-8') as file:
            return file.read()
        
    @staticmethod
    def filewriterlatex(file_path,content):
        with open(file_path,'w',encoding='utf-8') as file:
            file.write(content) 
    
#     @staticmethod
#     def fileWriter(file_path, content):
#         if isinstance(content, str):
#             if content.strip().startswith('```json'):
#                 content=content.strip()[7:].lstrip()
#             if content.strip().endswith('```'):
#                 content=content.strip()[:-3].rstrip()
#             try:
#                 content=json.loads(content)
#             except json.JSONDecodeError:
#                 pass
        
#         with open(file_path, 'w', encoding='utf-8') as file:
#             if isinstance(content, str):
#             # Write as plain text
#                 file.write(content)
#             else:
#                 json.dump(content, file, ensure_ascii=False, indent=4)
#         return f'File written successfully: {file_path}'
    
#     @staticmethod
#     def latex_to_pdf1(tex_file_path):
#         os.system(f"pdflatex {tex_file_path}")
#         content = Utility.fileReader(tex_file_path)
#         content=json.loads(content)
#         latexCode=content['LatexCode']['latex_code']
#         with open("resume.tex", "w", encoding="utf-8") as f:
#             f.write(latexCode)
        
#         try:
#             subprocess.run(["pdflatex", "resume.tex"])
#             print ('PDF generated successfully: {tex_file_path[:-4]}.pdf')
#         except subprocess.CalledProcessError:
#             print ('pdflatex not found. Please install pdflatex')
#         except FileNotFoundError:
#             print(" File not found")

#     # @staticmethod
# import json
# import re

# def fix_latex_json(file_path, output_path=None):
#     if output_path is None:
#         output_path = file_path
        
#     print(f"Reading file: {file_path}")
    
#     # Read the raw content
#     with open(file_path, 'r', encoding='utf-8') as f:
#         content = f.read()
    
#     # First, check if it's valid JSON already
#     try:
#         json_data = json.loads(content)
#         print("JSON already valid. No fixing needed.")
#         return json_data
#     except json.JSONDecodeError:
#         print("Invalid JSON. Attempting to fix...")
    
#     # Extract the LaTeX part for targeted fixing
#     latex_match = re.search(r'"LatexCode"\s*:\s*"(.*?)"', content, re.DOTALL)
#     if not latex_match:
#         print("Could not find LaTeX code section in JSON")
#         return
        
#     latex_code = latex_match.group(1)
    
#     # Fix the escaping in the LaTeX code
#     fixed_latex = latex_code.replace('\\', '\\\\')  # Double all backslashes
#     fixed_latex = fixed_latex.replace('\\"', '\\\\"')  # Fix quotes that might be already escaped
    
#     # Replace the LaTeX part in the original JSON
#     fixed_content = content.replace(latex_match.group(1), fixed_latex)
    
#     # Verify it's now valid JSON
#     try:
#         json_data = json.loads(fixed_content)
#         print("JSON successfully fixed!")
        
#         # Write the fixed content
#         with open(output_path, 'w', encoding='utf-8') as f:
#             json.dump(json_data, f, ensure_ascii=False, indent=4)
#         print(f"Fixed JSON saved to: {output_path}")
        
#         return json_data
#     except json.JSONDecodeError as e:
#         print(f"Still invalid JSON after fixing: {e}")
#         return None
# import json
# import re

# def extract_latex(file_path, output_tex_path="resume.tex"):
#     try:
#         # First try reading as valid JSON
#         with open(file_path, 'r', encoding='utf-8') as f:
#             try:
#                 data = json.load(f)
#                 latex_code = data.get("LatexCode")
                
#                 if isinstance(latex_code, str):
#                     print("Successfully extracted LaTeX from JSON!")
#                 else:
#                     print("LaTeX code not found in valid format")
#                     return
#             except json.JSONDecodeError:
#                 # If JSON is invalid, try regex to extract
#                 print("JSON invalid, trying regex extraction...")
#                 content = f.read()
#                 match = re.search(r'"LatexCode"\s*:\s*"(.*?)",\s*"', content, re.DOTALL)
                
#                 if not match:
#                     print("Could not extract LaTeX code")
#                     return
                    
#                 # Extract and unescape the LaTeX code
#                 latex_code = match.group(1)
#                 latex_code = latex_code.replace('\\n', '\n')  # Convert \n literals to actual newlines
#                 latex_code = latex_code.replace('\\t', '\t')  # Convert \t literals to actual tabs
                
#                 # Fix other escapes as needed
#                 latex_code = re.sub(r'\\\\([^\\])', r'\\\1', latex_code)
                
#         # Write LaTeX to .tex file
#         with open(output_tex_path, 'w', encoding='utf-8') as f:
#             f.write(latex_code)
            
#         print(f"LaTeX code saved to {output_tex_path}")
#         return latex_code
        
#     except Exception as e:
#         print(f"Error extracting LaTeX: {e}")

# # Extract the LaTeX code
# extract_latex("files/TailoredResume.json", "files/resume.tex")
# # Run the fix
# if __name__ == "__main__":
#     # fix_latex_json("files/TailoredResume.json", "files/TailoredResume_fixed.json")
#     # json_data = Utility.fileReader("files/TailoredResume_fixed.json")
#     # print(json_data)
#     # with open('files/output.tex', 'w', encoding='utf-8') as f:
#     #     f.write(json_data['LatexCode'])
#     extract_latex("files/TailoredResume_fixed.json", "files/resume.tex")
    

# # Fix the file path - use forward slashes
# # Utility.latex_to_pdf("files/TailoredResume.json", "files/TailoredResume.pdf")



# # Utility.latex_to_pdf("files\TailoredResume.json")