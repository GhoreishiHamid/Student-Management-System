class Student:
    def __init__(self, student_id, name, email, major):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.major = major

    def display_info(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Major: {self.major}")