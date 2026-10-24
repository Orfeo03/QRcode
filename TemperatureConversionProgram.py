#Temperature Conversion Program

temperature = float(input("Enter your temperature in Celsius/Fahrenheit: "))
unit = input("Is this temperature in Celsius or Fahrenheit?  (C or F): ")

if unit == "C":
    converter =round((temperature) * 9 / 5 + 32, 1)
    print(f"The temperature in Fanhreinheit is : {converter} F ")

elif unit == "F":
    converter = round((temperature) - 32 * 5 / 9 , 1)
    print(f"The temperature in Celsius is: {converter}C")
else:
    print(f"{unit}is an invalid unit of measurement")

#Bej kujdes me kllapat te temperature
# pasi duhet ta mbyllesh sepse kur e ben round del gabim






