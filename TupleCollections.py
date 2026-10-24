# collection = single "variable" used to store multiple values
# List = [] ordered and changeable.Duplicates OK
# Set = {} unordered and immutable,but ADD/Remove Ok.No duplicates
# Tuple = () ordered and unchangeable.Duplicates Ok.Faster

#A tuple is a collection that is sorrounded with a set ,()

fruits = ("apple", "banana", "cherry","coconut")


#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("cherry" in fruits) #Using the in operator,we can find if a value is found
# within our tipple.It returns true or false

#print(fruits.index("apple")) #this method is used when
# you want to find the position of an element in a tuple

#print(fruits.count("coconut"))

#You can iterate overthem using a for loop
for fruit in fruits:
    print(fruit)








