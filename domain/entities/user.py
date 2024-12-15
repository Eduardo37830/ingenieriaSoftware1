class User:
    def __init__(self, id: int, nombre: str, correo: str, contrasena: str, rol: str):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol

    def __repr__(self):
        return f"User(id={self.id}, nombre={self.nombre}, correo={self.correo}, rol={self.rol})"