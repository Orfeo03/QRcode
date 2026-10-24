

number = int (input("Enter a number between 1 - 10:"))
#Pra per sa kohe ti nuk e ploteson kushtin nuk del dot nga loopa

while number< 1 or number > 10: #while this condition is true or the other condition is true execute the code forever
    print(f"{number} is not valid")
    number = int (input("Enter a number between 1 - 10:"))

print(f"Your number is {number}")
