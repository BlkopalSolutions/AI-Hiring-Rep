def calculate_match_score(candidate_skills, candidate_experience, job_skills, job_experience):
    # Skill match: fraction of job skills the candidate has
    skill_match = len(set(candidate_skills) & set(job_skills)) / len(job_skills)
    # Experience match: candidate experience / job requirement (max 1.0)
    experience_match = min(candidate_experience / job_experience, 1.0)
    # Average the two scores
    return (skill_match + experience_match) / 2

def rank_candidates(candidates, job_skills, job_experience):
    scores = []
    for candidate in candidates:
        score = calculate_match_score(candidate["skills"], candidate["experience"], job_skills, job_experience)
        scores.append((candidate, score))
    return sorted(scores, key=lambda x: x[1], reverse=True)

# Test it
if __name__ == "__main__":
    candidates = [
        {"name": "Alice", "skills": ["Python", "Machine Learning"], "experience": 5},
        {"name": "Bob", "skills": ["Java"], "experience": 2},
    ]
    job_skills = ["Python", "Machine Learning", "NLP"]
    job_experience = 3
    ranked = rank_candidates(candidates, job_skills, job_experience)
    for candidate, score in ranked:
        print(f"{candidate['name']}: {score:.2f}")