


class ItemMenu:
    def __init__(self, nombre, precio, cantidad=1):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def calcular_subtotal(self):
        return self.precio * self.cantidad    
    
    
class Entrada(ItemMenu):
    def __init__(self, nombre, precio, cantidad=1):
        super().__init__(self, nombre, precio, cantidad)
        self.tipo = "Entrada"
            
class PlatoPrincipal(ItemMenu):
    def __init__(self, nombre, precio, cantidad=1):
        super().__init__(self, nombre, precio, cantidad)
        self.tipo = "Plato Principal"

class Postre(ItemMenu):
    def __init__(self, nombre, precio, cantidad=1):
        super().__init__(self, nombre, precio, cantidad)
        self.tipo = "Postre"
        
class Bebida(ItemMenu):
    def __init__(self, nombre, precio, cantidad=1):
        super().__init__(self, nombre, precio, cantidad)
        self.tipo = "Bebida"                          

class Menu:
    def __init__(self):
        self.entradas = []
        self.plato_principal = []
        self.postres = []
        self.bebidas = []
        