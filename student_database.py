class StudentDatabase:

    def __init__(self):
        self.db = {}

    def add_student(self, student):
        student_id = student.get_id()
        self.db[student_id] = student
        return f"Record added for student {student_id}."

    def get_student(self, student_id):
        return self.db.get(student_id)
