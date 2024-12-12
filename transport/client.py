class Client:
    def __init__(self, name, cargo_weight, is_vip = False):
        self.name = name # Имя клиента
        self.cargo_weight = cargo_weight # Вес груза
        self.is_vip = is_vip # флаг VIP-статуса
    
    def __str__(self): # Магический метод 
        return f'Client {self.name} (VIP: {self.is_vip}) with cargo_weight {self.cargo_weight}'
