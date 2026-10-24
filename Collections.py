# collection = single "variable" used to store multiple values
# List = [] ordered and changeable.Duplicates OK
# Set = {} unordered and immutable,but ADD/Remove Ok.No duplicates
# Tuple = () ordered and unchangeable.Duplicates Ok.Faster

#COLLECTIONS are a singe variable to store multiple values


#fruit = "apple"
fruits=["apple","orange","banana","coconut"]  #This is called a list.We can store []
# multiple valiables with a,.This values are ordered and changeable

#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))

#Use in operator we can find if a value is in variable
#print("apple" in fruits) #This returns a boolean

#fruits[0] = "pineaple" #Using an index you can reassign one of the values
# fruits.append("pineapple") #to add an element to the end of the list use this
# fruits.remove("apple")  #to remove an element from a list
#fruits.insert(0,"pineapple") #we use this method to add an element in a position in the list
#fruits.sort() #this method makes the element of the list in alphabetical order
#fruits.reverse() #this reverse the list
#fruits.clear() #Metoda clear() heq të gjithë elementet nga lista, duke e lënë atë bosh.
#print(fruits.index("banana")) #this method helps us find the position of an element in the list
#print(fruits.count("banana")) #counts how much time is an element in the list




print(fruits)




#print(fruits[0:3]) #if we want just to print one of them we can give them an index
#With the index operator,you could set a beginning index,an ending index and a step

#Another thing we can do with collections is that you can iterate over them with
#a for loop

# for fruit in fruits:
#     print(fruit)

#TO LIST THE DIFFERENT METHODS THAT ARE AVAILABLE TO A COLLECTION YOU CAN USE A
# DIR FUNCTION.with this fuction add your collection fruits

