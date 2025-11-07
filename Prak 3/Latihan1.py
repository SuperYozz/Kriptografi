class sb:

    @staticmethod
    def decToBin(value):
        return bin(value)[2:]

    @staticmethod
    def decToOct(value):
        return oct(value)[2:]

    @staticmethod
    def decToHex(value):
        return hex(value)[2:].upper()

    @staticmethod
    def binToDec(value):
        return int(value, 2)

    @staticmethod
    def binToOct(value):
        return oct(int(value, 2))[2:]

    @staticmethod
    def binToHex(value):
        return hex(int(value, 2))[2:].upper()

    @staticmethod
    def octToDec(value):
        return int(value, 8)

    @staticmethod
    def octToBin(value):
        return bin(int(value, 8))[2:]

    @staticmethod
    def octToHex(value):
        return hex(int(value, 8))[2:].upper()

    @staticmethod
    def hexToDec(value):
        return int(value, 16)

    @staticmethod
    def hexToBin(value):
        return bin(int(value, 16))[2:]

    @staticmethod
    def hexToOct(value):
        return oct(int(value, 16))[2:]
2


def main():
    print("=" * 40)
    print("PROGRAM KONVERSI BILANGAN By Yosua Tambunan")
    print("=" * 40)
    print("Pilih jenis konversi:")
    print("1. Desimal ke Biner / Oktal / Heksa")
    print("2. Biner ke Desimal/Heksadesimal/Oktal")
    print("3. Oktal ke Desimal/Heksadesimal/Biner")
    print("4. Heksadesimal ke Desimal/Biner/Oktal")

    try:
        pilihan = int(input("Masukkan pilihan (1-4): "))

        if pilihan == 1:
            des = int(input("Masukkan bilangan desimal: "))
            print(f"Biner       : {sb.decToBin(des)}")
            print(f"Oktal       : {sb.decToOct(des)}")
            print(f"Heksadesimal: {sb.decToHex(des)}")

        elif pilihan == 2:
            biner = input("Masukkan bilangan biner: ")
            print(f"Desimal     : {sb.binToDec(biner)}")
            print(f"Oktal       : {sb.binToOct(biner)}")
            print(f"Heksadesimal: {sb.binToHex(biner)}")

        elif pilihan == 3:
            oktal = input("Masukkan bilangan oktal: ")
            print(f"Desimal     : {sb.octToDec(oktal)}")
            print(f"Heksadesimal: {sb.octToHex(oktal)}")
            print(f"Biner       : {sb.octToBin(oktal)}")

        elif pilihan == 4:
            heksa = input("Masukkan bilangan heksadesimal: ")
            print(f"Desimal     : {sb.hexToDec(heksa)}")
            print(f"Biner       : {sb.hexToBin(heksa)}")
            print(f"Oktal       : {sb.hexToOct(heksa)}")

        else:
            print("Pilihan tidak valid! (1-4 saja)")

    except ValueError:
        print("Input tidak valid! Pastikan angka sesuai dengan jenis bilangan.")

    print("=" * 40)
    lanjut = input("Ingin melakukan konversi lagi? (y/n): ").strip().lower()
    if lanjut == 'y':
        main()
    else:
        print("Bye bye!")


if __name__ == "__main__":
    main()
