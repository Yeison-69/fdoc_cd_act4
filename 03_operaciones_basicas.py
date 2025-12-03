"""
Ejercicio 3: Operaciones básicas
Objetivo: Agregar columnas derivadas y aplicar operaciones vectorizadas.
"""

import pandas as pd

print("="*60)
print("EJERCICIO 3: OPERACIONES BÁSICAS")
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

# 3.1 Agregar columna derivada: precio_descuento (10% de descuento)
print("3.1 Agregar columna 'precio_descuento' (10% descuento):")
df['precio_descuento'] = df['precio'] * 0.9
print(df[['producto', 'precio', 'precio_descuento']])
print()

# 3.2 Agregar columna: valor_inventario (precio * stock)
print("3.2 Agregar columna 'valor_inventario' (precio × stock):")
df['valor_inventario'] = df['precio'] * df['stock']
print(df[['producto', 'precio', 'stock', 'valor_inventario']])
print()

# 3.3 Operación vectorizada: incrementar stock en 5 unidades
print("3.3 Operación vectorizada - Incrementar stock en 5 unidades:")
print("Stock original:")
print(df['stock'])
df['stock_nuevo'] = df['stock'] + 5
print("\nStock nuevo:")
print(df['stock_nuevo'])
print()

# 3.4 Operación vectorizada: calcular IVA (19%)
print("3.4 Calcular IVA (19%) sobre el precio:")
df['iva'] = df['precio'] * 0.19
df['precio_con_iva'] = df['precio'] + df['iva']
print(df[['producto', 'precio', 'iva', 'precio_con_iva']])
print()

# 3.5 Operación condicional: categorizar productos por precio
print("3.5 Categorizar productos por precio:")
df['categoria'] = df['precio'].apply(lambda x: 'Premium' if pd.notna(x) and x > 500 else 'Económico' if pd.notna(x) else 'Sin precio')
print(df[['producto', 'precio', 'categoria']])
print()

print("DataFrame final con todas las columnas:")
print(df)
print()

print("✓ Ejercicio 3 completado exitosamente")
