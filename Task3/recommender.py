from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

job_roles = {
    "Data Scientist": "python sql machine learning data analysis statistics pandas",
    "DevOps Engineer": "aws docker kubernetes ci cd automation linux cloud",
    "Backend Developer": "java python sql apis rest databases spring",
    "Frontend Developer": "javascript react html css ui design figma",
    "Cloud Architect": "aws azure cloud computing networking security automation",
    "ML Engineer": "python machine learning tensorflow pytorch deep learning data structures",
    "Cybersecurity Analyst": "security networking linux encryption firewalls monitoring",
    "Mobile App Developer": "java kotlin swift android ios mobile ui"
}

role_names = list(job_roles.keys())
role_docs = list(job_roles.values())

# taking 3 skills from the user, this is the minimum required by the spec
user_skills = input("Enter 3 skills you have (comma separated): ")
user_doc = user_skills.lower().replace(",", " ")

all_docs = role_docs + [user_doc]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_docs)

user_vector = tfidf_matrix[-1]
role_vectors = tfidf_matrix[:-1]

scores = cosine_similarity(user_vector, role_vectors)[0]

ranked = sorted(zip(role_names, scores), key=lambda x: x[1], reverse=True)

print("\nTop 3 recommended career paths for you:\n")
for i, (role, score) in enumerate(ranked[:3], start=1):
    match_percent = round(score * 100, 1)
    print(f"{i}. {role} - {match_percent}% match")
