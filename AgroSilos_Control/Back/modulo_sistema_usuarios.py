from modulo_usuario import Usuario

class Sistema_De_Usuarios:
    def __init__(self):
        self.usuarios = []  # Lista para almacenar usuarios
        self.contador_id = 1  # Para generar ID automáticamente

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
        self.contador_id += 1  # Incrementar ID para el siguiente usuario

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

    def cambiar_rol(self, id_usuario, nuevo_rol):
        for usuario in self.usuarios:
            if usuario.get_id_usuario() == id_usuario:
                usuario._Usuario__rol = nuevo_rol  # Acceso directo porque no hay set_rol
                print(f"{nuevo_rol} es el nuevo rol del usuario {usuario.get_nombre()} con número de ID: {id_usuario}")
                return
        print("ERROR!! Usuario no registrado.")

    def eliminar_usuario(self, id_usuario):
        for x, usuario in enumerate(self.usuarios):
            if usuario.get_id_usuario() == id_usuario:
                eliminado = self.usuarios.pop(x)
                print(f"Se eliminó al Usuario: {eliminado.get_nombre()} con número de ID: {eliminado.get_id_usuario()}.")
                return

        print(f"El Id_usuario: {id_usuario} no se encuentra registrado.")

    def menu_interno(self, usuario):
        while True:
            print("---------- MENU PRINCIPAL ----------")
            if usuario.get_rol() == "Estandar":
                print("[1] Ver Información Personal.")
                print("[2] Salir del Menú.")
                opcion = input("Seleccione una de las opciones: ")

                match opcion:
                    case "1":
                        print(usuario.ver_datos())

                    case "2":
                        print("Usted salió del Menú.")
                        break

                    case _:
                        print("ERROR!! Usted ingresó una opción no válida.")

            elif usuario.get_rol() == "Administrador":
                print("[1] Ver Información Personal.")
                print("[2] Ver el Listado de Usuarios Registrados.")
                print("[3] Cambiar el rol a un usuario.")
                print("[4] Eliminar a un usuario.")
                print("[5] Salir del Menú.")
                opcion = input("Seleccione una opción: ")

                match opcion:
                    case "1":
                        print(usuario.ver_datos())

                    case "2":
                        self.mostrar_usuarios()

                    case "3":
                        try:
                            id_usuario = int(input("Ingrese el ID del usuario a buscar: "))
                            nuevo_rol = input("Ingrese el nuevo rol del usuario: ")
                            self.cambiar_rol(id_usuario, nuevo_rol)
                        except ValueError:
                            print("ERROR: El ID debe ser numérico.")

                    case "4":
                        try:
                            id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
                            self.eliminar_usuario(id_usuario)
                        except ValueError:
                            print("ERROR: El ID debe ser numérico.")

                    case "5":
                        print("Usted salió del Menú.")
                        break

                    case _:
                        print("ERROR!! Usted ingresó una opción no válida.")