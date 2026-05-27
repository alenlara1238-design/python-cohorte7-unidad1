# Ejercicio 1: El Conversor de Divisas "AirTravel"

## Objetivo pedagógico

Este ejercicio busca que practiques cómo dividir un problema en pequeñas responsabilidades independientes.

Piensa como arquitecto de software:

- ¿Qué parte calcula?
- ¿Qué parte muestra información?
- ¿Qué parte coordina todo?

La meta no es solo que funcione, sino que el programa esté organizado correctamente.

---

# Resultado esperado

```plaintext
--- BIENVENIDO A AIRTRAVEL EXCHANGE ---
¿Cuántos dólares desea cambiar?: 150

=== RESUMEN DE CONVERSIÓN ===
Monto original: 150.0 USD
Monto en Euros: 135.0 EUR
================================
```

---

# Antes de programar, analiza

## Preguntas clave

### Sobre responsabilidades

- ¿La función que convierte dinero debería usar `print()`?
- ¿La función que imprime el resumen debería hacer cálculos?
- ¿Qué pasa si mañana cambia la tasa de conversión?
- ¿Qué pasa si luego quieren convertir a yenes o pesos?

---

# Paso 1 — Diseña las responsabilidades

Debes crear:

| Función | Responsabilidad |
|---|---|
| `convertir_usd_a_eur()` | Solo calcular |
| `mostrar_resumen()` | Solo imprimir |
| `main()` | Coordinar todo |

---

# Paso 2 — Completa la función matemática

## Tu misión

Crear una función que:

- reciba dólares
- aplique la conversión
- devuelva euros

---

## Piensa antes de escribir

### Preguntas guía

- ¿Qué dato necesita la función para trabajar?
- ¿Debe pedir datos con `input()`?
- ¿Debe mostrar resultados?
- ¿Qué debería retornar?

---

## Código base

```python
def convertir_usd_a_eur(dolares):
    tasa_conversion = 0.90

    # TU CÓDIGO AQUÍ
    # Calcula los euros

    return None
```

---

# Paso 3 — Completa la función visual

## Tu misión

Esta función no calcula.

Solo recibe datos ya listos y los muestra de forma ordenada.

---

## Preguntas guía

- ¿Esta función necesita saber cómo se hizo el cálculo?
- ¿Debería existir una multiplicación dentro de esta función?
- ¿Qué datos necesita recibir para poder imprimir?

---

## Código base

```python
def mostrar_resumen(dolares, euros):

    print("\n=== RESUMEN DE CONVERSIÓN ===")

    # TU CÓDIGO AQUÍ
    # Mostrar monto original

    # TU CÓDIGO AQUÍ
    # Mostrar monto convertido

    print("================================")
```

---

# Paso 4 — Construye el orquestador

## Tu misión

La función principal será el “director de la película”.

Debe:

1. pedir datos
2. llamar la función de cálculo
3. llamar la función visual

---

## Preguntas guía

- ¿Quién debe pedir el `input()`?
- ¿Quién conecta todas las funciones?
- ¿Dónde debería almacenarse el resultado de la conversión?
- ¿Qué función conoce todo el flujo completo?

---

## Código base

```python
def main():

    print("--- BIENVENIDO A AIRTRAVEL EXCHANGE ---")

    dolares = float(input("¿Cuántos dólares desea cambiar?: "))

    # TU CÓDIGO AQUÍ
    # Llamar función de conversión

    # TU CÓDIGO AQUÍ
    # Mostrar resumen


main()
```

---

# Reto adicional (Opcional)

## Nivel 2

Haz que el sistema también convierta a:

- pesos colombianos
- yenes
- libras

### Preguntas para pensar

- ¿Conviene crear una sola función gigante?
- ¿O varias funciones pequeñas?
- ¿Cómo evitar repetir código?

---

# Reflexión final

Cuando separas responsabilidades:

- el código se entiende más fácil
- puedes reutilizar funciones
- puedes corregir errores más rápido
- el programa escala mejor

Esto es pensamiento modular.

---

# Ejercicio 2: El Validador de Acceso "SecurePass"

## Objetivo pedagógico

Aprenderás a separar:

- la lógica de decisión
- la visualización
- la coordinación del sistema

Tu programa debe pensar como un sistema real de seguridad.

---

# Resultado esperado

```plaintext
--- CONTROL DE ACCESO SECUREPASS ---
Ingrese la edad del empleado: 17

=== ESTADO DE SEGURIDAD ===
Resultado: ACCESO DENEGADO. Área restringida para menores de edad.
==============================
```

---

# Analiza antes de programar

## Preguntas clave

- ¿Quién decide si alguien entra?
- ¿Quién solo muestra mensajes?
- ¿La función que valida debería usar `print()`?
- ¿La función visual debería contener condiciones `if`?
- ¿Qué ventaja tiene devolver `True` o `False`?

---

# Paso 1 — Diseña la arquitectura

Debes crear:

| Función | Responsabilidad |
|---|---|
| `validar_acceso()` | Decide acceso |
| `mostrar_estado()` | Imprime resultado |
| `main()` | Coordina el flujo |

---

# Paso 2 — Completa la función lógica

## Tu misión

La función debe:

- recibir una edad
- verificar si es mayor o igual a 18
- devolver `True` o `False`

---

## Preguntas guía

- ¿La función necesita imprimir mensajes?
- ¿Qué tipo de dato debería retornar?
- ¿Qué operador de comparación necesitas?
- ¿Qué ocurre exactamente cuando una función retorna un booleano?

---

## Código base

```python
def validar_acceso(edad):

    # TU CÓDIGO AQUÍ
    # Validar si cumple la edad mínima

    return None
```

---

# Paso 3 — Completa la función visual

## Tu misión

Esta función debe:

- recibir el resultado (`True` o `False`)
- mostrar el mensaje correcto

---

## Preguntas guía

- ¿La función sabe cómo se hizo la validación?
- ¿Solo necesita conocer el resultado?
- ¿Qué estructura condicional usarás?

---

## Código base

```python
def mostrar_estado(acceso):

    print("\n=== ESTADO DE SEGURIDAD ===")

    if acceso:

        # TU CÓDIGO AQUÍ
        # Mostrar acceso permitido

        pass

    else:

        # TU CÓDIGO AQUÍ
        # Mostrar acceso denegado

        pass

    print("==============================")
```

---

# Paso 4 — Construye el sistema central

## Tu misión

La función principal debe:

1. solicitar edad
2. llamar la validación
3. enviar el resultado al panel visual

---

## Preguntas guía

- ¿Quién debe usar `input()`?
- ¿Dónde se conecta todo?
- ¿Qué variable almacenará el resultado booleano?
- ¿Qué significa realmente “orquestar” un programa?

---

## Código base

```python
def main():

    print("--- CONTROL DE ACCESO SECUREPASS ---")

    edad = int(input("Ingrese la edad del empleado: "))

    # TU CÓDIGO AQUÍ
    # Validar acceso

    # TU CÓDIGO AQUÍ
    # Mostrar estado


main()
```

---

# Retos adicionales

## Nivel 2

Agrega nuevos niveles de acceso:

| Edad | Resultado |
|---|---|
| Menor de 18 | Acceso denegado |
| 18 a 59 | Acceso estándar |
| 60 o más | Acceso prioritario |

---

## Nivel 3

Crea funciones adicionales:

- una función para pedir datos
- otra para generar mensajes
- otra para validar rangos

---

# Reflexión final

Un programa profesional no es solo “código que funciona”.

Es código:

- organizado
- reutilizable
- fácil de mantener
- fácil de entender

La programación modular busca exactamente eso.
