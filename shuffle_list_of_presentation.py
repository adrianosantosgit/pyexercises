#Solicite ao usuário input de pessoas a ser sorteadas e apressente na tela o resultado
#import apenas modulo necessario
from random import shuffle

n1 = str(input('Nome do aluno: \n'))
n2 = str(input('Nome do aluno: \n'))
n3 = str(input('Nome do aluno: \n'))
n4 = str(input('Nome do aluno: \n'))

lista = [n1, n2, n3, n4]

shuffle(lista)

print('O aluno escolhido foi: {}\n'.format(lista))
