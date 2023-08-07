from string import ascii_letters

RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
RUS_UPPER = RUS.upper()


# Функция для проверки правильного имени банка
def verify_bank_name(name):
    if type(name) != str:
        raise TypeError("Название должно быть строкой")
    if len(name) < 1:
        raise TypeError("В названии должен быть хотя бы один символ")
    letters = ascii_letters + RUS + RUS_UPPER
    if len(name.strip(letters)) != 0:
        raise TypeError("В названии можно использовать только буквенные символы и дефис")


# Функция для проверки правильного имени
def verify_name(name):
    f = name.split()

    if type(name) != str:
        raise TypeError("Название должно быть строкой")

    if len(f) != 3:
        raise TypeError("Неверный формат ФИО")

    letters = ascii_letters + RUS + RUS_UPPER

    for s in f:
        if len(s) < 1:
            raise TypeError("В ФИО должен быть хотя бы один символ")
        if len(s.strip(letters)) != 0:
            raise TypeError("В названии можно использовать только буквенные символы и дефис")


# Функция для проверки в базе данных, есть ли там
def is_in_database(table_class, session, name):
    return session.query(table_class).filter_by(name=name).first() is not None


# Функция для проверки правильного написания типа счёта
def verify_type_account(type_account):
    lib_ac = ["сберегательный", "текущий", "расчётный", "кредитный"]
    if not type_account in lib_ac:
        raise TypeError("Такого счёта не существует в базе")


