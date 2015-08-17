# -*- encoding: utf-8 -*-


def main():
    ej10()


def ej1():
    # Read user values until you type a pair number
    flag = True
    while flag:
        num = int(input('Escribe un numero par: '))
        if 0 == (num % 2):
            flag = False


def ej2():
    # Screen printing for the first 15 potency of two
    num = 2
    for i in range(15):
        print num
        num *= 2


def ej3():
    # Read a string from the user and for each letter indicates whether it is a vowel or a consonant
    cadena = raw_input('Escribe un texto: ')
    num = len(cadena)
    letra = 0
    while num > 0:
        print cadena[letra]
        f = True
        for i in ['a', 'e', 'i', 'o', 'u']:
            if i == cadena[letra]:
                print "es una vocal"
                f = False
                break
        if f:
            print "es una consonante"
        letra += 1
        num -= 1


def ej4():
    # Other way to read a string from the user and for each letter indicates whether it is a vowel or a consonant
    vocales = "aeiou"
    palabra = raw_input("Introduzca palabra: ")
    for letra in palabra:
        print letra,
        if letra.lower() in vocales:
            print "es una vocal"
        else:
            print "es una consonante"


def ej5():
    # From two lists of integers, ' numeros1 ' and ' numeros2 ' , creates a list that contains those values ​​which are
    # also the first in the second and print the screen. That is , it calculates the intersection of both lists
    numeros1 = [1, 7, 13, 21, 27, 29, 34, 48, 50, 51, 53, 61, 68, 74, 82, 83, 84, 87, 92, 94]
    numeros2 = [4, 6, 10, 18, 23, 29, 30, 32, 43, 54, 55, 55, 71, 76, 77, 82, 88, 92, 94, 95]
    numeros3 = []
    for i in numeros1:
        for j in numeros2:
            if i == j:
                numeros3.append(i)
    print numeros3


def ej6():
    # From two lists of integers, ' numeros1 ' and ' numeros2 ' of equal size, generate another whose first element is
    # the product of the first element in the lists ' numeros1 ' and ' numeros2 ' , and so on.
    numeros1 = [1, 7, 13, 21, 27]
    numeros2 = [4, 6, 10, 18, 23]
    numeros3 = []
    cont = 0
    for i in numeros1:
        numeros3.append(i * numeros2[cont])
        cont += 1
    print numeros3


def ej7():
    # From two lists of integers , ' numeros1 ' and ' numeros2 ' , stored in a list the result of multiplying each of
    # the elements ' numeros1 ' by , in turn , each of the elements ' numeros2 ' . That is, the resulting list will
    # have len ( numeros1 ) * len ( numeros2 ) elements
    numeros1 = [1, 7, 13, 21, 27]
    numeros2 = [8, 9, 28, 41, 55, 77]
    numeros3 = []
    for i in numeros1:
        for j in numeros2:
            numeros3.append(i * j)
    print numeros3


def ej8():
    # For each string of data from a list to print out index and the chain itself and whether the word is too short
    # (five characters or less ) or long ( more than five characters )
    frase = """ Programmers are, in their hearts, architects, and the first thing
            they want to do when they get to a site is to bulldoze the place
            flat and build something grand """
    listado = frase.split()  # listado = ["Programmers", "are", ",",...]
    index = 0
    while index < len(listado):
        if 5 >= len(listado[index]):
            print str(index) + " " + listado[index] + " sort"
        else:
            print str(index) + " " + listado[index] + " long"
        index += 1


def otroej8():
    # Other way tho make exercise 8
    frase = """ Programmers are, in their hearts, architects, and the first thing
            they want to do when they get to a site is to bulldoze the place
            flat and build something grand """
    listado = frase.split()  # listado = ["Programmers", "are", ",",...]
    for index, palabra in enumerate(listado):
        print index, "(", palabra, ") is ",
        if len(palabra) > 5:
            print "long"
        else:
            print "sort"


def ej9():
    # Get a list of integers and calculates the arithmetic average
    enteros = [1, 5, 9, 12, 13, 19, 23, 27, 29, 30, 57, 59, 67, 83, 92, 98, 100]
    print sum(enteros) / len(enteros)


def ej10():
    # Read a string of user and prints a message on screen if and only if it contains all the vowels
    palabra = raw_input("Introduzca una palabra: ")
    vocales = ["a", "e", "i", "o", "u"]
    notall = False
    for i in vocales:
        if i not in palabra:
            notall = True
            break
    if notall:
        print ("The word don't have all vowels")
    else:
        print ("The word have all vowels")


if __name__ == "__main__":
    main()
