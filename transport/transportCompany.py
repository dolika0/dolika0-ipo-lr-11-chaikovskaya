from .vehicle import Vehicle
from .client import Client
from .airplane import Airplane
from .van import Van
from typing import List

class TransportCompany():
    # Инициализирует объект транспортной компании с именем name и пустыми списками для транспортных средств и клиентов
    def __init__(self, name):
        self.name = name
        self.vehicles : List[Vehicle] = []
        self.clients : List[Client] = []

    def list_vehicles(self):
        return self.vehicles
    
    def add_client(self, client):
        if not isinstance(client, Client):
            raise TypeError("Клиент должен быть экземпляром.")
        self.clients.append(client)

    def add_vehicle(self, vehicle):
        
