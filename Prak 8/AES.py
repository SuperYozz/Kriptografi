import tkinter as tk
from tkinter import scrolledtext, messagebox

SBOX = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
]
RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

def text_to_hex(text):
    """Konversi setiap karakter menjadi HEX (uppercase)."""
    return [format(ord(c), '02X') for c in text]

def to_matrix_4x4(hex_list):
    """Susun list HEX menjadi matriks 4x4 AES (kolom per kolom)."""
    matrix = [[0] * 4 for _ in range(4)]
    for i in range(16):
        row = i % 4
        col = i // 4
        matrix[row][col] = hex_list[i]
    return matrix

def xor_matrices(m1, m2):
    """XOR antara 2 matriks 4x4 HEX."""
    result = [[0] * 4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            v1 = int(m1[r][c], 16)
            v2 = int(m2[r][c], 16)
            result[r][c] = format(v1 ^ v2, '02X')
    return result

def rot_word(word):
    """RotWord: Geser ke kiri 1 byte."""
    return word[1:] + word[:1]

def sub_word(word):
    """SubWord: Substitusi menggunakan SBOX."""
    return [SBOX[b] for b in word]

def key_expansion(key_matrix, output_text):
    """Key Expansion untuk AES, dengan output ke GUI."""
    key_words = []
    for col in range(4):
        key_words.append([key_matrix[row][col] for row in range(4)])
    
    output_text.insert(tk.END, "\n=== KEY EXPANSION PROCESS ===\n")
    output_text.insert(tk.END, "Initial K0 (from cipherkey):\n")
    for i, word in enumerate(key_words):
        output_text.insert(tk.END, f"W{i}: {' '.join(f'{b:02X}' for b in word)}\n")
    for i in range(4, 44):
        temp = key_words[i-1].copy()
        output_text.insert(tk.END, f"\n--- Generating W{i} ---\n")
        output_text.insert(tk.END, f"temp = W{i-1} = {' '.join(f'{b:02X}' for b in temp)}\n")
        
        if i % 4 == 0:
            temp = rot_word(temp)
            output_text.insert(tk.END, f"After RotWord: {' '.join(f'{b:02X}' for b in temp)}\n")
            
            temp = sub_word(temp)
            output_text.insert(tk.END, f"After SubWord: {' '.join(f'{b:02X}' for b in temp)}\n")
  
            rcon_val = RCON[(i // 4) - 1]
            temp[0] ^= rcon_val
            output_text.insert(tk.END, f"After XOR with RCON[{ (i//4)-1 }] = {rcon_val:02X}: {' '.join(f'{b:02X}' for b in temp)}\n")
     
        prev_word = key_words[i-4]
        output_text.insert(tk.END, f"W{i-4} = {' '.join(f'{b:02X}' for b in prev_word)}\n")
        new_word = [temp[j] ^ prev_word[j] for j in range(4)]
        output_text.insert(tk.END, f"W{i} = temp XOR W{i-4} = {' '.join(f'{b:02X}' for b in new_word)}\n")
        
        key_words.append(new_word)
    
    return key_words

def words_to_matrix(words):
    """Konversi 4 words menjadi matriks 4x4."""
    matrix = [[0] * 4 for _ in range(4)]
    for col in range(4):
        for row in range(4):
            matrix[row][col] = words[col][row]
    return matrix

def process():
    plaintext = entry_plain.get().strip()
    cipherkey = entry_key.get().strip()
    
    if len(plaintext) != 16 or len(cipherkey) != 16:
        messagebox.showerror("Error", "Plaintext dan Cipherkey harus tepat 16 karakter.")
        return
    output_text.delete(1.0, tk.END)

    hex_plain = text_to_hex(plaintext)
    hex_key = text_to_hex(cipherkey)
    matrix_plain = to_matrix_4x4(hex_plain)
    matrix_key = to_matrix_4x4(hex_key)
    
    output_text.insert(tk.END, "\n=== PLAINTEXT (HEX) dalam Matriks 4x4 ===\n")
    for row in matrix_plain:
        output_text.insert(tk.END, " ".join(row) + "\n")
    
    output_text.insert(tk.END, "\n=== CIPHERKEY (HEX) dalam Matriks 4x4 ===\n")
    for row in matrix_key:
        output_text.insert(tk.END, " ".join(row) + "\n")
    
    matrix_xor = xor_matrices(matrix_plain, matrix_key)
    output_text.insert(tk.END, "\n=== HASIL XOR (AddRoundKey) ===\n")
    for row in matrix_xor:
        output_text.insert(tk.END, " ".join(row) + "\n")
    
    key_matrix_int = [[int(matrix_key[r][c], 16) for c in range(4)] for r in range(4)]
    all_keys = key_expansion(key_matrix_int, output_text)
    
    for r in range(11):
        start = r * 4
        end = start + 4
        key_mat = words_to_matrix(all_keys[start:end])
        output_text.insert(tk.END, f"\n=== K{r} ===\n")
        for row in key_mat:
            output_text.insert(tk.END, " ".join(f"{x:02X}" for x in row) + "\n")

root = tk.Tk()
root.title("AES Key Expansion GUI")
root.geometry("800x600")

tk.Label(root, text="Plaintext (16 karakter):").pack(pady=5)
entry_plain = tk.Entry(root, width=50)
entry_plain.pack()

tk.Label(root, text="Cipherkey (16 karakter):").pack(pady=5)
entry_key = tk.Entry(root, width=50)
entry_key.pack()

tk.Button(root, text="Process", command=process).pack(pady=10)

output_text = scrolledtext.ScrolledText(root, width=90, height=30)
output_text.pack(pady=10)

root.mainloop()