# **Programa de Estadísticas en Python (Datos Agrupados y No Agrupados)**

Este proyecto en Python realiza cálculos estadísticos básicos para conjuntos de datos agrupados y no agrupados, sin utilizar librerías externas. Se enfoca en calcular manualmente la media, la moda, la varianza y la desviación estándar, adaptándose al tamaño de los datos ingresados.

## **Características del Programa**

- **Datos No Agrupados** (menos de 30 elementos):
  - Calcula la **media aritmética**, **moda**, **varianza**, **desviación estándar**, **valor mayor** y **menor**.
  
- **Datos Agrupados** (30 o más elementos):
  - Calcula la **media aritmética**, **moda**, **varianza**, y **desviación estándar** sin necesidad de librerías externas.

## **Características**

- Cálculos para **datos no agrupados** (menos de 30 elementos).
- Cálculos para **datos agrupados** (30 o más elementos) mediante el ingreso de frecuencias.
- Funciones para calcular manualmente:
  - **Media aritmética**
  - **Moda**
  - **Varianza**
  - **Desviación estándar**
  - **Mayor** y **menor** valor (para datos no agrupados)

---
## **Requisitos Previos**

- **Python 3.x** instalado en tu sistema. Puedes descargar la última versión desde [python.org](https://www.python.org/downloads/).

## **Instalación y Ejecución**

Sigue los siguientes pasos para descargar y ejecutar el programa:

1. **Clona el repositorio o descarga el archivo** `proyecto_estadistica.py`:
   
   ```bash
   git clone https://github.com/usuario/proyecto-estadistica.git

## **Ejemplo de Ejecución**

### **Datos Agrupados** (30 o más elementos):

```plaintext
Ingrese el número de elementos: 31
Valor 1: 10
Frecuencia para el valor 10: 5
Valor 2: 20
Frecuencia para el valor 20: 15
Valor 3: 30
Frecuencia para el valor 30: 10
Valor 4: 40
Frecuencia para el valor 40: 1
Valor 5: 50
Frecuencia para el valor 50: 0

Resultados para datos agrupados:
Media: 18.45
Moda: 20
Varianza: 36.25
Desviación Estándar: 6.02

---

Ejemplo de Ejecución

Datos No Agrupados (menos de 30 elementos):

Ingrese el número de elementos: 4
Elemento 1: 12
Elemento 2: 8
Elemento 3: 10
Elemento 4: 16

Resultados para datos no agrupados:
Media: 11.5
Mayor: 16
Menor: 8
Moda: 12
Varianza: 10.25
Desviación Estándar: 3.20



