# -*- encoding: utf-8 -*-

def main():
  	ej4()

def ej2():
	flag=True	
	while flag:
		num=int(input('Escribe un numero par: '))
		if ((num%2)==0):
			flag=False

def ej3():
	num=2
	for i in range(15):
		print num 
		num=num*2

def ej4():
	cadena=raw_input('Escribe un texto: ')
	vocales=['a','e','i','o','u']
	num=len(cadena)
	numvoc=0
	while num>0:
		for i in ['a','e','i','o','u']:
			if (cadena[num-1]==i):
				numvoc+=1
		num-=1
	print "El numero de vocales es: " + str(numvoc)

def otraEj4():
	vocales = "aeiou"
	palabra = raw_input("Introduzca palabra: ")

	for letra in palabra:
	    print letra ,
	    if letra.lower() in vocales:
	        print "es una vocal"
	    else:
	        print "es una consonante"

def ej5():
	print "vacio"

		
if __name__ == "__main__":
    main()