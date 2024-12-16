from transport import Client, Vehicle, TransportCompany, Van, Airplane 

start = True
count = 0  # Счетчик для всех действий
all_clients = []
all_vehicles = []
company_list = []
id = 0 # Номер клиента

def validation(prompt): # готово
    while True:
        num = input(prompt)
        if num.isdigit():
            return int(num)
        else:
            print("Введите необходимую информацию числом!")


def menu(): # готово
    print()
    print(f" Меню ".center(70, "="))
    print("""
        1 - Создать клиента
        2 - Добавить транспорт
        3 - Вывести список клиентов
        4 - Вывести информацию о всех транспортах
        5 - Оптимизировать распределение груза
        6 - Выход с программы\n""")
    
    print(f"".center(70, "="))    
    print()

 
def createCompany(name): # вроде готво
    company = TransportCompany(name)
    return company


def createClient():  # Создание клиента # готово
    name = input("Введите имя клиента:")
    cargo_weight = validation("Введите вес груза клиента:")

    while True:
        vip = validation("Введите, имеет ли клиент VIP(1 - да, 2 - нет): ")
        if vip == 1 or vip == 2:
            is_vip = True if vip == 1 else False
            break
        else:
            print("Введите 1, если клиент имеет VIP. Если нет, введите 2.")

    all_clients.append(Client(name, cargo_weight, is_vip))
    print("Клиент успешно создан!")


def createTransport():  # Добавление транспорт # готово
    while True:
        global type_veh
        type_veh = validation("\nВыберите транспорт для добавления(1 - самолет, 2 - фургон): ")

        if type_veh == 1:
            capacity = validation("Введите грузоподъёмность самолёта: ")
            max_altitude = validation("Введите максимальную высоту полета: ")
            all_vehicles.append(Airplane(capacity, max_altitude))
            print("Самолёт успешно создан!")
            break

        elif type_veh == 2:
            capacity = validation("Введите грузоподъёмность фургона: ")
            while True:
                is_refrigerated = validation("Введите, имеет ли клиент холодильник (1 - да, 2 - нет): ")
                if is_refrigerated == 1 or is_refrigerated == 2:
                    is_refrigerated = True if is_refrigerated == 1 else False
                    break
                else:
                    print("Введите 1, если есть холодильник, 2 если нет.")
            all_vehicles.append(Van(capacity, is_refrigerated))
            print("Фургон успешно создан!")
            break

        else:
            print("Выберите 1, если хотите добавить самолет, 2 - если фургон.")


def printAllTransport(): # готово
    idVeh = 0 # Номер транспорта
    global typeVeh
    print()
    print("Все транспортные средства: ".center(70, "="))
    print()
    for vehicle in all_vehicles:
        idVeh += 1
        global type_veh
        if type_veh == 1:
            typeVeh = "самолёт" 
        else:
            typeVeh = "фургон" 
        print(f"{idVeh}) {vehicle}")
    print()


def printAllClients(): # готово
    global id
    print()
    print("Все клиенты: ".center(70, "="))
    print()
    for client in all_clients:
        id += 1
        vip = "Есть" if client.is_vip == True else "Нет"
        print(f"{id}. Имя: {client.name}. Вес груза: {client.cargo_weight}. VIP-статус: {vip} ")
    print()
    

def main():
    global start, count
    name = input("Введите название транспортной компании: ")
    company = createCompany(name)

    while start:

        menu()
        num = validation("Выберите необходимый пункт: ")

        if num == 1:  # Создание клиента
            createClient()
            count += 1

        elif num == 2:  # Добавление транспорт
            createTransport()
            count += 1


        elif num == 3:  # Вывод всех клиентов
            printAllClients()
            count += 1


        elif num == 4:  # Вывод всех транспортных средств
            printAllTransport()
            count += 1


        elif num == 4:  # Вывод всех транспортных средств
            optimize_cargo_distribution()#################################################
            count += 1


        elif num == 6: # Управление компаниями
            start = False
            print(f"Выход из программы. Количество проведедённых операций : {count}.")
            break        
        
        else:
            print("Выберите один из предложенных пунктов!!!")

main()
