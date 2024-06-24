class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, id_usuario, isbn):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        libro = next((l for l in self.libros if l.isbn == isbn), None)
        if usuario and libro:
            return usuario.tomar_prestado(libro)
        return False

    def devolver_libro(self, id_usuario, isbn):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        libro = next((l for l in self.libros if l.isbn == isbn), None)
        if usuario and libro:
            return usuario.devolver_libro(libro)
        return False
