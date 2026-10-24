# logical operators = evaluate multiple conditions (or, and ,not)
# or = at least one condition must be true
# and = both conditions must be true
# not = invert the condition (not False, not True

#Sure. In Python, not reverses a Boolean condition:
#- True → False
#- False → True

is_raining = True

if not is_raining:
    print("You don't need an umbrella.")
else:
    print("Raining.")