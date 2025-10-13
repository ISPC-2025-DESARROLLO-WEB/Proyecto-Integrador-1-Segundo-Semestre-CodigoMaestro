from sistema_usuarios import Sistema_Usuarios
from catalogo_productos import Catalogo_Productos

def main():
    sistema = Sistema_Usuarios()
    catalogo = Catalogo_Productos()

    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Opción: ")

        match opcion:
            case "1":
                nombre = input("Nombre: ")
                email = input("Email: ")
                contraseña = input("Contraseña (>=6): ")
                rol = input("Rol (Administrador/Estandar): ")
                print(sistema.registrar_usuario(nombre, email, contraseña, rol))
            
            case "2":
                email = input("Email: ")
                contraseña = input("Contraseña: ")
                usuario = sistema.iniciar_sesion(email, contraseña)
                if usuario:
                    if usuario.get_rol() == "Administrador":
                        usuario.menu_admin(catalogo)
                    else:
                        usuario.menu_estandar(catalogo)
            
            case "3":
                print("Saliendo...")
                break
            
            case _:
                print("Opción inválida.")

if __name__ == "__main__":
    main()