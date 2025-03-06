import spacy
import re

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

def extract_skills(resume_text, job_skills):
    # Look for job skills in the resume (case-insensitive)
    return [skill for skill in job_skills if skill.lower() in resume_text.lower()]

def extract_experience(resume_text):
    # Find numbers followed by "years" (e.g., "5 years")
    matches = re.findall(r'(\d+)\s+years', resume_text, re.IGNORECASE)
    return max([int(match) for match in matches]) if matches else 0

# Test the functions
if __name__ == "__main__":
    resume = "I have 5 years of experience in Python and Machine Learning."
    job_skills = ["Python", "Machine Learning", "NLP"]
    skills = extract_skills(resume, job_skills)
    experience = extract_experience(resume)
    print(f"Skills found: {skills}")
    print(f"Experience: {experience} years")