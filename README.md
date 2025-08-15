# Simulación de la Inestabilidad Two-Stream

Este proyecto simula el movimiento de partículas en un plasma electrostático unidimensional utilizando el método **PIC** (*Particle in Cell*).  
Se implementa en **Python** y permite visualizar el fenómeno de la **inestabilidad two-stream** mediante una animación en espacio de fases.

---

## 📜 Descripción
La simulación distribuye aleatoriamente un gran número de partículas en una línea de longitud \(L\), dividida en celdas de tamaño \(\Delta x\).  
Se calcula la densidad de carga en cada celda, se determina el campo eléctrico resolviendo la ecuación de Maxwell en 1D y se actualizan posiciones y velocidades usando las ecuaciones de movimiento.  
El resultado final es una animación que muestra cómo evoluciona el sistema y cómo emerge la inestabilidad two-stream.

---

## 🧮 Formulación matemática

El método **PIC** en 1D se basa en:

1. **Cálculo de densidad de carga:**
\[
\rho_i = \frac{N_i}{N_p} - 1
\]
donde \(N_i\) es el número de partículas en la celda \(i\), y \(N_p\) es el número total de partículas.

2. **Campo eléctrico a partir de la ecuación de Maxwell:**
\[
\frac{dE}{dx} = \rho
\]
Integrando numéricamente:
\[
E_i = \Delta x \sum_{j=0}^i \rho_j - \langle E \rangle
\]

3. **Ecuaciones de movimiento:**
\[
\frac{dv}{dt} = -E(x)
\]
\[
\frac{dx}{dt} = v
\]

4. **Condiciones de borde periódicas:**
\[
x \rightarrow x \ \mathrm{mod} \ L
\]

---

## 🎯 Objetivos
### Objetivo general
- Simular el movimiento de partículas en un plasma electrostático.

### Objetivos específicos
1. Formular las ecuaciones necesarias para el modelo.
2. Implementar en Python un código que realice la simulación.
3. Visualizar el fenómeno de la inestabilidad two-stream.

---

## 🛠️ Metodología
1. Verificar condiciones de borde (periódicas).
2. Calcular la densidad de carga en cada celda.
3. Estimar el campo eléctrico.
4. Actualizar posiciones y velocidades de las partículas en cada paso temporal.
5. Generar una animación del espacio de fases.

---

## 📊 Resultados esperados
- Descripción correcta del movimiento de partículas en 1D.
- Representación visual de la inestabilidad two-stream.
- Código eficiente capaz de manejar decenas de miles de partículas.

---

## 📦 Requisitos
Instalar las librerías necesarias:
```bash
pip install numpy matplotlib tqdm
