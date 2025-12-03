"""
Ejercicio 1: Series - crear y operar
Objetivo: Practicar creación de Series desde lista y diccionario,
acceso por índice, modificación y operaciones matemáticas.
"""

import pandas as pd

print("="*60)
print("EJERCICIO 1: SERIES - CREAR Y OPERAR")
print("="*60 + "\n")

# 1.1 Crear Series desde una lista
print("1.1 Series desde una lista:")
lista_precios = [1200, 800, 300, 1150, 450]
serie_lista = pd.Series(lista_precios, name='precios')
print(serie_lista)
print()

# 1.2 Crear Series desde un diccionario
print("1.2 Series desde un diccionario:")
dict_productos = {
    'Laptop': 1200,
    'Teléfono': 800,
    'Tablet': 300,
    'Monitor': 450,
    'Teclado': 80
}
serie_dict = pd.Series(dict_productos, name='precios_productos')
print(serie_dict)
print()

# 1.3 Acceder a elementos por índice
print("1.3 Acceso por índice:")
print(f"Precio en posición 0: {serie_lista[0]}")
print(f"Precio del producto 'Laptop': {serie_dict['Laptop']}")
print(f"Primeros 3 elementos: \n{serie_lista[:3]}")
print()

# 1.4 Modificar un valor
print("1.4 Modificar un valor:")
print(f"Precio original de Tablet: {serie_dict['Tablet']}")
serie_dict['Tablet'] = 350
print(f"Precio modificado de Tablet: {serie_dict['Tablet']}")
print()

# 1.5 Operación matemática (multiplicar por 2)
print("1.5 Operación matemática - Multiplicar precios por 2:")
serie_doble = serie_lista * 2
print(serie_doble)
print()

# 1.6 Operaciones adicionales
print("1.6 Operaciones adicionales:")
print(f"Suma total de precios: ${serie_lista.sum()}")
print(f"Precio promedio: ${serie_lista.mean():.2f}")
print(f"Precio máximo: ${serie_lista.max()}")
print(f"Precio mínimo: ${serie_lista.min()}")
print()

print("✓ Ejercicio 1 completado exitosamente")
