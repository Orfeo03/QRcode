
password = input("Enter your pasword :")

#Operatori != do të thotë not equal to (nuk është i barabartë me).

# WHILE LOOP
# A while loop repeats a block of code as long as
# its condition is True.

# != means "not equal to".

# If the password is incorrect, the loop continues.
# The user is asked to enter the password again.
# When the correct password is entered,
# the condition becomes False and the loop stops.

# If the condition never becomes False,
# an infinite loop can occur.

while password != "python123":
    print("Password is incorrect")
    password = input("Enter your password :")

