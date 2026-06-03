# Ejercicios de Programación Modular en Python

## Ejercicio 1: Sistema de Gestión de una Cafetería

### Contexto

Una cafetería necesita un sistema sencillo para administrar la atención de clientes durante el día.

El operador podrá:

1. Registrar una venta.
2. Reponer inventario.
3. Consultar estado de la cafetería.
4. Cerrar la cafetería.

Cada venta aumenta el dinero ganado y disminuye el inventario disponible.

---

## Vista de la pantalla final esperada

```text
Ingrese el nombre de la cafetería: Café Central

===== CAFETERÍA =====

1. Registrar venta
2. Reponer inventario
3. Ver estado
4. Cerrar cafetería

Seleccione una opción: 1

Venta registrada correctamente.

===== CAFETERÍA =====

1. Registrar venta
2. Reponer inventario
3. Ver estado
4. Cerrar cafetería

Seleccione una opción: 1

Venta registrada correctamente.

===== CAFETERÍA =====

1. Registrar venta
2. Reponer inventario
3. Ver estado
4. Cerrar cafetería

Seleccione una opción: 3

===== ESTADO ACTUAL =====

Cafetería: Café Central
Dinero acumulado: $40
Inventario disponible: 46
Ventas realizadas: 2

===== CAFETERÍA =====

1. Registrar venta
2. Reponer inventario
3. Ver estado
4. Cerrar cafetería

Seleccione una opción: 4

Cafetería cerrada.

===== RESUMEN DEL DÍA =====

Dinero total: $40
Ventas realizadas: 2
Inventario restante: 46
```

---

## Variables iniciales

Dentro de `main()` crea las siguientes variables:

```python
nombre_cafeteria
dinero
inventario
ventas_realizadas
```

Valores sugeridos:

```python
dinero = 0
inventario = 50
ventas_realizadas = 0
```

---

## Funciones sugeridas

### mostrar_menu()

**Responsabilidad**

Mostrar las opciones disponibles para el usuario.

### registrar_venta(inventario, dinero, ventas_realizadas)

**Responsabilidad**

Simular la venta de un producto.

#### Pistas

- Cada venta debe disminuir el inventario.
- Cada venta debe aumentar el dinero recaudado.
- Debe aumentar el contador de ventas realizadas.

#### Preguntas guía

- ¿Cuántas unidades se venden por operación?
- ¿Cuánto dinero genera cada venta?
- ¿Qué ocurre si ya no quedan productos disponibles?

#### Retorno esperado

```python
inventario, dinero, ventas_realizadas
```

### reponer_inventario(inventario)

**Responsabilidad**

Agregar nuevas unidades al inventario.

#### Pistas

- Solicita una cantidad al usuario.
- Suma esa cantidad al inventario actual.

#### Preguntas guía

- ¿Debe permitirse ingresar números negativos?
- ¿Qué mensaje mostrarías cuando el inventario sea actualizado?

#### Retorno esperado

```python
inventario
```

### mostrar_estado(nombre_cafeteria, dinero, inventario, ventas_realizadas)

**Responsabilidad**

Mostrar la información actual de la cafetería.

### main()

**Responsabilidad**

Coordinar toda la aplicación.

#### Pistas

- Crear variables iniciales.
- Ejecutar el menú dentro de un ciclo.
- Invocar las funciones necesarias según la opción elegida.
- Finalizar cuando el usuario seleccione cerrar cafetería.

---

## Desafíos adicionales

1. Agregar una opción para eliminar productos dañados.
2. Calcular la ganancia promedio por venta.
3. Mostrar advertencia cuando el inventario sea menor a 10 unidades.
4. Reemplazar `if-elif` por `match-case`.
5. Mostrar mensajes descriptivos después de cada acción.

---

# Ejercicio 2: Centro de Entrenamiento Pokémon

## Contexto

Un entrenador Pokémon está preparando a su equipo para un torneo.

El sistema permitirá:

1. Entrenar Pokémon.
2. Curar Pokémon.
3. Participar en combate.
4. Ver estadísticas.
5. Salir.

