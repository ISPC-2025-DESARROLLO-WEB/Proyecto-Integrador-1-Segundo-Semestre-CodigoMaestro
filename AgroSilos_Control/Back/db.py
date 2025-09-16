import pymysql

try:
    # Conexión a la base de datos
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='admin',
        database='sistema_usuarios'
    )
    cursor = connection.cursor()

    # Pedir datos del usuario por terminal
    nombre = input("Nombre: ")
    email = input("Email: ")
    password = input("Contraseña: ")
    rol = input("Rol (usuario/admin, opcional, presiona Enter para 'usuario'): ") or "usuario"

    # Insertar usuario en la tabla 'usuarios'
    sql = "INSERT INTO usuarios (nombre, email, password, rol) VALUES (%s, %s, %s, %s)"
    valores = (nombre, email, password, rol)
    cursor.execute(sql, valores)
    connection.commit()
    print(f"Usuario guardado correctamente, ID: {cursor.lastrowid}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
        print("Conexión cerrada correctamente.")