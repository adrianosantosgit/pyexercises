'''
co = float(input('Valor do cateto oposto: \n'))
ca = float(input('Valor do cateto adjacente: \n'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa nesse caso é : {:.2f}'.format(hi))
'''

#Usando biblioteca math temos
import math
co = float(input('Valor do cateto oposto: \n'))
ca = float(input('Valor do cateto adjacente: \n'))
hi = math.hypot(co, ca)
print('A hipotenusa nesse caso é : {:.2f}'.format(hi))
