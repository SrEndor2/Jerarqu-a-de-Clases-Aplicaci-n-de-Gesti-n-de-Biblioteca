class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def mostrar_informacion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}"

class Revista(Libro):
    def __init__(self, titulo, autor, isbn, numero_edicion):
        super().__init__(titulo, autor, isbn)
        self.numero_edicion = numero_edicion

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Número de Edición: {self.numero_edicion}"

class Usuario:
    def __init__(self, nombre, tipo_usuario):
        self.nombre = nombre
        self.tipo_usuario = tipo_usuario

    def prestar(self, libro):
        if self.tipo_usuario == "Estudiante":
            return f"El estudiante {self.nombre} ha prestado el libro: {libro.mostrar_informacion()}"
        elif self.tipo_usuario == "Profesor":
            return f"El profesor {self.nombre} ha prestado el libro: {libro.mostrar_informacion()}"

    def devolver(self, libro):
        return f"{self.nombre} ha devuelto el libro: {libro.mostrar_informacion()}"

# Ejemplo
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-0307474728")
revista1 = Revista("National Geographic", "Varios Autores", "123-456789", "2023-10")

usuario1 = Usuario("Endor Cuevas", "Estudiante")
usuario2 = Usuario("Antonio Rios", "Profesor")

print(usuario1.prestar(libro1))
print(usuario2.prestar(revista1))
print(usuario1.devolver(libro1))