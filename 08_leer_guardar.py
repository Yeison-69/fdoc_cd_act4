"""
Ejercicio 8: Leer y guardar datos
Objetivo: Practicar lectura y escritura de archivos CSV.
"""

import pandas as pd
import os

print("="*60)
print("EJERCICIO 8: LEER Y GUARDAR DATOS")
print("="*60 + "\n")

# 8.1 Crear y guardar el dataset base
print("8.1 Crear y guardar dataset base:")
datos = {
    'nombre':   ['Ana', 'Bob', 'Clara', 'Diego', 'Eva'],
    'edad':     [25, 30, 22, None, 28],
    'ciudad':   ['Madrid', 'Lima', 'Bogotá', 'Medellín', None],
    'producto': ['Laptop', 'Teléfono', 'Tablet', 'Laptop', 'Tablet'],
    'precio':   [1200, 800, 300, 1150, None],
    'stock':    [10, 15, 5, 8, 0]
}
df_original = pd.DataFrame(datos, index=['a', 'b', 'c', 'd', 'e'])

# Guardar con índice
df_original.to_csv('actividad_semana4.csv', index=True)
print("✓ Archivo 'actividad_semana4.csv' guardado exitosamente")
print()

# 8.2 Leer el CSV creado
print("8.2 Leer el archivo CSV:")
df_leido = pd.read_csv('actividad_semana4.csv', index_col=0)
print(df_leido)
print()

# 8.3 Mostrar las primeras filas
print("8.3 Mostrar las primeras 3 filas con head():")
print(df_leido.head(3))
print()

# 8.4 Mostrar las últimas filas
print("8.4 Mostrar las últimas 2 filas con tail():")
print(df_leido.tail(2))
print()

# 8.5 Guardar CSV con columnas seleccionadas
print("8.5 Guardar CSV con columnas seleccionadas:")
columnas_seleccionadas = ['nombre', 'producto', 'precio']
df_seleccion = df_leido[columnas_seleccionadas]
df_seleccion.to_csv('productos_precios.csv', index=False)
print("✓ Archivo 'productos_precios.csv' guardado con columnas:", columnas_seleccionadas)
print(df_seleccion)
print()

# 8.6 Leer el CSV sin índice
print("8.6 Leer CSV sin índice:")
df_sin_index = pd.read_csv('productos_precios.csv')
print(df_sin_index)
print()

# 8.7 Guardar con separador diferente
print("8.7 Guardar con separador punto y coma:")
df_leido.to_csv('actividad_separador.csv', sep=';', index=True)
print("✓ Archivo 'actividad_separador.csv' guardado con separador ';'")
print()

# 8.8 Leer con separador diferente
print("8.8 Leer CSV con separador punto y coma:")
df_sep = pd.read_csv('actividad_separador.csv', sep=';', index_col=0)
print(df_sep.head())
print()

# 8.9 Guardar solo filas filtradas
print("8.9 Guardar solo productos con precio > 500:")
df_filtrado = df_leido[df_leido['precio'] > 500]
df_filtrado.to_csv('productos_premium.csv', index=True)
print("✓ Archivo 'productos_premium.csv' guardado")
print(df_filtrado)
print()

# 8.10 Listar archivos CSV creados
print("8.10 Archivos CSV creados en este ejercicio:")
archivos_csv = [f for f in os.listdir('.') if f.endswith('.csv')]
for archivo in archivos_csv:
    tamaño = os.path.getsize(archivo)
    print(f"  - {archivo} ({tamaño} bytes)")
print()

print("✓ Ejercicio 8 completado exitosamente")
