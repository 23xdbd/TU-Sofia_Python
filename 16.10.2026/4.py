n = int(input("Въведи цяло число n = "))

if n < 2:
    print("Въведеното число не е просто")
else:
    i = 2

    while i < n:
        if n % i == 0:
            break
        i = i + 1

    if i < n:
        print("Въведеното число не е просто")
    else:
        print("Въведеното число е просто")