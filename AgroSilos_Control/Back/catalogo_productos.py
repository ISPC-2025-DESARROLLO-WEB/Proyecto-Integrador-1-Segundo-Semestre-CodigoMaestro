from producto import Producto
from conexion_mysql import connect_to_mysql

class Catalogo_Productos:
    def agregar_producto(self, nombre, precio, stock, id_usuario):
        conn = connect_to_mysql()
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO productos (nombre, precio, stock, agregado_por) VALUES (%s, %s, %s, %s)",
                        (nombre, precio, stock, id_usuario))
            conn.commit()
            print(f"Producto '{nombre}' agregado correctamente por el usuario ID {id_usuario}.")
        except Exception as e:
            conn.rollback()
            print("Error al agregar producto:", e)
        finally:
            cur.close() 
            conn.close()

    def mostrar_productos(self):
        #Lista TODOS los productos + quien los cargo (JOIN producto - usuario)
        conn = connect_to_mysql()
        cur = conn.cursor(dictionary=True)
        try:
            cur.execute(
                "SELECT p.id AS id_producto, p.nombre AS producto, p.precio, p.stock, "
                "u.nombre AS usuario, u.email AS correo "
                "FROM productos p INNER JOIN usuarios u ON p.agregado_por = u.id "
                "ORDER BY p.id;"
          )
            
            productos = cur.fetchall()
            if not productos:
                print("No hay productos en el catálogo.")
                return
            print("\n----- CATÁLOGO DE PRODUCTOS -----")
            for p in productos:
                print(f"[{p['id_producto']}] {p['producto']} | Precio: ${p['precio']:.2f} | Stock: {p['stock']} u. | Agregado por: {p['usuario']} ({p['correo']})")
        
        except Exception as e:
           print("Error al mostrar productos:", e)
        finally:
            cur.close()
            conn.close()

    def eliminar_producto(self, id_producto):
        conn = connect_to_mysql()
        cur = conn.cursor()
        try:
            cur.execute("DELETE FROM productos WHERE id=%s", (id_producto,))
            if cur.rowcount == 0:
                print("Producto no encontrado.")
            else:
                conn.commit()
                print(f"Producto (ID {id_producto}) eliminado.")
        except Exception as e:
            conn.rollback()
            print("Error al eliminar producto:", e)
        finally:
            cur.close()
            conn.close()

    def modificar_stock(self, id_producto, nuevo_stock):
        conn = connect_to_mysql()
        cur = conn.cursor()
        try:
            cur.execute("UPDATE productos SET stock=%s WHERE id=%s", (nuevo_stock, id_producto))
            if cur.rowcount == 0:
                print("Producto no encontrado.")
            else:
                conn.commit()
                print(f"Stock actualizado (ID {id_producto}) → {nuevo_stock}")
        except Exception as e:
            conn.rollback()
            print("Error al actualizar stock:", e)
        finally:
            cur.close()
            conn.close()

    # Menú propio del catálogo
    def menu_gestion_productos(self, usuario_id = None):
        while True:
            print("\n===== GESTIÓN DE PRODUCTOS =====")
            print("1. Agregar producto")
            print("2. Mostrar catálogo")
            print("3. Modificar stock")
            print("4. Eliminar producto")
            print("5. Volver")
            opcion = input("Opción: ")

            match opcion:
                case "1":
                    nombre = input("Nombre: ")
                    precio = float(input("Precio: "))
                    stock = int(input("Stock: "))
                    if usuario_id is None:
                        print("Error: ID de usuario no proporcionado.")
                    else:
                        self.agregar_producto(nombre, precio, stock, usuario_id)
                case "2":
                    self.mostrar_productos()
                case "3":
                    id_p = input("ID producto: ")
                    nuevo_stock = int(input("Nuevo stock: "))
                    self.modificar_stock(id_p, nuevo_stock)
                case "4":
                    id_p = input("ID producto: ")
                    self.eliminar_producto(id_p)
                case "5":
                    break
                case _:
                    print("Opción inválida.")