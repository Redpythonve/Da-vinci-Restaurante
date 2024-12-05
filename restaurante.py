from menu import Menu
from mesa import Mesa

class Restaurante:
    
    def __init__(self):
        self.mesas = []
        self.clientes = []
        self.pedidos_activos = []
        self.menu = Menu()
        self._inicializar_menu()
        
    def _inicializar_menu(self):
        self.menu.agregar_entrada(nombre: "Ensalada Cesar", precio: 8.56) # type: ignore
        self.menu.agregar_entrada(nombre: "Pollo", precio: 5.60) # type: ignore
        
        self.menu.agregar_plato_principal(nombre: "spaguettis", precio: 4.56) # type: ignore
        self.menu.agregar_plato_principal(nombre: "Pollo", precio: 5.60)  # type: ignore
        
        self.menu.agregar_postre(nombre: "Helado de Chocolate", precio: 1.50) # type: ignore
        self.menu.agregar_postre(nombre: "Helado de Fresa", precio: 1.50) # type: ignore
        
        self.menu.agregar_bebida(nombre: "pepsi", precio: 1.20) # type: ignore
        self.menu.agregar_bebida(nombre: "limonada", precio: 1.20) # type: ignore
        
    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)
        return(f"Mesa {mesa.numero} (capacidad:{mesa.tamaño}) agregada exitosamente" )