# Define which parts of the application to analyze
CONFIG = {
    'academic_analysis': True,
    'extracurricular_analysis': True,
    'essay_analysis': True,
    'recommendation_analysis': True,
    'research_paper_verification': True,
    'certification_verification': True,
    'ai_generated_content_detection': True,
    'background_adjustment': True,
    'score_normalization': True,
    'achievements_analysis': True
}

# Default GPA scale
GPA_SCALE = 4.0

# Weightings for each component in the analysis
WEIGHTINGS = {
    'academic': 0.4,
    'essay': 0.2,
    'extracurricular': 0.2,
    'recommendation': 0.2
}

# Maximum possible scores for each section
MAX_SCORES = {
    'academic': 100,  # This is a percentage
    'essay': 100,  # This is a percentage
    'extracurricular': 100,  # This is a percentage
    'recommendation': 100,  # This is a percentage
}


# Sample student data for testing
# SAMPLE_DATA = {
#     'student_id': '12345',
#     'academic_scores': {'math': 90, 'science': 85},
#     'standardized_scores': {'SAT': 1450, 'TOEFL': 110},
#     'extracurriculars': {'debate_club': True, 'sports': 'Basketball'},
#     'essay': 'I have always been passionate about computer science. My interest in AI and deep learning has led me to undertake several projects and write research papers.',
#     'recommendations': ['An excellent student', 'Has shown outstanding leadership qualities'],
#     'research_papers': [{'title': 'Deep Learning Approaches', 'journal': 'AI Journal'}, {'title': 'Neural Networks', 'journal': 'Nature'}],
#     'certifications': [{'title': 'Machine Learning', 'authority': 'Coursera'}],
#     'background_info': {'ethnicity': 'Asian', 'nationality': 'Indian', 'first_generation': True}
# }
