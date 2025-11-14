import numpy as np
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]
PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

SHIFT_TABLE = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
def text_to_binary(text):
    return "".join([format(ord(c), "08b") for c in text])
def apply_pc1(key_64bit):
    selected = [key_64bit[i-1] for i in PC1]
    C0 = selected[:28]
    D0 = selected[28:]
    return C0, D0
def left_shift(arr, n):
    return arr[n:] + arr[:n]
def apply_pc2(C, D):
    combined = C + D
    return [combined[i-1] for i in PC2]
def generate_subkeys_str(key):
    output = ""
    if len(key) != 8:
        messagebox.showerror("Kesalahan", "Key harus terdiri dari 8 karakter (64 bit).")
        return None
    key_bin = text_to_binary(key)
    key_bin = list(key_bin)

    output += "=== KONVERSI KEY → BINER ===\n"
    for i, ch in enumerate(key):
        output += f"{ch}\t{format(ord(ch),'08b')}\n"
    output += f"\nKey Biner 64 bit:\n{''.join(key_bin)}\n"
    C0, D0 = apply_pc1(key_bin)

    output += "\n=== HASIL PC-1 (56 bit) ===\n"
    output += f"C0: {''.join(C0)}\n"
    output += f"D0: {''.join(D0)}\n"

    C = C0
    D = D0
    subkeys = []

    output += "\n=== LEFT SHIFT C1 – C16 & D1 – D16 ===\n"
    for i in range(16):
        shift = SHIFT_TABLE[i]
        C = left_shift(C, shift)
        D = left_shift(D, shift)

        output += f"Round {i+1} (Shift {shift}):\n"
        output += f"C{i+1}: {''.join(C)}\n"
        output += f"D{i+1}: {''.join(D)}\n\n"
        Ki = apply_pc2(C, D)
        subkeys.append(Ki)

    output += "\n=== SUBKEY K1 – K16 (48 bit) ===\n"
    for i, k in enumerate(subkeys):
        output += f"K{i+1}: {''.join(k)}\n"
        
    return output
def run_key_schedule():
    key = key_entry.get()
    output_text.delete(1.0, tk.END)

    if len(key) != 8:
        messagebox.showerror("Kesalahan", "Key harus terdiri dari 8 karakter (64 bit).")
        return
    result = generate_subkeys_str(key)
    if result:
        output_text.insert(tk.END, result)
root = tk.Tk()
root.title("🔑 Key Schedule DES Generator")
root.geometry("800x650")

input_frame = ttk.Frame(root, padding="10")
input_frame.pack(fill='x')
ttk.Label(input_frame, text="Masukkan KEY (8 karakter):", font=('Arial', 10, 'bold')).grid(row=0, column=0, padx=5, pady=5, sticky='w')

key_entry = ttk.Entry(input_frame, width=30, font=('Consolas', 10))
key_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

generate_button = ttk.Button(input_frame, text="Generate Subkeys", command=run_key_schedule)
generate_button.grid(row=0, column=2, padx=10, pady=5)

output_frame = ttk.Frame(root, padding="10")
output_frame.pack(fill='both', expand=True)

ttk.Label(output_frame, text="Hasil Key Schedule (Langkah-langkah):", font=('Arial', 10, 'bold')).pack(anchor='w')

output_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, width=70, height=25, font=('Consolas', 10), bg='#f0f0f0')
output_text.pack(fill='both', expand=True, pady=5)

root.mainloop()