#conditonal expression = A one-line shortcut for the if-else statement (ternary operator)
# Print or assign one of two values based on a condition
# X if conditon else Y

# value_if_true if condition else value_if_false

number =  5
a = 6
b = 7


# print ("Positive" if number > 0 else "Negative")

#Another example

#result = "EVEN" if number % 2 ==0 else "ODD"
#print(result)

max_number = a if a > b else b
min_number = a if a < b else b


print(max_number)
print (min_number)