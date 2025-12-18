
p = 17
q = 11
e = 7

n = p * q
phi = (p - 1) * (q - 1)

def mod_inverse(a, m):
    r1, r2 = a, m
    t1, t2 = 1, 0

    while r2:
        q = r1 // r2
        r1, r2 = r2, r1 - q*r2
        t1, t2 = t2, t1 - q*t2

    if r1 != 1:
        raise ValueError("e dan phi tidak coprime")

    return t1 % m

d = mod_inverse(e, phi)

def encrypt(m):
    return pow(m, e, n)

def decrypt(c):
    return pow(c, d, n)

m = int(input(f"Masukkan angka (0 < m < {n}): "))

if not (0 < m < n):
    raise ValueError("m harus lebih kecil dari n!")

cipher = encrypt(m)
plain = decrypt(cipher)

print("n =", n)
print("phi =", phi)
print("d =", d)
print("cipher =", cipher)
print("decrypted =", plain)
