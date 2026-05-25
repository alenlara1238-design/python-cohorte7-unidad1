# Resumen — Funciones en Python

---

# ¿Por qué existen las funciones?

Las funciones nacen para resolver uno de los problemas más comunes en programación:

> La repetición de código.

Cuando un programador escribe las mismas instrucciones muchas veces, aparecen problemas como:

- Código desordenado
- Mayor probabilidad de errores
- Dificultad para modificar programas
- Programas difíciles de mantener

Las funciones permiten:

- Reutilizar código
- Organizar programas
- Dividir problemas grandes en tareas pequeñas
- Facilitar el mantenimiento
- Trabajar de forma modular

---

# Ejemplo SIN funciones

```python
print("Bienvenido Juan")
print("Bienvenido María")
print("Bienvenido Carlos")
```

Aquí estamos repitiendo la misma tarea varias veces.

---

# Ejemplo CON funciones

```python
def saludar():
    print("Bienvenido")
```

Ahora podemos reutilizar esa tarea cuando queramos.

```python
saludar()
saludar()
saludar()
```

---

# Sintaxis básica de una función

```python
def nombre_funcion():
    instrucciones
```

---

# Partes de una función

## 1. `def`

```python
def
```

La palabra reservada `def` significa:

> “Voy a definir una nueva función.”

Es el inicio de la creación de una función.

---

## 2. Nombre de la función

```python
saludar
```

El nombre representa la tarea que realiza la función.

Debe ser:

- Claro
- Descriptivo
- Fácil de entender

Ejemplos:

```python
calcular_promedio()
mostrar_menu()
validar_usuario()
```

---

## 3. Paréntesis

```python
()
```

Los paréntesis son obligatorios.

Más adelante permitirán enviar información a la función.

---

## 4. Dos puntos

```python
:
```

Indican que comienza el bloque de instrucciones de la función.

---

## 5. Bloque de código

```python
print("Hola")
```

Es el conjunto de instrucciones que pertenecen a la función.

Debe estar indentado correctamente.

Ejemplo:

```python
def saludar():
    print("Hola")
    print("Bienvenido")
```

---

# Importante

## Definir NO es ejecutar

Crear una función no significa ejecutarla.

```python
def saludar():
    print("Hola")
```

Aquí la función existe, pero todavía no se usa.

Para ejecutarla debemos invocarla:

```python
saludar()
```

---

# Ejemplo completo

```python
def mostrar_mensaje():
    print("Python es poderoso")

mostrar_mensaje()
```

---

# Ejercicios Progresivos y Guiados

---

# Nivel 1 — Reconocimiento

## Ejercicio 1

Observa el código:

```python
def saludar():
    print("Hola")
```

Responde:

1. ¿Cuál es el nombre de la función?
2. ¿Qué hace `def`?
3. ¿Cuál es el bloque de código?

---

## Ejercicio 2

Indica cuáles de estos nombres serían adecuados para funciones:

```python
calcular_total
x
mostrar_menu
hacer
procesar_pago
```

Explica por qué.

---

# Nivel 2 — Creación básica

## Ejercicio 3

Crea una función llamada:

```python
mostrar_nombre
```

Dentro debe imprimir tu nombre.

Luego ejecútala dos veces.

---

## Ejercicio 4

Crea una función llamada:

```python
mostrar_menu
```

Debe imprimir:

```python
1. Jugar
2. Configuración
3. Salir
```

Invoca la función tres veces.

---

# Nivel 3 — Análisis y comprensión

## Ejercicio 5

Analiza el código:

```python
def mensaje():
    print("Bienvenido")

mensaje()
mensaje()
```

Responde:

1. ¿Cuántas veces se ejecuta la función?
2. ¿Cuántas veces aparece el mensaje?
3. ¿Por qué las funciones ayudan a reutilizar código?

---

## Ejercicio 6

Corrige el error:

```python
def saludar()
    print("Hola")
```

Explica qué estaba mal.

---

# Nivel 4 — Pensamiento computacional

## Ejercicio 7

Piensa en una aplicación bancaria.

¿Qué funciones podrían existir?

Ejemplo:

- iniciar_sesion()
- retirar_dinero()

Escribe al menos 5 funciones posibles.

---

## Ejercicio 8

Imagina un videojuego.

Escribe funciones para tareas como:

- mover personaje
- atacar
- mostrar vida
- recoger objetos

No necesitas programarlas completas.
Solo diseña los nombres de las funciones.

---

# Nivel 5 — Mini reto

## Ejercicio 9

Crea un programa que tenga:

- una función para mostrar un saludo
- una función para mostrar un menú
- una función para despedirse

Luego ejecuta todas las funciones.

---

# Reflexión Final

> Las funciones no son solo sintaxis.

Son una forma de organizar el pensamiento y dividir problemas grandes en pequeñas tareas reutilizables.
