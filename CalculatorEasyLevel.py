# PYTHON calculator

operator = input ("Enter an operator(+ - * / %): ")

number1= float(input("Enter the first  number:"))
number2 = float(input("Enter the second number: "))

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)

elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print (number1 / number2)
elif operator == "%":
    print (number1 % number2);
else:
    print(f"{operator} is not a valid operator")


    #nese duam ta bejme ndryshe mund te shtojme nje variabel tjeter result dhe
    #mund ta bejme po doli me presje numrin print(round(result,3) ,ose thjesht ta
    #rrungullaposim me pa asnje presje dhjetore mbas print(round(result)

