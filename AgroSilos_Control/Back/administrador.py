from usuario import Usuario
from estandar import Estandar
from conexion_mysql import connect_to_mysql 

class Administrador(Usuario):
    def __init__(self, id_usuario, nombre, email, contraseña):
        super().__init__(id_usuario, nombre, email, contraseña, "Administrador")

    # --- Operaciones de administración sobre usuarios ---
    def mostrar_usuarios(self):
        conn = connect_to_mysql()
        cur = conn.cursor(dictionary=True)
        try:
            cur.execute("SELECT id, nombre, email, rol FROM usuarios ORDER BY id")
            filas = cur.fetchall()
            if not filas:
                print("No se ha registrado ningún usuario.")
                return
            print("---------- Listado de Usuarios ----------")
            for u in filas:
                print(f"[{u['id']}] {u['nombre']} | {u['email']} | Rol: {u['rol']}")
        finally:
            cur.close()
            conn.close()

    def eliminar_usuario(self, id_usuario):
        conn = connect_to_mysql()
        cursor = conn.cursor()
        try:
            id_usuario = int(id_usuario)
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
            if cursor.rowcount == 0:
                print("ERROR: Usuario no encontrado.")
            else:
                conn.commit()
                print(f"Se eliminó al usuario con ID {id_usuario}.")
        except Exception as e:
            conn.rollback()
            print (f"ERROR al eliminar usuario: {e}")
        finally:
            cursor.close()
            conn.close()

    def cambiar_rol(self, id_usuario, nuevo_rol):
        if nuevo_rol not in ("Administrador", "Estandar"):
            print("Rol no válido (use 'Administrador' o 'Estandar').")
            return
        conn = connect_to_mysql()
        cur = conn.cursor()
        try:
            cur.execute("UPDATE usuarios SET rol=%s WHERE id=%s", (nuevo_rol, id_usuario))
            if cur.rowcount == 0:
                print("ERROR: Usuario no encontrado.")
            else:
                conn.commit()
                print(f"Rol actualizado (ID {id_usuario}) → {nuevo_rol}")
        except Exception as e:
            conn.rollback()
            print("Error al cambiar rol:", e)
        finally:
            cur.close()
            conn.close()

    def crear_usuario(self, nombre, email, contraseña, rol):
        """Alta de usuario por un admin (similar a registrar, pero explícito desde Admin)."""
        from sistema_usuarios import Sistema_Usuarios
        sistema = Sistema_Usuarios()
        print(sistema.registrar_usuario(nombre, email, contraseña, rol))

    # --- Menú del administrador ---
    def menu_admin(self, catalogo):
        while True:
            print("\n===== MENU ADMIN =====")
            print("1. Mostrar usuarios")
            print("2. Eliminar usuario")
            print("3. Cambiar rol")
            print("4. Crear usuario")
            print("5. Gestionar productos")
            print("6. Cerrar sesión")
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
                    n = input("Nombre: "); e = input("Email: ")
                    c = input("Contraseña: "); r = input("Rol (Administrador/Estandar): ")
                    self.crear_usuario(n, e, c, r)
                
                case "5":
                    catalogo.menu_gestion_productos(self.get_id_usuario())
                
                case "6":
                    break
                
                case _:
                    print("Opción inválida.")