#Concession Stand Program

#dictionary{key:value}

concessions = {"Popcorn":"$1.00",
               "Hot DOg":"$2.00",
                "Giant Pretzel":"$2.00",
                 "Asst Cand":"$1.00",
               }


food = input("What concession would you like?").lower()


if concessions.get("Popcorn"):
    print(f"The concession is {concessions['Popcorn']}")
elif concessions.get("Hot DOg"):
    print(f"The concession is {concessions['Hot DOg']}")
elif concessions.get("Giant Pretzel"):
    print(f"The concession is {concessions['Giant Pretzel']}")
elif concessions.get("Asst Cand"):
    print(f"The concession is {concessions['Asst Cand']}")
else:
    print(f"You did not enter a concession")




