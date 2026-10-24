
# while loop = execute some code WHILE some condition remains true

#While është një cikël që përsërit një pjesë të kodit për sa kohë kushti është True.
#pra pa u plotesuar kushti while do ta perserise kodin

# while  kontrollon kushtin → nëse është True, përsërit kodin → nëse bëhet False, del nga cikli.


# name = input("Enter your name :")
#
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name :")
#
#     print(f"Hello {name}")

#age = int (input("Enter your age:"))

# while age <18:
#     print("You are too young")
#     age = int (input("Enter your age:"))
#
# print("You can enter")

#ANOTHER EXERCISE

age = int(input("Enter your age:"))

while age < 0:
    print ("Age can't be negative") #We let user know that they can't put number under 0
#and we give them a strategy to escape
#in this case
age = int(input("Enter your age:"))

print(f"You are {age} years old")

