def skill_gap_analyzer(skills, goal):

    skill_db = {
    "AI Engineer": [
        "Machine Learning",
        "Deep Learning",
        "LangChain",
        "Vector Databases",
        "LLMs"
    ],

    "Data Scientist": [
        "Statistics",
        "Machine Learning",
        "Python",
        "Data Visualization"
    ],

    "Software Engineer": [
        "Data Structures",
        "Algorithms",
        "System Design",
        "DBMS",
        "Operating Systems"
    ],

    "Cyber Security Engineer": [
        "Network Security",
        "Cryptography",
        "Ethical Hacking",
        "Linux",
        "Penetration Testing"
    ]
}
    required = skill_db.get(goal, [])

    missing = []

    for skill in required:
        if skill.lower() not in skills.lower():
            missing.append(skill)

    return missing


def project_recommender(goal):

    projects = {
    "AI Engineer": [
        "Resume Analyzer",
        "AI Interview Coach",
        "Research Assistant Agent"
    ],

    "Data Scientist": [
        "Sales Forecasting",
        "Customer Segmentation"
    ],

    "Software Engineer": [
        "Library Management System",
        "E-Commerce Website",
        "Task Management App"
    ],

    "Cyber Security Engineer": [
        "Port Scanner",
        "Vulnerability Scanner",
        "Network Monitoring Tool"
    ]
}

    return projects.get(goal, [])

def interview_questions(goal):

    questions = {

        "AI Engineer": [
            "What is Machine Learning?",
            "Difference between AI and ML?",
            "What is Deep Learning?",
            "What is RAG?",
            "What is LangChain?"
        ],

        "Data Scientist": [
            "What is Regression?",
            "Difference between Supervised and Unsupervised Learning?",
            "What is Overfitting?",
            "Explain Pandas.",
            "What is Data Visualization?"
        ],

        "Software Engineer": [
            "What is OOP?",
            "Difference between Stack and Queue?",
            "Explain HashMap.",
            "What is Time Complexity?",
            "What is Database Normalization?"
        ],

        "Cyber Security Engineer": [
            "What is SQL Injection?",
            "What is XSS?",
            "What is Encryption?",
            "Difference between Symmetric and Asymmetric Cryptography?",
            "What is Penetration Testing?"
        ]
    }

    return questions.get(goal, [])