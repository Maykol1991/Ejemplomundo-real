class Biblioteca:
    def _init_(self):
        self.libros_disponibles = {}  # Diccionario {ISBN: Libro}
        self.usuarios_registrados = set()  # Conjunto de IDs de usuario únicos
        self.prestamos_historial = {}  # Diccionario {ID_usuario: [Libros prestados]}

    def anadir_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)

    def dar_baja_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(usuario.id_usuario)

    def prestar_libro(self, isbn, usuario):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            usuario.prestar_libro(libro)
            self.prestamos_historial.setdefault(usuario.id_usuario, []).append(libro)

    def devolver_libro(self, isbn, usuario):
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.devolver_libro(libro)
                self.libros_disponibles[isbn] = libro
                self.prestamos_historial[usuario.id_usuario].remove(libro)

    def buscar_libro(self, criterio):
        resultados = [libro for libro in self.libros_disponibles.values() if criterio.lower() in libro.titulo_autor[0].lower() or criterio.lower() in libro.titulo_autor[1].lower() or criterio.lower() in libro.categoria.lower()]
        return resultados

    def listar_libros_prestados(self, usuario):
        return usuario.libros_prestados