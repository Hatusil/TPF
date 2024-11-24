## Gestión de Inventario - README

### Descripción
Esta es una aplicación desarrollada en **Python** para gestionar el inventario de una pequeña tienda. Permite registrar, actualizar, eliminar y mostrar productos, además de realizar búsquedas y generar reportes de bajo stock. La aplicación utiliza **SQLite** como base de datos y ofrece una interfaz interactiva basada en la línea de comandos.

---

### Funcionalidades

1. **Agregar producto**: Permite registrar nuevos productos ingresando datos como nombre, descripción, cantidad, precio y categoría.
2. **Mostrar productos**: Lista todos los productos registrados en el inventario.
3. **Actualizar cantidad de producto**: Modifica la cantidad disponible de un producto específico utilizando su ID.
4. **Eliminar producto**: Elimina un producto del inventario a partir de su ID.
5. **Buscar producto**: Busca productos por ID, nombre o categoría y muestra los resultados coincidentes.
6. **Reporte de bajo stock**: Genera un informe de productos con cantidad igual o menor a un límite especificado por el usuario.
7. **Salir**: Finaliza la ejecución del programa.

---

### Dependencias

- **Python** 3.x
- **Biblioteca** `colorama`

### Instalación de dependencias

Para instalar las dependencias necesarias, ejecuta este comando en tu terminal:

```bash
pip install colorama
```
---

## Configuración

### Creación de la base de datos
Ejecuta el archivo `crear_db.py` para inicializar la base de datos `inventario.db` y crear la tabla `productos`.

---

### Estructura de la base de datos
La tabla `productos` incluye las siguientes columnas:

- **id**: Identificador único del producto (clave primaria, autoincremental).
- **nombre**: Nombre del producto (texto, no nulo).
- **descripcion**: Breve descripción del producto (texto).
- **cantidad**: Cantidad disponible del producto (entero, no nulo).
- **precio**: Precio del producto (real, no nulo).
- **categoria**: Categoría del producto (texto).
---

### Ejecución
1. Asegúrate de que la base de datos `inventario.db` haya sido creada correctamente.
2. Ejecuta el archivo principal `inventario.py`:
   
   ```bash
   python inventario.py
   ```
4. Sigue las instrucciones en el menú interactivo.

---
### Uso de la aplicación

#### Menú Principal
Al iniciar la aplicación, se mostrará un menú con las siguientes opciones:

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

Selecciona una opción ingresando el número correspondiente.

---

### Ejemplo de Uso
#### 1. Agregar un Producto
Selecciona la opción 1 del menú.
 ```bash
Ingresa los datos solicitados:
Nombre
Descripción
Cantidad
Precio
Categoría
```
La aplicación confirmará que el producto fue agregado exitosamente.

#### 2. Generar Reporte de Bajo Stock
Selecciona la opción 6 del menú.

 ```bash
Ingresa el límite de stock.
```
La aplicación mostrará todos los productos con cantidad igual o menor al límite ingresado.

---

### Recomendaciones
#### Asegúrate de ingresar datos válidos (por ejemplo, cantidades mayores a 0 y precios reales positivos).
#### Para evitar errores, sigue las instrucciones de cada funcionalidad.

---

### Archivos incluidos
```bash
crear_db.py: Crea la base de datos y la tabla productos.
inventario.py: Archivo principal con las funcionalidades de la aplicación.
inventario.db: Base de datos SQLite (se genera automáticamente tras ejecutar crear_db.py).
README.md: Documento de ayuda y guía para la aplicación.
```

