from student_database import StudentDatabase
from student import Student
from analysis import Analysis
from dashboard import Dashboard


def run_sample():
    # Sample student data
    student_data = {
        'student_id': '12345',
        'gpa': 3.8,  # GPA out of 4.0 (or as per your scale in config.py)
        'standardized_scores': {'SAT': 1450, 'TOEFL': 110},
        'extracurriculars': {'debate_club': True, 'sports': 'Basketball'},
        'essay': 'I have always been passionate about computer science. My interest in AI and deep learning has led me to undertake several projects and write research papers.',
        'recommendations': ['An excellent student', 'Has shown outstanding leadership qualities'],
        'research_papers': [{'title': 'Deep Learning Approaches', 'journal': 'AI Journal'},
                            {'title': 'Neural Networks', 'journal': 'Nature'}],
        'certifications': [{'title': 'Machine Learning', 'authority': 'Coursera'}],
        'background_info': {'ethnicity': 'Asian', 'nationality': 'Indian', 'first_generation': True}
    }

    # Create a student object
    student = Student(**student_data)

    # Add the student to the database
    db = StudentDatabase()
    db.add_student(student)

    # Perform analyses
    academic_score = Analysis.academic_analysis(student.gpa)  # Adjusted for GPA
    extracurricular_score = Analysis.extracurricular_analysis(student.extracurriculars)
    essay_score = Analysis.essay_analysis(student.essay)
    recommendation_score = Analysis.recommendation_analysis(student.recommendations)

    analysis_results = {
        'academic': academic_score,
        'extracurricular': extracurricular_score,
        'essay': essay_score,
        'recommendation': recommendation_score
    }

    # Verification results
    research_papers_verified = Analysis.research_paper_verification(student.research_papers)
    certifications_verified = Analysis.certification_verification(student.certifications)
    ai_generated_essay = Analysis.ai_generated_content_detection(student.essay)

    verification_results = {
        'research_papers': research_papers_verified,
        'certifications': certifications_verified,
        'ai_generated_essay': ai_generated_essay
    }

    # Holistic results
    background_adjustment = Analysis.background_adjustment(student.background_info)
    # normalized_scores = Analysis.score_normalization(student.standardized_scores)

    holistic_results = {
        'background_adjustment': background_adjustment,
        # 'normalized_scores': normalized_scores
    }

    # Refined analysis results
    achievements_score = Analysis.achievements_analysis(student.extracurriculars)

    refined_results = {
        'achievements': achievements_score
    }

    # Generate dashboard
    dashboard = Dashboard.generate_dashboard(student, analysis_results, verification_results, holistic_results,
                                             refined_results)

    return dashboard


# Run the sample
if __name__ == '__main__':
    result = run_sample()
    for key, value in result.items():
        print(f"{key} : {value}")
