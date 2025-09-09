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
