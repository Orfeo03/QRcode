#Concession stand program


menu = {"pizza":3.00,
        "nachos":4.50,
        "popcorn":6.00,
        "fries":2.50,
         "pretzel":3.50,
        "soda":3.00,
        "lemonade":4.25,}

cart = []
total = 0

print ("-----------MENU-----------")
for key,value in menu.items():
    print (f"{key:10} :${value:.2f}")
print("------------------")

while True:  #if our condition is set to true,we'll need to break out of this loop
    food = (input("Select an item(q to quit): ").lower())
    if food == "q":
       break
       # menu.get(food) searches for the food in the dictionary.
       # is not None checks whether that food exists in the menu.
       # cart.append(food) adds the selected food to the shopping cart.
    elif menu.get(food) is not None:
        cart.append(food)
print("--------YOUR ORDER--------")
for food in cart:   #for food in cart: do të thotë: Për çdo ushqim që ndodhet në
    # listën cart, ekzekuto kodin brenda ciklit.
    total = total + menu.get(food) #Në çdo përsëritje
    # merr çmimin e ushqimit aktual dhe ia shton totalit ekzistues.
    print(food,end=" ")

print()
print(f"Total is: ${total:.2f}")


#