print("Въведете число 1:")
num = int(input())
print("Въведете число 2:")
num2 = int(input())
print("Изберете действие:")
deistvie = str(input())
if deistvie == "+":
    print("Резултата е:",num + num2)
elif deistvie == "-":
    print("Резултата е:",num - num2)
elif deistvie == "*":
    print("Резултата е:",num * num2)
elif deistvie == "/":
    print("Резултата е:",num / num2)
elif deistvie == "**":
    print("Резултата е:",num ** num2)

else:
    print("Действието не е налично ")


