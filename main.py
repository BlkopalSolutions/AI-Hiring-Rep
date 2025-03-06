from job_posting import create_job_posting
from resume_screener import extract_skills, extract_experience
from candidate_matcher import rank_candidates
from email_notifier import send_email

def main():
    # Create job posting
    title = "Software Engineer"
    job_skills = ["Python", "Machine Learning", "NLP"]
    job_experience = 3
    posting = create_job_posting(title, job_skills, job_experience)
    print("Job Posting:\n", posting)

    # Sample candidates
    candidates = [
        {"name": "Alice", "email": "alice@example.com", "resume": "I have 5 years of experience in Python and Machine Learning."},
        {"name": "Bob", "email": "bob@example.com", "resume": "I have 2 years of experience in Java."},
    ]

    # Screen resumes
    for candidate in candidates:
        resume_text = candidate["resume"]
        candidate["skills"] = extract_skills(resume_text, job_skills)
        candidate["experience"] = extract_experience(resume_text)

    # Rank candidates
    ranked_candidates = rank_candidates(candidates, job_skills, job_experience)
    print("Ranked Candidates:")
    for candidate, score in ranked_candidates:
        print(f"{candidate['name']}: {score:.2f}")

    # Notify top candidate
    top_candidate = ranked_candidates[0][0]
    send_email(top_candidate["email"], "Job Application Update", 
               "Congratulations! You’re a top match for the Software Engineer role.")

if __name__ == "__main__":
    main()