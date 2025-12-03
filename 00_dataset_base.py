"""
Actividad 4: Manejo de Datos con Pandas
Dataset Base - Preparación inicial
"""

import pandas as pd

# Crear el dataset base
datos = {
    'nombre':   ['Ana', 'Bob', 'Clara', 'Diego', 'Eva'],
    'edad':     [25, 30, 22, None, 28],
    'ciudad':   ['Madrid', 'Lima', 'Bogotá', 'Medellín', None],
    'producto': ['Laptop', 'Teléfono', 'Tablet', 'Laptop', 'Tablet'],
    'precio':   [1200, 800, 300, 1150, None],
    'stock':    [10, 15, 5, 8, 0]
}

df = pd.DataFrame(datos, index=['a', 'b', 'c', 'd', 'e'])

# Mostrar el DataFrame
print("Dataset Base:")
print(df)
print("\n" + "="*60 + "\n")

# Guardar el dataset para ejercicios de lectura/escritura
df.to_csv('actividad_semana4.csv', index=True)
print("✓ Archivo 'actividad_semana4.csv' creado exitosamente")
