#format specifiers = {:flags} format a value based on what
#                                          flags are inserted


price1 = 3000.14159
price2 = -987.65
price3 = 12.34

#print(f"Price 1 is {price1}")

#:.2f do të thotë të shfaqen 2 shifra pas presjes dhjetore.
#
# print(f"Price 1 is ${price1:.3f}")  #:.1f → 3.1
# print(f"Price 2 is ${price2:.1f}")
# print(f"Price 3 is ${price3:.2f}")


#print(f"Price 3 is ${price3:10}") # Kjo te lejon qe te kete 10hapesira min
# per numrin duke llogaritur dhe numrin pra ne kete rast shtohen 5 hapesira

#print(f"Price 3 is ${price3:010}") #nese do ti vendosesh zero numrave para

#Padding means that you will add empty spaces before or after a value and alignment
#decides where the value will be added left,right or center
#
# print(f"${price1:>30}") #vendos numrin ne te djathte
# print(f"${price2:<10}") #vendos numrin ne te majte
# print(f"${price3:^10}") # vendos numrin ne qender

# Positive values if you have positive values, and you want to display plus
#
# print(f"${price1:+}")
# print(f"${price2:-}") #this is for negative values

# We have the thousand separator ,this separate the thousand values by coma

#print(f"${price1:,}")

#AND IF YOU WANT in this case we have + before and a thousand separator with 2 number after the decimal

print(f"${price1:+,.2f}")

