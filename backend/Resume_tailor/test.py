import requests

# Define the API endpoint
url = "https://resumetailor-0b6a.onrender.com/generate_tailored_resume"

# Sample payload
payload = {
    "job_description": """ Job Description
At Visa, the Finance Technology organization enables Visa's revenue growth through flexible rule-based pricing engines and global revenue platforms built on next-generation technologies. This includes managing system requirements, evaluating cutting-edge technologies, design, development, integration, quality assurance, implementation, and maintenance of corporate revenue applications.

The candidate will work on developing and implementing applications that improve the effectiveness and efficiency of the Finance business function. The candidate should enjoy working on diverse technologies and should be excited to take initiatives to solve complex business problems and get the job done while taking on new challenges. You should thrive in team-oriented and fast-paced environments where each team-member is vital to the overall success of the projects.

Responsibilities

Build/Code applications using a variety of frontend and backend technologies.

Experience with the software development lifecycle, including version control, build processes, testing, and code release.

Writing test cases using tools like JUnit and performing testing to ensure applications are running as expected.

Maintaining and enhancing applications after deployment.

Design and build applications with high level of scalability, resiliency, and monitoring.

Stay abreast of emerging technologies and proactively assess and evaluate the adoption thereof into the organization.

Develop proofs of concept to validate ideas, facilitating the choice of the most effective solution approach.

Work with limited direction, usually within a complex environment, to drive delivery of solutions and meet service levels

Must be self-motivated with ability to work in a fast-paced agile delivery model.

With active engagement, collaboration, effective communication, quality, integrity and reliable delivery, develop and maintain a trusted and valued relationship with the team, customers and technology partners.

This is a hybrid position. Expectation of days in office will be confirmed by your hiring manager.

Qualifications
Basic Qualification
•Bachelor's degree in a Computer Science or other Engineering discipline.

Preferred Qualification
• 0.6- 1.6 years of work experience in technology industry with coding and testing skills.
· Strong technical competency and experience with web applications, web services, Java, JavaScript, J2EE, XML, unit-testing, shell-scripting and RDBMS is a plus.
· Experience with Cassandra/solr/nosql experience as a plus.
· Continuous Integration, Code/Test coverage working in different methodologies is a plus.
· Must have proactive and strong communications to work well across teams.
•Ability to work in a complex organization to determine business and customer
needs, providing the best solution to meet those needs.
•Strong teamwork focus and the ability to foster collaboration within and across
teams.
•Passionate about learning and applying new technologies and take pride in
delivering working software.
Please dont mess up with the formatting of the resume.
""",
# "resume": r"""
# \documentclass[a4paper,10.8pt]{article}
# \usepackage{geometry}
# \geometry{margin=0.37in}
# \usepackage{titlesec}
# \usepackage{enumitem}
# \usepackage[colorlinks=true, urlcolor=blue]{hyperref}

# \setlist[itemize]{noitemsep, topsep=0pt}
# \renewcommand{\baselinestretch}{1.0}
# \titlespacing*{\section}{0pt}{4pt}{2pt}
# \titlespacing*{\subsection}{0pt}{3pt}{1pt}

# \begin{document}

# \begin{center}
#     {\LARGE \textbf{YASH DILIP RAJPUT}}\\
#     \href{mailto:yashrajputO2.scoe.comp@gmail.com}{yashrajputO2.scoe.comp@gmail.com} \textbar
#     \href{https://www.linkedin.com/in/yashrajput7232}{LinkedIn} \textbar
#     \href{https://github.com/yashrajput7232}{GitHub} \textbar
#     \href{tel:+916281110280}{+91-6281110280}
# \end{center}

# \hrule
# \vspace{3pt}
# \section*{Summary}  
# Backend Developer with strong proficiency in \textbf{Java, Python, C++, and Go}, with over 1 year of experience building and optimizing \textbf{high-performance, scalable backend systems and APIs}. Skilled in \textbf{Object-Oriented Design, Algorithms, and Designing Large Scale Data-Intensive Applications}. Delivered impact in \textbf{FinTech systems} at BNY Mellon, integrating \textbf{Generative AI} for automation and efficiency. Comfortable in \textbf{agile environments}, with strong communication and problem-solving skills, passionate about delivering client-centric, robust solutions.

# \vspace{3 pt}
# \hrule
# \vspace{3pt}

# \section*{Education}
# \textbf{Bachelor of Engineering (B.E.) - Computer Engineering} \hfill \textbf{2024} \\
# \textbf{Pune University, Pune} \hfill \textbf{CGPA: 9.30/10}
# \vspace{3pt}

# \hrule
# \vspace{3 pt}

# \section*{Technical Skills}
# \textbf{Programming}: Java, Python, C++, Go \textbar \space
# \textbf{Backend}: Spring Boot, Flask, Django \textbar \space
# \textbf{Frontend}: React, HTML, CSS \textbar \space
# \textbf{DevOps-Cloud}: AWS (EKS, Lambda, S3), Terraform, Kubernetes, Docker \textbar \space
# \textbf{Databases}: MongoDB (NoSQL), Oracle, MySQL (SQL) \textbar \space
# \textbf{Tools-Others}: Gen AI, Git, Kafka, Redis, Bash, JSON, Grafana
# \vspace{3}

# \hrule
# \vspace{3pt}

# \section*{Work Experience}

# \textbf{BNY Mellon - Software Engineer} \hfill Jul 2024 -- Present\\
# \textbf{Key Skills}: \textbf{Java, Spring Boot, Python, Backend, SQL, Gen AI, RAG, LangChain, Git, Docker, Kubernetes, Agile}
# \begin{itemize}
#     \item Designed and implemented scalable \textbf{backend infrastructure and REST APIs} using \textbf{Java Spring Boot} for \textbf{regulatory FinTech applications}, reducing reporting errors by 50\%.
#     \item Developed \textbf{agentic - AI multi-threaded onboarding tools} using Generative AI, improving automation and reducing fund setup time by 90\%.
#     \item Built an \textbf{AI-powered} \textbf{production issue remediation system} analyzing logs and metadata to suggest fixes, improving resolution time by 70\%.
#     \item Followed \textbf{CI/CD best practices} with \textbf{GitLab, Docker, Kubernetes}; ensured reliable, secure deployments in an \textbf{agile environment}.
#     \item Collaborated across global teams including product and business, aligning solutions to user requirements and regulatory needs.
# \end{itemize}
# \vspace{3 pt}
# \textbf{BNY Mellon - SDE Intern} \hfill Jan 2024 -- Jun 2024\\
# \textbf{Key Skills}: Java, Spring Boot, Spring MVC, REST APIs, Kafka, Redis, CI/CD, Docker, GitLab, Agile
# \begin{itemize}
#     \item Developed and maintained \textbf{high-performance microservices} (FAST) automating repetitive workflows for fund support teams.
#     \item Integrated \textbf{Kafka} for real-time processing and event-driven architecture.
#     \item Contributed to a real-time \textbf{fund monitoring dashboard with chatbot interface} trained on internal knowledge base.
#     \item Improved \textbf{code maintainability, scalability}, and execution time through incremental Spring Boot optimizations.
# \end{itemize}
# \vspace{3 pt}


# \hrule
# \section*{Projects}
# \textbf{AI-Powered Job Search Assistant} \hfill \href{https://carrer-ai.vercel.app/}{apply.ai} \textbar
# \href{https://github.com/Yashrajput7232/apply.ai}{GitHub} \\
# \textbf{Technologies: Python, Java, Kafka, React (Frontend), Gen AI/ML, RAG, MongoDB, ATS}
# \begin{itemize}
#     \item Developed a \textbf{distributed Kafka-based job aggregation system} in Python and Java.
#     \item Designed an AI model to \textbf{rank job listings}, increasing user match accuracy by 80\%.
#     \item Integrated \textbf{personalized cover letter generator} and \textbf{resume optimization system}, boosting response rates and ATS pass rates.
#     \item Applied best practices in \textbf{NoSQL database design}, and \textbf{microservice deployment}.
# \end{itemize}

# \vspace{3 pt}

# \hrule
# \vspace{3pt}

# \section*{Achievements \& Certifications}
# \begin{itemize}
#  \item \textbf{Winner of AI-Hackathon at BNY Mellon}
#     \item \textbf{Finalist - Kavach 2023 Hackathon (Government of India)}, contributed to cybersecurity solutions.
    
# \end{itemize}

# \hrule
# \vspace{3pt}

# \section*{Extracurricular Activities}
# \begin{itemize}
#     \item \textbf{Technical Blogging} on DevOps, Cloud, and Backend systems - \href{https://medium.com/@yash.7232.rajput}{Medium}.
# \end{itemize}

# \end{document}

# """,

"resume": ''' SANKET ILAKE
Full Stack Java Developer
7 0 5 7 8 9 1 1 0 6 s a n k e t . i l a k e 2 0 1 9 @ g m a i l . c o m K o l h a p u r ,  I n d i a  4 1 6 2 3 4
SUMMARY
As a future software developer, I have a solid background in Java, Spring 
MVC, Hibernate ORM, and Angular from my demanding coursework. I have 
extensive knowledge of database administration, web development, and 
monolithic and three-tier architectures. I'm excited to add my abilities to a 
vibrant team and commit to developing professionally in the tech sector.
EXPERIENCE
Java Developer
C o d e  C r a f t e r s  S e r v i c e s
01/2024  12/2024  Kolhapur, India
A Java developer role focused on full stack development and software 
solutions
Developed responsive Angular interfaces with dynamic charts and 
secured backend systems using Spring Boot, JPA/Hibernate, and JWT
based authentication
Optimized backend services and database queries, reducing response 
times and enhancing performance
Designed and documented secure APIs, ensuring seamless 
communication between frontend and backend systems
PROJECTS
JDBC Project – Online Grocery Store
An online grocery store project showcasing database management and 
efficient user interfaces
Managed database connections using JDBC for efficient data retrieval 
and updates
Secured user data with robust authentication and authorization
Built a system for managing products with categorization, pricing, 
discounts, and stock
Developed order processing, including cart, checkout, payments, and 
tracking
Improved performance with connection pooling for optimized database 
access
Spring Boot Project – Project Management System
A Project Management System implemented with Three Tier Architecture, 
focusing on user-friendly interfaces and data security
Frontend Angular): Responsive UI with dynamic charts
Backend Spring Boot): Handles business logic
Data Access Spring Boot  JPA/Hibernate): Efficient database 
interactions
Security: JWT-based authentication with Spring Security and Angular 
guards
Optimization: Enhanced performance with optimized backend services 
and queries
LANGUAGES
E n g l i s h
ProficientH i n d i
AdvancedSKILLS
C S S G i t G i t H u b H T M L
J a v a J a v a  S p r i n g J D B C
J P A J W T M V C O O P
P y t h o n R E S T S p r i n g B o o t
S p r i n g M V C H i b e r n a t e G m a i l
A n g u l a r
EDUCATION
Masters of Computer 
Application
K . I . T ’ s  I n s t i t u t e  o f  M a n a g e m e n t  
E d u c a t i o n  &  R e s e a r c h
08/2023  04/2025 
Kolhapur, India  416234
Bachelor of Computer 
Application
T h e  N e w  C o l l a g e  K o l h a p u r
08/2020  06/2023  Kolhapur, India
Junior College
C h a t e  J r .  C o l l a g e  o f  S c i e n c e
01/2018  06/2019  Kolhapur, India
KEY ACHIEVEMENTS
C e r t i f i c a t i o n s
Completed an intensive 
certification course covering end-
to-end development using Core 
Java, Spring Boot, Hibernate, 
RESTful APIs for backend, and 
HTML, CSS, JavaScript, 
Angular/React for frontend. Gained 
hands-on experience in building 
and deploying full-stack web 
applications, integrating frontend 
and backend components, 
database handling with MySQL, 
and version control using 
Git/GitHub.
www .enhancv .comPowered by•
•
•
•
•
•
•
•
•
•
•
•
•E  
G'''

}

# Make the POST request
response = requests.post(url, json=payload)

# Check the response
if response.status_code == 200:
    # Save the PDF file
    with open("tailored_resume.pdf", "wb") as f:
        f.write(response.content)
    print("Tailored resume downloaded as 'tailored_resume.pdf'.")
else:
    print(f"Failed to generate tailored resume. Status code: {response.status_code}")
    print("Response:", response.json())

