import sqlite3

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('inventario.db')
cursor = conn.cursor()

# Crear tabla 'productos'
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL,
    categoria TEXT
)
''')

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()
print("Base de datos creada exitosamente.")