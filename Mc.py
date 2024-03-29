import math
import timeit
import numpy as np
import matplotlib.pyplot as plt


def taylor_seno(x):
    A = -1.0/6.0
    B = 1.0/120.0
    C = -1.0/5040.0
    D = 1.0/362880.0
    E = -1.0/39916800.0

    y = x*x

    return x * (1 + y * (K + y * (M + y * (N + y * (P + Q * y)))))


def pade_seno(x):
    A = -241.0/1650.0
    B = 601.0/118800.0
    C = -121.0/2268000.0
    D = 17.0/825.0
    E = 19.0/118800.0

    y = x*x

    p = x * (1 + y * (P1 + y * (P2 + y * C)))
    q = 1 + y * (D + E * y)

    return p/q


# Intervalo de ângulos de -π/4 a π/4
x = np.linspace(-math.pi/4, math.pi/4, num=1000)

# Valores reais da função seno
seno_real = np.sin(x)

# Aproximação da função seno com a série de Taylor
seno_aprox_taylor = np.array([taylor_seno(xi) for xi in x])

# Aproximação da função seno com a série de Padé
seno_aprox_pade = np.array([pade_seno(xi) for xi in x])

# Erro absoluto da aproximação com a série de Taylor
erro_taylor = abs(seno_real - seno_aprox_taylor)

# Erro absoluto da aproximação com a série de Padé
erro_pade = abs(seno_real - seno_aprox_pade)

# Plotando o erro absoluto das aproximações das funções
plt.plot(x, erro_taylor, linestyle='-', label='Taylor')
plt.plot(x, erro_pade, linestyle='--', label='Padé')

# Definindo o título e os rótulos dos eixos do gráfico
plt.title("Erro absoluto das aproximações da função seno")
plt.xlabel("Ângulo (rad)")
plt.ylabel("Erro absoluto")

# Adicionando uma legenda ao gráfico
plt.legend()

# Mostrando o gráfico
plt.show()


# Intervalo de ângulos de -π/4 a π/4
x = np.linspace(-math.pi/4, math.pi/4, num=1000)

# Medindo o tempo de execução da função de Taylor
tempo_taylor = timeit.timeit(lambda: [taylor_seno(xi) for xi in x], number=1000)

# Medindo o tempo de execução da função de Padé
tempo_pade = timeit.timeit(lambda: [pade_seno(xi) for xi in x], number=1000)

print("Tempo de execução da função de Taylor:", tempo_taylor)
print("Tempo de execução da função de Padé:", tempo_pade)