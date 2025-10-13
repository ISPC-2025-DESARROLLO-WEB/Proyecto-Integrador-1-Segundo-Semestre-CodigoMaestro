from administrador import Administrador
from estandar import Estandar
from conexion_mysql import connect_to_mysql

class Sistema_Usuarios:
    def registrar_usuario(self, nombre, email, contraseña, rol):
        # Validaciones mínimas
        if not (nombre and email and contraseña and rol):
            return "ERROR: Hay campos vacíos."
        if len(contraseña) < 6:
            return "ERROR: La contraseña debe tener al menos 6 caracteres."
        if rol not in ("Administrador", "Estandar"):
            return "ERROR: Rol inválido."

        conn = connect_to_mysql()
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO usuarios (nombre, email, contrasena, rol) VALUES (%s, %s, %s, %s)",
                        (nombre, email, contraseña, rol))
            conn.commit()
            return f"Usuario '{nombre}' registrado como {rol}."
        except Exception as e:
            conn.rollback()
            # Email duplicado u otro error
            return f"Error al registrar: {e}"
        finally:
            cur.close(); conn.close()

    def iniciar_sesion(self, email, contrasena):
        if not (email and contrasena):
            print("No se puede iniciar sesión: campos incompletos.")
            return None

        conn = connect_to_mysql()
        cur = conn.cursor(dictionary=True)
        try:
            cur.execute("SELECT * FROM usuarios WHERE email=%s AND contrasena=%s", (email, contrasena))
            u = cur.fetchone()
        finally:
            cur.close(); conn.close()

        if u:
            print(f"Inicio de sesión exitoso. Bienvenido {u['nombre']} ({u['rol']}).")
            if u["rol"] == "Administrador":
                return Administrador(u["id"], u["nombre"], u["email"], u["contrasena"])
            else:
                return Estandar(u["id"], u["nombre"], u["email"], u["contrasena"])
        else:
            print("ERROR: Credenciales inválidas.")
            return None