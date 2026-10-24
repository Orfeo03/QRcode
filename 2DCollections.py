# A two-dimensional list is just a list made up of list
# It's very useful if you ever need a grid or matrix of data,kind of like
# an Excel Spreadsheet.

fruits =     ["apple","orange","banana","coconut"]
vegetables = ["celery","carrots","potatoes"]
meats =      ["chicken","fish","turkey"]

groceries = [fruits,vegetables,meats]


#print(groceries[1])  #the output will be the vegetables list
#print(groceries[0][1]) #with this you can print the first list and the second
#element of that list ,it's like coordinates

#print(groceries[][]) #to access an element from a 2D list you would neeed two
#indices instead of one

#if you ever need to iterate over the elements of a 2D list,you can use nested loops

for collection in groceries:
    for food in collection:
        print(food,end = " ")
    print()


# #groceries = [["apple","orange","banana","coconut"],  #you can write in this way too
#              ["celery","carrots","potatoes"],
#              ["chicken","fish","turkey"]]

