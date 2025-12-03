# Instrucciones para Fork y Entrega

## 📋 Pasos para entregar la actividad

### 1. Hacer Fork del repositorio base

1. Ve al repositorio base: https://github.com/jfinfosena/fdoc_cd_act4.git
2. Haz clic en el botón **Fork** en la esquina superior derecha
3. Esto creará una copia del repositorio en tu cuenta de GitHub

### 2. Clonar tu Fork

```bash
# Clona tu fork (reemplaza TU_USUARIO con tu nombre de usuario de GitHub)
git clone https://github.com/TU_USUARIO/fdoc_cd_act4.git

# Entra al directorio
cd fdoc_cd_act4
```

### 3. Copiar los archivos de la solución

Copia todos los archivos de este directorio (`fdoc_cd_act4-main`) al directorio clonado:

- `00_dataset_base.py`
- `01_series.py`
- `02_dataframe.py`
- `03_operaciones_basicas.py`
- `04_datos_faltantes.py`
- `05_seleccion_filtrado.py`
- `06_ordenar_datos.py`
- `07_estadisticas.py`
- `08_leer_guardar.py`
- `09_ejercicio_integrado.py`
- `ejecutar_todos.py`
- `README.md`

### 4. Agregar y confirmar cambios

```bash
# Agregar todos los archivos
git add .

# Hacer commit con un mensaje descriptivo
git commit -m "Completar Actividad 4: Manejo de Datos con Pandas"
```

### 5. Subir cambios a GitHub

```bash
# Subir los cambios a tu fork
git push origin main
```

### 6. Verificar en GitHub

1. Ve a tu repositorio en GitHub: `https://github.com/TU_USUARIO/fdoc_cd_act4`
2. Verifica que todos los archivos estén presentes
3. Comparte el enlace de tu repositorio para la entrega

## ✅ Checklist de Entrega

Antes de entregar, verifica que:

- [ ] Has hecho fork del repositorio base
- [ ] Has clonado tu fork localmente
- [ ] Todos los archivos Python están en el repositorio
- [ ] El README.md está actualizado
- [ ] Has hecho commit de todos los cambios
- [ ] Has hecho push a tu fork en GitHub
- [ ] Todos los ejercicios funcionan correctamente
- [ ] El archivo `actividad_semana4.csv` se genera correctamente

## 🧪 Prueba antes de entregar

Ejecuta el script principal para verificar que todo funciona:

```bash
python ejecutar_todos.py
```

O ejecuta los ejercicios individuales:

```bash
python 00_dataset_base.py
python 01_series.py
# ... etc
```

## 📝 Notas Importantes

- **No modifiques** el repositorio original (jfinfosena/fdoc_cd_act4)
- Trabaja siempre en **tu fork**
- Asegúrate de que tu repositorio sea **público** para que pueda ser revisado
- Si necesitas hacer correcciones, simplemente haz commit y push de nuevo

## 🆘 Solución de Problemas

### Error: "fatal: not a git repository"
Asegúrate de estar dentro del directorio clonado: `cd fdoc_cd_act4`

### Error: "Permission denied"
Verifica que hayas clonado tu fork, no el repositorio original

### Error al ejecutar Python
Verifica que tengas Python instalado: `python --version`
Instala pandas si es necesario: `pip install pandas`

---

**¡Buena suerte con tu entrega! 🚀**
