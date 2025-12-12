import tkinter as tk
from tkinter import scrolledtext, messagebox
import random
import math

# ------------------------------
# Utility: generate primes list
# ------------------------------
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(n**0.5)
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True


PRIMES_50_200 = [x for x in range(50, 201) if is_prime(x)]


# ------------------------------
# Extended Euclidean with steps
# ------------------------------
def extended_gcd_with_steps(a, b):
    steps = []
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1

    steps.append(f"Init: r0={r0}, r1={r1}, s0={s0}, s1={s1}, t0={t0}, t1={t1}")

    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
        steps.append(f"q={q} → r0={r0}, r1={r1}, s0={s0}, s1={s1}, t0={t0}, t1={t1}")

    steps.append(f"Result: gcd={r0}, x={s0}, y={t0}")
    return r0, s0, t0, steps


def mod_inverse_with_steps(e, phi):
    g, x, y, steps = extended_gcd_with_steps(e, phi)
    if g != 1:
        raise ValueError("Inverse modular tidak ada, gcd != 1")
    inv = x % phi
    steps.append(f"Inverse modular d = {x} mod {phi} = {inv}")
    return inv, steps


# ------------------------------
# RSA ENGINE
# ------------------------------
class RSAEngine:
    def __init__(self):
        self.p = None
        self.q = None
        self.e = None
        self.d = None
        self.n = None
        self.phi = None
        self.extended_steps = []

    def generate_keys(self, debug):
        self.p = random.choice(PRIMES_50_200)
        self.q = random.choice(PRIMES_50_200)
        while self.q == self.p:
            self.q = random.choice(PRIMES_50_200)

        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

        debug(f"p = {self.p}")
        debug(f"q = {self.q}")
        debug(f"n = p * q = {self.n}")
        debug(f"phi = (p-1)(q-1) = {self.phi}")

        # pilih e
        candidates = [x for x in range(3, self.phi) if math.gcd(x, self.phi) == 1]
        self.e = random.choice(candidates)
        debug(f"e dipilih = {self.e}")

        # cari d
        self.d, self.extended_steps = mod_inverse_with_steps(self.e, self.phi)
        for st in self.extended_steps:
            debug(st)

        debug(f"Kunci Publik : (e={self.e}, n={self.n})")
        debug(f"Kunci Privat : (d={self.d}, n={self.n})")
        debug("=== KEY GENERATION FINISHED ===")

    def encrypt_message(self, plaintext, debug):
        nums = [ord(c) for c in plaintext]
        debug(f"Plaintext → ord = {nums}")

        result = []
        for m in nums:
            c = pow(m, self.e, self.n)
            debug(f"Encrypt: {m}^{self.e} mod {self.n} = {c}")
            result.append(c)

        cipher_text = " ".join(str(x) for x in result)
        debug(f"Ciphertext: {cipher_text}")
        return cipher_text

    def decrypt_message(self, cipher_text, debug):
        parts = cipher_text.split()
        nums = [int(x) for x in parts]
        debug(f"Cipher numeric = {nums}")

        result = []
        for c in nums:
            m = pow(c, self.d, self.n)
            debug(f"Decrypt: {c}^{self.d} mod {self.n} = {m}")
            result.append(m)

        plaintext = "".join(chr(x) for x in result)
        debug(f"Plaintext recovered = {repr(plaintext)}")
        return plaintext


# ------------------------------
# GUI
# ------------------------------
class RSAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RSA Debug GUI – p, q acak (50..200)")

        self.engine = RSAEngine()

        frm_keys = tk.Frame(root, padx=8, pady=6)
        frm_keys.pack(fill="x")

        tk.Button(frm_keys, text="Generate Keys", command=self.generate_keys).pack(
            side="left", padx=4
        )
        tk.Button(frm_keys, text="Clear Debug", command=self.clear_debug).pack(
            side="left", padx=4
        )

        self.lbl_keys = tk.Label(
            root, text="Kunci: (belum dibuat)", anchor="w", justify="left"
        )
        self.lbl_keys.pack(fill="x", padx=8)

        frm_plain = tk.Frame(root, padx=8, pady=6)
        frm_plain.pack(fill="x")

        tk.Label(frm_plain, text="Plaintext:").pack(side="left")
        self.entry_plain = tk.Entry(frm_plain, width=60)
        self.entry_plain.pack(side="left", padx=6)

        tk.Button(frm_plain, text="Encrypt →", command=self.encrypt).pack(
            side="left", padx=6
        )

        frm_cipher = tk.Frame(root, padx=8, pady=6)
        frm_cipher.pack(fill="x")

        tk.Label(frm_cipher, text="Ciphertext:").pack(side="left")
        self.entry_cipher = tk.Entry(frm_cipher, width=60)
        self.entry_cipher.pack(side="left", padx=6)

        tk.Button(frm_cipher, text="← Decrypt", command=self.decrypt).pack(
            side="left", padx=6
        )

        tk.Label(root, text="DEBUG:").pack(anchor="w", padx=8)

        self.debug_area = scrolledtext.ScrolledText(
            root, width=110, height=20, wrap="word"
        )
        self.debug_area.pack(padx=8, pady=6)

    def debug(self, msg):
        self.debug_area.insert(tk.END, msg + "\n")
        self.debug_area.see(tk.END)

    def clear_debug(self):
        self.debug_area.delete("1.0", tk.END)

    def generate_keys(self):
        self.clear_debug()
        self.engine.generate_keys(self.debug)
        self.lbl_keys.config(
            text=f"Public (e={self.engine.e}, n={self.engine.n})   |   Private (d={self.engine.d}, n={self.engine.n})"
        )

    def encrypt(self):
        text = self.entry_plain.get()
        if not text:
            messagebox.showinfo("Info", "Masukkan plaintext.")
            return

        cipher = self.engine.encrypt_message(text, self.debug)
        self.entry_cipher.delete(0, tk.END)
        self.entry_cipher.insert(tk.END, cipher)

    def decrypt(self):
        text = self.entry_cipher.get()
        if not text:
            messagebox.showinfo("Info", "Masukkan ciphertext.")
            return

        plain = self.engine.decrypt_message(text, self.debug)
        self.entry_plain.delete(0, tk.END)
        self.entry_plain.insert(0, plain)


# ------------------------------
# RUN APP
# ------------------------------
root = tk.Tk()
app = RSAApp(root)
root.mainloop()
