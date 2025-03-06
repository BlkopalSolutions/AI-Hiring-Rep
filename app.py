import streamlit as st
from job_posting import create_job_posting
from resume_screener import extract_skills, extract_experience
from candidate_matcher import rank_candidates
from email_notifier import send_email

def main():
    st.title("AI-Powered HR Rep")

    # Job Posting Section
    st.header("Create Job Posting")
    title = st.text_input("Job Title")
    skills_input = st.text_area("Required Skills (comma-separated)")
    experience = st.number_input("Required Experience (years)", min_value=0)
    if st.button("Generate Posting"):
        job_skills = [skill.strip() for skill in skills_input.split(",")]
        posting = create_job_posting(title, job_skills, experience)
        st.text_area("Job Posting", posting, height=200)

    # Candidate Section
    st.header("Candidate Management")
    uploaded_files = st.file_uploader("Upload Resumes (text files)", accept_multiple_files=True)
    if uploaded_files and skills_input and title:
        job_skills = [skill.strip() for skill in skills_input.split(",")]
        candidates = []
        for uploaded_file in uploaded_files:
            resume_text = uploaded_file.read().decode("utf-8")
            skills = extract_skills(resume_text, job_skills)
            exp = extract_experience(resume_text)
            candidates.append({"name": uploaded_file.name, "skills": skills, "experience": exp})
        
        if candidates:
            ranked = rank_candidates(candidates, job_skills, experience)
            st.write("Ranked Candidates:")
            for candidate, score in ranked:
                st.write(f"{candidate['name']}: {score:.2f}")
            
            if st.button("Notify Top Candidate"):
                top_candidate = ranked[0][0]
                send_email("test@example.com", "Job Update", "You’re a top match!")  # Replace email
                st.success("Email sent!")

if __name__ == "__main__":
    main()