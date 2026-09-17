class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, roll_no, program):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.program = program

    def show_info(self):
        super().show_info()
        print("Roll No:", self.roll_no)
        print("Program:", self.program)


class Teacher(Person):
    def __init__(self, name, age, teacher_id, subject):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.subject = subject

    def show_info(self):
        super().show_info()
        print("Teacher ID:", self.teacher_id)
        print("Subject:", self.subject)


student = Student(
    "Ali Raza",
    18,
    1001,
    "ICS"
)

teacher = Teacher(
    "Ahmed Khan",
    35,
    501,
    "Computer Science"
)

print("----- STUDENT -----")
student.show_info()

print("\n----- TEACHER -----")
teacher.show_info()
