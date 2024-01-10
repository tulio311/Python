import math

def run():
    num = int(input("Escribe un número entero: "))

    if num == 1:
        print("No es primo")
        return

    a = True
    for i in range(2,int(math.sqrt(num))+1):
        if int(num / i) * i == num:
            a = False

    if a == True:
        print("Es primo")
    else:
        print("No es primo")


if __name__ == '__main__':
    run()