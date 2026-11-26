class Student:
    count = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Student.count += 1
        self.number = Student.count
        self.grades = {}

    def display(self):
        print("{}:\t{}".format(self.number, self.name,self.surname ))
        print()
        if len(self.grades) == 0:
            print("\tNo subjects and results have been added")
        else:
            for key in self.grades:
                print("\t{}:\t{}".format(key, self.grades[key]))

            print("\tAverage:\t{}".format(self.calculate_average()))
        print("-" * 50)

    def add_subject_and_mark(self, subject, mark):
        self.grades[subject] = mark


    def calculate_average(self):
        total = 0

        for key in self.grades:
            total += self.grades[key]
        return total/len(self.grades)




#print("{}: {} {}".format(first_student.count, first_student.name, first_student.surname))
#print("{}: {} {}".format(second_student.count, second_student.name, second_student.surname))

