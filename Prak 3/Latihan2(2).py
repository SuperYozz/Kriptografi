from itertools import product

def semua_cara_penempatan(n, r):
    # Buat daftar bagian rak, misalnya [1, 2, 3, ..., r]
    rak = list(range(1, r + 1))
    
    print(f"\n=== Semua Cara Penempatan {n} Buku ke {r} Bagian Rak ===")
    kombinasi = list(product(rak, repeat=n))  # semua kombinasi kemungkinan

    # Cetak setiap kombinasi
    for i, cara in enumerate(kombinasi, start=1):
        print(f"Cara {i}: {cara}")

    # Hitung total kemungkinan
    total = r ** n
    print(f"\nTotal cara penempatan yang mungkin: {total}")

# --- Program utama ---
if __name__ == "__main__":
    # Input dari pengguna
    n = int(input("Masukkan jumlah buku (n): "))
    r = int(input("Masukkan jumlah bagian rak (r): "))
    
    # Panggil fungsi
    semua_cara_penempatan(n, r)
