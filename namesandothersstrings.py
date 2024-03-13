#Code to show some different strings/full names possible outputs
#Código para mostrar algumas diferentes possibilidades de saídas de strings/nomes completos
#Require user full name // Solicite nome completo do usuário
nome = str(input('Insira seu nome completo: '))
print('') #Used only to print a void/null line // Usado para imprimir uma linha vazia no terminal apenas por organização
print('Seu nome em MAIUSCULAS é: ', str.upper(nome)) #Output upper case full name // Imprime nome completo em letras maíusculas
print('Seu nome em minusculas é: ', str.lower(nome)) #Output lower case full name // Imprime nome completo em letras minúsculas
print('O total de caracteres de seu nome é: ', str(len(nome)-nome.count(' '))) #Output the characters name count, without blank spaces // Para mostrar o número de caracteres sem os espacos em branco encontrados(' ')
cada = nome.split() #Create a list with each name that compose the inserted full name // Cria uma lista com cada nome inserido no nome completo
nomeemlista = [] #Create a void list to receive captalized names by for loop below // Cria uma lista vazia para receber nomes com iniciais maíusculas do for loop abaixo
print('Nome com iniciais em maíusculo: ', end='')
for nome in cada:
    print(str.capitalize(nome),' ', end='')
print('')
print('Seu primeiro nome é: {} e seu número de letras é: {}'.format(str.upper(cada[0]), len(cada[0]))) #Output first name upper case // Imprime o primeiro nome em maíusculas
print('Seu último nome é: {} e seu número de letras é: {}'.format(str.upper(cada[-1]), len(cada[-1]))) #Output last name upper case // Imprime o último nome em maíusculas
print('Seu primeiro e útimo nome em formato CREDIT CARD: {} {}'.format (str.upper(cada[0]), str.upper(cada[-1]))) #Output first and last name upper case // Imprime o primeiro e último nome em maíusculas