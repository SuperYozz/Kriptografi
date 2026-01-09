import tkinter as tk
from tkinter import messagebox

def hitung_y():
    try:
        p = int(entry_p.get())
        g = int(entry_g.get())
        x = int(entry_x.get())

        # Validasi dasar
        if p <= 2:
            raise ValueError("p harus bilangan prima besar (> 2)")
        if not (1 < g < p):
            raise ValueError("g harus memenuhi 1 < g < p")
        if not (1 < x < p - 1):
            raise ValueError("x harus memenuhi 1 < x < p-1")

        y = pow(g, x, p)  # g^x mod p (aman & efisien)

        label_hasil.config(text=f"Hasil y = {y}")

    except ValueError as e:
        messagebox.showerror("Input Salah", str(e))


# Window utama
root = tk.Tk()
root.title("Perhitungan y = g^x mod p")
root.geometry("360x260")
root.resizable(False, False)

# Judul
tk.Label(root, text="Perhitungan Kunci Publik", font=("Arial", 12, "bold")).pack(pady=10)

# Input p
tk.Label(root, text="Bilangan prima besar (p):").pack()
entry_p = tk.Entry(root)
entry_p.pack()

# Input g
tk.Label(root, text="Generator (1 < g < p):").pack()
entry_g = tk.Entry(root)
entry_g.pack()

# Input x
tk.Label(root, text="Kunci privat (1 < x < p-1):").pack()
entry_x = tk.Entry(root)
entry_x.pack()

# Tombol hitung
tk.Button(root, text="Hitung y", command=hitung_y).pack(pady=10)

# Hasil
label_hasil = tk.Label(root, text="Hasil y = -", font=("Arial", 10, "bold"))
label_hasil.pack()

root.mainloop()
