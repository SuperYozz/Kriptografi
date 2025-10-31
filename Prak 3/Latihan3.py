from itertools import combinations

def faktorial(x): 
    if x == 0 or x == 1: 
        return 1 
    hasil = 1 
    for i in range(2, x + 1): 
        hasil *= i 
    return hasil 

def kombinasi(n, r): 
    if r > n: 
        return 0 
    faktorial_n = faktorial(n) 
    faktorial_r = faktorial(r) 
    faktorial_n_r = faktorial(n - r) 
    return faktorial_n // (faktorial_r * faktorial_n_r) 

# Input data
n = int(input("Masukkan jumlah total objek (n): ")) 
r = int(input("Masukkan jumlah objek yang dipilih (r): "))

# Buat daftar huruf sesuai jumlah n
huruf = []
for i in range(n):
    huruf.append(chr(65 + i))  # 65 = 'A', 66 = 'B', dst.

# Hitung kombinasi secara matematis
hasil = kombinasi(n, r)
print(f"\nJumlah kombinasi C({n}, {r}) adalah: {hasil}")

# Tampilkan semua kombinasi huruf
print("\nDaftar kombinasi huruf yang mungkin:")
kombinasi_huruf = list(combinations(huruf, r))
for i, k in enumerate(kombinasi_huruf, start=1):
    print(f"{i}. {''.join(k)}")
