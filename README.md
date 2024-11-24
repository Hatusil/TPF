## Paso a Paso para Ejecutar el Código

### 1. Instalar Python

1. Asegúrate de que tienes Python 3.x instalado en tu sistema.

2. Verifica la instalación ejecutando este comando en tu terminal:

```bash
python --version

```
O en algunos sistemas:

```bash
python3 --version

```
---

### 2. Instalar Dependencias

1. Asegúrate de tener instalado el paquete colorama, que se utiliza para dar color a los mensajes en la terminal.

2. Instálalo ejecutando el siguiente comando:

```bash
pip install colorama

```
```bash
pip3 install colorama

```
---

### 3. Crear la Base de Datos

1. Ejecuta el archivo 'crear_db.py' para inicializar la base de datos 'inventario.db' y crear la tabla productos:

```bash
python crear_db.py

```
- Este archivo creará automáticamente una base de datos llamada 'inventario.db' si no existe.
- Si todo está bien, verás un mensaje: "Base de datos creada exitosamente."

---

### 4. Ejecutar el Programa Principal

1. Ejecuta el archivo 'inventario.py' para iniciar la aplicación

```bash
python inventario.py

```

2. Al iniciar, verás un menú interactivo como este:

```bash
Menú Principal
1. Agregar producto
2. Mostrar productos
3. Actualizar cantidad de producto
4. Eliminar producto
5. Buscar producto
6. Reporte de bajo stock
7. Salir

```
---

### 5. Usar el Menú

#### Selecciona una opción ingresando el número correspondiente y presionando Enter.
Por ejemplo:

- Para agregar un producto, selecciona 1 e ingresa los datos solicitados.
- Para generar un reporte de bajo stock, selecciona 6 e ingresa el límite de stock.


### 6. Probar las Funcionalidades
- Agregar productos: Prueba registrando varios productos para asegurarte de que se almacenan correctamente en la base de datos.
- Visualizar productos: Selecciona la opción 2 y verifica que los productos se muestren en la tabla.
- Actualizar cantidad: Usa la opción 3 para modificar la cantidad de un producto específico.
- Eliminar productos: Selecciona la opción 4 e ingresa el ID del producto que deseas eliminar.
- Buscar productos: Con la opción 5, realiza búsquedas por ID, nombre o categoría.
- Generar reportes: Usa la opción 6 para listar productos con bajo stock.

---

### 7. Finalizar

- Cuando termines de usar la aplicación, selecciona la opción 7 para salir:

```bash
Saliendo del programa.

```
### 8. (Opcional) Revisar la Base de Datos

#### Si deseas inspeccionar manualmente los datos, puedes usar un visor de SQLite, como:

- DB Browser for SQLite (disponible en sqlitebrowser.org).
- O puedes abrir la base de datos desde Python usando este comando interactivo:

```bash
import sqlite3
conn = sqlite3.connect('inventario.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM productos")
print(cursor.fetchall())
conn.close()

```
---

### Problemas Comunes y Soluciones

1. Error: Módulo no encontrado (ModuleNotFoundError)
#### Asegúrate de instalar colorama usando pip install colorama.
2. Base de datos no encontrada
#### Asegúrate de ejecutar primero crear_db.py para crear la base de datos.
3. Problemas con permisos
- Si estás en un sistema operativo con permisos restringidos, ejecuta los comandos como administrador.

#### Si sigues estos pasos, tu aplicación debería ejecutarse sin problemas. ¡Avísame si necesitas ayuda adicional! 😊

