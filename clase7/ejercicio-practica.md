# Reto: El Radar de Tráfico Inteligente

Vamos a diseñar el software para un radar de velocidad de la policía. El sistema debe recibir la distancia recorrida por un auto y el tiempo que tardó, calcular su velocidad y determinar si debe recibir una multa por exceso de velocidad.

Aplicaremos la regla de oro de la programación modular: **Cada función tiene un solo trabajo en la vida.**

- Una función solo hace el cálculo físico.
- Una función solo evalúa la ley (`if-else`).
- Una función solo da avisos en pantalla (`print`).
- El sistema central solo actúa como el policía que opera el radar.

---
### Modelo de salida en pantalla
#### Escenario A: El conductor respeta la ley (Sin multa)

```plaintext
--- INICIANDO CONTROL DE TRÁFICO ---
Ingrese los kilómetros recorridos por el auto: 150
Ingrese las horas empleadas en el recorrido: 1.5

 === PANEL DEL RADAR DE TRÁFICO ===
Velocidad detectada: 100.0 km/h
Resultado: Vehículo dentro del rango permitido.
```
#### Escenario B: El conductor excede el límite de velocidad (Con multa)

```plaintext
--- INICIANDO CONTROL DE TRÁFICO ---
Ingrese los kilómetros recorridos por el auto: 140
Ingrese las horas empleadas en el recorrido: 1.0

 === PANEL DEL RADAR DE TRÁFICO ===
Velocidad detectada: 140.0 km/h
Resultado:  MULTA GENERADA. Exceso de velocidad detectado.
```