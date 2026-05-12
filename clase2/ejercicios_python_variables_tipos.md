# Ejercicios de práctica — Variables y tipos de datos en Python

## Temas a practicar

- Variables
- Tipos de datos (`int`, `float`, `str`, `bool`)
- Entrada y salida de datos (`input` / `print`)
- Conversión de tipos (`int()`, `float()`, `str()`, `bool()`)

---

# Ejercicio 1 — Saludo personalizado

## Objetivo
Practicar `input()` y `print()`.

## Instrucciones

1. Solicita el nombre del usuario.
2. Guarda el valor en una variable.
3. Muestra un saludo personalizado.

## Ejemplo esperado

```python
¿Cómo te llamas? Carlos
Hola Carlos, bienvenido a Python
```

---

# Ejercicio 2 — Edad del usuario

## Objetivo
Practicar conversión a `int`.

## Instrucciones

1. Solicita la edad del usuario.
2. Convierte el valor a entero.
3. Muestra:
   - la edad actual
   - la edad dentro de 10 años

## Ejemplo esperado

```python
Ingresa tu edad: 20
Tu edad actual es 20
En 10 años tendrás 30
```

---

# Ejercicio 3 — Calculadora de suma

## Objetivo
Practicar variables numéricas.

## Instrucciones

1. Solicita dos números enteros.
2. Convierte ambos valores.
3. Muestra:
   - suma
   - resta
   - multiplicación

## Ejemplo esperado

```python
Número 1: 10
Número 2: 5

Suma: 15
Resta: 5
Multiplicación: 50
```

---

# Ejercicio 4 — Promedio de notas

## Objetivo
Practicar `float`.

## Instrucciones

1. Solicita 3 notas decimales.
2. Calcula el promedio.
3. Muestra el resultado con 2 decimales.

## Ejemplo esperado

```python
Nota 1: 4.5
Nota 2: 3.8
Nota 3: 5.0

Promedio: 4.43
```

---

# Ejercicio 5 — Datos personales

## Objetivo
Combinar varios tipos de datos.

## Instrucciones

Solicita:

- nombre (`str`)
- edad (`int`)
- altura (`float`)
- si es estudiante (`bool` simulado)

Luego muestra toda la información organizada.

## Pista

Para el booleano puedes preguntar:

```python
¿Eres estudiante? (True/False)
```

## Ejemplo esperado

```python
Nombre: Ana
Edad: 22
Altura: 1.68
Estudiante: True
```

---

# Ejercicio 6 — Conversión de temperatura

## Objetivo
Practicar operaciones con `float`.

## Fórmula

```text
F = (C × 9/5) + 32
```

## Instrucciones

1. Solicita una temperatura en Celsius.
2. Convierte a `float`.
3. Calcula Fahrenheit.
4. Muestra el resultado.

---

# Ejercicio 7 — Área de un rectángulo

## Objetivo
Practicar variables y `float`.

## Fórmula

```text
A = base × altura
```

## Instrucciones

1. Solicita:
   - base
   - altura
2. Calcula el área.
3. Muestra el resultado con 2 decimales.

---

# Ejercicio 8 — Conversión de texto a número

## Objetivo
Comprender que `input()` devuelve texto.

## Instrucciones

1. Solicita dos números SIN convertirlos.
2. Intenta sumarlos.
3. Observa el resultado.
4. Luego conviértelos usando `int()`.
5. Realiza nuevamente la suma.

## Pregunta para reflexionar

¿Por qué cambia el resultado?

---

# Ejercicio 9 — Mini formulario

## Objetivo
Practicar múltiples entradas.

## Instrucciones

Solicita:

- nombre
- ciudad
- edad
- peso

Luego muestra algo así:

```python
Hola Laura
Vives en Montería
Tienes 20 años
Pesas 55.50 kg
```

---

# Ejercicio 10 — Precio con IVA

## Objetivo
Practicar `float` y formato.

## Fórmula

```text
total = precio + (precio × iva)
```

## Instrucciones

1. Solicita el precio de un producto.
2. Usa IVA = `0.19`
3. Calcula el total.
4. Muestra:
   - subtotal
   - IVA
   - total final

## Requisito

Mostrar los valores con 2 decimales.

---

# Ejercicio 11 — Conversión de tipos

## Objetivo
Practicar conversiones explícitas.

## Instrucciones

Crea variables:

```python
numero_texto = "100"
decimal_texto = "3.14"
```

Luego convierte:

- `"100"` → entero
- `"3.14"` → float
- entero → string

Muestra el tipo antes y después usando `type()`.

---

# Ejercicio 12 — Información del producto

## Objetivo
Combinar todo lo aprendido.

## Instrucciones

Solicita:

- nombre del producto
- precio
- cantidad

Calcula:

- subtotal
- total a pagar

## Ejemplo esperado

```python
Producto: Mouse
Precio: 50.5
Cantidad: 3

Subtotal: 151.50
```

Enlace de emojis:
https://unicode.org/emoji/charts/full-emoji-list.html
