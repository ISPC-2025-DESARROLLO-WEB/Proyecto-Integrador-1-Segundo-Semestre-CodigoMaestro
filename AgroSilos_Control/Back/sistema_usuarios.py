from usuarios import Usuario

class Sistema_De_Usuarios:
    def __init__(self):
        self.usuarios = []        # Lista de usuarios
        self.contador_id = 1      # Contador para asignar IDs únicos

    def registrar_usuario(self, nombre, email, contraseña, rol):
        if nombre == "" or email == "" or contraseña == "" or rol == "":
            return "ERROR!! Hay algunos campos inválidos."

        if rol not in ["Administrador", "Estandar"]:
            return "Rol no reconocido. Debe ser 'Administrador' o 'Estandar'."

        if len(contraseña) < 6:
            return "INVALIDA!! La contraseña debe contener como mínimo 6 caracteres."

        for usuario in self.usuarios:
            if usuario.get_email() == email:
                return "ERROR!! Ya existe un usuario registrado con ese email."

        nuevo_usuario = Usuario(self.contador_id, nombre, email, contraseña, rol)
        self.usuarios.append(nuevo_usuario)
        self.contador_id += 1     # Incrementar ID para el siguiente usuario

        return "EXCELENTE!! Usuario registrado."

    def iniciar_sesion(self, email, contraseña):
        if email == "" or contraseña == "":
            print("No se puede Iniciar Sesión. Campos incompletos.")
            return None

        for usuario in self.usuarios:
            if usuario.get_email() == email and usuario.get_contraseña() == contraseña:
                print("--------------------------")
                print(f"Inicio de sesión exitoso!! Bienvenido {usuario.get_nombre()}")
                return usuario

        print("ERROR!! Contraseña o email incorrecto.")    
        return None

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No se ha registrado ningún usuario.")
        else:
            print("---------- Listado de Usuarios ----------")
            for usuario in self.usuarios:
                print(usuario.ver_datos())

    def eliminar_usuario(self, id_usuario):
        try:
            id_usuario = int(id_usuario)  # asegurar número
        except ValueError:
            print("ERROR: El ID debe ser numérico.")
            return

        for x, usuario in enumerate(self.usuarios):
            if usuario.get_id_usuario() == id_usuario:
                eliminado = self.usuarios.pop(x)
                print(f"Se eliminó al Usuario: {eliminado.get_nombre()} con número de ID: {eliminado.get_id_usuario()}.")
                return

        print(f"El Id_usuario: {id_usuario} no se encuentra registrado.")

    def cambiar_rol(self, id_usuario, nuevo_rol):
        try:
            id_usuario = int(id_usuario)
        except ValueError:
            print("ERROR: El ID debe ser numérico.")
            return

        for usuario in self.usuarios:
            if usuario.get_id_usuario() == id_usuario:
                usuario.set_rol(nuevo_rol)  
                print(f"{nuevo_rol} es el nuevo rol del usuario {usuario.get_nombre()} con número de ID: {id_usuario}")
                return
        print("ERROR!! Usuario no registrado.")

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