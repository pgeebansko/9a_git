print("Изберете действие:")
deistvie = str(input())
f = True
while f :
    if deistvie == "+" :
        print("Въведете събираемо 1")
        n = int(input())
        print("Въведете събираемо 2")
        n2 = int(input())
        print("Резултата е:", n + n2)
    elif deistvie == "-":
        print("Въведете умаляемо")
        n = int(input())
        print("Въведете умалител")
        n2 = int(input())
        print("Резултата е:", n - n2)
    elif deistvie == "*":
        print("Въведете множител 1")
        n = int(input())
        print("Въведете множител 2")
        n2 = int(input())
        print("Резултата е:", n * n2)
    elif deistvie == "/":
        print("Въведете делимо")
        n = int(input())
        print("Въведете делител")
        n2 = int(input())
        print("Резултата е:", n / n2)
    elif deistvie == "**":
        print("Въведете число:")
        n =  int(input())
        print("Въведете степен:")
        n2 = int(input())
        print("Резултата е:", n ** n2)

    else:
        print("Действието не е налично ")




