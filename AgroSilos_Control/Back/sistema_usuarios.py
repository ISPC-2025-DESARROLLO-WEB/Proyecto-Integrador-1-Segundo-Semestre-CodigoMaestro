from usuarios import Usuario
import db

class Sistema_De_Usuarios:
    def __init__(self):
        self.conn = db.conectar()
        self.cursor = self.conn.cursor(dictionary=True)

    def registrar_usuario(self, nombre, email, contraseña, rol):
        if nombre == "" or email == "" or contraseña == "" or rol == "":
            return "ERROR!! Hay algunos campos inválidos."

        if rol not in ["Administrador", "Estandar"]:
            return "Rol no reconocido. Debe ser 'Administrador' o 'Estandar'."

        if len(contraseña) < 6:
            return "INVALIDA!! La contraseña debe contener como mínimo 6 caracteres."

        try:
            sql = "INSERT INTO usuarios (nombre, email, password, rol) VALUES (%s, %s, %s, %s)"
            valores = (nombre, email, contraseña, rol)
            self.cursor.execute(sql, valores)
            self.conn.commit()
            return "EXCELENTE!! Usuario registrado en la BD."
        except Exception as e:
            return f"ERROR!! No se pudo registrar: {e}"

    def iniciar_sesion(self, email, contraseña):
        if email == "" or contraseña == "":
            print("No se puede Iniciar Sesión. Campos incompletos.")
            return None

        sql = "SELECT * FROM usuarios WHERE email=%s AND password=%s"
        self.cursor.execute(sql, (email, contraseña))
        usuario_db = self.cursor.fetchone()

        if usuario_db:
            print("--------------------------")
            print(f"Inicio de sesión exitoso!! Bienvenido {usuario_db['nombre']}")
            return Usuario(usuario_db["id"], usuario_db["nombre"], usuario_db["email"], usuario_db["password"], usuario_db["rol"])
        else:
            print("ERROR!! Contraseña o email incorrecto.")    
            return None

    def mostrar_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        usuarios = self.cursor.fetchall()

        if not usuarios:
            print("No se ha registrado ningún usuario.")
        else:
            print("---------- Listado de Usuarios ----------")
            for usuario in usuarios:
                print(f"ID: {usuario['id']} | Nombre: {usuario['nombre']} | Email: {usuario['email']} | Rol: {usuario['rol']}")

    def eliminar_usuario(self, id_usuario):
        try:
            id_usuario = int(id_usuario)
            sql = "DELETE FROM usuarios WHERE id=%s"
            self.cursor.execute(sql, (id_usuario,))
            self.conn.commit()

            if self.cursor.rowcount > 0:
                print(f"Usuario con ID {id_usuario} eliminado correctamente.")
            else:
                print("ERROR!! Usuario no encontrado.")
        except ValueError:
            print("ERROR: El ID debe ser numérico.")

    def cambiar_rol(self, id_usuario, nuevo_rol):
        try:
            id_usuario = int(id_usuario)
            sql = "UPDATE usuarios SET rol=%s WHERE id=%s"
            self.cursor.execute(sql, (nuevo_rol, id_usuario))
            self.conn.commit()

            if self.cursor.rowcount > 0:
                print(f"Rol cambiado correctamente para el usuario con ID {id_usuario}.")
            else:
                print("ERROR!! Usuario no registrado.")
        except ValueError:
            print("ERROR: El ID debe ser numérico.")

    def menu_interno(self, usuario):
        if usuario.get_rol() == "Administrador":
            self.menu_admin(usuario)
        else:
            self.menu_estandar(usuario)

    def menu_admin(self, usuario):
        while True:
            print("\n===== MENU ADMIN =====")
            print("1. Mostrar usuarios")
            print("2. Eliminar usuario")
            print("3. Cambiar rol")
            print("4. Gestionar productos")
            print("5. Cerrar sesión")
            opcion = input("Opción: ")

            match opcion:
                case "1":
                    self.mostrar_usuarios()
                case "2":
                    id_u = input("ID del usuario a eliminar: ")
                    self.eliminar_usuario(id_u)
                case "3":
                    id_u = input("ID del usuario: ")
                    nuevo_rol = input("Nuevo rol (Administrador/Estandar): ")
                    self.cambiar_rol(id_u, nuevo_rol)
                case "4":
                    import main
                    main.menu_productos()
                case "5":
                    break
                case _:
                    print("Opción inválida.")

    def menu_estandar(self, usuario):
        while True:
            print("\n===== MENU ESTÁNDAR =====")
            print("1. Ver mis datos")
            print("2. Ver catálogo de productos")
            print("3. Cerrar sesión")
            opcion = input("Opción: ")

            match opcion:
                case "1":
                    print(usuario.ver_datos())
                case "2":
                    import main
                    main.catalogo.mostrar_productos()
                case "3":
                    break
                case _:
                    print("Opción inválida.")