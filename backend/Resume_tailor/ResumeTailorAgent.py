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
        self.give_instructions('/workspaces/apply.ai/backend/Resume_tailor/instructions.txt')
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


