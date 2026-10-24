#Python weight converter

weight = float (input("Enter your weight: "))
unit = input("kilograms or Pounds? (K or L): " )

if unit == "K" :
    weight = weight * 2.205
    unit = "Lbs"
elif unit == "L" :
    weight = weight / 2.205
    unit = "Kgs"
else:
    print(f"{unit} was not valid")

print(f" Your weight is:  {round(weight,1)} {unit}")

#This is one of the most important things to learn in Python:
# indentation determines which code belongs inside if, elif, else, loops, functions, etc.
#So Bro Code's version works because his final print() is also at 0 indentation.
#Kujdes me hapesirat Po, pikërisht. Në Python duhet të kesh shumë kujdes me hapësirat (indentation),
# sepse ato përcaktojnë se ku bën pjesë një komandë.
#
#
