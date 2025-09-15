class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    # Getters
    def get_id_producto(self):
        return self.__id_producto
    
    def get_nombre(self):
        return self.__nombre
    
    def get_precio(self):
        return self.__precio
    
    def get_stock(self):
        return self.__stock

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_precio(self, precio):
        self.__precio = precio
    
    def set_stock(self, stock):
        self.__stock = stock

    def __str__(self):
        return (
            f"[{self.get_id_producto()}] "
            f"{self.get_nombre()} | "
            f"Precio: ${self.get_precio():.2f} | "
            f"Stock: {self.get_stock()} unidades"
        )