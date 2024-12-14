from .vehicle import Vehicle # Импорт класс Vehicle

class Airplane(Vehicle):
    def __init__(self, max_altitude):
        super().__init__(self, max_altitude)
        self.max_altitude = max_altitude #  максимальная высота полета (в метрах)

    def __str__(self):
        return super().__str__() + f"\nМаксимальная высота полета(в метрах): {self.max_altitude}"
    
    
