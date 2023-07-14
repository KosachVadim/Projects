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

def dencryption_B(message,open_key_A, open_key_B, sk_A, sk_B, r, R):  # функция шифровки и расшифровки информации
    if r < R:
        e_B0 = message ** sk_B % r
        e_B = e_B0 ** open_key_A % R
        d_A0 = e_B ** sk_A % R
        d_A = d_A0 ** open_key_B % r
        return e_B0, e_B, d_A0, d_A
    elif r > R:
        e_B0 = message ** open_key_A % R
        e_B = e_B0 ** sk_B % r
        d_A0 = e_B ** open_key_B % r
        d_A = d_A0 ** sk_A % R
        return e_B0, e_B, d_A0, d_A

def dencryption_A(message,open_key_A, open_key_B, sk_A, sk_B, r, R):  # функция шифровки и расшифровки информации
    if r > R:
        e_A0 = message ** sk_A % R
        e_A = e_A0 ** open_key_B % r
        d_B0 = e_A ** sk_B % r
        d_B = d_B0 ** open_key_A % R
        return e_A0, e_A, d_B0, d_B
    elif r < R:
        e_A0 = message ** open_key_B % r
        e_A = e_A0 ** sk_A % R
        d_B0 = e_A ** open_key_A % R
        d_B = d_B0 ** sk_B % r
        return e_A0, e_A, d_B0, d_B

def dencryption_B_word(message, open_key_A, open_key_B, sk_A, sk_B, r, R):
    encrypted = []  # Список для хранения зашифрованных значений
    decrypted = []
    m1 = []
    m3 = []
    if r < R:
        for char in message:
            m = ord(char)  # Преобразование символа в числовое значение
            e_B0 = m ** sk_B % r
            m1.append(e_B0)
            e_B = e_B0 ** open_key_A % R
            encrypted.append(e_B)
            d_A0 = e_B ** sk_A % R
            m3.append(d_A0)
            d_A = d_A0 ** open_key_B % r
            decrypted.append(chr(d_A))

        return encrypted, "".join(decrypted), m1, m3

    elif r > R:
        for char in message:
            m = ord(char)  # Преобразование символа в числовое значение
            e_B0 = m ** open_key_A % R
            m1.append(e_B0)
            e_B = e_B0 ** sk_B % r
            encrypted.append(e_B)
            d_A0 = e_B ** open_key_B % r
            m3.append(d_A0)
            d_A = d_A0 ** sk_A % R
            decrypted.append(chr(d_A))

        return encrypted, "".join(decrypted), m1, m3

def dencryption_A_word(message,open_key_A, open_key_B, sk_A, sk_B, r, R):  # функция шифровки и расшифровки информации
    encrypted = []  # Список для хранения зашифрованных значений
    decrypted = []
    if r > R:
        for char in message:
            m = ord(char)
            e_A0 = m ** sk_A % R
            e_A = e_A0 ** open_key_B % r
            encrypted.append(e_A)
            d_B0 = e_A ** sk_B % r
            d_B = d_B0 ** open_key_A % R
            decrypted.append(chr(d_B))
        return encrypted, "".join(decrypted)
    elif r < R:
        for char in message:
            m = ord(char)
            e_A0 = m ** open_key_B % r
            e_A = e_A0 ** sk_A % R
            encrypted.append(e_A)
            d_B0 = e_A ** open_key_A % R
            d_B = d_B0 ** sk_B % r
            decrypted.append(chr(d_B))
        return encrypted, "".join(decrypted)

def EDS(simple_A_p1, simple_A_p2, simple_B_q1, simple_B_q2, open_key_A, open_key_B, message, index):
    fRa = (simple_A_p1-1) * (simple_A_p2-1)
    frb = (simple_B_q1-1) * (simple_B_q2-1)
    R = simple_A_p1 * simple_A_p2
    r = simple_B_q1 * simple_B_q2
    sk_A = secret_key(open_key_A, fRa)
    sk_B = secret_key(open_key_B, frb)
    if index == 0 or index ==  1:
        e_A0, e_A, d_B0, d_B = dencryption_A(message, open_key_A, open_key_B, sk_A, sk_B, r, R)
        print(e_A0, e_A, d_B0, d_B)
        return e_A0, e_A, d_B0, d_B
    elif index == 2 or index == 3:
        e_B0, e_B, d_A0, d_A = dencryption_B(message, open_key_A, open_key_B, sk_A, sk_B, r, R)
        print(e_B0, e_B, d_A0, d_A)
        return e_B0, e_B, d_A0, d_A

def EDS_WORD(simple_A_p1, simple_A_p2, simple_B_q1, simple_B_q2, open_key_A, open_key_B, message, index):
    fRa = (simple_A_p1 - 1) * (simple_A_p2 - 1)
    frb = (simple_B_q1 - 1) * (simple_B_q2 - 1)
    R = simple_A_p1 * simple_A_p2
    r = simple_B_q1 * simple_B_q2
    sk_A = secret_key(open_key_A, fRa)
    sk_B = secret_key(open_key_B, frb)
    if index == 0 or index == 1:
        e_A, d_B = dencryption_A_word(message, open_key_A, open_key_B, sk_A, sk_B, r, R)
        print(e_A, d_B)
        return e_A, d_B
    elif index == 2 or index == 3:
        e_B, d_A, m1, m3 = dencryption_B_word(message, open_key_A, open_key_B, sk_A, sk_B, r, R)
        print( e_B, d_A)
        return e_B, d_A


