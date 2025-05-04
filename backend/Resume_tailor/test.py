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
   "YASH DILIP RAJPUT\nyashrajput7232@gmail.com |LinkedIn |GitHub |+91-6281110280\nSummary\nSoftware Engineer with expertise in Java, Python, and Go , specializing in Spring Boot, Django, and microservices\narchitecture . Experienced in building scalable, cloud-native applications and optimizing production systems. Proficient\ninDevOps, Kubernetes, Terraform, and CI/CD pipelines to streamline deployments. Demonstrated ability to improve\nefficiency by solving 300+ coding problems on platforms like LeetCode and CodeChef. Skilled in leveraging AI and\nautomation to enhance workflows and optimize system performance.\nEducation\nBachelor of Engineering (B.E.) - Computer Engineering\nPune University, Pune CGPA: 9.30/10\nTechnical Skills\nProgramming : Java, Python, C++ |Backend : Spring Boot, Flask, Django |DevOps\nCloud : AWS (EKS, Lambda, S3), Terraform, Kubernetes, Docker |Databases : MongoDB, MySQL, PostgreSQL |Tools\nOthers : Git, Kafka, Redis, Prometheus, Grafana\nWork Experience\nBank of New York Mellon - Analyst Jul 2024 – Present\nKey Skills : Java, Spring Boot, Python, Deployment, Backend, SQL, AI, LangChain, Git\n•Worked on the Complex Fund Reporting and Fund Admin Financial Reporting Tool , aJava Spring Boot\nmicroservices platform, reducing financial reporting errors by 50% for SEC, NECN, and NPORT compliance.\n•Automated fund onboarding with a Generative AI-powered tool , decreasing manual configuration time from 5\nhours to 30 minutes per fund (a90% reduction ).\n•Developed a GenAI-based production issue analysis tool that analyzes logs and suggests fixes, accelerating inci-\ndent resolution by 70% and reducing downtime.\n•Worked on Optimization of real-time fund reporting by integrating Kafka for event-driven architecture, cutting\nreport generation time by 60% and improving system scalability.\n•Led deployment enhancements using Docker, Kubernetes, and CI/CD pipelines ,reducing deployment failures\nby 90% and ensuring 99.9% uptime.\nBank of New York Mellon - Winter Intern Jan 2024 – Jun 2024\nKey Skills : Java, Spring Boot, Spring MVC, REST API, Kafka, Redis, CI/CD, Docker, GitLab\n•Designed FAST (Fund Admin Support Tool) , automating 40% of manual tasks in incident management , reducing\naverage resolution time from 3 hours to 1.5 hours .\n•Developed a real-time fund tracking dashboard withSpring Boot and Angular , improving fund tracking accu-\nracy by 98% andreducing query latency by 60% .\n•Enhanced CI/CD pipelines with GitLab and Docker , ensuring zero-downtime deployments and minimizing\nrollback occurrences.\nShyena Tech Yarns - Software Engineer Intern Oct 2023 – Dec 2023\nKey Skills : Python, Django, REST API, Celery, Stripe API, AI/ML\n•Built an AI-powered call analytics tool that extracted real-time insights from customer conversations, reducing\ncustomer support issue resolution time by 50% .\n•Developed Django REST APIs , enabling seamless data retrieval with a 30% improvement in response times .\n•Optimized Celery-based background task execution ,increasing system efficiency by 40% .\nProjects\nAI-Powered Job Search Assistant\n•Automated job search by integrating real-time job scraping with Kafka ,reducing manual effort by 70% .\n•Developed an AI-driven job ranking algorithm , improving job-match accuracy by 80% .\n•Generated personalized cover letters and recruiter emails , boosting response rates by 60% .\n•Created an ATS-optimized resume generator , Which aligns with the job description and the skill of candidate\nincreasing resume shortlisting probability by 50% .\nAchievements & Certifications\n•Finalist - Kavach 2023 Hackathon , contributed to cybersecurity solutions.\n•Published Research Paper in Explainable AI (XAI) - IJARSCT.\n•Contributed to Open Source - HacktoberFest 2022 participant.\nExtracurricular Activities\n•Technical Blogging on DevOps & Cloud - Medium.\n1\n"
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