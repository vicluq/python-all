'''
NOTE Numpy é uma lib que lida com numeros e operações com numeros

- Numpy vs Listas -> numpy eh mais rapido pois os array numpy sao fixos em tipo (m tem check de type)
    - Numpy usa inteiros de menos tamanho em bytes, pois eh mais otimizado, logo mais rapido
    - Em numpy, os blocos de memoria dos arrays sao contínuos em sequencias de indexes grandes tipo em C (fixo array) entao eh mais rapido de acessar
    - Multiplicar listas em py, nao rola, mas em numpy posso fazer [..] * [..] 
      Ele multiplica os elementos de mesmo indice, retornando um novo array
'''
import numpy as np

# Criando Numpy Arrays
arr = [2, 5, 12, 6]
npArr = np.array(arr) # Basic syntax -> np.array(list, dtype="...")

# Numpy arrays só com zeros, uns
onlyZero = np.zeros((2, 2)) # -> np.zeros(shape(lines, columns), dtype)
print(onlyZero)

onlyOnes = np.ones((3, 4)) # -> np.ones(shape(lines, columns), dtype)
print(onlyOnes)

# Numpy arrays com elementos sendo um range
rangeArray = np.arange(2, 12) # -> np.arange(start, stop, step, dtype=None, *, like=None)
print(rangeArray)

# SORTING
sortedNpArr = np.sort(npArr) # -> Podemos escolher o algoritmo, o padrão é o quicksort 

# Concatenando arrays
arr1 = np.array([1, 5, 3])
arr2 = np.array([8, 55, 3])
concatArr = np.concatenate((arr1, arr2)) # -> uso tuplas para passar eles (dim devem ser iguais)
                                         # -> axis = 0 | 1 | None

# Propriedades dos Arrays: shape, size (length), ndim (dimensoes/axis)
print(npArr.size)
print(onlyOnes.shape)
print(onlyZero.ndim)

# Mudando o shape -> lembrar que o novo array deve ter a mesma quantia de elementos (l * c)
newArr = npArr.reshape(2, 2) # Coloca os consecutivos ate formar uma coluna e vai p prox linha

# np.reshape(npArr, newshape=(l, c), order='C')

# Adicionando mais axis

# Criar matriz identidade (passando um argumento, pois M = N)
idMatrix = np.eye(3)

# np.random.randint(low, high, quantia) -> manda um numero aleatorio de low ate high - 1 (retorna um só ou uma lista)
