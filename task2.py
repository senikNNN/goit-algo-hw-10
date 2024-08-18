import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Кількість випадкових точок
N = 10000

# Генерація випадкових точок
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, max(f(x_rand)), N)

# Обчислення кількості точок під кривою
points_under_curve = y_rand < f(x_rand)
integral_mc = (b - a) * max(f(x_rand)) * np.mean(points_under_curve)

print(f"Значення інтегралу методом Монте-Карло: {integral_mc:.5f}")

# Визначення функції
def f(x):
    return x**2

# Межі інтегрування
a = 0
b = 2

# Обчислення інтегралу
result, error = spi.quad(f, a, b)

print(f"Значення інтегралу з використанням функції quad: {result:.5f}")

# Візуалізація
x = np.linspace(a, b, 400)
y = f(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'r', label="f(x) = x^2", linewidth=2)
plt.fill_between(x, y, alpha=0.2, color='gray', label="Інтегральна область")

# Показ точок Монте-Карло
plt.scatter(x_rand, y_rand, color='blue', s=1, alpha=0.5, label="Випадкові точки")
plt.scatter(x_rand[points_under_curve], y_rand[points_under_curve], color='green', s=1, alpha=0.5, label="Точки під кривою")

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Інтегрування методом Монте-Карло, N = {N}')
plt.legend()
plt.grid(True)
plt.show()
