import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Latihan Python")
root.geometry("450x400")
root.configure(bg="#e6f2ff")

# ---------------- Fungsi Switch Frame ----------------
def show_frame(frame):
    frame.tkraise()

# ---------------- Latihan 1 ----------------
frame1 = tk.Frame(root, bg="#fdf6e3")
frame1.place(x=0, y=50, relwidth=1, relheight=1)

def latihan1_hitung():
    try:
        a = float(entry_a1.get())
        b = float(entry_b1.get())
        hasil = (f"Penjumlahan : {a + b}\n"
                 f"Pengurangan : {a - b}\n"
                 f"Perkalian   : {a * b}\n"
                 f"Pembagian   : {a / b if b != 0 else 'Error (bagi 0)'}")
        label_hasil1.config(text=hasil, fg="blue")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

tk.Label(frame1, text="Latihan 1 - Operasi Aritmatika",
         font=("Arial", 12, "bold"), bg="#657b83", fg="white").pack(fill="x", pady=5)

frm1 = ttk.Frame(frame1, padding=15)
frm1.pack()

ttk.Label(frm1, text="Angka 1:").grid(row=0, column=0, pady=5, sticky="w")
entry_a1 = ttk.Entry(frm1, width=10)
entry_a1.grid(row=0, column=1, padx=10)

ttk.Label(frm1, text="Angka 2:").grid(row=1, column=0, pady=5, sticky="w")
entry_b1 = ttk.Entry(frm1, width=10)
entry_b1.grid(row=1, column=1, padx=10)

ttk.Button(frm1, text="Hitung", command=latihan1_hitung).grid(row=2, columnspan=2, pady=10)
label_hasil1 = tk.Label(frame1, text="", font=("Arial", 10), bg="#fdf6e3")
label_hasil1.pack(pady=10)

# ---------------- Latihan 2 ----------------
frame2 = tk.Frame(root, bg="#f0f8ff")
frame2.place(x=0, y=50, relwidth=1, relheight=1)

def latihan2_hitung():
    try:
        a = float(entry_a2.get())
        b = float(entry_b2.get())
        op = combo_op.get()

        if op == "+": hasil = a + b
        elif op == "-": hasil = a - b
        elif op == "*": hasil = a * b
        elif op == "/":
            if b == 0:
                messagebox.showerror("Error", "Tidak bisa dibagi nol!")
                return
            hasil = a / b
        else:
            messagebox.showerror("Error", "Operator tidak valid!")
            return
        label_hasil2.config(text=f"Hasil: {hasil}", fg="blue")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

tk.Label(frame2, text="Latihan 2 - Kalkulator Sederhana",
         font=("Arial", 12, "bold"), bg="#cd5c5c", fg="white").pack(fill="x", pady=5)

frm2 = ttk.Frame(frame2, padding=15)
frm2.pack()

ttk.Label(frm2, text="Angka 1:").grid(row=0, column=0, pady=5, sticky="w")
entry_a2 = ttk.Entry(frm2, width=10)
entry_a2.grid(row=0, column=1, padx=10)

ttk.Label(frm2, text="Angka 2:").grid(row=1, column=0, pady=5, sticky="w")
entry_b2 = ttk.Entry(frm2, width=10)
entry_b2.grid(row=1, column=1, padx=10)

ttk.Label(frm2, text="Operator:").grid(row=2, column=0, pady=5, sticky="w")
combo_op = ttk.Combobox(frm2, values=["+", "-", "*", "/"], width=7, state="readonly")
combo_op.grid(row=2, column=1, padx=10)
combo_op.current(0)

ttk.Button(frm2, text="Hitung", command=latihan2_hitung).grid(row=3, columnspan=2, pady=10)
label_hasil2 = tk.Label(frame2, text="", font=("Arial", 10), bg="#f0f8ff")
label_hasil2.pack(pady=10)

# ---------------- Latihan 3 ----------------
frame3 = tk.Frame(root, bg="#fffaf0")
frame3.place(x=0, y=50, relwidth=1, relheight=1)

def latihan3_hitung():
    try:
        sikap = float(entry_sikap.get())
        tugas = float(entry_tugas.get())
        uts   = float(entry_uts.get())
        uas   = float(entry_uas.get())
        total = (sikap*0.10) + (tugas*0.30) + (uts*0.25) + (uas*0.35)

        if 81 <= total <= 100:
            grade, bobot = "A", 4
        elif 76 <= total <= 80:
            grade, bobot = "B+", 3.5
        elif 71 <= total <= 75:
            grade, bobot = "B", 3
        elif 66 <= total <= 70:
            grade, bobot = "C+", 2.5
        elif 56 <= total <= 65:
            grade, bobot = "C", 2
        elif 46 <= total <= 55:
            grade, bobot = "D", 1
        else:
            grade, bobot = "E", 0

        keterangan = "Lulus" if total >= 56 else "Tidak Lulus"
        warna = "green" if total >= 56 else "red"

        hasil = (f"Total Nilai : {total:.2f}\n"
                 f"Nilai Akhir : {grade}\n"
                 f"Bobot       : {bobot}\n"
                 f"Keterangan  : {keterangan}")
        label_hasil3.config(text=hasil, fg=warna)
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

tk.Label(frame3, text="Latihan 3 - Kalkulator Nilai Akhir",
         font=("Arial", 12, "bold"), bg="#4682b4", fg="white").pack(fill="x", pady=5)

frm3 = ttk.Frame(frame3, padding=15)
frm3.pack()

ttk.Label(frm3, text="Sikap (10%)").grid(row=0, column=0, pady=5, sticky="w")
entry_sikap = ttk.Entry(frm3, width=10)
entry_sikap.grid(row=0, column=1, padx=10)

ttk.Label(frm3, text="Tugas (30%)").grid(row=1, column=0, pady=5, sticky="w")
entry_tugas = ttk.Entry(frm3, width=10)
entry_tugas.grid(row=1, column=1, padx=10)

ttk.Label(frm3, text="UTS (25%)").grid(row=2, column=0, pady=5, sticky="w")
entry_uts = ttk.Entry(frm3, width=10)
entry_uts.grid(row=2, column=1, padx=10)

ttk.Label(frm3, text="UAS (35%)").grid(row=3, column=0, pady=5, sticky="w")
entry_uas = ttk.Entry(frm3, width=10)
entry_uas.grid(row=3, column=1, padx=10)

ttk.Button(frm3, text="Hitung Nilai", command=latihan3_hitung).grid(row=4, columnspan=2, pady=10)
label_hasil3 = tk.Label(frame3, text="", font=("Arial", 10, "bold"), bg="#fffaf0")
label_hasil3.pack(pady=10)

# ---------------- Menu Atas ----------------
menu_frame = tk.Frame(root, bg="#004080")
menu_frame.place(x=0, y=0, relwidth=1, height=50)

judul = tk.Label(menu_frame, text="Latihan Kriptography",
                 font=("Arial", 14, "bold"), bg="#004080", fg="white")
judul.pack(side="left", padx=10)

btn1 = ttk.Button(menu_frame, text="Latihan 1", command=lambda: show_frame(frame1))
btn1.pack(side="left", padx=5)
btn2 = ttk.Button(menu_frame, text="Latihan 2", command=lambda: show_frame(frame2))
btn2.pack(side="left", padx=5)
btn3 = ttk.Button(menu_frame, text="Latihan 3", command=lambda: show_frame(frame3))
btn3.pack(side="left", padx=5)

# ---------------- Default frame yang muncul ----------------
show_frame(frame1)

root.mainloop()
