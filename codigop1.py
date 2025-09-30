import random
import matplotlib.pyplot as plt
import numpy as np

class GeneradorLinealCongruencial:
    """
    Implementación del Generador Lineal Congruencial (LCG)
    Fórmula: X(n+1) = (a * X(n) + c) mod m
    """
    
    def __init__(self, semilla=123, a=1664525, c=1013904223, m=2**32):
        """
        Parámetros comunes del LCG (usados en Numerical Recipes):
        - semilla: valor inicial (seed)
        - a: multiplicador
        - c: incremento
        - m: módulo
        """
        self.semilla = semilla
        self.a = a
        self.c = c
        self.m = m
        self.actual = semilla
    
    def siguiente(self):
        """Genera el siguiente número pseudoaleatorio"""
        self.actual = (self.a * self.actual + self.c) % self.m
        return self.actual / self.m  # Normalizar entre 0 y 1
    
    def generar_n(self, n):
        """Genera n números pseudoaleatorios"""
        return [self.siguiente() for _ in range(n)]
    
    def reiniciar(self, nueva_semilla=None):
        """Reinicia el generador con una nueva semilla"""
        if nueva_semilla is not None:
            self.semilla = nueva_semilla
        self.actual = self.semilla


def comparar_generadores(n=1000):
    """
    Compara el LCG con random de Python
    """
    # Generar números con LCG
    lcg = GeneradorLinealCongruencial(semilla=42)
    numeros_lcg = lcg.generar_n(n)
    
    # Generar números con random de Python
    random.seed(42)
    numeros_random = [random.random() for _ in range(n)]
    
    # Crear visualizaciones
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Histograma LCG
    axes[0, 0].hist(numeros_lcg, bins=50, color='blue', alpha=0.7, edgecolor='black')
    axes[0, 0].set_title('Distribución LCG')
    axes[0, 0].set_xlabel('Valor')
    axes[0, 0].set_ylabel('Frecuencia')
    
    # Histograma random
    axes[0, 1].hist(numeros_random, bins=50, color='green', alpha=0.7, edgecolor='black')
    axes[0, 1].set_title('Distribución random() de Python')
    axes[0, 1].set_xlabel('Valor')
    axes[0, 1].set_ylabel('Frecuencia')
    
    # Dispersión LCG (pares consecutivos)
    axes[1, 0].scatter(numeros_lcg[:-1], numeros_lcg[1:], alpha=0.5, s=1)
    axes[1, 0].set_title('Pares consecutivos LCG')
    axes[1, 0].set_xlabel('X(n)')
    axes[1, 0].set_ylabel('X(n+1)')
    
    # Dispersión random
    axes[1, 1].scatter(numeros_random[:-1], numeros_random[1:], alpha=0.5, s=1)
    axes[1, 1].set_title('Pares consecutivos random()')
    axes[1, 1].set_xlabel('X(n)')
    axes[1, 1].set_ylabel('X(n+1)')
    
    plt.tight_layout()
    plt.savefig('comparacion_generadores.png', dpi=300)
    plt.show()
    
    # Análisis estadístico
    print("="*60)
    print("ANÁLISIS COMPARATIVO DE GENERADORES")
    print("="*60)
    print(f"\nNúmero de valores generados: {n}\n")
    
    print("GENERADOR LINEAL CONGRUENCIAL (LCG):")
    print(f"  Media: {np.mean(numeros_lcg):.6f} (esperado: 0.5)")
    print(f"  Desviación estándar: {np.std(numeros_lcg):.6f} (esperado: 0.289)")
    print(f"  Mínimo: {min(numeros_lcg):.6f}")
    print(f"  Máximo: {max(numeros_lcg):.6f}")
    
    print("\nRANDOM() DE PYTHON:")
    print(f"  Media: {np.mean(numeros_random):.6f} (esperado: 0.5)")
    print(f"  Desviación estándar: {np.std(numeros_random):.6f} (esperado: 0.289)")
    print(f"  Mínimo: {min(numeros_random):.6f}")
    print(f"  Máximo: {max(numeros_random):.6f}")
    
    print("\n" + "="*60)
    print("PRIMEROS 10 NÚMEROS DE CADA GENERADOR:")
    print("="*60)
    print(f"{'LCG':<15} {'random()':<15}")
    print("-"*30)
    for i in range(10):
        print(f"{numeros_lcg[i]:<15.6f} {numeros_random[i]:<15.6f}")
    
    return numeros_lcg, numeros_random


# Ejemplo de uso
if __name__ == "__main__":
    print("Generando y comparando números pseudoaleatorios...\n")
    
    # Comparar generadores
    lcg_nums, random_nums = comparar_generadores(n=10000)
    
    print("\n" + "="*60)
    print("ANÁLISIS COMPLETADO")
    print("="*60)
    print("Se ha generado el gráfico 'comparacion_generadores.png'")
