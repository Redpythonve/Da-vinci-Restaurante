from menu import Menu
class Restaurante:
    def __init__(self):
        self.mesas = []
        self.clientes = []
        self.pedidos_activos = []
        self.menus = Menu()