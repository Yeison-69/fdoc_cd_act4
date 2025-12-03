"""
Ejercicio 5: Selección y filtrado
Objetivo: Filtrar filas según condiciones en columnas.
"""

import pandas as pd

print("="*60)
print("EJERCICIO 5: SELECCIÓN Y FILTRADO")
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

# 5.1 Filtrar filas con precio > 500
print("5.1 Filtrar productos con precio > 500:")
filtro_precio = df[df['precio'] > 500]
print(filtro_precio)
print(f"\nTotal de productos con precio > 500: {len(filtro_precio)}")
print()

# 5.2 Filtrar productos 'Laptop' con stock > 5
print("5.2 Filtrar productos 'Laptop' con stock > 5:")
filtro_laptop = df[(df['producto'] == 'Laptop') & (df['stock'] > 5)]
print(filtro_laptop)
print(f"\nTotal de Laptops con stock > 5: {len(filtro_laptop)}")
print()

# 5.3 Filtrar por múltiples condiciones (OR)
print("5.3 Filtrar productos 'Laptop' O 'Teléfono':")
filtro_or = df[(df['producto'] == 'Laptop') | (df['producto'] == 'Teléfono')]
print(filtro_or)
print()

# 5.4 Filtrar usando isin()
print("5.4 Filtrar usando isin() - Productos en lista:")
productos_buscar = ['Laptop', 'Tablet']
filtro_isin = df[df['producto'].isin(productos_buscar)]
print(filtro_isin)
print()

# 5.5 Filtrar por rango de edad
print("5.5 Filtrar personas con edad entre 25 y 30 (inclusive):")
filtro_edad = df[(df['edad'] >= 25) & (df['edad'] <= 30)]
print(filtro_edad)
print()

# 5.6 Filtrar valores no nulos
print("5.6 Filtrar filas donde 'precio' no es nulo:")
filtro_no_nulo = df[df['precio'].notna()]
print(filtro_no_nulo)
print()

# 5.7 Filtrar y seleccionar columnas específicas
print("5.7 Filtrar precio > 500 y mostrar solo nombre, producto y precio:")
filtro_columnas = df[df['precio'] > 500][['nombre', 'producto', 'precio']]
print(filtro_columnas)
print()

# 5.8 Filtrar usando query()
print("5.8 Filtrar usando query() - stock >= 5:")
filtro_query = df.query('stock >= 5')
print(filtro_query)
print()

print("✓ Ejercicio 5 completado exitosamente")
