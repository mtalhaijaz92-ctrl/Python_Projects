class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def show_role(self):
        print("Role: Doctor")
        print("Specialization:", self.specialization)


class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease

    def show_role(self):
        print("Role: Patient")
        print("Disease:", self.disease)


doctor = Doctor("Dr. Ahmed", 40, "Cardiology")
patient = Patient("Ali", 20, "Fever")

doctor.show_role()
patient.show_role()
