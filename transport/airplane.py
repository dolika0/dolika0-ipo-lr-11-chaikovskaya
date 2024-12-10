from vehicle import Vehicle # Импорт класс Vehicle

class Airplane(Vehicle):
    def __init__(self, max_altitude):

        if not isinstance(max_altitude, (int, float)) or max_altitude <= 0:
            raise ValueError("Максимальная амплитуда должна быть положительным числом.")

        self.max_altitude = max_altitude #  максимальная высота полета (в метрах)
    
    
