import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

while input("Apakah Anda ingin memulai operasi perhitungan? (y/n): ").lower() == 'y':
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))
    c = input("Masukkan operator (+, -, *, /): ")

    try:
        hasil = ops[c](a, b)
        print(f"Hasil dari {a} {c} {b} = {hasil}\n")
    except KeyError:
        print("Operator tidak valid.\n")
    except ZeroDivisionError:
        print("Pembagian dengan nol tidak diperbolehkan.\n")

print("Program selesai. Terima kasih!")
