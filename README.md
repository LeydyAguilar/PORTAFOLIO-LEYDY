# Analizador de Funciones Matemáticas

Este programa en Python recibe una función matemática como entrada (por ejemplo: `3*x + 4*y - 2`) e identifica:

- Las **variables** utilizadas (máximo 2)
- Las **operaciones** matemáticas presentes (`+`, `-`, `*`, `/`, `^`, etc.)

---

import re

def analizar_funcion(entrada):
    funcion = entrada.replace(" ", "")
    variables = sorted(set(re.findall(r'[a-zA-Z]', funcion)))
    if len(variables) > 2:
        print("Error: más de dos variables encontradas.")
        return
    operaciones = sorted(set(re.findall(r'[\+\-\*/\^]', funcion)))
    print("Variables encontradas:", variables)
    print("Operaciones encontradas:", operaciones)

entrada_usuario = input()
analizar_funcion(entrada_usuario)


