from fpdf import FPDF
from dotenv import load_dotenv 
import os
import sys
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add backend to sys.path

load_dotenv('applicaton.properties')
from AI_Engiene import AIEngine as Agent
# import AI_Engiene.AIEngine as Agent


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, ListFlowable, ListItem
def text_to_pdf(text, output_filename="cover_letter.pdf"):
    import re
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Custom styles
    normal_style = styles["Normal"]
    bold_style = ParagraphStyle("BoldStyle", parent=normal_style, fontName="Helvetica-Bold", fontSize=12)
    heading_style = ParagraphStyle("HeadingStyle", parent=normal_style, fontName="Helvetica-Bold", 
                                  fontSize=14, spaceAfter=10)
    
    elements = []
    lines = text.strip().split("\n")
    
    # Process line by line
    skip_lines = 0
    for i, line in enumerate(lines):
        if skip_lines > 0:
            skip_lines -= 1
            continue
            
        line = line.strip()
        
        # Empty line - add spacer
        if not line:
            elements.append(Spacer(1, 8))
            
        # Full line bolding - headings (line is entirely bold)
        elif re.match(r'^\*\*.*\*\*$', line) or re.match(r'^__.*__$', line):
            # Remove the bold markers
            clean_text = re.sub(r'^\*\*|\*\*$|^__|__$', '', line)
            elements.append(Paragraph(clean_text, heading_style))
            
        # Bullet points
        elif line.startswith("* ") or line.startswith("- "):
            bullet_points = []
            current_idx = i
            
            # Collect all consecutive bullet points
            while current_idx < len(lines) and (lines[current_idx].strip().startswith("* ") or 
                                              lines[current_idx].strip().startswith("- ")):
                bullet_text = lines[current_idx].strip()[2:]
                # Process inline bold in bullet points
                bullet_text = process_inline_formatting(bullet_text)
                bullet_points.append(ListItem(Paragraph(bullet_text, normal_style), bulletColor=colors.black))
                current_idx += 1
            
            skip_lines = current_idx - i - 1
            elements.append(ListFlowable(bullet_points, bulletType="bullet"))
            
        # Normal text with possible inline formatting
        else:
            # Process inline bold text using regex
            formatted_line = process_inline_formatting(line)
            elements.append(Paragraph(formatted_line, normal_style))
    
    doc.build(elements)
    print(f"✅ PDF Generated: {output_filename}")

def process_inline_formatting(text):
    """Process inline formatting like bold, italic, etc."""
    import re
    
    # Replace **bold text** with <b>bold text</b>
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    
    # Replace __bold text__ with <b>bold text</b> (alternative syntax)
    text = re.sub(r'__(.*?)__', r'<b>\1</b>', text)
    
    # Replace *italic text* with <i>italic text</i>
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    
    # Replace _italic text_ with <i>italic text</i> (alternative syntax)
    text = re.sub(r'_(.*?)_', r'<i>\1</i>', text)
    
    return text

def generate_cover_letter(job_description,resume):
    # Create a new agent
    agent = Agent.AIEngine("Coverletter agent")
    # Generate a cover letter
    agent.store_memory('job_description', job_description)
    agent.store_memory('resume', resume)
    agent.store_memory('instructions',os.getenv('instructions'))

    cover_letter = agent.generate_content(agent.retrieve_memory('instructions')+agent.retrieve_memory('job_description') + agent.retrieve_memory('resume'))   

    return cover_letter


jobdescription = os.getenv('jobDescription')
resume= os.getenv('resume')
coverletter= os.getenv('coverLetter')
# print(jobdescription)

cover_letter=generate_cover_letter(jobdescription,resume)
# print(cover_letter) 

text_to_pdf(cover_letter, "cover_letter.pdf")
# text_to_pdf(cover_letter, "cover_letter.pdf")

# generate_cover_letter()