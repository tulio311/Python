def palindromo(palabra):
    palabra = palabra.replace(' ','')
    print(palabra)
    n = int(len(palabra) / 2)
    palabraInvertida = palabra[::-1]

    if palabra[:n] == palabraInvertida[:n]:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Palindromo')
    else:
        print('No Palindromo')

if __name__ == '__main__':
    run()



