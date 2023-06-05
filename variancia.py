""" Variancia

Como a variancia e calculada e  built-in functions usadas.

"""

import numpy as np
import statistics


def calcular_variancia(data):  # Criando uma funcao que usa a formula da variancia
    n = len(data)  # Contando a quantidade de dados
    media = sum(data) / n  # Calculando a media
    variancia = sum((x - media) ** 2 for x in data) / n  # Usando a formula da variancia
    return variancia  # Retorna a variancia


# Exemplo de uso com a funcao criada acima:
numeros = [2, 4, 6, 8, 10]   # Lista com os dados
resultado = calcular_variancia(numeros)  # Chamando a funcao
print('Variancia:', resultado)  # Mostra o resultado


# Usando o numpy.var
numeros1 = np.var(numeros)
print('Variancia usando numpy.var:', numeros1)
