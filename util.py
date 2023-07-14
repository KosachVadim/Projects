import random as r
import math
import pyzipper

def is_prime(n):
    """
    Возвращает True, если число n является простым, и False в противном случае.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_prime_number():
    # Генерируем случайное число
    num1 = r.randint(3, 32)
    num2 = r.randint(3, 32)
    while num1 == num2 or not is_prime(num1) or not is_prime(num2):
        num1 = r.randint(3, 32)
        num2 = r.randint(3, 32)
    return num1, num2

def get_prime_number_forword():
    # Генерируем случайное число
    num1 = r.randint(12, 32)
    num2 = r.randint(12, 32)
    while num1 == num2 or not is_prime(num1) or not is_prime(num2):
        num1 = r.randint(12, 32)
        num2 = r.randint(12, 32)
    return num1, num2


def open_keya(p1, p2):
    fr = (p1 - 1) * (p2 - 1)
    a = int(r.choice([x for x in range(2, 32) if math.gcd(x, fr) == 1]))
    while a > fr:
        a = int(r.choice([x for x in range(2, 32) if math.gcd(x, fr) == 1]))
    return (a)

def open_keyb(q1, q2, a):
    fr = (q1 - 1) * (q2 - 1)
    b = int(r.choice([x for x in range(2, 32) if math.gcd(x, fr) == 1]))
    while b == a or b > fr:
        b = int(r.choice([x for x in range(2, 32) if math.gcd(x, fr) == 1]))
    return (b)


def message_RSA(p1, p2):
    # функция для нашего сообщения
    rm = (p1 - 1) * (p2 - 1)
    return (r.randint(3, rm))

def message_RSA_text():
    with pyzipper.AESZipFile('message_text_RSA.zip') as zip_file:
        zip_file.pwd = b'proParol123'

        # извлекаем файлы из архива
        zip_file.extractall()

    # читаем содержимое текстового документа
    with open('message_text_RSA.txt', 'r') as file:
        content = file.read().split(" ")
    return r.choice(content)

def message_EDS(q1, q2, p1, p2):
    rm = q1 * q2
    Rm = p1 * p2
    m = r.randint(3,rm)
    while m > Rm:
        m = r.randint(3, rm)
    return m

def read_text(filename):
    f = open(filename, 'r', encoding='utf-8')
    ot = f.read()
    f.close()
    return ot


def name_choise():
    task_list = ["Зашифровать сообщение для Боба", "Расшифровать сообщение для Боба", "Зашифровать сообщение для Алисы", "Расшифровать сообщение для Алисы"]
    random_task = r.choice(task_list)
    index_name = task_list.index(random_task)
    return random_task, index_name

def numbers_to_string(numbers):
    return ' '.join(str(num) for num in numbers)

def string_to_ASCII(message):
    ascii_codes = [ord(c) for c in message]
    return ascii_codes