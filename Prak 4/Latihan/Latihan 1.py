def substitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext

aturan_substitusi = {}

print("=== Program Substitusi Cipher ===")
print("Masukkan aturan substitusi (contoh: A -> X)")
print("Ketik 'SELESAI' jika sudah selesai.\n")

while True:
    huruf_asli = input("Huruf asli (A-Z): ").upper()
    if huruf_asli == "SELESAI":
        break
    if len(huruf_asli) != 1 or not huruf_asli.isalpha():
        print("⚠️ Masukkan hanya satu huruf!")
        continue

    huruf_ganti = input(f"Ganti {huruf_asli} menjadi: ").upper()
    if len(huruf_ganti) != 1 or not huruf_ganti.isalpha():
        print("⚠️ Masukkan hanya satu huruf!")
        continue

    aturan_substitusi[huruf_asli] = huruf_ganti
    print(f"Aturan ditambahkan: {huruf_asli} → {huruf_ganti}\n")

plaintext = input("Masukkan plaintext: ").upper()
ciphertext = substitusi_cipher(plaintext, aturan_substitusi)

print("\n=== HASIL ENKRIPSI ===")
print(f"Plaintext : {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Aturan    : {aturan_substitusi}")
