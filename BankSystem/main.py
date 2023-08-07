from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Bank, Client, Account, Manager
from utils import verify_name, verify_bank_name, is_in_database, verify_type_account


engine = create_engine('sqlite:///bank.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


# Класс для реализации функций банка
class BankFunctions:
    # В инициализации мы создаём и добавляем банк в бд, если такого банка ещё нет
    def __init__(self, bank_name):
        self.__session = Session()
        verify_bank_name(bank_name)
        self.__bank_name = bank_name
        if not is_in_database(Bank, self.__session, self.__bank_name):
            bank = Bank(name=self.__bank_name)
            self.__session.add(bank)
            self.__session.commit()
            print(f"Ваш банк {self.__bank_name} успешно создан!")

    # В функции банк проверяет всех клиентов и их счета
    def get_clients(self):
        self.__bank_id = self.__session.query(Bank).filter_by(name=self.__bank_name).first().id
        clients = self.__session.query(Client).filter_by(bank_id=self.__bank_id).all()
        for client in clients:
            if not client.accounts:  # Проверяем, есть ли у клиента счета
                print(f"ID:{client.id}. Имя клиента: {client.name}\nУ клиента нет счетов.\n")
            else:
                print(f"ID:{client.id}. Имя клиента: {client.name}")
                for account in client.accounts:  # Проходимся по всем счетам клиента
                    print(f"ID:{account.id}. Тип счёта: {account.type_account}. Баланс: {account.balance}")
                print()

    # В функции банк проверяет всех менеджеров
    def get_managers(self):
        self.__bank_id = self.__session.query(Bank).filter_by(name=self.__bank_name).first().id
        managers = self.__session.query(Manager).filter_by(bank_id=self.__bank_id).all()
        for manager in managers:
            print(f"ID:{manager.id}. Имя менеджера: {manager.name}\n")


# Класс для реализации функций менеджера
class ManagerFunctions:
    # В инициализации мы создаём и добавляем менеджера в бд, если такого ещё нет
    def __init__(self, manager_name, bank_name):
        self.__session = Session()
        verify_name(manager_name)
        self.__manager_name = manager_name
        self.__bank_name = bank_name
        bank = self.__session.query(Bank).filter_by(name=self.__bank_name).first()
        if not is_in_database(Manager, self.__session, self.__manager_name):
            manager = Manager(name=self.__manager_name, bank_id=bank.id)
            self.__session.add(manager)
            self.__session.commit()
            print(f"Менеджер, {self.__manager_name}, успешно добавлен!")

    # Функция нужно только для получения id клиента по его имени
    def __get_client_id(self, client_name):
        client = self.__session.query(Client).filter_by(name=client_name).first()
        if id:
            return client.id
        return None

    # Функция для создания счёта клиенту
    def create_account(self, client_name):
        if is_in_database(Client, self.__session, client_name):
            type_account = str(input("Введите тип счёта: \n"))
            verify_type_account(type_account)
            client_id = self.__get_client_id(client_name)
            account = Account(client_id=client_id, type_account=type_account)
            self.__session.add(account)
            self.__session.commit()
            print(f"Ваш счёт был успешно создан!\n")
        else: print("Такого человека нет в базе данных!\n")

    # В функции менеджер проверяет всех клиентов и их счета
    def get_clients(self):
        self.__bank_id = self.__session.query(Bank).filter_by(name=self.__bank_name).first().id
        clients = self.__session.query(Client).filter_by(bank_id=self.__bank_id).all()
        for client in clients:
            if not client.accounts:  # Проверяем, есть ли у клиента счета
                print(f"ID:{client.id}. Имя клиента: {client.name}\nУ клиента нет счетов.\n")
            else:
                print(f"ID:{client.id}. Имя клиента: {client.name}")
                for account in client.accounts:  # Проходимся по всем счетам клиента
                    print(f"ID:{account.id}. Тип счёта: {account.type_account}. Баланс: {account.balance}")
                print()


# Класс для реализации функций клиента
class ClientFunctions:
    # В инициализации мы создаём и добавляем клиента в бд, если такого ещё нет
    def __init__(self, client_name, bank_name):
        self.__session = Session()
        verify_name(client_name)
        self.__client_name = client_name
        self.__bank_name = bank_name
        bank = self.__session.query(Bank).filter_by(name=self.__bank_name).first()
        if not is_in_database(Client, self.__session, self.__client_name):
            client = Client(name=self.__client_name, bank_id=bank.id)
            self.__session.add(client)
            self.__session.commit()
            print(f"Клиент {self.__client_name} успешно добавлен!")

    # Функция для просмотра счетов у клиента и их id
    def get_accounts(self, client_name):
        if is_in_database(Client, self.__session, client_name):
            client = self.__session.query(Client).filter_by(name=client_name).first()
            if not client.accounts:
                print(f"ID:{client.id}. Имя клиента: {client.name}\nУ клиента нет счетов.\n")
            else:
                for account in client.accounts:
                    print(f"ID:{account.id}. Тип счёта: {account.type_account}. Баланс: {account.balance}")
                print()

    # В функции определённый клиент узнаёт свой баланс по определённому id его счёта
    def get_balance(self, client_name, id_account):
        if is_in_database(Client, self.__session, client_name):
            account = self.__session.get(Account, id_account)
            if account:
                if client_name == account.client.name:
                    return f"Ваш баланс: {account.balance}\n"
                else:
                    raise "Данный счёт не связан с пользователем\n"
            else:
                return "Счёт с таким id не найден\n"
        else:
            return "Такого человека нет в базе данных!\n"

    # В функции определённый клиент пополняет свой баланс по определённому id его счёта
    def deposit(self, client_name, id_account, amount):
        if is_in_database(Client, self.__session, client_name):
            account = self.__session.get(Account, id_account)
            if account:
                if client_name == account.client.name:
                    account.balance += amount
                    self.__session.commit()
                    return f"Ваш баланс был успешно пополнен!\n"
                else:
                    raise "Данный счёт не связан с пользователем\n"
            else:
                return "Счёт с таким id не найден\n"
        else:
            return "Такого человека нет в базе данных!\n"

    # В функции определённый клиент снимает деньги со своего счёта по определённому id счёта
    def withdraw(self, client_name, id_account, amount):
        if is_in_database(Client, self.__session, client_name):
            account = self.__session.get(Account, id_account)
            if account:
                if client_name == account.client.name:
                    if account.balance >= amount:
                        account.balance -= amount
                        self.__session.commit()
                        return "Снятие средств успешно проведено!\n"
                    else:
                        return "Недостаточно средств!\n"
                else:
                    raise "Данный счёт не связан с пользователем\n"
            else:
                return "Счёт с таким id не найден\n"
        else:
            return "Такого человека нет в базе данных!\n"

# Реализации функций
def main():

    # Создадим банк
    bank = BankFunctions("Банк")

    # Создаём клиентов и менеджеров
    client1 = ClientFunctions("Корин Антон Павлович", "Банк")
    client2 = ClientFunctions("Дорова Екатерина Петровна", "Банк")
    manager1 = ManagerFunctions("Рюрик Георгий Сергеевич", "Банк")
    manager2 = ManagerFunctions("Ляпин Дмитрий Анатольевич", "Банк")



    help_list = """ 
0. Проверить доступные счета (счета, которые существует в данном примере)    
1. Создать счёт для клиента
2. Проверить счета (узнать ID счёта)
3. Проверить баланс
4. Пополнить баланс
5. Снять деньги 
6. Банк проверяет клиентов
7. Банк проверяет менеджеров
8. Менеджер проверяет клиентов
9. Выход
    """


    while True:
        print(help_list)
        command = int(input("Введите цифру нужной вам операции (или 9 для выхода): \n"))
        if command == 9:
            break
        match command:

            case 0:

                print("сберегательный\nтекущий\nрасчётный\nкредитный")

            case 1:

                manager1.create_account(str(input("Введите имя клиента для создания нового счёта: ")))

            case 2:

                client1.get_accounts(str(input("Введите имя клиента для просмотра счёта: ")))

            case 3:

                print(client1.get_balance(str(input("Введите имя клиента: ")), str(input("Введите номер id счёта: "))))

            case 4:

                print(client1.deposit(str(input("Введите имя клиента: ")), str(input("Введите номер id счёта: ")), float(input("Введите сумму: "))))

            case 5:

                print(client1.withdraw(str(input("Введите имя клиента: ")), str(input("Введите номер id счёта: ")), float(input("Введите сумму: "))))

            case 6:

                bank.get_clients()

            case 7:

                bank.get_managers()

            case 8:
                manager1.get_clients()


# Пример использования:
if __name__ == '__main__':
    main()









