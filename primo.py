# This code takes in an integer from stdin and tells if the number is a prime (primo) or not. It uses
# the theorem that says that a number is a prime if and only if it has a divisor lesser or equal
# than its square root.

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
