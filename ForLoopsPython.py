#for loops = execute a block of code a fixed number of times
#            You can iterate over a range,string , sequence ,etc.

#for loop përdoret për të përsëritur një bllok kodi
# duke kaluar nëpër elemente të një sekuence, si numra, shkronja ose lista.

# - for → Fillon ciklin.
# - x → Variabli që merr një vlerë të re në çdo përsëritje.
# - in → Merr vlerat nga sekuenca.
# - range(1, 11) → Gjeneron numrat nga 1 deri në 10.
# - print(x) → Printon vlerën aktuale të x.
# Kujdes: Numri i fundit te range() nuk përfshihet!

# for x in range(1,11):
#     print(x)
#
# print("Happy new year")

#kemi dhe reversed range
#perseri numri i fundit i pari ne kte rast nuk perfshihet

for x in reversed(range(1,11)):
    print(x)