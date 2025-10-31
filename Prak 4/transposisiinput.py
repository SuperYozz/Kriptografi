def transposisi_cipher(plaintext):

    num_cols = 4

    part_length = len(plaintext) // num_cols
    if len(plaintext) % num_cols != 0:
        part_length += 1  

    parts = [plaintext[i:i + part_length] for i in range(0, len(plaintext), part_length)]
    
    ciphertext = ""

    for col in range(num_cols):
        for part in parts:
            if col < len(part):
                ciphertext += part[col]
    
    return ciphertext

plaintext = input("Masukkan plaintext: ")

ciphertext = transposisi_cipher(plaintext)

print(f"\nPlaintext : {plaintext}")
print(f"Ciphertext: {ciphertext}")
