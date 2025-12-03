"""
Ejercicio 9: Ejercicio integrado
Objetivo: Aplicar múltiples operaciones en secuencia:
- Aplicar descuento del 10% a precio
- Filtrar productos con stock > 5
- Ordenar por precio_descuento
- Guardar como inventario_procesado.csv
"""

import pandas as pd

print("="*60)
print("EJERCICIO 9: EJERCICIO INTEGRADO")
print("="*60 + "\n")

# Cargar dataset base
print("Paso 1: Cargar dataset base")
datos = {
    'nombre':   ['Ana', 'Bob', 'Clara', 'Diego', 'Eva'],
    'edad':     [25, 30, 22, None, 28],
    'ciudad':   ['Madrid', 'Lima', 'Bogotá', 'Medellín', None],
    'producto': ['Laptop', 'Teléfono', 'Tablet', 'Laptop', 'Tablet'],
    'precio':   [1200, 800, 300, 1150, None],
    'stock':    [10, 15, 5, 8, 0]
}
df = pd.DataFrame(datos, index=['a', 'b', 'c', 'd', 'e'])
print(df)
print("\n" + "="*60 + "\n")

# Paso 1: Aplicar descuento del 10% a precio
print("Paso 2: Aplicar descuento del 10% al precio")
df['precio_descuento'] = df['precio'] * 0.9
print(df[['producto', 'precio', 'precio_descuento', 'stock']])
print("\n" + "="*60 + "\n")

# Paso 2: Filtrar productos con stock > 5
print("Paso 3: Filtrar productos con stock > 5")
df_filtrado = df[df['stock'] > 5]
print(df_filtrado[['producto', 'precio', 'precio_descuento', 'stock']])
print(f"\nProductos filtrados: {len(df_filtrado)} de {len(df)}")
print("\n" + "="*60 + "\n")

# Paso 3: Ordenar por precio_descuento (descendente)
print("Paso 4: Ordenar por precio_descuento (descendente)")
df_ordenado = df_filtrado.sort_values('precio_descuento', ascending=False)
print(df_ordenado[['producto', 'precio', 'precio_descuento', 'stock']])
print("\n" + "="*60 + "\n")

# Paso 4: Guardar como inventario_procesado.csv
print("Paso 5: Guardar resultado como 'inventario_procesado.csv'")
df_ordenado.to_csv('inventario_procesado.csv', index=True)
print("✓ Archivo 'inventario_procesado.csv' guardado exitosamente")
print()

# Verificación: Leer el archivo guardado
print("Verificación: Leer el archivo guardado")
df_verificacion = pd.read_csv('inventario_procesado.csv', index_col=0)
print(df_verificacion)
print()

# Resumen del proceso
print("="*60)
print("RESUMEN DEL PROCESO INTEGRADO")
print("="*60)
print(f"1. Dataset original: {len(df)} registros")
print(f"2. Descuento aplicado: 10% sobre precio")
print(f"3. Filtrado: stock > 5 → {len(df_filtrado)} registros")
print(f"4. Ordenamiento: por precio_descuento (descendente)")
print(f"5. Archivo guardado: inventario_procesado.csv")
print()

# Estadísticas finales
print("Estadísticas del inventario procesado:")
print(f"  - Precio promedio original: ${df_ordenado['precio'].mean():.2f}")
print(f"  - Precio promedio con descuento: ${df_ordenado['precio_descuento'].mean():.2f}")
print(f"  - Stock total: {df_ordenado['stock'].sum()} unidades")
print(f"  - Ahorro total por descuento: ${(df_ordenado['precio'] - df_ordenado['precio_descuento']).sum():.2f}")
print()

print("✓ Ejercicio 9 completado exitosamente")
