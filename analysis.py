import google.generativeai as genai
from pdf import process_pdf
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables
import streamlit as st

# Configure the Google Generative AI API key and model

genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))
model=genai.GenerativeModel("gemini-1.5-flash")


def analyse_profile(pdf_doc, job_desc):
    if pdf_doc is not None:
        pdf= process_pdf(pdf_doc)
        st.sidebar.markdown("**UPLOADED SUCCESSFULLY** :green[✔️]")
    else:
        st.sidebar.markdown("**PLEASE UPLOAD A RESUME m(PDF FORMAT)** :red[❌]")



    good_fit = model.generate_content(f'''Compare the {job_desc} with resume{pdf} and suggest Am I  a good fit for the role?''')
    ats_scores = model.generate_content(f'''Compare the {job_desc} with resume{pdf} and suggest the ATS Scores of the resume''')
    probability  = model.generate_content(f'''Compare the {job_desc} with resume{pdf} and suggest the Probability of getting selected in Percentage''')
    keywords = model.generate_content(f'''Compare the {job_desc} with resume{pdf} and give me a list of the Keywords shown in job description but missing from the resume''')
    swot = model.generate_content(f'''Compare the {job_desc} with resume{pdf} and give me the SWOT Analysis followed by actionable insights in bullet points''')
    projects = model.generate_content(f'''Compare the {job_desc} with resume{pdf} and give me a list of the ML Competitions are Projects that are aligned with the Job Description & the Role in bullet points along with chances of getting selected in percentage''')
    return (st.write(good_fit.text), 
            st.write(ats_scores.text), 
            st.write(probability.text), 
            st.write(keywords.text), 
            st.write(swot.text), 
            st.write(projects.text))