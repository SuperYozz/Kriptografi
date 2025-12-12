# RSA dengan p, q, e tetap
p = 17
q = 11
e = 7

# 1. Hitung n dan phi(n)
n = p * q
phi = (p - 1) * (q - 1)

# 2. Extended Euclid untuk inverse
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

# 3. Fungsi enkripsi & dekripsi
def encrypt(m):
    return pow(m, e, n)

def decrypt(c):
    return pow(c, d, n)

# ===== INPUT DARI USER =====
m = int(input(f"Masukkan angka (0 < m < {n}): "))

if not (0 < m < n):
    raise ValueError("m harus lebih kecil dari n!")

# Proses
cipher = encrypt(m)
plain = decrypt(cipher)

print("n =", n)
print("phi =", phi)
print("d =", d)
print("cipher =", cipher)
print("decrypted =", plain)
