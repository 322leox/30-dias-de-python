import calendar
from datetime import datetime
import os


# Variables que almacenan la fecha actual del sistema
fecha_actual = datetime.now()
mes_actual = fecha_actual.month
ano_actual = fecha_actual.year


#limpia la pantalla
os.system("cls") 

# Almacena el nombre de los meses 
mes_nombre = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre", "octubre","noviembre","diciembre"]

# Almacena los datos de cumpleaños [Nombre, año, mes, destacado]
cumpleanos = ["Maria",30,"febrero",1],["Juan",5,"junio",0],["Julian","23","noviembre",1]

# Imprime el calendario con el mes actual
print(calendar.month(ano_actual, mes_actual))

while True:
    print('Calendario de cumpleaños.')
    print('=========================')

    print('A- Ver los cumpleaños guardados\n'
          'B- Añadir un cumpleaños\n'
          'C- Eliminar un cumpleaños\n')
    opcion= input('Introduce una opción: ')
    
    if opcion =='A' or opcion == 'a':
            # seleccion ver los cumpleaños guardados
            os.system("cls") 
            print('Ver los cumpleaños guardados')
            mes_elegido = input('Que mes quieres ver: ')
            for i in range(len(mes_nombre)):
                   if mes_nombre[i] == mes_elegido:
                          mes_en_numero = (i+1)
            print(mes_en_numero)
            print(calendar.month(ano_actual, mes_en_numero))
    
    elif opcion == 'B'or opcion == 'b':
            # seleccion añadir un cumpleañosA

            print('Hola')
    elif opcion == 'C'or opcion == 'c':
            # seleccion eliminar un cumpleños
            print('hola')
    else:
            print('Opcion incorrecta')
    continue

