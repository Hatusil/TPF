import sqlite3
from colorama import Fore


def agregar_producto():
    try:
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()
        nombre = input('Ingrese el nombre del producto: ')
        descripcion = input('Ingrese una breve descripción del producto: ')
        cantidad = int(input('Ingrese la cantidad disponible: '))
        precio = float(input('Ingrese el precio del producto: '))
        categoria = input('Ingrese la categoría del producto: ')

        cursor.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, cantidad, precio, categoria))
        conn.commit()
        print(Fore.GREEN + "Producto agregado exitosamente.")
    except ValueError:
        print(Fore.RED + "Error: Entrada inválida. Verifique los datos e intente nuevamente.")
    except Exception as e:
        print(Fore.RED + f"Error inesperado: {e}")
    finally:
        conn.close()



def mostrar_productos():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    conn.close()

    print("\nListado de productos:")
    print("ID | Nombre | Descripción | Cantidad | Precio | Categoría")
    print("-" * 50)
    for producto in productos:
        print(f"{producto[0]} | {producto[1]} | {producto[2]} | {producto[3]} | {producto[4]} | {producto[5]}")


def actualizar_cantidad():
    try:
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()
        id_producto = int(input('Ingrese el ID del producto a actualizar: '))
        nueva_cantidad = int(input('Ingrese la nueva cantidad: '))
        if nueva_cantidad < 0:
            print(Fore.RED + "La cantidad no puede ser negativa.")
            return

        cursor.execute('''
        UPDATE productos SET cantidad = ? WHERE id = ?
        ''', (nueva_cantidad, id_producto))
        conn.commit()
        print(Fore.YELLOW + "Cantidad actualizada exitosamente.")
    except ValueError:
        print(Fore.RED + "Error: Ingrese un número válido.")
    finally:
        conn.close()



def eliminar_producto():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    id_producto = int(input('Ingrese el ID del producto a eliminar: '))

    cursor.execute('''
    DELETE FROM productos WHERE id = ?
    ''', (id_producto,))
    conn.commit()
    conn.close()
    print(Fore.RED + "Producto eliminado exitosamente.")


def buscar_producto():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    print("Buscar producto por:")
    print("1. ID")
    print("2. Nombre")
    print("3. Categoría")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        id_producto = input("Ingrese el ID del producto: ")
        cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto,))
    elif opcion == '2':
        nombre = input("Ingrese el nombre del producto: ")
        cursor.execute('SELECT * FROM productos WHERE nombre LIKE ?', (f"%{nombre}%",))
    elif opcion == '3':
        categoria = input("Ingrese la categoría del producto: ")
        cursor.execute('SELECT * FROM productos WHERE categoria LIKE ?', (f"%{categoria}%",))
    else:
        print(Fore.RED + "Opción no válida.")
        return

    resultados = cursor.fetchall()
    conn.close()

    if resultados:
        for producto in resultados:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[3]}, Precio: {producto[4]}")
    else:
        print(Fore.RED + "No se encontraron productos.")



def reporte_bajo_stock():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    limite = int(input('Ingrese el límite de stock: '))

    cursor.execute('''
    SELECT * FROM productos WHERE cantidad <= ?
    ''', (limite,))
    productos = cursor.fetchall()
    conn.close()

    print("\nProductos con bajo stock:")
    for producto in productos:
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[3]}")


def menu():
    while True:
        print(Fore.CYAN + "\nMenú Principal")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Actualizar cantidad de producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Reporte de bajo stock")
        print("7. Salir")
        print(Fore.RESET)
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            mostrar_productos()
        elif opcion == '3':
            actualizar_cantidad()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            buscar_producto()
        elif opcion == '6':
            reporte_bajo_stock()
        elif opcion == '7':
            print(Fore.GREEN + "Saliendo del programa.")
            break
        else:
            print(Fore.RED + "Opción no válida. Intente nuevamente.")

