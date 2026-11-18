#maintaining scope
def calculate_person_total():

    def inner_function():
        global inner_variable
        print("inner function called")
        inner_variable = 50

    global total
    name = input("Please enter your name: ")
    amount = int(input("How many items do you wish to purchase? "))
    total = amount * price
    print(name,", your total for ", amount," items is: ", total, sep='')

    inner_function()


price = 70

while(input("Type 'y' to calculate a user's details: ") == 'y'):
    calculate_person_total()


print("Price: ", price)
print("Total: ", total)
print("Inner variable: ", inner_variable)

print()
print("=========== END: MAINTAINING SCOPE ============")
print()


#Passing arguments
def with_one_argument(first):
    print("With one argument: first - ", first)

def with_two_arguments(first, second):
    print("With two arguments: first - ", first, "and second - ", second)

with_one_argument(10)
with_two_arguments("one", 2)

print()
print("=========== END: PASSING ARGUMENTS ============")
print()


#Returning values
def add_values(first_value, second_value):
    return  first_value + second_value

result = add_values(10, 20)
print(result)
print(add_values(10, 20))


def calc_all(first_value, second_value):
    Addition = first_value + second_value
    Subtraction = first_value - second_value
    Division = first_value / second_value
    Multiplication = first_value * second_value
    return Addition, Subtraction, Division, Multiplication

first, second, third, fourth = calc_all(100, 200)
print(first, second, third, fourth)

values = calc_all(100, 200)
print(values)

print()
print("=========== END: RETURNING VALUES ============")
print()


#Callbacks: lambda expression
def subtraction_method(f_value, s_value):
    return f_value - s_value

print(subtraction_method(100, 50))

subtractor = lambda f_value, s_value: f_value - s_value
print(subtractor(100, 50))


def use_function_object(function_object, f_value, s_value):
    return function_object(f_value, s_value)

summing_machine = lambda f_value, s_value: f_value + s_value
subtractor =lambda f_value, s_value: f_value - s_value

print(use_function_object(summing_machine,30, 15))
print(use_function_object(subtractor, 30, 15))

print()
print("=========== END: CALLBACKS ============")
print()


#Placeholders
def placeholder():
    return

value_one = 50
value_two = 70

if value_one > value_two:
    print("Value 1 is not greater than Value 2")
else:
    pass

print("Statement after ifs")

print()
print("Normal loop: ", end="")
for value in range(0,5):
    print(value, end="")

print()
print("------------------------")
for value in range(0,5):
        if value == 2:
            print("#", end="")
            continue
        print(value, end="")

print()
print("------------------------")
print("Looping with pass: ", end="")
for value in range(0,5):
    if value == 2:
        print("#", end="")
        pass
    print(value, end="")

print()
print("------------------------")
print("Looping with break: ", end="")
for value in range(0,5):
    if value == 2:
        print("#", end="")
        break
    print(value, end="")


print()
print("========= END: PLACEHOLDERS ===========")
print()


#Generators
def simple_yield():
    print("First statement")
    yield
    print("Second statement")
    yield
    print("Third statement")

first_yield_test = simple_yield()
#next(first_yield_test)
#next(first_yield_test)
#next(first_yield_test)

print("This statement will not print")


def increment():
    i = 0
    while True:
        yield i
        i += 1

incrementor = increment()
print(next(incrementor))
print(next(incrementor))
print(next(incrementor))


print()
print("========= END: GENERATORS ===========")
print()


def increment():
    i = 0
    while True:
        yield i
        i += 1
inc_one = increment()
inc_two = increment()
print("First incrementor generator")
print(next(inc_one))
print(next(inc_one))
print(next(inc_one))
print("Second incrementor generator")
print(next(inc_two))


def my_range(initial_value, increment):
    i = initial_value
    while True:
        yield i
        i += increment

inc_one = my_range(0, 1)
inc_two = my_range(0, 5)

print("First generator: ", end="")
for i in inc_one:
    if i> 10:
        break;
    else:
        print(i, end=", ")
print()
print("Second generator: ", end="")
for i in inc_two:
    if i > 10:
        break;
    else:
        print(i, end=", ")