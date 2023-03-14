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
cumpleanos=[['Juan','20','agosto',1],
            ['Maria','30','enero',0],
            ['Marcos','17','noviembre',0],
            ['Elena','2','septiembre',0],
            ['Carlos','28','marzo',1]]


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
            fecha=input('Quieres 1-buscar por mes o 2-mostrar todo:')
            if fecha=='2':
                   print(cumpleanos)
            elif fecha=='1':       
                mes_elegido = input('Que mes quieres ver: ')
                for i in range(len(mes_nombre)):
                        if mes_nombre[i] == mes_elegido:
                                mes_en_numero = (i+1)
                print(mes_en_numero)
                print(calendar.month(ano_actual, mes_en_numero))
                for i in range(len(cumpleanos)):
                        for j in range(len(cumpleanos[i])):
                          if cumpleanos[i][j]== mes_elegido:
                                 print(cumpleanos[i])
            else:
                   print('Opcion no valida')
    elif opcion == 'B'or opcion == 'b':
            nombre_persona=input('Dime el nombre de la persona: ')
            dia_persona=input('Que dia cumple años:')
            mes_persona=input('Que mes cumple años:')
            destacado_persona= input('Este cumpleaños es destacado (S/N)\n'
                                     '(Donde destacado es 0 y no destacado es 1): ')
            if destacado_persona== 'S':
                   cumpleanos.append([nombre_persona,dia_persona,mes_persona,0])
                   print('Cumpleaños añadido correctamente')
            else:
                cumpleanos.append([nombre_persona,dia_persona,mes_persona,1])
            print(cumpleanos)
            print('Cumpleaños añadido correctamente')
    elif opcion == 'C'or opcion == 'c':
            print(cumpleanos)
            nombre_eliminado=input('Cual quieres eliminar:')
            for i in range(len(cumpleanos)):
                        for j in range(len(cumpleanos[i])):
                                if cumpleanos[i][j]== nombre_eliminado:
                                        #print(cumpleanos[i])
                                        cumpleanos.remove[i][j]
                                        print(cumpleanos)
    else:
            print('Opcion incorrecta')
    continue