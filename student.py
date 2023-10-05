class Student:

    def __init__(self, student_id, gpa, standardized_scores, extracurriculars, essay, recommendations, research_papers,
                 certifications, background_info):
        self.student_id = student_id
        self.gpa = gpa
        self.standardized_scores = standardized_scores
        self.extracurriculars = extracurriculars
        self.essay = essay
        self.recommendations = recommendations
        self.research_papers = research_papers
        self.certifications = certifications
        self.background_info = background_info

    def get_id(self):
        return self.student_id

    def input_data(self):
        # Method to input student data
        self.gpa = float(input("Enter student GPA: "))
        self.standardized_scores = eval(input("Enter standardized scores (e.g. {'SAT': 1450}): "))
        self.extracurriculars = eval(
            input("Enter extracurriculars (e.g. {'debate_club': True, 'sports': 'Basketball'}): "))
        self.essay = input("Enter essay content: ")
        self.recommendations = eval(input("Enter recommendations (e.g. ['Good student', 'Hard worker']): "))
        self.research_papers = eval(
            input("Enter research papers (e.g. [{'title': 'Deep Learning', 'journal': 'AI Journal'}]): "))
        self.certifications = eval(input("Enter certifications (e.g. [{'title': 'ML', 'authority': 'Coursera'}]): "))
        self.background_info = eval(input(
            "Enter background info (e.g. {'ethnicity': 'Asian', 'nationality': 'Indian', 'first_generation': True}): "))
