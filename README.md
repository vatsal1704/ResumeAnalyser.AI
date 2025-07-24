## ResumeAnalyser.AI

This is a repository that will cater a resume analysis with the help of Generative AI

# ResumeAnalyser.AI
ResumeAnalyser.AI is a GenAI-powered application that intelligently evaluates resumes against job descriptions to offer in-depth insights for job seekers and recruiters. With the help of advanced natural language processing and machine learning models, the tool provides key metrics such as ATS compatibility, hiring probability, keyword relevance, SWOT analysis, and personalized improvement suggestions.

## 🚀 Features

- 📊 **ATS Score**: Analyzes your resume and gives an Applicant Tracking System score based on keyword matching and formatting.
- 📈 **Hiring Probability**: Estimates the likelihood of getting shortlisted for the role based on your resume’s alignment with the job description.
- 🧠 **Keyword Analysis**: Highlights important keywords you’ve missed or used effectively compared to the JD.
- 🔍 **SWOT Analysis**: Uses AI to evaluate your Strengths, Weaknesses, Opportunities, and Threats from the resume content.
- ✍️ **Improvement Suggestions**: Personalized and actionable tips to refine and enhance your resume.

## 🖥️ Live Demo

👉 Click here to check out the **[Live Demo](https://match-reusme-ai.streamlit.app/)**  
*(Replace with your actual deployed app link, e.g. Vercel, Netlify, Render, etc.)*

## 📷Screenshots
<img width="1920" height="798" alt="Screenshot (376)" src="https://github.com/user-attachments/assets/9187ba04-38fc-400a-a305-2cbe9d8fc153" />

<img width="1920" height="847" alt="Screenshot (377)" src="https://github.com/user-attachments/assets/4a55b193-ae7f-4992-af7a-95926d4dcae7" />




## Create the Virtual Environment

- We create the Virtual Environment and install all the packages mentioned in `requirements.txt`

## Coding the application

We will use modular code to build our application.

# resume-analyser.ai

Resume Analysis...

### Steps for creating the project

- Create the Virtual Environment using `python -m venv .venv`
- Activate the Virtual Environment using `source .venv/
scripts/activate`
- Create the .env file to store the API key
- Create the requirements.txt file and add the libraries for installation using `pip install -r requirements.txt`

### Project Synopsis

- We want to create an Application that will analyse the resume of the candidate using Gen AI model with the job desc and provide insights such as :-

* ATS scores
* probability of getting hired
* keyword analysis
* SWOT Analysis
* Suggestion for Overall Improvements

### Architecture

- app.py : Front end creation and output of the Genai Model.
  It will have the feature of capturing information such as Resume and JD
- Information we are capturing is `Resume.pdf` and ` job_des`.
- Pdf.py that will process the information in pdf and thats why we have installed `pypdf `
- analysis.py that will triangulate the pdf information and the JD and will provide insights and next step.




**Live Demo:** https://match-reusme-ai.streamlit.app/
