def create_job_posting(title, skills, experience):
    posting = f"""
    Job Title: {title}
    Required Skills: {', '.join(skills)}
    Experience: {experience} years
    Description: We are looking for a talented {title} to join our team. 
    The ideal candidate should have experience in {', '.join(skills)} and at least {experience} years of experience.
    """
    return posting

# Test the function
if __name__ == "__main__":
    title = "Software Engineer"
    skills = ["Python", "Machine Learning", "NLP"]
    experience = 3
    print(create_job_posting(title, skills, experience))