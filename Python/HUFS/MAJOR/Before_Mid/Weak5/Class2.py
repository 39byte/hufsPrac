class Student:
    def __init__(self, name, score, age):
        self.name = name
        self.score = score
        self.age = age

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, Student_info):
        self.students.append(Student_info)

    def get_average(self):
        return sum(s.score for s in self.students) / len(self.students)
    
    def print_students(self):
        for s in self.students:
            print(f"{s.name} : {s.score}")

classA = Classroom()
classB = Classroom()

s1101 = Student("Alice", 91, 19)
s1102 = Student("Bob", 87, 28)
s1126 = Student("Jiwon",100, 20)

classA.add_student(s1101)
classA.add_student(s1102)
classA.add_student(s1126)

classA.print_students()
print(f"평균 : {classA.get_average():.4f}")