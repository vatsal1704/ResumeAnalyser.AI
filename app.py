import streamlit as st
from dotenv import load_dotenv
load_dotenv() #activate the api key
from analysis import analyse_profile
from pdf import process_pdf
 
# create the frontend of the app
st.header("ResumeAnalyser:blue[.AI]🧾📑📚",divider="green")
st.subheader("Match your resume with the job description using AI")



notes = f'''
* **Upload the Resume(pdf only):** Please upload the resume in the pdf format only
* **Paste the Job Desc:** Copy paste the Job Desc below
* **Unleash the Power of LLMS:** Use the power of LLM'S to derive insights about the resume.'''

st.write(notes)




# sidebar
st.sidebar.subheader("Upload the Resume🧾📑")
pdf_doc=st.sidebar.file_uploader("Upload your resume in pdf format", type=["pdf"])
st.sidebar.write("Created by Vatsal")


# Job Description Text Box
st.subheader("Job Description",divider=True)
job_desc=st.text_area(label="Paste the Job Description here",max_chars=10000)
submit=st.button(label="Get AI Powered Insights")

if submit:
    st.markdown(analyse_profile(pdf_doc=pdf_doc,job_desc=job_desc))
    