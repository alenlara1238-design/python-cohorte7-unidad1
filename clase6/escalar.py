def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

def evaluar_promedio(promedio):
    if promedio >= 5:
        print("Aprobado")
    else:
        print("Reprobado")

def promedio(*numeros):
    cantidad = len(numeros)
    suma = sum(numeros)
    return suma / cantidad


print("---SISTEMA ESCOLAR----")

mi_promedio_juan = calcular_promedio(8,9,7)
print(f"EL promedio final es: {mi_promedio_juan}")
evaluar_promedio(mi_promedio_juan)

mi_promedio_victor = calcular_promedio(2,6,9)
print(f"EL promedio final es: {mi_promedio_victor}")
evaluar_promedio(mi_promedio_victor)


print("Función de prueba...")
print(promedio(8, 9, 10, 7, 4))      # 20.0
print(promedio)



