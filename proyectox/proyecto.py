import statistics as stats
import math
from collections import Counter

# Función para datos no agrupados
def datos_no_agrupados(muestra):
    media = sum(muestra) / len(muestra)
    mayor = max(muestra)
    menor = min(muestra)
    moda = Counter(muestra).most_common(1)[0]  # (dato, frecuencia)
    
    varianza = sum((x - media) ** 2 for x in muestra) / len(muestra)
    desviacion_estandar = math.sqrt(varianza)
    
    return {
        "Media": media,
        "Mayor": mayor,
        "Menor": menor,
        "Moda": moda,
        "Varianza": varianza,
        "Desviación Estándar": desviacion_estandar
    }

# Función para datos agrupados (recibe frecuencias y valores)
def datos_agrupados(valores, frecuencias):
    total_elementos = sum(frecuencias)
    
    media = sum(v * f for v, f in zip(valores, frecuencias)) / total_elementos
    moda = Counter(frecuencias).most_common(1)[0]  # (frecuencia, veces que se repite)
    
    varianza = sum(((v - media) ** 2) * f for v, f in zip(valores, frecuencias)) / total_elementos
    desviacion_estandar = math.sqrt(varianza)
    
    return {
        "Media": media,
        "Moda": moda,
        "Varianza": varianza,
        "Desviación Estándar": desviacion_estandar
    }

# Función principal
def main():
    n = int(input("Ingrese el número de elementos: "))
    muestra = [int(input(f"Elemento {i+1}: ")) for i in range(n)]
    
    if n < 30:
        resultados = datos_no_agrupados(muestra)
    else:
        frecuencias = [int(input(f"Frecuencia para el valor {v}: ")) for v in muestra]
        resultados = datos_agrupados(muestra, frecuencias)
    
    # Mostrar resultados
    for key, value in resultados.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
