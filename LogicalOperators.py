# logical operators = evaluate multiple conditions (or, and ,not)
# or = at least one condition must be true
# and = both conditions must be true
# not = invert the condition (not False, not True

temp = 25
is_raining = False

#In logical operator at least one condition must be true and it's okay 

if temp > 35 or temp < 0 or is_raining:
    print ("The outdoor event is cancelled")
else:
    print (" The outdoor event is still scheduled ")
