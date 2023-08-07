import math
from util import string_to_ASCII
def secret_key(e, phi):
        """
        Возвращает обратный элемент e по модулю phi, используя расширенный алгоритм Евклида.
        """
        if math.gcd(e, phi) != 1:
            return None
        s, old_s = 0, 1
        t, old_t = 1, 0
        r, old_r = phi, e
        while r != 0:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t
        return old_s % phi

def dencryption(message, key, r):  # функция шифровки и расшифровки информации
    m = (message ** key) % r
    return m

def encrypt_word(plaintext, key, r):
    ciphertext = [(ord(char) ** key) % r for char in plaintext]
    return ciphertext

def decrypt_word(ciphertext, private_key, r):
    plaintext = [chr((char ** private_key) % r) for char in ciphertext]
    return ''.join(plaintext)


def RSA(simple_A_p1, simple_A_p2, simple_B_q1, simple_B_q2, open_key_A, open_key_B, message):
    ra = simple_A_p1 * simple_A_p2
    rb = simple_B_q1 * simple_B_q2
    fa = (simple_A_p1-1) * (simple_A_p2-1)
    fb = (simple_B_q1-1) * (simple_B_q2-1)
    sk_A = secret_key(open_key_A, fa)
    sk_B = secret_key(open_key_B, fb)
    e_B = dencryption(message, open_key_B, rb)
    d_B = dencryption(e_B, sk_B, rb)
    e_A = dencryption(message, open_key_A, ra)
    d_A = dencryption(e_A, sk_A, ra)

    return e_B, d_B, e_A, d_A
def RSA_word(simple_A_p1, simple_A_p2, simple_B_q1, simple_B_q2, open_key_A, open_key_B, message):
    ra = simple_A_p1 * simple_A_p2
    rb = simple_B_q1 * simple_B_q2
    fa = (simple_A_p1 - 1) * (simple_A_p2 - 1)
    fb = (simple_B_q1 - 1) * (simple_B_q2 - 1)
    sk_A = secret_key(open_key_A, fa)
    sk_B = secret_key(open_key_B, fb)
    print(sk_A, sk_B)
    e_B = encrypt_word(message, open_key_B, rb)
    d_B = decrypt_word(e_B, sk_B, rb)
    e_A = encrypt_word(message, open_key_A, ra)
    d_A = decrypt_word(e_A, sk_A, ra)

    return e_B, d_B, e_A, d_A

def RSA_Formula(p1, p2, q1, q2, open_key_A, open_key_B, message):

    outp = []
    outp.append(f'Зашифровка и расшифровка алгоритмом RSA для сообщения {message}<br>')
    ra = p1 * p2
    rb = q1 * q2
    fa = (p1 - 1) * (p2 - 1)
    fb = (q1 - 1) * (q2 - 1)
    outp.append(f'Находим модуль n для Алисы и Боба:<br>n = p1 * p2 = {p1} * {p2} = {ra} - для Алисы<br>n = q1 * q2 = {q1} * {q2} = {rb} - для Боба<br>')
    outp.append(f'Находим φ(n) для Алисы и Боба:<br>φ(n) = (p1 - 1) * (p2 - 1) = ({p1} - 1) * ({p2} - 1) = {fa} - для Алисы<br>φ(n) = (q1 - 1) * (q2 - 1) = ({q1} - 1) * ({q2} - 1) = {fb} - для Боба<br>')
    sk_A = secret_key(open_key_A, fa)
    sk_B = secret_key(open_key_B, fb)
    outp.append(f'Находим секретный ключ по обратному алгоритму Евклида: <br>Секретный ключ Алисы: {sk_A}<br>Секретный ключ Боба: {sk_B}<br>')
    e_B = dencryption(message, open_key_B, rb)
    d_B = dencryption(e_B, sk_B, rb)
    e_A = dencryption(message, open_key_A, ra)
    d_A = dencryption(e_A, sk_A, ra)
    outp.append(f'Проведём шифрование и расшифрование со стороны Алисы и Боба:<br>Передача сообщения от Алисы к Бобу:<br>Шифрование: e = message<sup>open_key_Bob</sup> (mod n), n - модуль Боба<br>e = {message}<sup>{open_key_B}</sup> (mod {rb}) = {e_B}<br>Расшифрование: d = e <sup>secret_key_Bob</sup> (mod n)<br>d = {e_B}<sup>{sk_B}</sup> (mod {rb}) = {d_B}<br>')
    outp.append(f'Передача сообщения от Боба к Алисе:<br>Шифрование: e = message<sup>open_key_Alice</sup> (mod n), n - модуль Алисы<br>e = {message}<sup>{open_key_A}</sup> (mod {ra}) = {e_A} <br>Расшифрование: d = e <sup>secret_key_Alice</sup> (mod n)<br>d = {e_A}<sup>{sk_A}</sup> (mod {ra}) = {d_A}<br>')
    res = "".join(outp)
    return res

