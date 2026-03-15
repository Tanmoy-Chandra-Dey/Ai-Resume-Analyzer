import re

SKILLS_DATABASE = [
    "python",
    "java",
    "c++",
    "machine learning",
    "data science",
    "cybersecurity",
    "network security",
    "sql",
    "react",
    "node",
    "cloud",
    "aws",
    "linux",
    "git",
    "docker",
]


def extract_skills(resume_text):
    resume_text = resume_text.lower()

    found_skills = []

    for skill in SKILLS_DATABASE:
        if skill in resume_text:
            found_skills.append(skill)

    return found_skills


def match_job_description(resume_text, job_description):

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    job_words = set(re.findall(r"\w+", job_description))
    resume_words = set(re.findall(r"\w+", resume_text))

    matched_words = job_words.intersection(resume_words)

    score = len(matched_words) / len(job_words) * 100

    return round(score, 2), matched_words


def analyze_resume(resume_text, job_description):

    skills = extract_skills(resume_text)

    score, matched_words = match_job_description(resume_text, job_description)

    print("\nResume Analysis Result")
    print("----------------------")

    print("\nDetected Skills:")
    for skill in skills:
        print("-", skill)

    print("\nJob Match Score:", score, "%")

    print("\nMatched Keywords:")
    for word in matched_words:
        print("-", word)

    if score < 40:
        print("\nSuggestion: Add more relevant keywords from the job description.")
    else:
        print("\nGood match for the job role!")


def main():

    print("AI Resume Analyzer")
    print("------------------")

    print("\nPaste your resume text:")
    resume_text = input()

    print("\nPaste job description:")
    job_description = input()

    analyze_resume(resume_text, job_description)


if __name__ == "__main__":
    main()
