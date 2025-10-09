import math

# ===================================================
# MÉTODO DE NEWTON-RAPHSON (O RAPHSON SIMPLE)
# ===================================================
def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0

    print("\n" + "="*65)
    print(" MÉTODO DE NEWTON-RAPHSON - TABLA DE ITERACIONES ")
    print("="*65)
    print(f"{'Iter':<6}{'x':<15}{'f(x)':<15}{'f\'(x)':<15}{'Error':<15}")
    print("-"*65)

    for i in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)

        if abs(dfx) < 1e-10:
            print("⚠️  Error: Derivada muy pequeña. Deteniendo el método.")
            break

        x_nuevo = x - fx / dfx
        error = abs(x_nuevo - x)

        print(f"{i:<6}{x:<15.8f}{fx:<15.8f}{dfx:<15.8f}{error:<15.8e}")

        if error < tol:
            print("-"*65)
            print(f"✅ Convergencia alcanzada en {i} iteraciones.")
            print("="*65)
            return x_nuevo, i

        x = x_nuevo

    print("-"*65)
    print(f"⚠️  No se alcanzó la tolerancia después de {max_iter} iteraciones.")
    print("="*65)
    return x, max_iter


# ===================================================
# PROGRAMA PRINCIPAL (INTERACTIVO)
# ===================================================
if __name__ == "__main__":
    print("🔹 MÉTODO DE NEWTON-RAPHSON 🔹")
    print("Puedes usar funciones como: sin(x), cos(x), exp(x), log(x), etc.\n")

    # Entrada del usuario
    func_str = input("👉 Ingresa f(x): ")
    dfunc_str = input("👉 Ingresa f'(x): ")
    x0 = float(input("👉 Ingresa el valor inicial x₀: "))

    # Crear funciones a partir del texto ingresado
    def f(x):
        return eval(func_str, {"x": x, "math": math, **math.__dict__})

    def df(x):
        return eval(dfunc_str, {"x": x, "math": math, **math.__dict__})

    # Ejecutar el método
    raiz, iteraciones = newton_raphson(f, df, x0)

    # Resultados finales
    print(f"\n{'='*65}")
    print(" RESULTADOS FINALES ")
    print("="*65)
    print(f"✨ Raíz aproximada: x = {raiz:.10f}")
    print(f"✨ f(raíz) = {f(raiz):.6e}")
    print(f"🔁 Iteraciones realizadas: {iteraciones}")
    print("="*65)
