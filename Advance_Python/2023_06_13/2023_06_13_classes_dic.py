import math


class StudentInfo:
    def __init__(self, Name, T1, T2):
        self.Name = Name
        self.Test1 = T1
        self.Test2 = T2

    def classfinal(self):
        return math.floor((self.Test1 + self.Test2) / 2)

    def print_student(self):
        print(f"{self.Name} has a final grade of {self.classfinal()}.")


if __name__ == "__main__":
    student1 = StudentInfo("João Silva", 12, 20)
    print(f"{student1.Name} has a final grade of {student1.classfinal()}.")

    students = {}
    n_students = int(input("How many students do you want to input: "))

    for i in range(n_students):
        name = input("Enter student name: ")
        t1 = float(input("Enter Test 1 score: "))
        t2 = float(input("Enter Test 2 score: "))
        student_info = StudentInfo(name, t1, t2)
        students[name] = student_info
    
    print("Content of the students dictionary:")
    for student_name, student in students.items():
        print(f"Name={student.Name}, Test1={student.Test1}, Test2={student.Test2}")

    for student_name, student in students.items():
        student.print_student()
