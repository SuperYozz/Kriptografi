# Program Kalkulator Sederhana
print("=== Program Kalkulator Sederhana ===")

# Input nilai
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

# Input operator
operator = input("Masukkan operator (+, -, *, /): ")

# Proses perhitungan berdasarkan operator
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

print("=== Program selesai. Terima kasih! ===")
1