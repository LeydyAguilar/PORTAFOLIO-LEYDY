import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')

def ejercicio1():
    # Max 8x + 12y
    # Restricciones: x + y ≤ 15, x ≥ 5, x, y ≥ 0
    x = np.linspace(0, 15, 100)
    y = 15 - x
    x_opt, y_opt = 5, 10
    z_opt = 8*x_opt + 12*y_opt

    plt.figure(figsize=(6, 5))
    plt.fill_between(x, 0, y, where=(x >= 5), alpha=0.3, color='lightgreen', label='Región factible')
    plt.plot(x, y, 'k-', label='x + y = 15')
    plt.axvline(5, color='orange', linestyle='--', label='x = 5')
    plt.plot(x_opt, y_opt, 'ro', label='Solución óptima')
    plt.title(f'Ejercicio 1: 8x + 12y máx = {z_opt}')
    plt.xlabel('x (Front-end)')
    plt.ylabel('y (Back-end)')
    plt.legend()
    plt.show()

def ejercicio2():
    # Max 12x + 6y
    # Restricciones: 40x + 20y ≤ 520, x + y ≥ 2, x,y ≥ 0
    x = np.linspace(0, 15, 100)
    y = (520 - 40*x) / 20
    x_opt, y_opt = 13, 0  # mejor RAM
    z_opt = 12*x_opt + 6*y_opt

    plt.figure(figsize=(6, 5))
    plt.fill_between(x, 0, y, alpha=0.3, color='lightgreen', label='Región factible')
    plt.plot(x, y, 'k-', label='40x + 20y = 520')
    plt.axhline(2, color='orange', linestyle='--', label='x + y ≥ 2')
    plt.plot(x_opt, y_opt, 'ro', label='Solución óptima')
    plt.title(f'Ejercicio 2: 12x + 6y máx = {z_opt}')
    plt.xlabel('x (Servidores A)')
    plt.ylabel('y (Servidores B)')
    plt.legend()
    plt.show()

def ejercicio3():
    # Max 15x + 20y
    # Restricciones: x + y ≤ 12, x ≥ 4, y ≥ 6
    x = np.linspace(0, 12, 100)
    y = 12 - x
    x_opt, y_opt = 6, 6
    z_opt = 15*x_opt + 20*y_opt

    plt.figure(figsize=(6, 5))
    plt.fill_between(x, 6, y, where=(x >= 4) & (y >= 6), alpha=0.3, color='lightgreen', label='Región factible')
    plt.plot(x, y, 'k-', label='x + y = 12')
    plt.axvline(4, color='orange', linestyle='--', label='x = 4')
    plt.axhline(6, color='purple', linestyle='--', label='y = 6')
    plt.plot(x_opt, y_opt, 'ro', label='Solución óptima')
    plt.title(f'Ejercicio 3: 15x + 20y máx = {z_opt}')
    plt.xlabel('x (Reuniones)')
    plt.ylabel('y (Documentación)')
    plt.legend()
    plt.show()

def ejercicio4():
    # Max 50x + 30y
    # Restricciones: 5x + 3y ≤ 18, x ≤ 3
    x = np.linspace(0, 4, 100)
    y = (18 - 5*x) / 3
    x_opt, y_opt = 3, 1
    z_opt = 50*x_opt + 30*y_opt

    plt.figure(figsize=(6, 5))
    plt.fill_between(x, 0, y, where=(x <= 3), alpha=0.3, color='lightgreen', label='Región factible')
    plt.plot(x, y, 'k-', label='5x + 3y = 18')
    plt.axvline(3, color='orange', linestyle='--', label='x ≤ 3')
    plt.plot(x_opt, y_opt, 'ro', label='Solución óptima')
    plt.title(f'Ejercicio 4: 50x + 30y máx = {z_opt}')
    plt.xlabel('x (Modelos 3D)')
    plt.ylabel('y (Texturas 2D)')
    plt.legend()
    plt.show()

def ejercicio5():
    # Max 100x + 180y
    # Restricciones: 5x + 10y ≤ 50
    x = np.linspace(0, 11, 100)
    y = (50 - 5*x) / 10
    x_opt, y_opt = 0, 5
    z_opt = 100*x_opt + 180*y_opt

    plt.figure(figsize=(6, 5))
    plt.fill_between(x, 0, y, alpha=0.3, color='lightgreen', label='Región factible')
    plt.plot(x, y, 'k-', label='5x + 10y = 50')
    plt.plot(x_opt, y_opt, 'ro', label='Solución óptima')
    plt.title(f'Ejercicio 5: 100x + 180y máx = {z_opt}')
    plt.xlabel('x (Tipo A)')
    plt.ylabel('y (Tipo B)')
    plt.legend()
    plt.show()

# Menú principal
def main():
    ejercicios = [ejercicio1, ejercicio2, ejercicio3, ejercicio4, ejercicio5]
    for i, f in enumerate(ejercicios, 1):
        print(f"\nMostrando Ejercicio {i}...")
        f()
        input("Presiona Enter para continuar...")
