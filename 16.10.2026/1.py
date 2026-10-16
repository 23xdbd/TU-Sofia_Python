n = int(input("Въведи броя на числата: "))

if n > 0:
    i = 0
    max_number = None

    while i < n:
        number = int(input("Въведи число: "))

        if i == 0:
            max_number = number
        elif number > max_number:
            max_number = number

        i = i + 1

    print("Най-голямото число е:", max_number)
else:
    print("n трябва да е по-голямо от 0!")
