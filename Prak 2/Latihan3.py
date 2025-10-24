print("=== Program Kalkulator Sederhana ===")

# Perulangan agar program bisa digunakan berulang kali
while True:
    # Input nilai dari pengguna
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))
    operator = input("Masukkan operator (+, -, *, /): ")

    # Percabangan menggunakan if-elif-else
    if operator == '+':
        hasil = a + b
        print(f"Hasil dari {a} + {b} = {hasil}")
    elif operator == '-':
        hasil = a - b
        print(f"Hasil dari {a} - {b} = {hasil}")
    elif operator == '*':
        hasil = a * b
        print(f"Hasil dari {a} * {b} = {hasil}")
    elif operator == '/':
        if b != 0:
            hasil = a / b
            print(f"Hasil dari {a} / {b} = {hasil}")
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")
    else:
        print("Operator yang Anda masukkan tidak valid.")

    # Tanya apakah ingin menghitung lagi
    ulang = input("\nApakah Anda ingin menghitung lagi? (y/n): ").lower()
    if ulang != 'y':
        print("=== Program selesai. Terima kasih! ===")
        break