Cada acción afectará la energía, el nivel o las victorias acumuladas.

---

## Vista de la pantalla final esperada

```text
Ingrese el nombre del entrenador: Ash

===== CENTRO DE ENTRENAMIENTO =====

1. Entrenar
2. Curar
3. Combatir
4. Ver estadísticas
5. Salir

Seleccione una opción: 1

Tu Pokémon ha entrenado.

===== CENTRO DE ENTRENAMIENTO =====

1. Entrenar
2. Curar
3. Combatir
4. Ver estadísticas
5. Salir

Seleccione una opción: 3

¡Combate ganado!

===== CENTRO DE ENTRENAMIENTO =====

1. Entrenar
2. Curar
3. Combatir
4. Ver estadísticas
5. Salir

Seleccione una opción: 4

===== ESTADÍSTICAS =====

Entrenador: Ash
Energía: 70
Nivel: 2
Combates ganados: 1

===== CENTRO DE ENTRENAMIENTO =====

1. Entrenar
2. Curar
3. Combatir
4. Ver estadísticas
5. Salir

Seleccione una opción: 5

Fin del entrenamiento.

===== RESUMEN FINAL =====

Entrenador: Ash
Nivel alcanzado: 2
Combates ganados: 1
Energía restante: 70
```

---

## Variables iniciales

Dentro de `main()`:

```python
nombre_entrenador
energia
nivel
combates_ganados
```

Valores sugeridos:

```python
energia = 100
nivel = 1
combates_ganados = 0
```

---

## Funciones sugeridas

### mostrar_menu()

Mostrar las opciones disponibles para el entrenador.

### entrenar(energia, nivel)

**Responsabilidad**

Realizar una sesión de entrenamiento.

#### Pistas

- El entrenamiento consume energía.
- El entrenamiento aumenta el nivel.

#### Preguntas guía

- ¿Cuánta energía debería consumir?
- ¿Cuánto debería aumentar el nivel?

#### Retorno esperado

```python
energia, nivel
```

### curar(energia)

**Responsabilidad**

Recuperar energía.

#### Pistas

- La energía no debe superar un límite máximo.
- Define ese límite dentro de tu lógica.

#### Preguntas guía

- ¿Qué ocurre si el Pokémon ya tiene energía máxima?
- ¿Cuántos puntos de energía recupera?

#### Retorno esperado

```python
energia
```

### combatir(energia, combates_ganados)

**Responsabilidad**

Participar en una batalla.

#### Pistas

- Combatir consume energía.
- Si hay suficiente energía, aumenta el número de victorias.

#### Preguntas guía

- ¿Cuál será la energía mínima para poder combatir?
- ¿Qué mensaje mostrarás cuando no haya energía suficiente?

#### Retorno esperado

```python
energia, combates_ganados
```

### mostrar_estadisticas(nombre_entrenador, energia, nivel, combates_ganados)

**Responsabilidad**

Mostrar toda la información actual del entrenador.

### main()

**Responsabilidad**

Coordinar todo el programa.

#### Pistas

- Crear variables iniciales.
- Ejecutar un ciclo principal.
- Invocar las funciones según la opción seleccionada.
- Finalizar cuando el usuario decida salir.

---

## Desafíos adicionales

1. Agregar experiencia además del nivel.
2. Implementar un sistema de captura de Pokémon.
3. Agregar varios Pokémon al equipo.
4. Mostrar mensajes detallados después de cada acción.
5. Utilizar `match-case`.
6. Mostrar un resumen completo al finalizar.

---

## Preguntas de reflexión para ambos ejercicios

1. ¿Cuál es la responsabilidad exacta de cada función?
2. ¿Qué información necesita recibir cada función?
3. ¿Qué información debe devolver?
4. ¿Qué variables deben vivir únicamente dentro de `main()`?
5. ¿Cómo evitarías repetir código?
6. ¿Qué ventajas tiene dividir el programa en varias funciones?
7. ¿Cómo sería el programa si toda la lógica estuviera escrita en un único bloque de código?
