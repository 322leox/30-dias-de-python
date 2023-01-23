it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
len(it_companies)
it_companies.add('Twitter')
it_companies.add('Netflix', 'Iphone', 'Youtube')
it_companies.remove('Apple')
C= A.union(B)
B.intersection(C)
D= B.union(A)
B.symmetric_difference(A)
B.difference(A)
del it_companies