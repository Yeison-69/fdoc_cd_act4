"""
Script principal para ejecutar todos los ejercicios de la Actividad 4
Ejecuta este archivo para ver todos los ejercicios en secuencia.
"""

import os
import sys

print("="*70)
print(" "*15 + "ACTIVIDAD 4: MANEJO DE DATOS CON PANDAS")
print("="*70)
print()

ejercicios = [
    ("00_dataset_base.py", "Dataset Base - Preparación"),
    ("01_series.py", "Ejercicio 1: Series - crear y operar"),
    ("02_dataframe.py", "Ejercicio 2: DataFrame - crear y explorar"),
    ("03_operaciones_basicas.py", "Ejercicio 3: Operaciones básicas"),
    ("04_datos_faltantes.py", "Ejercicio 4: Manejo de datos faltantes"),
    ("05_seleccion_filtrado.py", "Ejercicio 5: Selección y filtrado"),
    ("06_ordenar_datos.py", "Ejercicio 6: Ordenar datos"),
    ("07_estadisticas.py", "Ejercicio 7: Estadísticas básicas"),
    ("08_leer_guardar.py", "Ejercicio 8: Leer y guardar datos"),
    ("09_ejercicio_integrado.py", "Ejercicio 9: Ejercicio integrado"),
]

def ejecutar_ejercicio(archivo, titulo):
    """Ejecuta un ejercicio individual"""
    print("\n" + "="*70)
    print(f"EJECUTANDO: {titulo}")
    print("="*70 + "\n")
    
    if not os.path.exists(archivo):
        print(f"❌ Error: No se encontró el archivo {archivo}")
        return False
    
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            codigo = f.read()
        exec(codigo)
        return True
    except Exception as e:
        print(f"❌ Error al ejecutar {archivo}: {str(e)}")
        return False

def main():
    """Función principal"""
    print("Este script ejecutará todos los ejercicios de la Actividad 4.")
    print("Presiona Enter para continuar o Ctrl+C para salir...")
    
    try:
        input()
    except KeyboardInterrupt:
        print("\n\n❌ Ejecución cancelada por el usuario.")
        sys.exit(0)
    
    resultados = []
    
    for archivo, titulo in ejercicios:
        exito = ejecutar_ejercicio(archivo, titulo)
        resultados.append((titulo, exito))
        
        if exito:
            print(f"\n✓ {titulo} completado")
        else:
            print(f"\n❌ {titulo} falló")
        
        print("\n" + "-"*70)
        print("Presiona Enter para continuar al siguiente ejercicio...")
        try:
            input()
        except KeyboardInterrupt:
            print("\n\n❌ Ejecución cancelada por el usuario.")
            break
    
    # Resumen final
    print("\n" + "="*70)
    print(" "*20 + "RESUMEN DE EJECUCIÓN")
    print("="*70 + "\n")
    
    exitosos = sum(1 for _, exito in resultados if exito)
    total = len(resultados)
    
    for titulo, exito in resultados:
        estado = "✓" if exito else "❌"
        print(f"{estado} {titulo}")
    
    print("\n" + "="*70)
    print(f"Ejercicios completados: {exitosos}/{total}")
    print("="*70)

if __name__ == "__main__":
    main()
