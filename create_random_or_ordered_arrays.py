import numpy as np

# Define the range and size
low = 1
high = 82
size = (9, 9)

# Create a shuffled list of unique integers
deck = list(range(low, high)) 
np.random.shuffle(deck)

#Create a ordered list of unique integers
#deck = np.arange(low, high)

# Generate non-repeating random integers
result = np.array(deck[:np.prod(size)]).reshape(size)

print('\n',result, '\n')

'''
Generate array that can have repeated values
import random
import numpy

#Criar o array AxB com numeros aleatorios entre X e Y

num = numpy.random.randint(1,201, (3,3))

print("\nNumeros Aleatorios: \n\n", num, '\n')
'''
