from sistema_usuarios import Sistema_De_Usuarios
from catalogo_productos import Catalogo

sistema = Sistema_De_Usuarios()
catalogo = Catalogo()

def menu_principal():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Registrar Usuario")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                nombre = input("Nombre: ")
                email = input("Email: ")
                contraseña = input("Contraseña: ")
                rol = input("Rol (Administrador/Estandar): ")
                print(sistema.registrar_usuario(nombre, email, contraseña, rol))

            case "2":
                email = input("Email: ")
                contraseña = input("Contraseña: ")
                usuario = sistema.iniciar_sesion(email, contraseña)
                if usuario:
                    sistema.menu_interno(usuario)  
            case "3":
                print("Saliendo del sistema...")
                break

            case _:
                print("Opción inválida.")

# Submenú de productos (solo accesible desde Admin)
def menu_productos():
    while True:
        print("\n===== MENU PRODUCTOS =====")
        print("1. Agregar producto")
        print("2. Mostrar catálogo")
        print("3. Modificar stock")
        print("4. Eliminar producto")
        print("5. Volver al menú principal")
        opcion = input("Opción: ")

        match opcion:
            case "1":
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                stock = int(input("Stock: "))
                print(catalogo.agregar_producto(nombre, precio, stock))

            case "2":
                catalogo.mostrar_productos()

            case "3":
                id_p = input("ID producto: ")
                nuevo_stock = int(input("Nuevo stock: "))
                catalogo.modificar_stock(id_p, nuevo_stock)

            case "4":
                id_p = input("ID producto: ")
                catalogo.eliminar_producto(id_p)

            case "5":
                break

            case _:
                print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()