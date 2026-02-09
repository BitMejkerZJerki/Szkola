class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = []

    def add_grade(self, grade):
        if 1<= grade <= 6:  #pierwsza poprawa kodu
            self.grades.append(grade)
        else:
            print("Nieprawidłowa ocena")

    def average(self):
        if len(self.grades) == 0:
            return 0
        total = 0
        for g in self.grades:
            total = total + g
        return total / len(self.grades)

    def is_passing(self):
        if self.average() >= 3:
            return True
        else:
            return False


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def print_students(self):
        for s in self.students:
            print(s.name, s.surname)

    def print_passing_students(self):
        for s in self.students:
            if s.is_passing() == True:
                print(s.name, s.surname)


# Przykładowe użycie
school = School()

s1 = Student("Jan", "Kowalski")
s2 = Student("Anna", "Nowak")

s1.add_grade(5)
s1.add_grade(4)
s2.add_grade(2)
s2.add_grade(3)

school.add_student(s1)
school.add_student(s2)

school.print_students()
school.print_passing_students()
