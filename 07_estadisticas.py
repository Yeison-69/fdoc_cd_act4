"""
Ejercicio 7: Estadísticas básicas
Objetivo: Obtener estadísticas descriptivas y conteos de valores.
"""

import pandas as pd

print("="*60)
print("EJERCICIO 7: ESTADÍSTICAS BÁSICAS")
print("="*60 + "\n")

# Cargar dataset base
datos = {
    'nombre':   ['Ana', 'Bob', 'Clara', 'Diego', 'Eva'],
    'edad':     [25, 30, 22, None, 28],
    'ciudad':   ['Madrid', 'Lima', 'Bogotá', 'Medellín', None],
    'producto': ['Laptop', 'Teléfono', 'Tablet', 'Laptop', 'Tablet'],
    'precio':   [1200, 800, 300, 1150, None],
    'stock':    [10, 15, 5, 8, 0]
}
df = pd.DataFrame(datos, index=['a', 'b', 'c', 'd', 'e'])

print("DataFrame original:")
print(df)
print("\n" + "="*60 + "\n")

# 7.1 Estadísticas descriptivas con describe()
print("7.1 Estadísticas descriptivas para columnas numéricas:")
print(df.describe())
print()

# 7.2 Estadísticas para una columna específica
print("7.2 Estadísticas para la columna 'precio':")
print(df['precio'].describe())
print()

# 7.3 Estadísticas individuales
print("7.3 Estadísticas individuales:")
print(f"Media de edad: {df['edad'].mean():.2f}")
print(f"Mediana de precio: {df['precio'].median():.2f}")
print(f"Desviación estándar de stock: {df['stock'].std():.2f}")
print(f"Valor mínimo de precio: {df['precio'].min():.2f}")
print(f"Valor máximo de precio: {df['precio'].max():.2f}")
print(f"Suma total de stock: {df['stock'].sum()}")
print()

# 7.4 Conteo de valores con value_counts()
print("7.4 Conteo de valores para 'producto':")
print(df['producto'].value_counts())
print()

# 7.5 Conteo de valores con porcentajes
print("7.5 Conteo de valores para 'producto' (porcentajes):")
print(df['producto'].value_counts(normalize=True) * 100)
print()

# 7.6 Conteo de valores para 'ciudad'
print("7.6 Conteo de valores para 'ciudad':")
print(df['ciudad'].value_counts())
print()

# 7.7 Conteo incluyendo valores nulos
print("7.7 Conteo de valores para 'ciudad' (incluyendo nulos):")
print(df['ciudad'].value_counts(dropna=False))
print()

# 7.8 Estadísticas por grupos
print("7.8 Precio promedio por producto:")
precio_por_producto = df.groupby('producto')['precio'].mean()
print(precio_por_producto)
print()

# 7.9 Múltiples estadísticas por grupos
print("7.9 Estadísticas de stock por producto:")
stats_stock = df.groupby('producto')['stock'].agg(['mean', 'sum', 'count'])
print(stats_stock)
print()

# 7.10 Correlación entre variables numéricas
print("7.10 Matriz de correlación:")
print(df[['edad', 'precio', 'stock']].corr())
print()

# 7.11 Información general del DataFrame
print("7.11 Información general del DataFrame:")
print(df.info())
print()

print("✓ Ejercicio 7 completado exitosamente")
