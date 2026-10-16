a = float(input("Enter a number: "))
deistvie = input("Enter an operation (+, -, *, /): ")
b = float(input("Enter another number: "))

if deistvie == "+":
    result = a + b
    print("Сумата е:", result)
elif deistvie == "-":
    result = a - b
    print("Разликата е:", result)
elif deistvie == "*":
    result = a * b
    print("Резултатът от умножението е:", result)
elif deistvie == "/":
    if b != 0:
        result = a / b
        print("Резултатът от делението е:", result)
    else:
        print("Грешка: Делението на нула не е позволено.")