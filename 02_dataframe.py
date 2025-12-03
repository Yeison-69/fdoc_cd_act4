"""
Ejercicio 2: DataFrame - crear y explorar
Objetivo: Crear DataFrame desde diccionario con índice personalizado,
acceder a columnas, usar loc e iloc.
"""

import pandas as pd

print("="*60)
print("EJERCICIO 2: DATAFRAME - CREAR Y EXPLORAR")
print("="*60 + "\n")

# 2.1 Crear DataFrame desde diccionario con índice personalizado
print("2.1 Crear DataFrame con índice personalizado:")
datos = {
    'nombre':   ['Ana', 'Bob', 'Clara', 'Diego', 'Eva'],
    'edad':     [25, 30, 22, 35, 28],
    'ciudad':   ['Madrid', 'Lima', 'Bogotá', 'Medellín', 'Santiago'],
    'salario':  [3000, 3500, 2800, 4000, 3200]
}
df = pd.DataFrame(datos, index=['emp1', 'emp2', 'emp3', 'emp4', 'emp5'])
print(df)
print()

# 2.2 Acceder a una columna
print("2.2 Acceder a la columna 'nombre':")
print(df['nombre'])
print()

print("2.3 Acceder a múltiples columnas:")
print(df[['nombre', 'salario']])
print()

# 2.4 Usar loc para acceder por etiqueta
print("2.4 Usar loc - Acceder a fila 'emp3' por etiqueta:")
print(df.loc['emp3'])
print()

print("2.5 Usar loc - Acceder a múltiples filas y columnas:")
print(df.loc['emp2':'emp4', ['nombre', 'edad']])
print()

# 2.6 Usar iloc para acceder por posición
print("2.6 Usar iloc - Acceder a fila en posición 1:")
print(df.iloc[1])
print()

print("2.7 Usar iloc - Acceder a rango de filas y columnas:")
print(df.iloc[0:3, 0:2])
print()

# 2.8 Información del DataFrame
print("2.8 Información del DataFrame:")
print(f"Forma (filas, columnas): {df.shape}")
print(f"Columnas: {list(df.columns)}")
print(f"Índice: {list(df.index)}")
print(f"Tipos de datos:\n{df.dtypes}")
print()

print("✓ Ejercicio 2 completado exitosamente")
