a = input("altezza : ")
b = input("peso : ")
operatore1 = int(a)
operatore2 = int(b)

def status(a, b):
    if a > 160 and b > 60:
        print("obesità moderata, Mettiti a dieta per un breve periodo!!!")
    else:
        print("stato di salute nella norma")

    return a and b

print("il tuo stato di salute è " + str(status(operatore1,operatore2)))
