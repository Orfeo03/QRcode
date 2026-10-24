# collection = single "variable" used to store multiple values
# List = [] ordered and changeable.Duplicates OK
# Set = {} unordered and immutable,but ADD/Remove Ok.No duplicates
# Tuple = () ordered and unchangeable.Duplicates Ok.Faster


#As a summary,a set is a collection unordered and immutable. {}
#You can't change the values but adding and remove elements is ok

fruits = {"apple", "banana", "cherry","coconut"} #when you print them they are unordered
#so everytime you print them they will be in a different order


#fruits.add("pineapple") #with this method we can add an element
#fruits.remove("apple")  #to remove an element we use this method
#fruits.pop() #the pop method will remove whatever element is first.DON'T forget
#they are different in every order
fruits.clear() #to remove all elements we use this

print(fruits)


#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))