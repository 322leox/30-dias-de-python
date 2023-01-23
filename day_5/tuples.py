vacia= []
juegos= ['pelota', 'cartas', 'barbie', 'robot', 'osito', 'coche', 'parchis']
print(len(juegos))
unos_juegos= juegos[0,3,6]
print(unos_juegos)
tipos_de_datos_mixtos=['irene', '17', '160', 'soltera', 'C.S.Catalina']
it_companies= ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
print(it_companies)
print(len(it_companies))
algunas= it_companies[0,1,6]
it_companies.append('Netflix')
print(it_companies)
mayuscula= it_companies[2]
print(mayuscula.upper)
existe= 'Facebook' in it_companies
it_companies.sort()
it_compaines2 = it_companies
it_compaines2.remove('Facebook', 'Google', 'Microsoft')
it_compaines3 = it_companies
it_compaines3.remove('Amazon', 'Oracle', 'IBM')
print(it_compaines3)
print(it_compaines2)
it_companies.remove('Netflix')

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
lista= front_end + back_end
print(lista)
full_stack= lista
full_stack.insert(10, 'Python',11 'SQL')
