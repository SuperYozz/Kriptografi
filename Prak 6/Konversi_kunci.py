def text_to_binary_table(text):
    binary_table = []
    for char in text:
        binary_code = format(ord(char), '08b')
        binary_table.append((char.upper(), binary_code))
    for _ in range(8 - len(text)):
        binary_table.append(("SPASI", "00000000"))

    return binary_table
text = "marto"
binary_table = text_to_binary_table(text)

print("Key (huruf kecil)\tBiner")
for key, biner in binary_table:
    print(f"{key}\t\t{biner}")
