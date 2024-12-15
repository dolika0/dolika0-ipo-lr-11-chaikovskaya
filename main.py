from transport import Client, Vehicle, TransportCompany, Van, Airplane 

start = True
count = 0  # Счетчик для всех действий
all_clients = []
all_vehicles = []
all_company = []


def validation(prompt):
    while True:
        num = input(prompt)
        if num.isdigit():
            return int(num)
        else:
            print("Введите необходимую информацию числом!")


def menu():
    print()
    print(f" Меню ".center(70, "="))
    print("""
        1 - Создать клиента
        2 - Добавить транспорт
        3 - Вывести информацию о всех транспортах
        4 - Вывести информацию о всех клиентах
        5 - Вывести информацию о всех компаниях
        6 - Управление компаниями
        7 - Выход с программы\n""")
    print(f"".center(70, "="))    
    print()


def createCompany(name):
    company = TransportCompany(name)
    return company


def createClient(company):  # Создание клиента
    name = input("Введите имя клиента:")
    cargo_weight = validation("Введите вес груза клиента:")

    while True:
        vip = validation("Введите, имеет ли клиент VIP(1 - да, 2 - нет): ")
        if vip == 1 or vip == 2:
            is_vip = True if vip == 1 else False
            break
        else:
            print("Введите 1, если клиент имеет VIP. Если нет, введите 2.")

    company.add_client(Client(name, cargo_weight, is_vip))


def createTransport(company):  # Добавление транспорт
    while True:
        type_veh = validation("Выберите транспорт для добавления(1 - самолет, 2 - фургон): ")

        if type_veh == 1:
            capacity = validation("Введите грузоподъёмность самолёта: ")
            max_altitude = validation("Введите максимальную высоту полета: ")
            company.add_vehicle(Airplane(capacity, max_altitude))
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

            company.add_vehicle(Van(capacity, is_refrigerated))
            break

        else:
            print("Выберите 1, если хотите добавить самолет, 2 - если фургон.")


def printAllTransport(company):
    print("Все транспортные средства: ".center(70, "="))
    for vehicle in company.vehicles:
        print(vehicle)


def printAllClients(company):
    print("Все клиенты: ".center(70, "="))
    for client in company.clients:
        print(client)
    print()

def companyMenu():
    print(f"1 - Создать компанию")
    print(f"2 - Добавить транспортное средство в компанию")
    print(f"3 - Список всех транспортных средств компании")
    print(f"4 - Добавить клиента в компанию")
    print(f"5 - Распределить грузы клиентов по транспортным средствам")


def main():
    global start, count
    name = input("Введите название транспортной компании: ")
    company = createCompany(name)

    while start:
        menu()
        num = validation("Выберите необходимый пункт: ")

        if num == 1:  # Создание клиента
            createClient(company)
            count += 1

        elif num == 2:  # Добавление транспорт
            createTransport(company)
            count += 1

        elif num == 3:  # Вывод всех транспортных средств
            printAllTransport(company)
            count += 1

        elif num == 4:  # Вывод всех клиентов
            printAllClients(company)
            count += 1

        elif num == 5:  # Вывод всех компаний
            print(f"Название компании: {company.name}")
            count += 1

        elif num == 6: # Управление компаниями
            companyMenu()

        elif num == 7:  # Выход из программы
            start = False
            print("Выход из программы.")
            break


main()
