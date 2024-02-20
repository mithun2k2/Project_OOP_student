class Student:
 
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.subjects = []
        self.grades = []

    def display_profile(self):
    
        profile  = f"Student Name: {self.name} {self.surname}\n\n"
        profile += f"Subject\t\t\tGrade\n"
        for subject, grade in zip(self.subjects, self.grades):
            profile += f"{subject}\t\t\t{grade}\n"
        profile += f"\nAverage :{self.get_average()}\n"
        print(profile)
   

    def get_average(self):
        return(sum(self.grades)/len(self.grades))

from random import randint

student1 = Student("Jack", "Black")
student2 = Student("Clare", "Steward")
student3 = Student("Peter", "Johnson")
student4 = Student("Nichole", "Turn")
student5 = Student("Hammond", "Sharp")
student6 = Student("Mahmudul", "Hassan")
student7 = Student("Ashikur", "Rahman")
student8 = Student("Rony", "Rahman")
student9 = Student("Jannatul", "Ferdous")
student10 = Student("Tushar", "Khan")

students = [student1, student2, student3, student4, student5, student6, student7, student8, student9, student10]

# Adding subjects and grades
subjects = ["English","History", "Math", "Biology", "Physics", "Music" ]
for student in students:
    student.subjects = [subject for subject in subjects]
    student.grades = [randint(40,100) for _ in range(6)]

for student in students:
    student.display_profile()