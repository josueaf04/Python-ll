# Calculator 

# Menú 

print('SELECCIONE LA OPERACION QUE DESEA REALIZAR:\n 1: SUMA \n 2: RESTA \n 3: MULTIPLICACION \n 4: DIVISION \n 5: VER TABLA \n 6: SALIR\n')

choice = int(input())

if choice == 1: 

    print('**SUMA** \n')

    plus = float(input('INTRODUZCA EL PRIMER VALOR: \n'))
    plus1 = float(input('INTRODUZCA EL SEGUNDO VALOR: \n'))

    def sumar (plus, plus1): 
        suma = plus + plus1
        print(f'EL RESULTADO DE LA SUMA ES: {suma}')
    sumar(plus, plus1)


elif choice == 2: 

    print('**RESTA**\n')

    minus = float(input('INTRODUZCA EL PRIMER VALOR: \n'))
    minus1 = float(input('INTRODUZCA EL SEGUNDO VALOR: \n'))

    def restar (minus, minus1): 
        resta = minus - minus1
        print(f'EL RESULTADO DE LA RESTA ES: {resta}')
    restar(minus, minus1)

elif choice == 3: 

    print('**MULTIPLICACION**\n')

    mult = float(input('INTRODUZCA EL PRIMER VALOR: \n'))
    mult1 = float(input('INTRODUZCA EL SEGUNDO VALOR: \n'))

    def multiplicar(mult, mult1): 
        multiplicacion = mult * mult1 
        print(f'EL RESULTADO DE LA MULTIPLICACION ES: {multiplicacion}')
    multiplicar(mult, mult1)

elif choice == 4: 

    print('**DIVISION**\n') 

    div = float(input('INTRODUZCA EL PRIMER VALOR: \n'))
    div1 = float(input('INTRODUZCA EL SEGUNDO VALOR: \n'))

    def dividir(div, div1): 
        division = div / div1 
        print(f'EL RESULTADO DE LA DIVISION ES: {division}')
    dividir(div, div1)

elif choice == 5: 

    print('**TABLA**\n')

    print(' 1 * 0 = 0\n 1 * 1 = 1\n 1 * 2 = 2\n 1 * 3 = 3\n 1 * 4 = 4\n 1 * 5 = 5\n 1 * 6 = 6\n 1 * 7= 7\n 1 * 8 = 8\n ')

elif choice == 6: 
    print('GRACIAS POR UTILIZAR LA CALCULADORA') 

else: 
    print('PORFAVOR INGRESE UNO DE LOS NUMEROS INDICADOS')    
        