def EDS_Formula(p1, p2, q1, q2, open_key_A, open_key_B, message):

    outp = []
    outp.append(f'Зашифровка и расшифровка ЭЦП алгоритмом RSA  для сообщения {message}<br>')
    R = p1 * p2
    r = q1 * q2
    fa = (p1 - 1) * (p2 - 1)
    fb = (q1 - 1) * (q2 - 1)
    outp.append(f'Находим модуль n для Алисы и Боба:<br>n = p1 * p2 = {p1} * {p2} = {r} - для Алисы<br>n = q1 * q2 = {q1} * {q2} = {R} - для Боба<br>')
    outp.append(f'Находим φ(n) для Алисы и Боба:<br>φ(n) = (p1 - 1) * (p2 - 1) = ({p1} - 1) * ({p2} - 1) = {fa} - для Алисы<br>φ(n) = (q1 - 1) * (q2 - 1) = ({q1} - 1) * ({q2} - 1) = {fb} - для Боба<br>')
    sk_A = secret_key(open_key_A, fa)
    sk_B = secret_key(open_key_B, fb)
    outp.append(f'Находим секретный ключ по обратному алгоритму Евклида: <br>Секретный ключ Алисы: {sk_A}<br>Секретный ключ Боба: {sk_B}<br>')
    e_B0, e_B, d_A0, d_A = dencryption_B(message, open_key_A, open_key_B, sk_A, sk_B, r, R)
    outp.append(f'Проведём шифрование и расшифрование: Если r &lt; R<br>Шифрование:<br>  m1 = message<sup>sk_B</sup> (mod r), r - модуль Боба<br>m1 = {message}<sup>{sk_B}</sup> (mod {r}) = {e_B0}<br>m2 = {e_B0}<sup>{open_key_A}</sup> (mod {R}) = {e_B}<br>Расшифрование:<br>m3 = {e_B}<sup>{sk_A}</sup> (mod {R}) = {d_A0}<br>m4 = {d_A0}<sup> {open_key_B}</sup> (mod {r}) = {d_A}<br>')
    outp.append(
        f'Шифрование: Если r > R<br>m1 = message<sup>open_key_A</sup> (mod R), R - модуль Алисы<br>m1 = {message}<sup>{open_key_A}</sup> (mod {R}) = {e_B0}<br>m2 = {e_B0}<sup>{sk_B}</sup> (mod {r}) = {e_B}<br>Расшифрование:<br>m3 = {e_B}<sup>{open_key_B}</sup> (mod {r}) = {d_A0}<br>m4 = {d_A0}<sup> {sk_A}</sup> (mod {R}) = {d_A}<br>')
    res = "".join(outp)
    return res

def EDS_Formula_Word(p1, p2, q1, q2, open_key_A, open_key_B, message):
    outp = []
    outp.append(f'Зашифровка и расшифровка ЭЦП алгоритмом RSA  для сообщения {message}<br>')
    R = p1 * p2
    r = q1 * q2
    fa = (p1 - 1) * (p2 - 1)
    fb = (q1 - 1) * (q2 - 1)
    outp.append(
        f'Находим модуль n для Алисы и Боба:<br>n = p1 * p2 = {p1} * {p2} = {r} - для Алисы<br>n = q1 * q2 = {q1} * {q2} = {R} - для Боба<br>')
    outp.append(
        f'Находим φ(n) для Алисы и Боба:<br>φ(n) = (p1 - 1) * (p2 - 1) = ({p1} - 1) * ({p2} - 1) = {fa} - для Алисы<br>φ(n) = (q1 - 1) * (q2 - 1) = ({q1} - 1) * ({q2} - 1) = {fb} - для Боба<br>')
    sk_A = secret_key(open_key_A, fa)
    sk_B = secret_key(open_key_B, fb)
    message1 = string_to_ASCII(message)
    outp.append(
        f'Находим секретный ключ по обратному алгоритму Евклида: <br>Секретный ключ Алисы: {sk_A}<br>Секретный ключ Боба: {sk_B}<br>')

    e_B, d_B, m1, m3 = dencryption_B_word(message, open_key_A, open_key_B, sk_A, sk_B, r, R)
    print(e_B, d_B, m1, m3)
    outp.append(
        f'Проведём шифрование и расшифрование: Переведём наше сообщение в аски: {message} = {message1}<br>Если r &lt; R<br>Шифрование:<br>  m1 = message<sup>sk_B</sup> (mod r), r - модуль Боба<br>m1 = {message1}<sup>{sk_B}</sup> (mod {r}) = {m1}<br>m2 = {m1}<sup>{open_key_A}</sup> (mod {R}) = {e_B}<br>Расшифрование:<br>m3 = {e_B}<sup>{sk_A}</sup> (mod {R}) = {m3}<br>m4 = {m3}<sup> {open_key_B}</sup> (mod {r}) = {d_B}<br>')
    outp.append(
        f'Шифрование: Если r > R<br>m1 = message<sup>open_key_A</sup> (mod R), R - модуль Алисы<br>m1 = {message1}<sup>{open_key_A}</sup> (mod {R}) = {m1}<br>m2 = {m1}<sup>{sk_B}</sup> (mod {r}) = {e_B}<br>Расшифрование:<br>m3 = {e_B}<sup>{open_key_B}</sup> (mod {r}) = {m3}<br>m4 = {m3}<sup> {sk_A}</sup> (mod {R}) = {d_B}<br>')

    res = "".join(outp)
    return res
