from usuario import Usuario

class Estandar(Usuario):
    def __init__(self, id_usuario, nombre, email, contraseña):
        super().__init__(id_usuario, nombre, email, contraseña, "Estandar")

    def menu_estandar(self, catalogo):
        while True:
            print("\n===== MENU ESTÁNDAR =====")
            print("1. Ver mis datos")
            print("2. Ver catálogo de productos")
            print("3. Cerrar sesión")
            opcion = input("Opción: ")

            match opcion:
                case "1":
                    print(self.ver_datos())
                case "2":
                    catalogo.mostrar_productos()
                case "3":
                    break
                case _:
                    print("Opción inválida.")