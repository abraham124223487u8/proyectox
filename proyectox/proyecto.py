import math
from collections import Counter

# Función para datos no agrupados
def datos_no_agrupados(muestra):
    media = sum(muestra) / len(muestra)
    mayor = max(muestra)
    menor = min(muestra)
    moda = Counter(muestra).most_common(1)[0][0]  # Solo el dato más frecuente
    
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

# Función para datos agrupados sin frecuencias
def datos_agrupados(valores):
    n = len(valores)
    media = sum(valores) / n
    moda = Counter(valores).most_common(1)[0][0]  # Valor con mayor frecuencia
    
    varianza = sum((x - media) ** 2 for x in valores) / n
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
        resultados = datos_agrupados(muestra)
    
    for key, value in resultados.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
