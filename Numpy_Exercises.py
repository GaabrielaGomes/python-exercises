# 1. Crie um array unidimensional (vetor) com os valores de 10 a 50. Depois, Crie uma matriz de zeros com 
# dimensões 3 x 4 e uma matriz de “uns” de dimensões 2 x 2. Finalmente, crie um array utilizando np.linspace 
# que contenha 15 valores linearmente espaçados entre 0 e 1.

# importando numpy
import numpy as np
import time
import matplotlib.pyplot as plt

print("EXERCICIOS 1\n")

# criando array unidimensional com valores de 10 a 50
array_uni = np.arange(10,51)
print(f"Array unidimensional de 10 a 50: {array_uni}\n")

# matriz de zeros com dimensões 3 x 4
matriz_zeros = np.zeros((3, 4))
print(f"Matriz de zeros 3x4: {matriz_zeros}\n")

# matriz de "uns" de dimensão 2 x 2
matriz_uns = np.ones((2, 2))
print(f"Matriz de uns 2x2: {matriz_uns}\n")

# Array com linspace (15 valores entre 0 e 1)
array_linspace = np.linspace(0, 1, num=15)
print(f"Array linspace com 15 valores entre 0 e 1: {array_linspace}\n")

# 2. Crie um array tridimensional com formato = (2, 3, 4) preenchido com números inteiros aleatórios. 
# Imprima o formato (shape), o número de dimensões (ndim) e a quantidade total de elementos (size) desse array.
print("EXERCICIOS 2\n")

# Array 3D com números aleatórios
array_3dim = np.random.randint(0, 100, size=(2, 3, 4))
print(f"Array tridimensional (2x3x4):\n{array_3dim}\n")
print(f"Formato (shape): {array_3dim.shape}")
print(f"Número de dimensões (ndim): {array_3dim.ndim}")
print(f"Quantidade total de elementos (size): {array_3dim.size}\n")

# 3. Crie um vetor com 12 elementos (0 a 11) usando np.arange. Adicione uma nova dimensão a este vetor para 
# transformá-lo em uma matriz linha e, em seguida, em uma matriz coluna usando np.newaxis
print("EXERCICIOS 3\n")

# Vetor 12 elementos
vetor_12 = np.arange(12)
print(f"Vetor original (12 elementos):\n{vetor_12}")
print(f"Shape: {vetor_12.shape}\n")

# Matriz linha
matriz_linha = vetor_12[np.newaxis, :]
print(f"Matriz linha (1x12):\n{matriz_linha}")
print(f"Shape: {matriz_linha.shape}\n")

# Matriz coluna
matriz_coluna = vetor_12[:, np.newaxis]
print(f"Matriz coluna (12x1):{matriz_coluna}\n")
print(f"Shape: {matriz_coluna.shape}\n")

# 4. Dada a matriz A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]):
# a. Extraia todos os valores maiores que 7
# b. Crie uma nova matriz contendo apenas os números pares da matriz original.
print("EXERCICIOS 4\n")

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"Matriz A:\n{A}")

# a. Valores maiores que 7
maior_sete = A[A > 7]
print(f"a) Valores maiores que 7: {maior_sete}\n")

# b. Apenas números pares
numeros_pares = A[A % 2 == 0]
print(f"b) Números pares: {numeros_pares}\n")

# 5. Gere uma matriz 5 x 5 de números aleatórios entre 1 e 100. Calcule o valor máximo,
# o valor mínimo, a média e a soma total de todos os elementos.
print("EXERCICIOS 5\n")

# Matriz 5x5 com números aleatórios entre 1 e 100
matriz_random = np.random.randint(1, 101, size=(5, 5))
print(f"Matriz 5x5 aleatória:\n{matriz_random}\n")

print(f"Valor máximo: {matriz_random.max()}")
print(f"Valor mínimo: {matriz_random.min()}")
print(f"Média: {matriz_random.mean():.2f}")
print(f"Soma total: {matriz_random.sum()}\n")

# 6. Crie uma lista com 1 milhão de números inteiros aleatórios e um array NumPy com os mesmos valores.
# Utilize a biblioteca time para comparar o tempo necessário para multiplicar cada elemento por 2 em ambos os casos. 
# Explique por que o NumPy é mais eficiente (considere a homogeneidade dos dados).
print("EXERCICIOS 6\n")

# lista e array com 1 milhão de elementos
tamanho = 1000000
lista = list(range(tamanho))
array = np.arange(tamanho)

# Teste com lista Python
inicio = time.time()
lista_multiplicada = [x * 2 for x in lista]
tempo_lista = time.time() - inicio

# Teste com NumPy
inicio = time.time()
array_multiplicado = array * 2
tempo_numpy = time.time() - inicio

print(f"Tempo com lista Python: {tempo_lista:.6f} segundos")
print(f"Tempo com NumPy: {tempo_numpy:.6f} segundos")
print(f"NumPy foi {tempo_lista/tempo_numpy:.2f}x mais rápido!\n")

print("EXPLICAÇÃO DA EFICIÊNCIA DO NUMPY: O NumPy é mais eficiente que as listas do Python porque trabalha com dados homogêneos, " \
"o que elimina verificações de tipo durante as operações. Essa padronização permite um processamento muito mais rápido, " \
"especialmente em grandes volumes de dados, tornando tarefas que levariam segundos com listas comuns executáveis em frações de" \
" segundo com NumPy.\n")

# 7. Utilize o novo gerador default_rng() para simular o lançamento de dois dados (valores de 1 a 6) 1.000 vezes. 
# Armazene os resultados em uma matriz 1000 x 2. Calcule a frequência de vezes que a soma dos dados foi igual a 7.
print("EXERCICIOS 7\n")

# Usando o novo gerador
rng = np.random.default_rng()

# Simulando 1000 lançamentos de dois dados
lancamentos = rng.integers(1, 7, size=(1000, 2))
print(f"Primeiros 10 lançamentos:{lancamentos[:10]}\n")

# Calculando a soma dos dados
soma_dados = lancamentos.sum(axis=1)

# Frequência de soma igual a 7
freq = (soma_dados == 7).sum()
percentual = (freq / 1000) * 100

print(f"Frequência de soma igual a 7: {freq} vezes")
print(f"Percentual: {percentual:.1f}%")
print(f"Probabilidade teórica: 16.67% (6 combinações em 36 possíveis)\n")

# 8. Gere um conjunto de 100 pontos aleatórios para as coordenadas X e Y usando NumPy. 
# Utilize a biblioteca matplotlib para criar um gráfico de dispersão (scatter plot) desses pontos, 
# demonstrando como o NumPy serve de base para ferramentas de visualização.
print("EXERCICIOS 8\n")

rng = np.random.default_rng(42)  

dados_x = rng.integers(0, 100, size=100)  
dados_y = rng.integers(0, 100, size=100)  

plt.figure(figsize=(7, 4))
plt.scatter(dados_x, dados_y, alpha=0.75, edgecolor="black")
plt.title("Scatter Plot — NumPy + Matplotlib")
plt.xlabel("Coordenadas X")
plt.ylabel("Coordenadas Y")
plt.grid(True, linestyle="--", alpha=0.35)
plt.show()
