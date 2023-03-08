import math
import timeit
import numpy as np
import matplotlib.pyplot as plt

def taylor_seno(x, grau):
    f = x
    seno = x
    for n in range(1, grau+1):
        f = -f * x**2 / ((2*n) * (2*n+1))
        seno += f
    return seno

def pade_seno(x):
    p = [71/240, -71/1152, 71/8064, -71/72576, 71/798336]
    q = [1, -1/6, 1/120, -1/5040, 1/362880]
    u = x*x
    num = p[4]
    for i in range(3, -1, -1):
        num = p[i] + num * u
    den = q[4]
    for i in range(3, -1, -1):
        den = q[i] + den * u
    return x * num / den

# Intervalo de ângulos de -π/4 a π/4
x = np.linspace(-math.pi/4, math.pi/4, num=1000)

# Cálculo dos valores do seno usando a função seno, série de Taylor e polinômio de Padé
seno = np.sin(x)
seno_taylor = np.array([taylor_seno(xi, 11) for xi in x])
seno_pade = pade_seno(x)

# Cálculo dos erros
erro_taylor = np.abs(seno - seno_taylor)
erro_pade = np.abs(seno - seno_pade)

# Plotagem do gráfico dos erros
plt.plot(x, erro_taylor, label='Erro série de Taylor')
plt.plot(x, erro_pade, label='Erro polinômio de Padé')
plt.xlabel('Ângulo (rad)')
plt.ylabel('Erro')
plt.legend()
plt.show()

# Definir um array com 1000 valores de -π/4 a π/4
valores = np.linspace(-np.pi/4, np.pi/4, num=1000)

# Medição do tempo de execução da função pade_seno para 1000 valores de entrada
tempo_pade = timeit.timeit(lambda: [pade_seno(x) for x in valores], number=1000)

# Medição do tempo de execução da função taylor_seno para 1000 valores de entrada
tempo_taylor = timeit.timeit(lambda: [taylor_seno(x, 11) for x in valores], number=1000)

print(f"Tempo de execução polinômio de Padé: {tempo_pade:.5f}")
print(f"Tempo de execução série de Taylor: {tempo_taylor:.5f}")