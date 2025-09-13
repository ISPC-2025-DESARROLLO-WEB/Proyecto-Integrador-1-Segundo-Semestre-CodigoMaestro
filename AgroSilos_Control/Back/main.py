from modulo_sistema_usuarios import Sistema_De_Usuarios

sistema = Sistema_De_Usuarios()

def menu_principal():
    while True:
        print("----------- MENU PRINCIPAL ----------")
        print("[1] Registrar Usuario") 
        print("[2] Iniciar Sesión")
        print("[3] Salir del Menú Principal")
        opcion = input("Seleccione una de las opciones: ")

        match opcion:
            case "1":
                nombre = input("Ingrese su Nombre: ").strip()
                email = input("Ingrese su Email: ").strip()
                contraseña = input("Ingrese una Contraseña (mínimo 6 caracteres): ").strip()
                
                while True:
                    rol = input("Ingrese su rol (Administrador / Estandar): ").strip().capitalize()
                    if rol in ["Administrador", "Estandar"]:
                        break
                    else:
                        print("Rol inválido. Ingrese 'Administrador' o 'Estandar'.")

                resultado = sistema.registrar_usuario(nombre, email, contraseña, rol)
                print(resultado)

            case "2":
                email = input("Ingrese su Email: ").strip()
                contraseña = input("Ingrese su Contraseña: ").strip()
                usuario = sistema.iniciar_sesion(email, contraseña)
                if usuario:
                    sistema.menu_interno(usuario)
            
            case "3":
                print("Usted salió del Menú Principal.")
                break
            
            case _:
                print("ERROR!! Usted ingresó una opción no válida.")

menu_principal()


