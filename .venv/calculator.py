num = float(input("Molq vavedete chislo 1:"))
num2 = float(input("Molq vavedete chislo 2:"))
deistvie = input("Molq vavedete deistvie 1:")
if deistvie ==  "+" :
    print("Rezultata e :" , num + num2)
elif deistvie == "-" :
    print("Rezultata e : ", num - num2)
elif deistvie == "*":
    print("Rezultata e : ", num * num2)
elif deistvie == "/" :
    print("Rezultata e : ", num / num2)

else:
    print("Error")


