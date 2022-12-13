a= '30'
b= 'Days'
c= 'of'
d= 'Python'
e= ' '
Completa= a+e+b+e+c+e+d
print(Completa)

f='Coding'
g='For'
h='All'
one_completa= f+e+g+e+h
print(one_completa)
empresa= one_completa
print(empresa)
print(len(empresa))
print(empresa.upper())
print(empresa.lower())
print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())

print(empresa.count('Coding'))
print(empresa.replace('Coding', 'Python'))
print(empresa.replace('All', 'Everyone'))
print(empresa.split(   ))
redes="Facebook, Google, Microsft, Apple, IBM, Oracle, Amzon"
print(redes.split( ))
first_letter= empresa[0]
print(first_letter)
ten= empresa[10]
print(ten)
empresa_one= 'Python for everyone'
acr= empresa_one[0]
oni= empresa_one[7]
mo= empresa_one[11]
acronimo= acr+oni+mo
print(acronimo)
abre=empresa[0]
viatu= empresa[7]
ra=empresa[11]
abreviatura= abre+viatu+ra
print(abreviatura)

letra_a= 'C'
letra_b= 'F'
letra_c= 'l'
print(empresa.index(letra_a))
print(empresa.index(letra_b))
print(empresa.index(letra_c))
oracion= 'No puede terminar una oración con porque porque porque es una conjunción'
oculta='porque'
print(oracion.index(oculta))
print(oracion.rindex(oculta))

frase= 'No puedes terminar una oración con porque porque porque es una conjunción'
elimina= 'porque porque porque'
print(frase.strip('porque porque porque'))
print(frase.index(oculta))