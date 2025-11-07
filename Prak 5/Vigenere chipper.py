import tkinter as tk
from tkinter import ttk, messagebox


class VigenereCipher:
    """Kelas Vigenère Cipher tanpa sinkronisasi kunci untuk karakter non-alfabet."""
    def __init__(self, text: str, key: str):
        self.text = text.upper()
        self.key = key.upper()

    @staticmethod
    def alpha_index(ch: str) -> int:
        return ord(ch) - ord('A')

    @staticmethod
    def index_alpha(i: int) -> str:
        return chr((i % 26) + ord('A'))

    def generate_key(self):
        """Bangun kunci hanya untuk huruf alfabet (tidak untuk spasi/tanda baca)."""
        if not self.key:
            return ""
        key_result = []
        key_index = 0
        for ch in self.text:
            if ch.isalpha():
                key_result.append(self.key[key_index % len(self.key)])
                key_index += 1
            else:
                key_result.append(' ')  # biar panjang selaras untuk visualisasi
        return "".join(key_result)

    def encrypt(self):
        cipher = []
        log = []
        gen_key = self.generate_key()

        log.append("=== PROSES ENKRIPSI (tanpa sinkronisasi) ===")
        log.append(f"Teks Asli        : {self.text}")
        log.append(f"Kunci            : {self.key}")
        log.append(f"Kunci Digunakan  : {gen_key}\n")

        key_index = 0
        for i, ch in enumerate(self.text):
            if ch.isalpha():
                p = self.alpha_index(ch)
                k = self.alpha_index(self.key[key_index % len(self.key)])
                total = p + k
                mod = total % 26
                c = self.index_alpha(mod)

                cipher.append(c)
                log.append(
                    f"[{i}] '{ch}' (P={p}) + '{self.key[key_index % len(self.key)]}' (K={k}) -> "
                    f"P+K={p}+{k}={total} -> {total}%26={mod} -> '{c}'"
                )
                key_index += 1
            else:
                cipher.append(ch)
                log.append(f"[{i}] '{ch}' bukan huruf -> dilewatkan, tetap '{ch}'")

        hasil = "".join(cipher)
        log.append(f"\nHasil Enkripsi: {hasil}")
        return hasil, "\n".join(log)

    def decrypt(self):
        plain = []
        log = []
        gen_key = self.generate_key()

        log.append("=== PROSES DEKRIPSI (tanpa sinkronisasi) ===")
        log.append(f"Teks Enkripsi    : {self.text}")
        log.append(f"Kunci Asli       : {self.key}")
        log.append(f"Kunci Digunakan  : {gen_key}\n")

        key_index = 0
        for i, ch in enumerate(self.text):
            if ch.isalpha():
                c = self.alpha_index(ch)
                k = self.alpha_index(self.key[key_index % len(self.key)])
                diff = c - k
                mod = (diff + 26) % 26
                p = self.index_alpha(mod)

                plain.append(p)
                log.append(
                    f"[{i}] '{ch}' (C={c}) - '{self.key[key_index % len(self.key)]}' (K={k}) -> "
                    f"C-K={c}-{k}={diff} -> ({diff}+26)%26={mod} -> '{p}'"
                )
                key_index += 1
            else:
                plain.append(ch)
                log.append(f"[{i}] '{ch}' bukan huruf -> dilewatkan, tetap '{ch}'")

        hasil = "".join(plain)
        log.append(f"\nHasil Dekripsi: {hasil}")
        return hasil, "\n".join(log)


class CipherApp:
    """GUI Tkinter untuk Vigenère Cipher tanpa sinkronisasi kunci."""
    def __init__(self, root):
        self.root = root
        self.root.title("Vigenère Cipher — Detail Perhitungan (Tanpa Sinkronisasi)")
        self.root.geometry("750x630")
        self.root.resizable(False, False)

        ttk.Label(root, text="Vigenère Cipher ", font=("Segoe UI", 16, "bold")).pack(pady=10)

        # Frame input
        frame = ttk.Frame(root, padding=10)
        frame.pack(fill="x", padx=15)

        ttk.Label(frame, text="Teks:", font=("Segoe UI", 11)).grid(row=0, column=0, sticky="w", pady=6)
        self.text_entry = ttk.Entry(frame, width=65)
        self.text_entry.grid(row=0, column=1, padx=8)

        ttk.Label(frame, text="Kunci:", font=("Segoe UI", 11)).grid(row=1, column=0, sticky="w", pady=6)
        self.key_entry = ttk.Entry(frame, width=65)
        self.key_entry.grid(row=1, column=1, padx=8)

        # Tombol aksi
        btn_frame = ttk.Frame(root, padding=10)
        btn_frame.pack()

        ttk.Button(btn_frame, text="🔒 Encrypt", command=self.encrypt_text).grid(row=0, column=0, padx=8)
        ttk.Button(btn_frame, text="🔓 Decrypt", command=self.decrypt_text).grid(row=0, column=1, padx=8)
        ttk.Button(btn_frame, text="🧾 Salin Hasil", command=self.copy_output).grid(row=0, column=2, padx=8)
        ttk.Button(btn_frame, text="🧹 Clear", command=self.clear_text).grid(row=0, column=3, padx=8)

        # Area output
        ttk.Label(root, text="Detail Proses:", font=("Segoe UI", 12, "bold")).pack(pady=(10, 0))
        self.output_text = tk.Text(root, wrap="word", height=26, width=90, bg="#f8f9fb", fg="#111", font=("Consolas", 10))
        self.output_text.pack(padx=10, pady=10)

        ttk.Label(root, text="Catatan: Huruf non-alfabet dilewatkan, tidak memajukan kunci.", font=("Segoe UI", 9)).pack(pady=(0, 8))

    # Fungsi tombol
    def encrypt_text(self):
        text, key = self.text_entry.get(), self.key_entry.get()
        if not text or not key:
            messagebox.showwarning("Peringatan", "Isi teks dan kunci terlebih dahulu.")
            return

        cipher = VigenereCipher(text, key)
        _, log = cipher.encrypt()

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, log)

    def decrypt_text(self):
        text, key = self.text_entry.get(), self.key_entry.get()
        if not text or not key:
            messagebox.showwarning("Peringatan", "Isi teks dan kunci terlebih dahulu.")
            return

        cipher = VigenereCipher(text, key)
        _, log = cipher.decrypt()

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, log)

    def copy_output(self):
        result = self.output_text.get(1.0, tk.END).strip()
        if result:
            self.root.clipboard_clear()
            self.root.clipboard_append(result)
            messagebox.showinfo("Disalin", "Detail proses telah disalin ke clipboard.")
        else:
            messagebox.showwarning("Kosong", "Tidak ada hasil untuk disalin.")

    def clear_text(self):
        self.text_entry.delete(0, tk.END)
        self.key_entry.delete(0, tk.END)
        self.output_text.delete(1.0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()
