"""
Ejercicio 4: Manejo de datos faltantes
Objetivo: Detectar nulos, contar faltantes y completar valores faltantes.
"""

import pandas as pd

print("="*60)
print("EJERCICIO 4: MANEJO DE DATOS FALTANTES")
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

# 4.1 Detectar nulos con isna()
print("4.1 Detectar valores nulos con isna():")
print(df.isna())
print()

# 4.2 Contar faltantes por columna
print("4.2 Contar valores faltantes por columna:")
print(df.isna().sum())
print()

print("4.3 Porcentaje de valores faltantes:")
porcentaje_nulos = (df.isna().sum() / len(df)) * 100
print(porcentaje_nulos)
print()

# 4.4 Identificar filas con al menos un valor nulo
print("4.4 Filas con al menos un valor nulo:")
filas_con_nulos = df[df.isna().any(axis=1)]
print(filas_con_nulos)
print()

# 4.5 Completar faltantes en 'edad' con 0
print("4.5 Completar faltantes en 'edad' con 0:")
print(f"Antes: {df['edad'].tolist()}")
df['edad'] = df['edad'].fillna(0)
print(f"Después: {df['edad'].tolist()}")
print()

# 4.6 Completar faltantes en 'ciudad' con 'Desconocido'
print("4.6 Completar faltantes en 'ciudad' con 'Desconocido':")
print(f"Antes: {df['ciudad'].tolist()}")
df['ciudad'] = df['ciudad'].fillna('Desconocido')
print(f"Después: {df['ciudad'].tolist()}")
print()

# 4.7 Completar faltantes en 'precio' con la media
print("4.7 Completar faltantes en 'precio' con la media:")
print(f"Antes: {df['precio'].tolist()}")
media_precio = df['precio'].mean()
print(f"Media de precios: {media_precio:.2f}")
df['precio'] = df['precio'].fillna(media_precio)
print(f"Después: {df['precio'].tolist()}")
print()

print("DataFrame final sin valores nulos:")
print(df)
print()

print("Verificación - Valores nulos restantes:")
print(df.isna().sum())
print()

print("✓ Ejercicio 4 completado exitosamente")
