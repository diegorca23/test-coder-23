class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print(f"El alumno {self.nombre} tiene una nota de: {self.nota}")
