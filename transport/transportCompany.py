from .vehicle import Vehicle # Импорт класс Vehicle
from .airplane import Airplane
from .van import Van
from .client import Client

class TransportCompany:
    def __init__(self, name):
        self.name = name
        self.vehicles = [] # список транспортных средств
        self.clients = [] # список клиентов

    def add_vehicle(self, vehicle): # добавляет транспортное средство
        if not isinstance(vehicle, Vehicle): # — это условие, которое проверяет, является ли объект vehicle экземпляром класса Vehicle
            raise ValueError("vehicle должен быть объектом класса Vehicle")
        self.vehicles.append(vehicle)

    def list_vehicles(self): # возвращает список всех транспортных средств
        vehicles_list = []
        for vehicle in self.vehicles:
            vehicles_list.append(str(vehicle))
        return vehicles_list 


    def add_client(self, client): # добавляет клиента
        if not isinstance(client, Client):
            raise ValueError("client должен быть объектом класса Client")
        self.clients.append(client)

    def optimize_cargo_distribution(self): # распределяет грузы клиентов по транспортным средствам
        vip_clients = [client for client in self.clients if client.is_vip] # создает новый список, состоящий из клиентов, у которых атрибут is_vip равен True
        other_clients = [client for client in self.clients if not client.is_vip] # создает новый список, состоящий из клиентов, у которых атрибут is_vip равен False
        all_clients = vip_clients + other_clients

        for client in all_clients:
            for vehicle in self.vehicles: # цикл проходит по каждому транспортному средству в списке self.vehicles
                if vehicle.current_load + client.cargo_weight <= vehicle.capacity: # тек.загрузка + вес груза клиента <= грузоподьемность транспорта
                    vehicle.load_cargo(client) # загружает груз клиента в транспортное средство и обновляет текущую загрузку
                    break


