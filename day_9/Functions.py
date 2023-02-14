edad = input('ingrese su edad: ')
if edad < 18:
    print('No tiene la edad suficiente para conducir')
else:
    print('Edad suficiente para conducir')

mi_edad= input('Ingrese tu edad: ')
su_edad= input('Ingrese otra edad: ')
if mi_edad < su_edad:
    print('Usted es menor')
else: 
    print('Usted es mayor')

number_one= input('Ingrese el valor a: ')
number_two= input('ingrese el valor b: ')
if a<b:
    print('a es menor que b o b es mayor que a')
elif a>b:
    print('a es mayor que b o b es menor que a')
else:
    print('a y b son iguales')


nota= input('ingrese su calificación: ')
if nota < 49:
    print('Tienes un F')
elif 49<nota<59:
    print('Tienes una D')
elif 59<nota<69:
    print('Tienes un C')
elif 69<nota<89:
    print('Tienes una B')
elif 89<nota<100:
    print('Tienes una A')

invierno= 'diciembre','enero', 'febrero'
verano= 'junio','julio','agosto'
primavera= 'marzo', 'abril', 'mayo'
epoca= input('Ingrese un mes del año: ')
if epoca== 'diciembre''enero''febrero':
    print('Es invierno')
elif epoca=='junio''julio''agosto':
    print('Es verano')
else:
    print('es primavera')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruta= input('Di una fruta: ')
if fruta == fruits:
    print('Esa esta en la lista')
else: 
    fruits.append(fruta)
    
