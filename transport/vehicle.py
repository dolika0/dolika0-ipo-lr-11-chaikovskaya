
from transport.client import Client
import random 

def validation(prompt):
    while(True):
        num = input(prompt)
        if num.isdigit():
            return int(num)
        else: 
            return "Введите необходимую информацию числом!"


class Vehicle:
    def __init__(self, capacity = 0, current_load = 0):
        self.vehicle_id = random.randint(100, 10000)
        self.capacity = validation("Введите грузоподъёмность транспорта (числом): ") # Грузоподъёмность
        self.current_load = validation("Введите текущую загрузку(числом): ") # Текущая загрузка
        self.clients_list = []

    def load_cargo(self, client):
        try:
            new_weight = self.current_load + client.cargo_weight
        except AttributeError:
            raise AttributeError("Вы должны передать клиента в параметр функции!")
        if new_weight > self.capacity:
            print("Грузоподъемность превышена! Действие отменено!")
        else:
            self.current_load = new_weight
            self.clients_list.append(client)
            
    def __str__(self):
        return f"ID транспорта: {self.vehicle_id}, грузоподъёмность в тоннах: {self.capacity}, текущая загрузка: {self.current_load}"
    
