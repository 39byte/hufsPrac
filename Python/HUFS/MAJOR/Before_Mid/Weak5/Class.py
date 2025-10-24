classA = {}

def add_student(classname, name, score):
    classname[name] = score

def print_students(classname):
    for name, score in classname.items():
        print(f"{name}: {score}")

def get_average(classname):
    return sum(classname.values()) / len(classname.values())

add_student(classA, "Alice", 96)
add_student(classA, "Bob", 83)
add_student(classA, "Jiwon", 100)
print_students(classA)
print("평균 :", get_average(classA))