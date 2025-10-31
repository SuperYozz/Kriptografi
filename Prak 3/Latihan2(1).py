import math

def permutasi_menyeluruh():
    n = int(input("Masukkan jumlah elemen (n): "))
    hasil = math.factorial(n)
    print(f"Permutasi Menyeluruh dari {n} elemen adalah: {hasil}")

def permutasi_sebagian():
    n = int(input("Masukkan jumlah total elemen (n): "))
    r = int(input("Masukkan jumlah elemen yang diambil (r): "))
    hasil = math.factorial(n) // math.factorial(n - r)
    print(f"Permutasi Sebagian dari {n} elemen diambil {r} adalah: {hasil}")

def permutasi_keliling():
    n = int(input("Masukkan jumlah elemen (n): "))
    if n < 2:
        print("Permutasi keliling minimal memerlukan 2 elemen.")
        return
    hasil = math.factorial(n - 1)
    print(f"Permutasi Keliling dari {n} elemen adalah: {hasil}")

def permutasi_berkelompok():
    n = int(input("Masukkan total jumlah elemen (n): "))
    jumlah_kelompok = int(input("Masukkan banyak kelompok elemen sama (misal huruf yang berulang): "))

    penyebut = 1
    for i in range(jumlah_kelompok):
        ni = int(input(f"Masukkan jumlah elemen sama ke-{i+1}: "))
        penyebut *= math.factorial(ni)

    hasil = math.factorial(n) // penyebut
    print(f"Permutasi Data Berkelompok adalah: {hasil}")

# Menu utama
print("=== PROGRAM BERBAGAI JENIS PERMUTASI ===")
print("1. Permutasi Menyeluruh")
print("2. Permutasi Sebagian")
print("3. Permutasi Keliling")
print("4. Permutasi Data Berkelompok")

pilihan = input("Pilih jenis permutasi (1-4): ")

if pilihan == '1':
    permutasi_menyeluruh()
elif pilihan == '2':
    permutasi_sebagian()
elif pilihan == '3':
    permutasi_keliling()
elif pilihan == '4':
    permutasi_berkelompok()
else:
    print("Pilihan tidak valid! Silakan jalankan ulang program.")
