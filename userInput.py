#input() A function that prompts the user to enter data
# Returns the entered data as a string

name =input("What is your name?")
age = input("How old are you?:")
#or shortly we can do this age = int (input("How old are you?:"))

#before doing this duhet ta kthejme input ne integer pasi returns the entered data as a string
age = int (age)
age = age + 1



print(f"Hello {name} !")
print("Happy Birthday!")
print(f"You are {age} years old")
