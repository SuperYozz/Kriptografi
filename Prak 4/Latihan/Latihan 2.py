def substitusi_cipher(plaintext, aturan):
    """Melakukan substitusi berdasarkan aturan yang diberikan"""
    ciphertext = ''
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char  
    return ciphertext


def transposisi_cipher(ciphertext):
    """Membagi hasil substitusi menjadi 4 blok, lalu baca kolom per kolom"""
    ciphertext = ciphertext.replace(" ", "")
    panjang = len(ciphertext)
    blok = 4
    part_length = panjang // blok

    parts = [ciphertext[i:i+part_length] for i in range(0, panjang, part_length)]

    while len(parts[-1]) < part_length:
        parts[-1] += "X"

    hasil = ""
    for col in range(part_length):
        for part in parts:
            if col < len(part):
                hasil += part[col]
    return hasil

print("=== PROGRAM SUBSTITUSI + TRANSPOSISI CIPHER ===")
plaintext = input("Masukkan Plaintext : ").upper()

print("\nMasukkan aturan substitusi huruf (contoh: A=D, B=E, C=F).")
print("Ketik 'STOP' jika sudah selesai.\n")

aturan_substitusi = {}

while True:
    pasangan = input("Aturan (contoh A=D): ").strip().upper()
    if pasangan == "STOP":
        break
    if "=" in pasangan and len(pasangan.split("=")[0]) == 1 and len(pasangan.split("=")[1]) == 1:
        p, c = pasangan.split("=")
        aturan_substitusi[p] = c
    else:
        print("Format salah! Gunakan format A=D")


cipher_substitusi = substitusi_cipher(plaintext, aturan_substitusi)
cipher_transposisi = transposisi_cipher(cipher_substitusi)


print("\n=== HASIL PROSES ENKRIPSI ===")
print(f"Plaintext                     : {plaintext}")
print(f"Setelah Substitusi Cipher     : {cipher_substitusi}")
print(f"Setelah Transposisi (4 blok)  : {cipher_transposisi}")
