# logical operators = evaluate multiple conditions (or, and ,not)
# or = at least one condition must be true
# and = both conditions must be true
# not = invert the condition (not False, not True


temp = 20
is_sunny = True

#for and operator 2 conditions must be true if not the conditon is going to pass
if temp >= 28 and is_sunny:
    print("it is hot outside♨️")
    print("It is Sunny☀️")
elif temp<=0 and is_sunny:
    print("It is COLD outside 🥶")
    print ("It is Sunny ☀️")
elif temp < 28 and temp > 0 and is_sunny:
    print("It is WARM outside 🙂")
    print("It is sunny")

