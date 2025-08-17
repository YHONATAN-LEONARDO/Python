import numpy as np
import matplotlib.pyplot as plt

def regresion_lineal(a, b):
    n = len(a)
    sum_x = sum(a)
    sum_y = sum(b)
    sum_x2 = sum(x**2 for x in a)
    sum_xy = sum(x * y for x, y in zip(a, b))

    beta_1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    beta_0 = (sum_y * sum_x2 - sum_x * sum_xy) / (n * sum_x2 - sum_x**2)

    return beta_0, beta_1

X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

b0, b1 = regresion_lineal(X, Y)

print(f"Beta0 (intercepto): {b0}")
print(f"Beta1 (pendiente): {b1}")

# Graficar
x_line = np.linspace(min(X), max(X), 100)
y_line = b0 + b1 * x_line

plt.scatter(X, Y, color='blue', label='Datos')
plt.plot(x_line, y_line, color='red', label='Recta de regresión')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Regresión Lineal Simple')
plt.show()
