# dictionary = a collection of {key:value} pairs
#                ordered and changeable. No duplicates

#A dictionary is a structure that saves the data in forms
#key:value
# Key → çelësi me të cilin kërkojmë informacionin.
# Value → vlera që i përket atij çelësi.


capitals = {"USA":"Washigton D.C.",
           "India":"New Delhi",
            "China":"Beijing",
             "Russia":"Moscow"}

# print(dir(capitals))
# print(help(capitals))

#print(capitals.get("USA"))  #Metoda .get() kërkon një key në dictionary dhe kthen
# vlerën e tij.

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital does not exist")

#metoda .update() përdoret për të shtuar ose përditësuar elemente në dictionary.
#capitals.update({"Germany":"Berlin"})
#capitals.update({"China:Pekin"}) #ne kte rast kemi ber perditesim te ketij celesi

#To remove a key value pair,we can use the pop method
#capitals.pop("China")  #

#The popitem method will remove the latest key value pair that was inserted
#capitals.popitem()

#The clear method will cleae the dictionary
#capitals.clear()

#keys = capitals.keys() #this wiill return all the keys
#Technically,key is an object which resembles a list

#if you need keys in a dictionary ,you can use for loop
#for every in capitals keys,let's print every key

# for key in capitals.keys():
#     print(key)

#This will print all the values all the dictionary
#values = capitals.values()
#
# for value in capitals.values():
#     print(value)
#
# items = capitals.items()
# print(items)

for key,value in capitals.items():
    print(f"{key}:{value}")












