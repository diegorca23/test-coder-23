class cliente():
    def __init__(self, nombre):
        self.nombre = nombre

    def obtener_nombre(self):
        return self.nombre
    
cliente1 = cliente("Rocio")

print(cliente1.obtener_nombre())

# ESTOY PONIENDO COSAS DEMÁS