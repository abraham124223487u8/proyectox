# **Programa de Estadísticas para Datos Agrupados y No Agrupados (Sin Librerías Externas)**

Este es un proyecto de Python que calcula estadísticas para datos no agrupados (menos de 30 elementos) y datos agrupados (30 o más elementos), sin hacer uso de librerías externas como `math` o `statistics`. Todos los cálculos, como la media aritmética, moda, varianza y desviación estándar, se realizan manualmente dentro del código.

![Captura de pantalla 2024-09-24 132744](https://github.com/user-attachments/assets/2712ec9f-4230-4af1-86cc-1cef292a4098)

## **Instalación**

Para ejecutar este programa en tu máquina local, sigue estos pasos:

1. Descarga el archivo `proyecto.py` desde el repositorio de GitHub. Haz clic en el botón "Code" y selecciona "Download ZIP". 

2. Extrae el archivo ZIP descargado en tu computadora.

3. Abre la terminal o consola de comandos en la carpeta donde se encuentra el archivo `proyecto.py`.

4. Asegúrate de tener Python instalado en tu computadora. Si no lo tienes, descárgalo desde [python.org](https://www.python.org/downloads/).

5. Ejecuta el programa desde la terminal con el siguiente comando:

    ```bash
    python proyecto_estadistica.py
    ```


## **Estructura del Proyecto**

- `proyecto.py`: el archivo principal que contiene todo el código fuente del proyecto.
- `docs/`: esta carpeta contiene los recursos, imágenes y documentación del proyecto.

## **Descripción del Programa**

El programa solicita al usuario ingresar el número de elementos que tiene su muestra, y de acuerdo a ese número, realiza los cálculos correspondientes para datos agrupados o no agrupados. Todos los cálculos se realizan sin el uso de librerías externas.

- Para **datos no agrupados**:
  - Calcula manualmente la media aritmética, el dato mayor, el dato menor, la moda, la varianza y la desviación estándar.
  
- Para **datos agrupados**:
  - Genera la tabla de frecuencias y calcula manualmente la media aritmética, la moda, la varianza y la desviación estándar.

## **Ejemplo de Ejecución**

```plaintext
Elemento 1: 10
Elemento 2: 2
Elemento 3: 45
...
Datos no agrupados:
Media: 19.0
Mayor: 45
Menor: 2
Moda: (10, 1)
Varianza: 348.6666666666667
Desviación Estándar: 18.672618098881223
