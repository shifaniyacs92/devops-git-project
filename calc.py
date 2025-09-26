# program to do the arithmetic operations (+,-,*,/) between any two given numbers using match case
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
op = input("enter the arithmetic operator (+,-,*,/):")
match op:
    case '+':
        result = a+b
        print("sum of",a,"and",b,"is",result)
    case '-':
        result = a-b
        print("diff of",a,"and",b,"is",result)
    case '*':
        result = a*b
        print("multiplication of",a,"and",b,"is",result)
    case _:
        print("invalid operator")