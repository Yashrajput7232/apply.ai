import requests

# Define the API endpoint
url = "http://localhost:5000/generate_tailored_resume"

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
"resume": r"""
   \documentclass[a4paper,10pt]{article}
\usepackage{geometry}
\geometry{margin=0.37in}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage{hyperref}

\setlist[itemize]{noitemsep, topsep=0pt}
\renewcommand{\baselinestretch}{1.0}
\titlespacing*{\section}{0pt}{4pt}{2pt}
\titlespacing*{\subsection}{0pt}{3pt}{1pt}

\begin{document}

\begin{center}
    {\LARGE \textbf{YASH DILIP RAJPUT}}\\
    \href{mailto:yashrajput02.scoe.comp@gmail.com}{yashrajput02.scoe.comp@gmail.com} \textbar
    \href{https://www.linkedin.com/in/yashrajput7232}{LinkedIn} \textbar
    \href{https://github.com/yash7232}{GitHub} \textbar
    +91-6281110280
\end{center}

\hrule
\vspace{3pt}
\section*{Summary}  
Software Engineer with expertise in \textbf{Java, Python, and Go}, specializing in \textbf{Spring Boot, Django, and microservices architecture}. Experienced in building \textbf{scalable, cloud-native applications} and optimizing production systems. Proficient in \textbf{DevOps, Kubernetes, Terraform, and CI/CD pipelines} to streamline deployments. Demonstrated ability to improve efficiency by solving \textbf{300+ coding problems} on platforms like LeetCode and CodeChef. Skilled in leveraging \textbf{AI and automation} to enhance workflows and optimize system performance.

\vspace{3 pt}
\hrule
\vspace{3pt}

\section*{Education}
\textbf{Bachelor of Engineering (B.E.) - Computer Engineering}\\
Pune University, Pune \hfill CGPA: 9.30/10
\vspace{3 pt}
\hrule
\vspace{3 pt}

\section*{Technical Skills}
\textbf{Programming}: Java, Python, C++ \textbar \space
\textbf{Backend}: Spring Boot, Flask, Django \textbar \space
\textbf{DevOps-cloud}:AWS (EKS, Lambda, S3), Terraform, Kubernetes, Docker \textbar \space
\textbf{Databases}: MongoDB, MySQL, PostgreSQL \textbar \space
\textbf{Tools-Others}: Git, Kafka, Prometheus, Grafana
\vspace{3}

\hrule
\vspace{3pt}

\section*{Work Experience}

\textbf{Bank of New York Mellon - Analyst} \hfill Jul 2024 -- Present\\
\textbf{Key Skills}: Java, Spring Boot, Python, Deployment, Backend, SQL, AI, LangChain, Git  
\begin{itemize}
    \item Worked on the \textbf{Complex Fund Reporting and Fund Admin Financial Reporting Tool}, a \textbf{Java Spring Boot microservices} platform, \textbf{reducing financial reporting errors by 50\%} for SEC, NECN, and NPORT compliance.  
    \item \textbf{Automated fund onboarding} with a \textbf{Generative AI-powered tool}, decreasing manual configuration time from \textbf{5 hours to 30 minutes per fund} (a \textbf{90\% reduction}).  
    \item Developed a \textbf{GenAI-based production issue analysis tool} that analyzes logs and suggests fixes, \textbf{accelerating incident resolution by 70\%} and reducing downtime.  
    \item \textbf{Worked on Optimization of real-time fund reporting} by integrating \textbf{Kafka} for event-driven architecture, \textbf{cutting report generation time by 60\%} and improving system scalability.  
    \item Led deployment enhancements using \textbf{Docker, Kubernetes, and CI/CD pipelines}, \textbf{reducing deployment failures by 90\%} and ensuring 99.9\% uptime.
\end{itemize}
\vspace{3 pt}
\textbf{Bank of New York Mellon - Winter Intern} \hfill Jan 2024 -- Jun 2024\\
\textbf{Key Skills}: Java, Spring Boot, Spring MVC, REST API, Kafka, Redis, CI/CD, Docker, GitLab  
\begin{itemize}
    \item Designed \textbf{FAST (Fund Admin Support Tool)}, automating 40\% of manual tasks in \textbf{incident management}, reducing \textbf{average resolution time .}  
    \item Developed a \textbf{real-time fund tracking dashboard} with \textbf{Spring Boot and Angular}, improving \textbf{fund tracking accuracy by 98\%} and  integrated a \textbf{GEN-AI chat bot }to actively solve queries of the users which was trained on the Whole application.
    \item Enhanced \textbf{CI/CD pipelines with GitLab and Docker}, ensuring \textbf{zero-downtime deployments} and minimizing rollback occurrences.  
\end{itemize}
\vspace{3 pt}
\textbf{Shyena Tech Yarns - Software Engineer Intern} \hfill Oct 2023 -- Dec 2023\\
\textbf{Key Skills}: Python, Django, REST API, Celery, Stripe API, AI/ML  
\begin{itemize}
    \item Built an \textbf{AI-powered call analytics tool} that extracted real-time insights from customer conversations, \textbf{reducing customer support issue resolution time by 50\%}.  
    \item Developed \textbf{Django REST APIs}, enabling seamless \textbf{data retrieval with a 30\% improvement in response times}.  
    \item Optimized \textbf{Celery-based background task execution}, \textbf{increasing system efficiency by 40\%}.  
\end{itemize}
\vspace{3 pt}


\hrule
\section*{Projects}
\textbf{AI-Powered Job Search Assistant}  
\begin{itemize}
    \item Automated job search by integrating \textbf{real-time job scraping with Kafka}, \textbf{reducing manual effort by 70\%}.  
    \item Developed an \textbf{AI-driven job ranking algorithm}, improving \textbf{job-match accuracy by 80\%}.  
    \item \textbf{Generated personalized cover letters and recruiter emails}, boosting \textbf{response rates by 60\%}.  
    \item Created an \textbf{ATS-optimized resume generator}, Which aligns with the job description and the skill of candidate \textbf{increasing resume shortlisting probability by 50\%}.  
\end{itemize}

\vspace{3 pt}

\hrule
\vspace{3pt}

\section*{Achievements \& Certifications}
\begin{itemize}
    \item \textbf{Finalist - Kavach 2023 Hackathon}, contributed to cybersecurity solutions.
    \item \textbf{Published Research Paper in Explainable AI (XAI)} - \href{https://ijarsct.co.in/Paper18344.pdf}{IJARSCT}.
    \item \textbf{Contributed to Open Source} - HacktoberFest 2022 participant.
\end{itemize}

\hrule
\vspace{3pt}

\section*{Extracurricular Activities}
\begin{itemize}
    \item \textbf{Technical Blogging} on DevOps \& Cloud - \href{https://medium.com/@yash.7232.rajput}{Medium}.
\end{itemize}

\end{document}
    """,
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