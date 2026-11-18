import math

print('Hello World')
print("*" * 10)

x          = 1
unit_price = 3

print(math.ceil(2.9))

x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")
#print(type(x))
#y = x + 1

temperature = 35

if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("its nice")
else:
    print("It's cool")
print("Done")


succesful = True
for number in range(3):
    print("You're getting the job offer!", (number) * ".")
    if succesful:
        print("Successful!")
        break

else:
    print("Attempted 3 times and was rejected.")

#For...else
for x in range(5):
    for y in range(3):
        print(f"x: {x}, y: {y}")


#Iterables

for x in "Python":
    print(x)

for x in [1,2,3,4,5,6]:
    print(x)


#While loops
number = 100
while number > 0:
    print(number)
    number //= 2


#Infinit loops
while True:
    command = input("> ")
    print("ECHO", command)
    if command.lower() == "quit":
        break
