class Student:
    def _init_(self, name, id):
        self.name = name
        self.id = id
        self.grades = {}

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def get_average_grade(self):
        total_grade = sum(self.grades.values())
        return total_grade / len(self.grades)

class GradeTracker:
    def _init_(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.id] = student

    def add_grade_to_student(self, student_id, course, grade):
        if student_id in self.students:
            self.students[student_id].add_grade(course, grade)
        else:
            print("Student not found!")

    def get_student_average_grade(self, student_id):
        if student_id in self.students:
            return self.students[student_id].get_average_grade()
        else:
            print("Student not found!")

# Example usage:
grade_tracker = GradeTracker()

# Adding students
student1 = Student("John Doe", 1)
student2 = Student("Jane Smith", 2)
grade_tracker.add_student(student1)
grade_tracker.add_student(student2)

# Adding grades to students
grade_tracker.add_grade_to_student(1, "Math", 90)
grade_tracker.add_grade_to_student(1, "Science", 85)
grade_tracker.add_grade_to_student(2, "Math", 95)
grade_tracker.add_grade_to_student(2, "Science", 88)

# Getting average grade of a student
print("Average grade for John Doe:", grade_tracker.get_student_average_grade(1))
print("Average grade for Jane Smith:", grade_tracker.get_student_average_grade(2))