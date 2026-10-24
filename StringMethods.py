from gettext import find

from MathMethods import result

name = input("Enter your full name:")

#The legth of a string  and name in this case
#result = len(name)
#result = name.find("f")   finds the first letter in a string
#result = name.rfind("e") #kur eshte nje String i madh llogariten dhe hapesirat pra nje hapesire nje numer

#print(result)

### String Methods: find() dhe rfind()

# - `find()` → gjen **index-in e parë** ku shfaqet një karakter ose fjalë.
# - `rfind()` → gjen **index-in e fundit** ku shfaqet një karakter ose fjalë.
# - Indeximi fillon nga `0`.
# - Hapësirat llogariten gjithashtu si karaktere dhe kanë index.
# - Kur kërkojmë një fjalë, merret index-i ku **fillon fjala**.
# - Nëse karakteri/fjala nuk gjendet, rezultati është `-1`.

# Shembull:
#
# text = "hello world hello"
# text.find("hello")   # 0
# text.rfind("hello")  # 12

#name = name.capitalize() #Kjo metode ben me shkronja kapitale nje String,por vetem fjalen e pare
#name = name.upper() #Ndersa kjo e ben te ter Stringun me shkronja te medha
#name = name.lower() #Ndersa kjo ben te ter Stringun me shkronja te vogla
#print(name)

# Metoda .isdigit() kontrollon nëse një string përmban vetëm shifra.
# isdigit() → Returns True if the string contains only digits.
# Otherwise, it returns False.

#result = name.isdigit() #Kjo rikthen true nese string permban vetem numra nese permban fjale do kthej false
result = name.isalpha() # Metoda isalpha() kontrollon nëse një string përmban vetëm shkronja
#true nese te gjitha jane shkronja, false nese ka numra,hapesire ose simbole

print(result)

#if you need a list of string methods you can write

#help(str)






