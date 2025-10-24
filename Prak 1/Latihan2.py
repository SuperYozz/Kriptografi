def hitung_nilai_akhir():
    print("=== Program Menghitung Nilai Akhir Akademik ===")

    # Input nilai dari user
    sikap = float(input("Masukkan nilai Sikap/Kehadiran (0-100): "))
    tugas = float(input("Masukkan nilai Tugas (0-100): "))
    uts   = float(input("Masukkan nilai UTS (0-100): "))
    uas   = float(input("Masukkan nilai UAS (0-100): "))

    # Bobot penilaian
    total = (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)

    # Menentukan grade dan bobot
    if 81 <= total <= 100:
        grade, bobot = "A", 4
    elif 76 <= total <= 80:
        grade, bobot = "B+", 3.5
    elif 71 <= total <= 75:
        grade, bobot = "B", 3
    elif 66 <= total <= 70:
        grade, bobot = "C+", 2.5
    elif 56 <= total <= 65:
        grade, bobot = "C", 2
    elif 46 <= total <= 55:
        grade, bobot = "D", 1
    else:
        grade, bobot = "E", 0

    # Keterangan lulus atau tidak
    if total >= 56:
        keterangan = "Lulus"
    else:
        keterangan = "Tidak Lulus"

    # Output hasil
    print("\n=== Hasil Perhitungan ===")
    print(f"Total Nilai   : {total:.2f}")
    print(f"Nilai Akhir   : {grade}")
    print(f"Bobot         : {bobot}")
    print(f"Keterangan    : {keterangan}")

# Program utama
if __name__ == "__main__":
    hitung_nilai_akhir()
