import tkinter as tk
from tkinter import messagebox
import binascii

# ====== Tabel DES ======
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

IP_INV = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25]

PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

SHIFT = [1, 1, 2, 2, 2, 2, 2, 2,
         1, 2, 2, 2, 2, 2, 2, 1]

E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]

S_BOX = [
    # S1
    [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
     [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
     [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
     [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],
    # S2
    [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
     [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
     [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
     [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],
    # S3
    [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
     [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
     [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
     [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],
    # S4
    [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
     [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
     [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
     [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],
    # S5
    [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
     [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
     [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
     [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],
    # S6
    [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
     [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
     [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
     [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],
    # S7
    [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
     [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
     [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
     [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],
    # S8
    [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
     [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
     [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
     [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]]

# ====== Fungsi Utility ======
def str_to_bin(text):
    """Konversi string ke biner 8-bit per karakter"""
    return ''.join(f'{ord(c):08b}' for c in text)

def bin_to_hex(binary):
    """Konversi biner ke heksadesimal"""
    return hex(int(binary, 2))[2:].upper()

def permute(block, table):
    return ''.join(block[i-1] for i in table)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def xor(a, b):
    return ''.join('0' if i==j else '1' for i,j in zip(a,b))

def sbox_substitute(bits48):
    output = ""
    for i in range(8):
        block = bits48[i*6:(i+1)*6]
        row = int(block[0]+block[5], 2)
        col = int(block[1:5], 2)
        val = S_BOX[i][row][col]
        output += f'{val:04b}'
    return output

# ====== DES Key Schedule ======
def generate_subkeys(key_bin):
    # PC-1
    key56 = permute(key_bin, PC1)
    C, D = key56[:28], key56[28:]
    subkeys = []
    for shift in SHIFT:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        subkeys.append(permute(C+D, PC2))
    return subkeys

# ====== DES Encrypt 64-bit block ======
def des_encrypt_block(plaintext_bin, subkeys):
    block = permute(plaintext_bin, IP)
    L, R = block[:32], block[32:]
    for i in range(16):
        # Expansion
        R_exp = permute(R, E)
        # XOR dengan subkey
        X = xor(R_exp, subkeys[i])
        # S-box
        S = sbox_substitute(X)
        # P-permutation
        P_perm = permute(S, P)
        # XOR dengan L
        newR = xor(L, P_perm)
        L = R
        R = newR
    # Gabung R16 + L16
    preoutput = R + L
    ciphertext = permute(preoutput, IP_INV)
    return ciphertext

# ====== GUI ======
def encrypt_des():
    plaintext = entry_plain.get()
    key = entry_key.get()

    if len(key) > 8:
        messagebox.showerror("Error", "Kunci maksimal 8 karakter")
        return
    # Padding plaintext ke 8 karakter jika perlu
    if len(plaintext) < 8:
        plaintext += ' '*(8-len(plaintext))

    plaintext_bin = str_to_bin(plaintext)
    key_bin = str_to_bin(key.ljust(8))  # pastikan 8 karakter

    subkeys = generate_subkeys(key_bin)
    ciphertext_bin = des_encrypt_block(plaintext_bin, subkeys)
    ciphertext_hex = bin_to_hex(ciphertext_bin)

    # Tampilkan subkey
    subkey_text.delete('1.0', tk.END)
    for i, k in enumerate(subkeys):
        subkey_text.insert(tk.END, f"K{i+1}: {k}\n")

    # Tampilkan ciphertext
    entry_cipher_bin.config(state='normal')
    entry_cipher_bin.delete(0, tk.END)
    entry_cipher_bin.insert(0, ciphertext_bin)
    entry_cipher_bin.config(state='readonly')

    entry_cipher_hex.config(state='normal')
    entry_cipher_hex.delete(0, tk.END)
    entry_cipher_hex.insert(0, ciphertext_hex)
    entry_cipher_hex.config(state='readonly')

# ====== Tkinter GUI ======
root = tk.Tk()
root.title("DES Encryption GUI")
root.geometry("700x600")

tk.Label(root, text="Plaintext:").pack()
entry_plain = tk.Entry(root, width=50)
entry_plain.pack()

tk.Label(root, text="Key (max 8 chars):").pack()
entry_key = tk.Entry(root, width=20)
entry_key.pack()

tk.Button(root, text="Encrypt DES", command=encrypt_des).pack(pady=10)

tk.Label(root, text="Ciphertext (Binary):").pack()
entry_cipher_bin = tk.Entry(root, width=70, state='readonly')
entry_cipher_bin.pack()

tk.Label(root, text="Ciphertext (Hex):").pack()
entry_cipher_hex = tk.Entry(root, width=70, state='readonly')
entry_cipher_hex.pack()

tk.Label(root, text="16 Subkeys:").pack()
subkey_text = tk.Text(root, width=85, height=20)
subkey_text.pack()

root.mainloop()
