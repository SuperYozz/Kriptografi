import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memproses ekspresi
def proses_ekspresi():
    ekspresi = entry_input.get().strip()

    if not ekspresi:
        messagebox.showwarning("Peringatan", "Masukkan ekspresi terlebih dahulu!")
        return

    try:
        # Evaluasi ekspresi matematika secara aman
        hasil = eval(ekspresi, {"__builtins__": None}, {"abs": abs, "round": round})
        label_hasil_proses.config(text="Hasil Diproses")
        label_output.config(text=f"Output > {hasil}")
    except Exception as e:
        label_hasil_proses.config(text="Terjadi Kesalahan ❌")
        label_output.config(text=f"Error: {str(e)}")

# Fungsi untuk menghapus input dan output
def reset():
    entry_input.delete(0, tk.END)
    label_hasil_proses.config(text="Hasil Diproses")
    label_output.config(text="Output >")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Hybrid")
root.geometry("400x300")
root.config(bg="#f0f4f7")

# Judul
tk.Label(root, text="Kalkulator Hybrid", font=("Segoe UI", 16, "bold"), bg="#f0f4f7", fg="#2c3e50").pack(pady=10)

# Frame Input
frame_input = tk.Frame(root, bg="#f0f4f7")
frame_input.pack(pady=10)

tk.Label(frame_input, text="Input (Ekspresi):", font=("Segoe UI", 12), bg="#f0f4f7").grid(row=0, column=0, padx=5, sticky="w")
entry_input = tk.Entry(frame_input, font=("Consolas", 12), width=25, justify="center")
entry_input.grid(row=0, column=1, padx=5)

# Tombol proses
btn_proses = tk.Button(root, text="Proses", font=("Segoe UI", 11, "bold"), bg="#4CAF50", fg="white", width=12, command=proses_ekspresi)
btn_proses.pack(pady=5)

# Label hasil proses
label_hasil_proses = tk.Label(root, text="Hasil Diproses", font=("Segoe UI", 12), bg="#f0f4f7", fg="#2c3e50")
label_hasil_proses.pack(pady=5)

# Label output hasil
label_output = tk.Label(root, text="Output >", font=("Consolas", 13, "bold"), bg="#f0f4f7", fg="#1e88e5")
label_output.pack(pady=10)

# Tombol reset
btn_reset = tk.Button(root, text="Reset", font=("Segoe UI", 10), bg="#e74c3c", fg="white", width=10, command=reset)
btn_reset.pack(pady=5)

# Jalankan aplikasi
root.mainloop()
