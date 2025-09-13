class Usuario:
    def __init__(self, id_usuario, nombre, email, contraseña, rol):
        # Atributos privados (con doble guión bajo para mejor proteccion)
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__email = email
        self.__contraseña = contraseña
        self.__rol = rol

    # Getters (buena practica)
    def get_id_usuario(self):
        return self.__id_usuario

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    def get_rol(self):
        return self.__rol

    def get_contraseña(self):
        return self.__contraseña

    # Método para ver datos sin contraseña
    def ver_datos(self):
        print("----------- INFORMACIÓN PERSONAL ----------")
        return (
            f"ID Usuario: {self.__id_usuario}\n"
            f"Nombre: {self.__nombre}\n"
            f"Email: {self.__email}\n"
            f"Rol: {self.__rol}\n"
        )

   
    