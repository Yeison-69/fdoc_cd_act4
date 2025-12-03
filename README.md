# Actividad 4: Manejo de Datos con Pandas

Este repositorio contiene la solución completa de la **Actividad 4: Manejo de Datos con Pandas**, alineada con el contenido "Guía de Introducción a Estructuras de Datos en Pandas".

## 📋 Contenido

El proyecto incluye ejercicios prácticos sobre:

1. **Series** - Crear y operar con Series de Pandas
2. **DataFrame** - Crear y explorar DataFrames
3. **Operaciones básicas** - Columnas derivadas y operaciones vectorizadas
4. **Manejo de datos faltantes** - Detectar y completar valores nulos
5. **Selección y filtrado** - Filtrar datos según condiciones
6. **Ordenar datos** - Ordenamiento por columnas y criterios
7. **Estadísticas básicas** - Análisis descriptivo y agregaciones
8. **Leer y guardar datos** - Lectura/escritura de archivos CSV
9. **Ejercicio integrado** - Aplicación completa de múltiples operaciones

## 📁 Estructura del Proyecto

```
fdoc_cd_act4-main/
│
├── 00_dataset_base.py           # Creación del dataset base
├── 01_series.py                 # Ejercicio 1: Series
├── 02_dataframe.py              # Ejercicio 2: DataFrame
├── 03_operaciones_basicas.py    # Ejercicio 3: Operaciones básicas
├── 04_datos_faltantes.py        # Ejercicio 4: Datos faltantes
├── 05_seleccion_filtrado.py     # Ejercicio 5: Filtrado
├── 06_ordenar_datos.py          # Ejercicio 6: Ordenamiento
├── 07_estadisticas.py           # Ejercicio 7: Estadísticas
├── 08_leer_guardar.py           # Ejercicio 8: Lectura/escritura
├── 09_ejercicio_integrado.py    # Ejercicio 9: Integrado
├── ejecutar_todos.py            # Script para ejecutar todos los ejercicios
└── README.md                    # Este archivo
```

## 🚀 Requisitos

- Python 3.7 o superior
- Pandas

### Instalación de dependencias

```bash
pip install pandas
```

## 💻 Cómo usar

### Opción 1: Ejecutar todos los ejercicios

```bash
python ejecutar_todos.py
```

Este script ejecutará todos los ejercicios en secuencia, mostrando los resultados de cada uno.

### Opción 2: Ejecutar ejercicios individuales

Puedes ejecutar cada ejercicio por separado:

```bash
python 00_dataset_base.py
python 01_series.py
python 02_dataframe.py
# ... y así sucesivamente
```

### Opción 3: Ejecutar en Jupyter Notebook

Puedes copiar el contenido de cada archivo `.py` en celdas de Jupyter Notebook para una ejecución interactiva.

## 📊 Dataset Base

El dataset base utilizado en los ejercicios contiene información de productos:

| Índice | nombre | edad | ciudad   | producto  | precio | stock |
|--------|--------|------|----------|-----------|--------|-------|
| a      | Ana    | 25   | Madrid   | Laptop    | 1200   | 10    |
| b      | Bob    | 30   | Lima     | Teléfono  | 800    | 15    |
| c      | Clara  | 22   | Bogotá   | Tablet    | 300    | 5     |
| d      | Diego  | None | Medellín | Laptop    | 1150   | 8     |
| e      | Eva    | 28   | None     | Tablet    | None   | 0     |

El dataset incluye:
- Columnas numéricas: `edad`, `precio`, `stock`
- Columnas categóricas: `nombre`, `ciudad`, `producto`
- Índices personalizados: `a`, `b`, `c`, `d`, `e`
- Valores faltantes para practicar su manejo

## 📝 Descripción de Ejercicios

### Ejercicio 1: Series
- Crear Series desde listas y diccionarios
- Acceder a elementos por índice
- Modificar valores
- Realizar operaciones matemáticas

### Ejercicio 2: DataFrame
- Crear DataFrames con índices personalizados
- Acceder a columnas
- Usar `loc` e `iloc` para selección

### Ejercicio 3: Operaciones Básicas
- Agregar columnas derivadas (descuentos, IVA)
- Operaciones vectorizadas
- Categorización de datos

### Ejercicio 4: Datos Faltantes
- Detectar nulos con `isna()`
- Contar valores faltantes
- Completar con `fillna()`

### Ejercicio 5: Selección y Filtrado
- Filtrar por condiciones simples y múltiples
- Usar `isin()` y `query()`
- Filtrar valores no nulos

### Ejercicio 6: Ordenar Datos
- Ordenar por una o múltiples columnas
- Manejo de nulos en ordenamiento
- Resetear índices

### Ejercicio 7: Estadísticas
- `describe()` para estadísticas descriptivas
- `value_counts()` para conteos
- Agrupaciones con `groupby()`

### Ejercicio 8: Leer y Guardar
- Leer y escribir archivos CSV
- Usar diferentes separadores
- Guardar columnas seleccionadas

### Ejercicio 9: Integrado
- Aplicar descuento del 10%
- Filtrar por stock > 5
- Ordenar por precio con descuento
- Guardar resultado procesado

## 📤 Archivos Generados

Los ejercicios generan los siguientes archivos CSV:

- `actividad_semana4.csv` - Dataset base
- `productos_precios.csv` - Columnas seleccionadas
- `actividad_separador.csv` - Con separador `;`
- `productos_premium.csv` - Productos filtrados
- `inventario_procesado.csv` - Resultado del ejercicio integrado

## 🎯 Objetivos de Aprendizaje

Al completar esta actividad, habrás practicado:

✅ Creación y manipulación de Series y DataFrames  
✅ Operaciones vectorizadas y columnas derivadas  
✅ Manejo efectivo de valores faltantes  
✅ Técnicas de filtrado y selección de datos  
✅ Ordenamiento de datos con diferentes criterios  
✅ Cálculo de estadísticas descriptivas  
✅ Lectura y escritura de archivos CSV  
✅ Integración de múltiples operaciones en flujos de trabajo

## 📚 Recursos Adicionales

- [Documentación oficial de Pandas](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

## 👨‍💻 Autor

Actividad desarrollada para el curso de Ciencia de Datos.

## 📄 Licencia

Este proyecto es de uso educativo.

---

**¡Feliz aprendizaje con Pandas! 🐼**