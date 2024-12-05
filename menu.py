


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
        self.plato_principales = []
        self.postres = []
        self.bebidas = []
    
    def agregarEntrada(self, nombre, precio):
        entrada = Entrada(nombre, precio)
        self.entradas.append(entrada)
        return entrada    
    
    def agregar_plato_principal(self, nombre, precio):
        plato = PlatoPrincipal(nombre, precio)
        self.plato_principales.append(plato)
        return plato   
    
    def agregar_postre(self, nombre, precio):
        postre = Postre(nombre, precio)
        self.postres.append(postre)
        return postre 
    
    def agregar_bebida(self, nombre, precio):
        bebida = Bebida(nombre, precio)
        self.bebidas.append(bebida)
        return bebida
    
    def eliminar_item(self, tipo, nombre):
        if tipo == "Entradas":
            items = self.entradas
        if tipo == "Plato Principal":
            items = self.plato_principales
        if tipo == "Postres":
            items = self.postres
        if tipo == "Bebidas":
            items = self.bebidas
        else:
            return False
        
        for item in items [:]:
            if item.nombre == nombre:
               items.remove(item)
               return True
        return False    
            
                        