def RSA_Formula_Word(p1, p2, q1, q2, open_key_A, open_key_B, message, index):

    outp = []
    outp.append(f'Зашифровка и расшифровка алгоритмом RSA для сообщения {message}<br>')
    ra = p1 * p2
    rb = q1 * q2
    fa = (p1 - 1) * (p2 - 1)
    fb = (q1 - 1) * (q2 - 1)
    outp.append(f'Находим модуль n для Алисы и Боба:<br>n = p1 * p2 = {p1} * {p2} = {ra} - для Алисы<br>n = q1 * q2 = {q1} * {q2} = {rb} - для Боба<br>')
    outp.append(f'Находим φ(n) для Алисы и Боба:<br>φ(n) = (p1 - 1) * (p2 - 1) = ({p1} - 1) * ({p2} - 1) = {fa} - для Алисы<br>φ(n) = (q1 - 1) * (q2 - 1) = ({q1} - 1) * ({q2} - 1) = {fb} - для Боба<br>')
    sk_A = secret_key(open_key_A, fa)
    sk_B = secret_key(open_key_B, fb)
    outp.append(f'Находим секретный ключ по обратному алгоритму Евклида: <br>Секретный ключ Алисы: {sk_A}<br>Секретный ключ Боба: {sk_B}<br>')
    e_B = encrypt_word(message, open_key_B, rb)
    d_B = decrypt_word(e_B, sk_B, rb)
    e_A = encrypt_word(message, open_key_A, ra)
    d_A = decrypt_word(e_A, sk_A, ra)
    print(e_B, d_B, e_A, d_A)
    if index == 1:
        outp.append(f'Получение сообщения от Алисы к Бобу:<br> Расшифрование: d = e <sup>secret_key_Bob</sup> (mod n)<br>d = {e_B}<sup>{sk_B}</sup> (mod {rb}) = {d_B}<br>')


    elif index == 3:
        outp.append(
            f'Получение сообщения от Боба к Алисе:<br>Расшифрование: d = e <sup>secret_key_Alice</sup> (mod n)<br>d = {e_A}<sup>{sk_A}</sup> (mod {ra}) = {d_A}<br>')

    elif index == 0 or 2:
        outp.append(
            f'Проведём шифрование и расшифрование со стороны Алисы и Боба:<br>Передача сообщения от Алисы к Бобу:<br>Шифрование: e = message<sup>open_key_Bob</sup> (mod n), n - модуль Боба<br>Переведём наше сообщение в ASCII: {message} = {string_to_ASCII(message)}<br>e = {string_to_ASCII(message)}<sup>{open_key_B}</sup> (mod {rb}) = {e_B}<br>Расшифрование: d = e <sup>secret_key_Bob</sup> (mod n)<br>d = {e_B}<sup>{sk_B}</sup> (mod {rb}) = {d_B}<br>')
        outp.append(
            f'Передача сообщения от Боба к Алисе:<br>Шифрование: e = message<sup>open_key_Alice</sup> (mod n), n - модуль Алисы<br>e = {string_to_ASCII(message)}<sup>{open_key_A}</sup> (mod {ra}) = {e_A} <br>Расшифрование: d = e <sup>secret_key_Alice</sup> (mod n)<br>d = {e_A}<sup>{sk_A}</sup> (mod {ra}) = {d_A}<br>')

    res = "".join(outp)
    return res



