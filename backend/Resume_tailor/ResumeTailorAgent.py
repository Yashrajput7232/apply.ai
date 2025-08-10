from AIEngine import AIEngine
from Utility import Utility
class ResumeTailorAgent(AIEngine):
    def __init__(self):
        super().__init__("ResumeTailor")
        self.memory = {}
        self.memory['instructions']=''''''

    def read_resume(self, resume_path ):
        print(f'Reading resume from: {resume_path}')
        resume = Utility.fileReader(resume_path)
        self.store_memory('resume', resume)
        return "Resume Stored Succesfully" 
        
    def read_job_description(self, job_description_path):
        print(f'Reading job description from: {job_description_path}')
        job_description= Utility.fileReader(job_description_path)
        self.store_memory('job_description', job_description)
        return  str(self.generate_content(job_description))


    def generate_tailored_resume(self):
        self.give_instructions('instructions.txt')
        print(f'Generating tailored resume')
        instructions = self.retrieve_memory('instructions')  # Note: plural, not singular
        job_description = self.retrieve_memory('job_description')
        resume = self.retrieve_memory('resume')
        return self.generate_content(  instructions + job_description + resume) 
    
    def give_instructions(self, instructions_path):
        print('Giving instructions')
        print(f'Reading instructions from: {instructions_path}')
        instructions=Utility.fileReader(instructions_path)
        self.store_memory('instructions', instructions)
        return "Instructions Stored Succesfully"

    # ...existing code...

    def fix_latex_with_llm(self, latex_code, error_message):
        """
        Calls the LLM to fix LaTeX code based on the error message from the compiler.
        Escapes common LaTeX special characters outside of tabular environments.
        Returns the fixed LaTeX code as a string.
        """

        import re

        # Characters to escape
        escape_map = {
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '^': r'\textasciicircum{}',
            '\\': r'\textbackslash{}',
        }

        def escape_outside_tabular(text):
            """
            Escapes special LaTeX characters only outside tabular environments.
            """
            escaped_parts = []
            last_end = 0
            # Regex to match tabular environments
            tabular_pattern = re.compile(r'\\begin\{tabular\}.*?\\end\{tabular\}', re.DOTALL)

            for match in tabular_pattern.finditer(text):
                # Escape text before the tabular
                before_tabular = text[last_end:match.start()]
                escaped_parts.append(''.join(escape_map.get(c, c) for c in before_tabular))
                # Keep the tabular content untouched
                escaped_parts.append(match.group(0))
                last_end = match.end()

            # Escape text after the last tabular
            after_tabular = text[last_end:]
            escaped_parts.append(''.join(escape_map.get(c, c) for c in after_tabular))

            return ''.join(escaped_parts)

        # Preprocess LaTeX to escape special characters outside tabular
        preprocessed_code = escape_outside_tabular(latex_code)

        # Prompt for LLM
        prompt = (
            "You are an expert LaTeX assistant. "
            "Given the following LaTeX code and the error message from the compiler, "
            "fix the LaTeX code so it compiles successfully. "
            "Do not change the formatting or structure, only fix the errors. "
            "Ensure that LaTeX special characters are escaped properly outside of tabular environments.\n\n"
            "LaTeX code:\n"
            f"{preprocessed_code}\n\n"
            "Compiler error message:\n"
            f"{error_message}\n\n"
            "Return only the fixed LaTeX code."
        )

        # Use the LLM to generate the fixed LaTeX code
        fixed_latex = self.generate_content(prompt)
        return fixed_latex
    

    

    def clean_and_validate_latex_resume(self, latex_code, original_resume_text):
        """
        Uses the LLM to ensure only sections present in the original resume are included in the LaTeX code.
        If a section (like 'Extracurricular Activities') is added by the LLM but not present in the input,
        it removes that section from the LaTeX code.
        Returns the cleaned LaTeX code and a list of removed sections. You can add sections which are present in the existing resume to make it look full of information and cover everything required.
        """
        # Compose a prompt for the LLM
        prompt = (
            "You are an expert LaTeX resume assistant. "
            "Given the following LaTeX resume code and the original resume text, "
            "remove any sections from the LaTeX code that are not present in the original resume text. "
            "Do not fabricate or invent content for sections that do not exist in the original resume. "
            "If a section is present in the LaTeX but not in the original, remove it entirely. "
            "If a section is present in the original resume, keep it and ensure it is filled with the available information. "
            "Return only the cleaned LaTeX code. "
            "LaTeX code:\n"
            f"{latex_code}\n\n"
            "Original resume text:\n"
            f"{original_resume_text}\n\n"
            "Return only the cleaned LaTeX code."
        )
        cleaned_latex = self.generate_content(prompt)
        # Optionally, you could diff the old and new code to list removed sections
        return cleaned_latex, []  # If you want to list removed sections, you can implement a diff
   


    def call_llm_for_cover_letter(self, job_description, resume_content):
        """
        Calls your LLM to create a professional cover letter.
        Replace with your actual LLM integration.
        """
        prompt = f"""
        Write a professional, concise cover letter based on the following job description and resume.
        Keep it 3–4 paragraphs, professional tone, and tailored to the role. give code in latex only

        Job Description:
        {job_description}

        Resume:
        {resume_content}
        """

        response=AIEngine.generate_content(self, prompt, model="gemini-2.0-flash")
        
        return response

    def format_cover_letter_as_latex(self, cover_letter_text):
        """
        Wraps the cover letter into a minimal LaTeX template for PDF generation.
        """
        return f"""
        \\documentclass[11pt]{{letter}}
        \\usepackage[margin=1in]{{geometry}}
        \\begin{{document}}

        {cover_letter_text}

        \\end{{document}}
        """
