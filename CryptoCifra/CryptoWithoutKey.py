def CryptoWithoutKey(simple_number, message, open_key_A, open_key_B):
    p = simple_number

    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = extended_gcd(b % a, a)
            return gcd, (y - (b // a) * x), x

    def secret_key(key, p):
        gcd, x, y = extended_gcd(key, p - 1)
        return (x % (p-1))

    def dencryption(message, key, p):
        m = (message**key)%p
        return m


    if __name__ == '__main__':
        sa = secret_key(open_key_A, p)
        sb = secret_key(open_key_B, p)
        start = True
        while start:
            unit = input()
            if unit == '1':
                print(message)
            elif unit == '2':
                e = dencryption(message, open_key_A, p)
                print(e)
                e = dencryption(e, open_key_B, p)
                print(e)
                e = dencryption(e, sa, p)
                print(e)
            elif unit == '3':
                d = dencryption(e, sb, p)
                print(d)
            elif unit == '4':
                start = False
print(CryptoWithoutKey(31,11, 7, 17))