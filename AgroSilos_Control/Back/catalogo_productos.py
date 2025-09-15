from productos import Producto

class Catalogo:
    def __init__(self):
        self.productos = []
        self.contador_id = 1   # Contador para IDs automáticos

    def agregar_producto(self, nombre, precio, stock):
        nuevo = Producto(self.contador_id, nombre, precio, stock)
        self.productos.append(nuevo)
        self.contador_id += 1  
        return f"Producto '{nombre}' agregado con ID {nuevo.get_id_producto()}."

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el catálogo.")
        else:
            print("\n----- CATÁLOGO DE PRODUCTOS -----")
            for p in self.productos:
                print(p)

    def eliminar_producto(self, id_producto):
        try:
            id_producto = int(id_producto)
        except ValueError:
            print("ERROR: El ID debe ser numérico.")
            return

        for p in self.productos:
            if p.get_id_producto() == id_producto:
                self.productos.remove(p)
                print(f"Producto '{p.get_nombre()}' eliminado.")
                return
        print("Producto no encontrado.")

    def modificar_stock(self, id_producto, nuevo_stock):
        try:
            id_producto = int(id_producto)
        except ValueError:
            print("ERROR: El ID debe ser numérico.")
            return

        for p in self.productos:
            if p.get_id_producto() == id_producto:
                p.set_stock(nuevo_stock)
                print(f"Stock actualizado para '{p.get_nombre()}'. Nuevo stock: {nuevo_stock}")
                return
        print("Producto no encontrado.")