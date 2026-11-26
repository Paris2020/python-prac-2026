class Employee:
    def __init__(self, name):
        self.name = name

first = Employee("Freya")
second = Employee("Sarah")
#del second.name
setattr(first, "name", "Freya")
print(getattr(first, "name"))

delattr(second, "name")
#setattr(second, "name", "Sarah")

if  hasattr(second, "name"):
    print(getattr(second, "name"))
else:
    print("second does not have attribute name")
