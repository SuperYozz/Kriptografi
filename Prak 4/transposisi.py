def transposisi_cipher(plaintext):
    plaintext = plaintext.replace(" ", "")

    num_cols = 4

    parts = [plaintext[i:i + num_cols] for i in range(0, len(plaintext), num_cols)]
    
    ciphertext = ""

    for col in range(num_cols):
        for part in parts:
            if col < len(part):
                ciphertext += part[col]
    
    return ciphertext

plaintext = "UNIKA SANTO THOMAS"
ciphertext = transposisi_cipher(plaintext)

print(f"Plaintext : {plaintext}")
print(f"Ciphertext: {ciphertext}")
