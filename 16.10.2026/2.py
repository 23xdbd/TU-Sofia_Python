n = int(input("Въведи броя на числата: "))

if n > 0:
    suma = 0
    i = 0
    while i < n:
        number = int(input("Въведи число: "))
        suma = suma + number
        i = i + 1

    print("Сумата на числата е:", suma)
else:
    print("n трябва да е по-голямо от 0!")