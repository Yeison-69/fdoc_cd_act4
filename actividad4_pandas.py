# ============================================================
# Actividad 4: Manejo de Datos con Pandas
# ============================================================
# Basado en la guía "Introducción a estructuras de datos en Pandas"
# Autor: [Tu nombre]
# ============================================================

import pandas as pd
import numpy as np

# ============================================================
# Dataset base
# ============================================================

datos = {
    'nombre':   ['Ana', 'Bob', 'Clara', 'Diego', 'Eva'],
    'edad':     [25, 30, 22, None, 28],
    'ciudad':   ['Madrid', 'Lima', 'Bogotá', 'Medellín', None],
    'producto': ['Laptop', 'Teléfono', 'Tablet', 'Laptop', 'Tablet'],
    'precio':   [1200, 800, 300, 1150, None],
    'stock':    [10, 15, 5, 8, 0]
}

df = pd.DataFrame(datos, index=['a', 'b', 'c', 'd', 'e'])

# Guardar dataset base
df.to_csv('actividad_semana4.csv', index=True)

print("=== DATAFRAME BASE ===")
print(df, "\n")

# ============================================================
# 1) SERIES — crear y operar
# ============================================================

print("=== 1) SERIES ===")

# Series desde una lista
serie_lista = pd.Series([10, 20, 30, 40], index=['x', 'y', 'z', 'w'])
print("\nSeries desde lista:")
print(serie_lista)

# Series desde un diccionario
serie_dic = pd.Series({'manzana': 5, 'banana': 8, 'naranja': 3})
print("\nSeries desde diccionario:")
print(serie_dic)

# Acceso, modificación y operación
print("\nValor en 'banana':", serie_dic['banana'])
serie_dic['manzana'] = 10
print("Series modificada:")
print(serie_dic)
print("\nSeries multiplicada por 2:")
print(serie_dic * 2)

# ============================================================
# 2) DATAFRAME — crear y explorar
# ============================================================

print("\n=== 2) DATAFRAME ===")

datos_df = {
    'nombre': ['Luis', 'María', 'José'],
    'edad': [21, 35, 27],
    'ciudad': ['Quito', 'Caracas', 'Bogotá']
}

df2 = pd.DataFrame(datos_df, index=['x', 'y', 'z'])
print("\nDataFrame creado:")
print(df2)

# Acceso a columna
print("\nColumna 'nombre':")
print(df2['nombre'])

# Acceso a fila con loc
print("\nFila con loc['x']:")
print(df2.loc['x'])

# Acceso con iloc
print("\nFila con iloc[0]:")
print(df2.iloc[0])

# ============================================================
# 3) OPERACIONES BÁSICAS
# ============================================================

print("\n=== 3) OPERACIONES BÁSICAS ===")

# Agregar columna derivada
df['precio_descuento'] = df['precio'] * 0.9

# Operación vectorizada (por ejemplo, sumar 5 al stock)
df['stock'] = df['stock'] + 5

print("\nDataFrame con columna derivada y stock actualizado:")
print(df)

# ============================================================
# 4) MANEJO DE DATOS FALTANTES
# ============================================================

print("\n=== 4) MANEJO DE DATOS FALTANTES ===")

# Detectar nulos
print("\nValores nulos en el DataFrame:")
print(df.isna())

# Contar faltantes por columna
print("\nConteo de faltantes por columna:")
print(df.isna().sum())

# Rellenar valores faltantes
df['edad'] = df['edad'].fillna(0)
df['ciudad'] = df['ciudad'].fillna('Desconocido')
df['precio'] = df['precio'].fillna(0)

print("\nDataFrame después de completar faltantes:")
print(df)

# ============================================================
# 5) SELECCIÓN Y FILTRADO
# ============================================================

print("\n=== 5) SELECCIÓN Y FILTRADO ===")

# Precio > 500
filtro_precio = df[df['precio'] > 500]
print("\nFilas con precio > 500:")
print(filtro_precio)

# Producto = 'Laptop' y stock > 5
filtro_laptop = df[(df['producto'] == 'Laptop') & (df['stock'] > 5)]
print("\nProductos 'Laptop' con stock > 5:")
print(filtro_laptop)

# ============================================================
# 6) ORDENAR DATOS
# ============================================================

print("\n=== 6) ORDENAR DATOS ===")

# Ordenar por edad ascendente
orden_edad = df.sort_values('edad')
print("\nOrdenado por edad ascendente:")
print(orden_edad)

# Ordenar por precio descendente (rellenando nulos con 0)
orden_precio = df.sort_values('precio', ascending=False)
print("\nOrdenado por precio descendente:")
print(orden_precio)

# ============================================================
# 7) ESTADÍSTICAS BÁSICAS
# ============================================================

print("\n=== 7) ESTADÍSTICAS BÁSICAS ===")

print("\nDescripción de columnas numéricas:")
print(df.describe())

print("\nConteo de valores por producto:")
print(df['producto'].value_counts())

# ============================================================
# 8) LEER Y GUARDAR DATOS
# ============================================================

print("\n=== 8) LECTURA Y ESCRITURA DE CSV ===")

# Leer CSV
df_leido = pd.read_csv('actividad_semana4.csv')
print("\nPrimeras filas del CSV leído:")
print(df_leido.head())

# Guardar nuevo CSV con columnas seleccionadas
df[['nombre', 'producto', 'precio_descuento']].to_csv('datos_filtrados.csv', index=False)
print("\nArchivo 'datos_filtrados.csv' guardado correctamente.")

# ============================================================
# 9) EJERCICIO INTEGRADO
# ============================================================

print("\n=== 9) EJERCICIO INTEGRADO ===")

# Aplicar descuento del 10% (ya lo hicimos antes)
df['precio_descuento'] = df['precio'] * 0.9

# Filtrar productos con stock > 5
df_filtrado = df[df['stock'] > 5]

# Ordenar por precio_descuento
df_ordenado = df_filtrado.sort_values('precio_descuento')

# Guardar resultado
df_ordenado.to_csv('inventario_procesado.csv', index=False)
print("\nArchivo 'inventario_procesado.csv' guardado correctamente.")
print("\nResultado final:")
print(df_ordenado)

# ============================================================
# FIN DE LA ACTIVIDAD
# ============================================================
