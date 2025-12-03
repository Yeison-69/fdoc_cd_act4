"""
Ejercicio 6: Ordenar datos
Objetivo: Ordenar DataFrame por diferentes columnas y criterios.
"""

import pandas as pd

print("="*60)
print("EJERCICIO 6: ORDENAR DATOS")
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

# 6.1 Ordenar por edad ascendente
print("6.1 Ordenar por edad (ascendente):")
df_edad_asc = df.sort_values('edad')
print(df_edad_asc)
print()

# 6.2 Ordenar por edad ascendente (nulos al final)
print("6.2 Ordenar por edad (ascendente, nulos al final):")
df_edad_asc_na = df.sort_values('edad', na_position='last')
print(df_edad_asc_na)
print()

# 6.3 Ordenar por precio descendente
print("6.3 Ordenar por precio (descendente):")
df_precio_desc = df.sort_values('precio', ascending=False)
print(df_precio_desc)
print()

# 6.4 Ordenar por precio descendente (rellenar nulos temporalmente)
print("6.4 Ordenar por precio descendente (rellenar nulos con 0):")
df_temp = df.copy()
df_temp['precio_temp'] = df_temp['precio'].fillna(0)
df_ordenado = df_temp.sort_values('precio_temp', ascending=False)
df_ordenado = df_ordenado.drop('precio_temp', axis=1)
print(df_ordenado)
print()

# 6.5 Ordenar por múltiples columnas
print("6.5 Ordenar por producto (asc) y luego por precio (desc):")
df_multi = df.sort_values(['producto', 'precio'], ascending=[True, False])
print(df_multi)
print()

# 6.6 Ordenar por índice
print("6.6 Ordenar por índice (descendente):")
df_index = df.sort_index(ascending=False)
print(df_index)
print()

# 6.7 Ordenar por nombre alfabéticamente
print("6.7 Ordenar por nombre (alfabéticamente):")
df_nombre = df.sort_values('nombre')
print(df_nombre)
print()

# 6.8 Resetear índice después de ordenar
print("6.8 Ordenar por stock y resetear índice:")
df_reset = df.sort_values('stock', ascending=False).reset_index(drop=True)
print(df_reset)
print()

print("✓ Ejercicio 6 completado exitosamente")
