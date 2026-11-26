class Student:
    count = 0

    def __init__(self):
        self.name = ""
        self.surname = ""
        Student.count += 1
        self.number = Student.count


first_student = Student()
first_student.name = "John"
first_student.surname = "Doe"

second_student = Student()
second_student.name = "Jane"
second_student.surname = "Doe"

print("{}: {} {}".format(first_student.count, first_student.name, first_student.surname))
print("{}: {} {}".format(second_student.count, second_student.name, second_student.surname))
print("Number of students: {}".format(Student.count))


print()
print("============= END: Initialising a class instance ===============")
print()

