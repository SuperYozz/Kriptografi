import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import math
import time

class ElGamalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ElGamal Cryptography Suite")
        self.root.geometry("1100x800")
        self.root.configure(bg='#2c3e50')
        
        # Variabel untuk kunci
        self.p = tk.IntVar()
        self.g = tk.IntVar()
        self.x = tk.IntVar()
        self.y = tk.IntVar()
        
        # Daftar bilangan prima untuk demo
        self.primes = [
            101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
            151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
            199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
            263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
            317, 331, 337, 347, 349, 353, 359, 367, 373, 379,
            383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
            443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
            503, 509, 521, 523, 541, 547, 557, 563, 569, 571,
            577, 587, 593, 599, 601, 607, 613, 617, 619, 631,
            641, 643, 647, 653, 659, 661, 673, 677, 683, 691
        ]
        
        # Setup UI
        self.setup_ui()
        
    def setup_ui(self):
        # Judul
        title_frame = tk.Frame(self.root, bg='#2c3e50')
        title_frame.pack(pady=10)
        
        title_label = tk.Label(
            title_frame, 
            text="🔐 ElGamal Cryptography Suite", 
            font=("Arial", 24, "bold"), 
            fg="#ecf0f1", 
            bg="#2c3e50"
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame, 
            text="Key Generation, Encryption, and Decryption with Detailed Calculation Process", 
            font=("Arial", 12), 
            fg="#bdc3c7", 
            bg="#2c3e50"
        )
        subtitle_label.pack()
        
        # Notebook untuk tab
        notebook = ttk.Notebook(self.root)
        notebook.pack(pady=10, padx=10, fill='both', expand=True)
        
        # Tab 1: Key Generation
        key_frame = tk.Frame(notebook, bg='#34495e')
        notebook.add(key_frame, text='🔑 Key Generation')
        
        # Tab 2: Encryption
        encrypt_frame = tk.Frame(notebook, bg='#34495e')
        notebook.add(encrypt_frame, text='🔒 Encryption')
        
        # Tab 3: Decryption
        decrypt_frame = tk.Frame(notebook, bg='#34495e')
        notebook.add(decrypt_frame, text='🔓 Decryption')
        
        # Tab 4: Explanation
        explain_frame = tk.Frame(notebook, bg='#34495e')
        notebook.add(explain_frame, text='📚 Explanation')
        
        # Build each tab
        self.build_key_generation_tab(key_frame)
        self.build_encryption_tab(encrypt_frame)
        self.build_decryption_tab(decrypt_frame)
        self.build_explanation_tab(explain_frame)
        
    def build_key_generation_tab(self, parent):
        # Input frame
        input_frame = tk.Frame(parent, bg='#34495e')
        input_frame.pack(pady=20, padx=20, fill='x')
        
        # Prime number p
        tk.Label(input_frame, text="Prime Number (p):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=0, column=0, sticky='w', pady=5)
        
        p_entry = tk.Entry(input_frame, textvariable=self.p, font=("Arial", 11), width=30)
        p_entry.grid(row=0, column=1, pady=5, padx=10)
        
        # Button untuk generate prime
        tk.Button(input_frame, text="Generate Prime", command=self.generate_prime,
                 bg="#3498db", fg="white", font=("Arial", 10)).grid(row=0, column=2, pady=5, padx=5)
        
        # Generator g
        tk.Label(input_frame, text="Generator (g):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=1, column=0, sticky='w', pady=5)
        
        g_entry = tk.Entry(input_frame, textvariable=self.g, font=("Arial", 11), width=30)
        g_entry.grid(row=1, column=1, pady=5, padx=10)
        
        # Button untuk generate g
        tk.Button(input_frame, text="Find Generator", command=self.find_generator_button,
                 bg="#3498db", fg="white", font=("Arial", 10)).grid(row=1, column=2, pady=5, padx=5)
        
        # Private key x
        tk.Label(input_frame, text="Private Key (x):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=2, column=0, sticky='w', pady=5)
        
        x_entry = tk.Entry(input_frame, textvariable=self.x, font=("Arial", 11), width=30)
        x_entry.grid(row=2, column=1, pady=5, padx=10)
        
        # Button untuk generate private key
        tk.Button(input_frame, text="Generate Private Key", command=self.generate_private_key,
                 bg="#3498db", fg="white", font=("Arial", 10)).grid(row=2, column=2, pady=5, padx=5)
        
        # Button untuk generate keys
        generate_button = tk.Button(input_frame, text="Generate All Keys", command=self.generate_keys,
                                   bg="#2ecc71", fg="white", font=("Arial", 11, "bold"), width=20)
        generate_button.grid(row=3, column=0, columnspan=3, pady=20)
        
        # Info label
        info_label = tk.Label(input_frame, 
                             text="Note: p harus bilangan prima, g adalah generator dari Zp* (harus < p), x adalah bilangan acak antara 1 dan p-1",
                             font=("Arial", 9), fg="#f1c40f", bg="#34495e", wraplength=400, justify='left')
        info_label.grid(row=4, column=0, columnspan=3, pady=10)
        
        # Output frame
        output_frame = tk.LabelFrame(parent, text="Generated Keys", font=("Arial", 12, "bold"),
                                    fg="#ecf0f1", bg="#34495e", relief=tk.RIDGE)
        output_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Public key display
        tk.Label(output_frame, text="Public Key (p, g, y):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").pack(anchor='w', pady=(10, 5), padx=10)
        
        self.public_key_display = tk.Text(output_frame, height=2, font=("Consolas", 10), width=80)
        self.public_key_display.pack(padx=10, pady=(0, 10))
        
        # Private key display
        tk.Label(output_frame, text="Private Key (x):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").pack(anchor='w', pady=(10, 5), padx=10)
        
        self.private_key_display = tk.Text(output_frame, height=2, font=("Consolas", 10), width=80)
        self.private_key_display.pack(padx=10, pady=(0, 10))
        
        # Calculation process for key generation
        calc_frame = tk.LabelFrame(parent, text="Key Generation Calculation Process", font=("Arial", 12, "bold"),
                                  fg="#ecf0f1", bg="#34495e", relief=tk.RIDGE)
        calc_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        self.key_calc_display = scrolledtext.ScrolledText(calc_frame, height=8, font=("Consolas", 9), width=80, bg='#2c3e50', fg='#ecf0f1')
        self.key_calc_display.pack(padx=10, pady=10, fill='both', expand=True)
        
    def build_encryption_tab(self, parent):
        # Create a paned window for better layout
        paned = tk.PanedWindow(parent, orient=tk.HORIZONTAL, bg='#34495e')
        paned.pack(fill='both', expand=True, pady=5, padx=5)
        
        # Left panel for inputs
        left_panel = tk.Frame(paned, bg='#34495e')
        paned.add(left_panel, width=400)
        
        # Right panel for calculation process
        right_panel = tk.Frame(paned, bg='#34495e')
        paned.add(right_panel)
        
        # Input frame in left panel
        input_frame = tk.LabelFrame(left_panel, text="Encryption Input", font=("Arial", 12, "bold"),
                                   fg="#ecf0f1", bg="#34495e", relief=tk.RIDGE)
        input_frame.pack(pady=10, padx=10, fill='both', expand=True)
        
        # Message input
        tk.Label(input_frame, text="Message to Encrypt:", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=0, column=0, sticky='w', pady=5)
        
        self.message_entry = tk.Text(input_frame, height=3, font=("Arial", 11), width=40)
        self.message_entry.grid(row=0, column=1, pady=5, padx=10, columnspan=2)
        
        # Public key inputs
        tk.Label(input_frame, text="Public Key (p):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=1, column=0, sticky='w', pady=5)
        
        self.encrypt_p_entry = tk.Entry(input_frame, font=("Arial", 11), width=25)
        self.encrypt_p_entry.grid(row=1, column=1, pady=5, padx=10)
        
        tk.Label(input_frame, text="Public Key (g):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=2, column=0, sticky='w', pady=5)
        
        self.encrypt_g_entry = tk.Entry(input_frame, font=("Arial", 11), width=25)
        self.encrypt_g_entry.grid(row=2, column=1, pady=5, padx=10)
        
        tk.Label(input_frame, text="Public Key (y):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=3, column=0, sticky='w', pady=5)
        
        self.encrypt_y_entry = tk.Entry(input_frame, font=("Arial", 11), width=25)
        self.encrypt_y_entry.grid(row=3, column=1, pady=5, padx=10)
        
        # Random k value input
        tk.Label(input_frame, text="Random k (1 ≤ k ≤ p-2):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=4, column=0, sticky='w', pady=5)
        
        k_frame = tk.Frame(input_frame, bg='#34495e')
        k_frame.grid(row=4, column=1, pady=5, padx=10, sticky='w')
        
        self.encrypt_k_entry = tk.Entry(k_frame, font=("Arial", 11), width=15)
        self.encrypt_k_entry.pack(side='left', padx=(0, 10))
        
        # Button untuk generate k
        tk.Button(k_frame, text="Generate k", command=self.generate_random_k,
                 bg="#9b59b6", fg="white", font=("Arial", 9)).pack(side='left')
        
        # Button untuk encrypt
        encrypt_button = tk.Button(input_frame, text="Encrypt Message", command=self.encrypt_message,
                                  bg="#2ecc71", fg="white", font=("Arial", 11, "bold"), width=20)
        encrypt_button.grid(row=5, column=0, columnspan=3, pady=20)
        
        # Ciphertext output in left panel
        cipher_frame = tk.LabelFrame(left_panel, text="Ciphertext Output", font=("Arial", 12, "bold"),
                                    fg="#ecf0f1", bg="#34495e", relief=tk.RIDGE)
        cipher_frame.pack(pady=10, padx=10, fill='both', expand=True)
        
        # Ciphertext display
        tk.Label(cipher_frame, text="Ciphertext (c1, c2 pairs):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").pack(anchor='w', pady=(10, 5), padx=10)
        
        self.ciphertext_display = scrolledtext.ScrolledText(cipher_frame, height=6, font=("Consolas", 10), width=80, bg='#2c3e50', fg='#ecf0f1')
        self.ciphertext_display.pack(padx=10, pady=(0, 10), fill='both', expand=True)
        
        # Calculation process in right panel
        calc_frame = tk.LabelFrame(right_panel, text="Encryption Calculation Process (Step by Step)", font=("Arial", 12, "bold"),
                                  fg="#ecf0f1", bg="#34495e", relief=tk.RIDGE)
        calc_frame.pack(pady=10, padx=10, fill='both', expand=True)
        
        self.encrypt_calc_display = scrolledtext.ScrolledText(calc_frame, height=30, font=("Consolas", 9), width=80, bg='#2c3e50', fg='#ecf0f1')
        self.encrypt_calc_display.pack(padx=10, pady=10, fill='both', expand=True)
        
    def build_decryption_tab(self, parent):
        # Create a paned window for better layout
        paned = tk.PanedWindow(parent, orient=tk.HORIZONTAL, bg='#34495e')
        paned.pack(fill='both', expand=True, pady=5, padx=5)
        
        # Left panel for inputs
        left_panel = tk.Frame(paned, bg='#34495e')
        paned.add(left_panel, width=400)
        
        # Right panel for calculation process
        right_panel = tk.Frame(paned, bg='#34495e')
        paned.add(right_panel)
        
        # Input frame in left panel
        input_frame = tk.LabelFrame(left_panel, text="Decryption Input", font=("Arial", 12, "bold"),
                                   fg="#ecf0f1", bg="#34495e", relief=tk.RIDGE)
        input_frame.pack(pady=10, padx=10, fill='both', expand=True)
        
        # Ciphertext input
        tk.Label(input_frame, text="Ciphertext (c1, c2 pairs):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=0, column=0, sticky='w', pady=5)
        
        self.ciphertext_entry = tk.Text(input_frame, height=3, font=("Arial", 11), width=40)
        self.ciphertext_entry.grid(row=0, column=1, pady=5, padx=10, columnspan=2)
        
        # Private key input
        tk.Label(input_frame, text="Private Key (x):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=1, column=0, sticky='w', pady=5)
        
        self.decrypt_x_entry = tk.Entry(input_frame, font=("Arial", 11), width=25)
        self.decrypt_x_entry.grid(row=1, column=1, pady=5, padx=10)
        
        # Prime p input
        tk.Label(input_frame, text="Prime Number (p):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=2, column=0, sticky='w', pady=5)
        
        self.decrypt_p_entry = tk.Entry(input_frame, font=("Arial", 11), width=25)
        self.decrypt_p_entry.grid(row=2, column=1, pady=5, padx=10)
        
        # Button untuk decrypt
        decrypt_button = tk.Button(input_frame, text="Decrypt Message", command=self.decrypt_message,
                                  bg="#2ecc71", fg="white", font=("Arial", 11, "bold"), width=20)
        decrypt_button.grid(row=3, column=0, columnspan=3, pady=20)
        
        # Decrypted output in left panel
        output_frame = tk.LabelFrame(left_panel, text="Decrypted Message", font=("Arial", 12, "bold"),
                                    fg="#ecf0f1", bg="#34495e", relief=tk.RIDGE)
        output_frame.pack(pady=10, padx=10, fill='both', expand=True)
        
        # Decrypted message display
        tk.Label(output_frame, text="Decrypted Message:", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").pack(anchor='w', pady=(10, 5), padx=10)
        
        self.decrypted_display = scrolledtext.ScrolledText(output_frame, height=6, font=("Consolas", 10), width=80, bg='#2c3e50', fg='#ecf0f1')
        self.decrypted_display.pack(padx=10, pady=(0, 10), fill='both', expand=True)
        
        # Calculation process in right panel
        calc_frame = tk.LabelFrame(right_panel, text="Decryption Calculation Process (Step by Step)", font=("Arial", 12, "bold"),
                                  fg="#ecf0f1", bg="#34495e", relief=tk.RIDGE)
        calc_frame.pack(pady=10, padx=10, fill='both', expand=True)
        
        self.decrypt_calc_display = scrolledtext.ScrolledText(calc_frame, height=30, font=("Consolas", 9), width=80, bg='#2c3e50', fg='#ecf0f1')
        self.decrypt_calc_display.pack(padx=10, pady=10, fill='both', expand=True)
        
    def build_explanation_tab(self, parent):
        # Explanation text
        explanation = """
ELGAMAL CRYPTOGRAPHY ALGORITHM - DETAILED CALCULATION PROCESS

ElGamal adalah sistem kriptografi asimetris yang dibuat oleh Taher Elgamal pada tahun 1985.
Algoritma ini didasarkan pada pertukaran kunci Diffie-Hellman.

PROSES DETAIL:

1. KEY GENERATION:
   - Pilih bilangan prima p yang besar
   - Pilih generator g dari grup siklik Zp* (g < p)
   - Pilih kunci privat x (1 < x < p-1)
   - Hitung kunci publik y = g^x mod p
   - Kunci publik: (p, g, y)
   - Kunci privat: x

   Contoh Perhitungan:
     Misal p = 23, g = 5, x = 6
     y = g^x mod p = 5^6 mod 23
     5^2 = 25 mod 23 = 2
     5^4 = (5^2)^2 = 2^2 mod 23 = 4
     5^6 = 5^4 * 5^2 = 4 * 2 mod 23 = 8
     Jadi y = 8

2. ENCRYPTION (Per Karakter):
   - Konversi karakter ke ASCII: m = ord(char)
   - Pilih k acak dengan syarat 1 ≤ k ≤ p-2
   - Hitung c1 = g^k mod p
   - Hitung c2 = m * y^k mod p
   - Ciphertext adalah pasangan (c1, c2)

   Contoh Perhitungan (lanjutan contoh di atas):
     Misal karakter 'A' dengan ASCII 65, k = 3
     c1 = g^k mod p = 5^3 mod 23 = 125 mod 23 = 10
     c2 = m * y^k mod p = 65 * 8^3 mod 23
     8^2 = 64 mod 23 = 18
     8^3 = 8^2 * 8 = 18 * 8 mod 23 = 144 mod 23 = 6
     c2 = 65 * 6 mod 23 = 390 mod 23 = 22
     Ciphertext: (10, 22)

3. DECRYPTION (Per Pasangan Ciphertext):
   - Hitung s = c1^x mod p
   - Hitung invers modular s_inv dari s mod p
   - Hitung m = c2 * s_inv mod p
   - Konversi m kembali ke karakter: char = chr(m)

   Contoh Perhitungan (lanjutan):
     Dengan ciphertext (10, 22), x = 6, p = 23
     s = c1^x mod p = 10^6 mod 23
     10^2 = 100 mod 23 = 8
     10^4 = (10^2)^2 = 8^2 mod 23 = 64 mod 23 = 18
     10^6 = 10^4 * 10^2 = 18 * 8 mod 23 = 144 mod 23 = 6
     
     Cari s_inv: s_inv * 6 ≡ 1 mod 23
     Karena 4 * 6 = 24 ≡ 1 mod 23, maka s_inv = 4
     
     m = c2 * s_inv mod p = 22 * 4 mod 23 = 88 mod 23 = 19
     ASCII 19 bukan karakter yang dapat dicetak, contoh ini hanya ilustrasi.

PERHATIAN:
- Program ini menampilkan proses perhitungan detail untuk setiap karakter
- Pada tab Encryption dan Decryption, lihat panel kanan untuk proses perhitungan
- Setiap langkah dijelaskan dengan rinci termasuk rumus dan hasil perhitungan

KEUNGGULAN:
- Keamanan bergantung pada kesulitan masalah logaritma diskrit
- Menggunakan kunci acak berbeda untuk setiap enkripsi
- Cocok untuk enkripsi dan tanda tangan digital

CATATAN:
- Program ini menggunakan bilangan prima yang telah ditentukan (tidak generate secara dinamis)
- Nilai generator dicari secara brute-force untuk prima kecil
- Untuk keamanan nyata, gunakan library kriptografi yang lebih komprehensif
"""
        
        text_widget = scrolledtext.ScrolledText(parent, height=30, font=("Arial", 11), width=80, bg='#2c3e50', fg='#ecf0f1')
        text_widget.pack(pady=20, padx=20, fill='both', expand=True)
        text_widget.insert(tk.END, explanation)
        text_widget.configure(state='disabled')
        
    def is_prime(self, n):
        """Check if a number is prime"""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
            
        # Check divisibility up to sqrt(n)
        limit = int(math.sqrt(n)) + 1
        for i in range(3, limit, 2):
            if n % i == 0:
                return False
        return True
    
    def generate_prime(self):
        """Generate a random prime number from predefined list"""
        prime = random.choice(self.primes)
        self.p.set(prime)
        
    def generate_private_key(self):
        """Generate a random private key"""
        p = self.p.get()
        if p > 2:
            x = random.randint(2, p - 2)
            self.x.set(x)
        else:
            messagebox.showwarning("Warning", "Please generate or enter a prime number first!")
    
    def generate_random_k(self):
        """Generate a random k value for encryption"""
        try:
            p_str = self.encrypt_p_entry.get()
            if not p_str:
                messagebox.showwarning("Warning", "Please enter prime p first!")
                return
                
            p = int(p_str)
            if p <= 2:
                messagebox.showerror("Error", "p must be > 2")
                return
                
            # Generate k with 1 ≤ k ≤ p-2
            k = random.randint(1, p - 2)
            self.encrypt_k_entry.delete(0, tk.END)
            self.encrypt_k_entry.insert(0, str(k))
            
            messagebox.showinfo("Random k Generated", f"Random k value generated: {k}\n\nk harus memenuhi: 1 ≤ k ≤ p-2\nk={k}, p={p}, p-2={p-2}")
            
        except ValueError:
            messagebox.showerror("Error", "Invalid p value. Please enter a valid prime number.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate k: {str(e)}")
    
    def find_generator_button(self):
        """Button handler untuk mencari generator"""
        p = self.p.get()
        if p <= 2:
            messagebox.showwarning("Warning", "Please enter a prime number first!")
            return
            
        g = self.find_generator(p)
        if g:
            self.g.set(g)
            messagebox.showinfo("Generator Found", f"Generator found: g = {g} (g < p = {p})")
        else:
            messagebox.showwarning("Warning", "Could not find a generator. Try a different prime.")
    
    def find_generator(self, p):
        """Find a generator for prime p (simple brute-force method)"""
        if p == 2:
            return 1
        
        # Factor p-1 (simplified for small primes)
        factors = []
        n = p - 1
        
        # Simple factorization
        temp = n
        i = 2
        while i * i <= temp:
            if temp % i == 0:
                factors.append(i)
                while temp % i == 0:
                    temp //= i
            i += 1
        if temp > 1:
            factors.append(temp)
        
        # Test potential generators (g harus < p)
        for g in range(2, min(p, 100)):  # Limit search for simplicity, dan g < p
            is_generator = True
            for q in factors:
                if pow(g, (p-1)//q, p) == 1:
                    is_generator = False
                    break
            if is_generator:
                return g
        
        # If no generator found in limited search, try common small generators (yang < p)
        common_generators = [2, 3, 5, 6, 7, 10]
        for g in common_generators:
            if g < p:  # Pastikan g < p
                is_generator = True
                for q in factors:
                    if pow(g, (p-1)//q, p) == 1:
                        is_generator = False
                        break
                if is_generator:
                    return g
        
        return None
    
    def generate_keys(self):
        """Generate ElGamal keys"""
        try:
            p = self.p.get()
            if p <= 1:
                messagebox.showerror("Error", "p must be a prime number > 1")
                return
                
            if not self.is_prime(p):
                messagebox.showerror("Error", "p must be a prime number!")
                return
            
            # Validasi g (jika diinput manual)
            g_input = self.g.get()
            if g_input != 0:  # Jika user telah menginput nilai g
                if g_input >= p:
                    messagebox.showerror("Error", f"Generator g must be less than prime p. g={g_input}, p={p}")
                    return
            
            # Find a generator g
            if g_input == 0:
                g = self.find_generator(p)
                if g is None:
                    messagebox.showerror("Error", "Could not find a generator for p. Try a different prime.")
                    return
                self.g.set(g)
            else:
                g = g_input
                # Validasi tambahan untuk generator
                if g >= p:
                    messagebox.showerror("Error", f"Generator g must be less than prime p. g={g}, p={p}")
                    return
                if g <= 1:
                    messagebox.showerror("Error", f"Generator g must be greater than 1. g={g}")
                    return
            
            # Validasi x (jika diinput manual)
            x_input = self.x.get()
            if x_input != 0:  # Jika user telah menginput nilai x
                if x_input >= p-1 or x_input <= 1:
                    messagebox.showerror("Error", f"Private key x must satisfy: 1 < x < p-1. x={x_input}, p={p}")
                    return
            
            # Generate private key if not set
            if x_input == 0:
                self.generate_private_key()
                
            x = self.x.get()
            
            # Validasi akhir untuk x
            if x >= p-1 or x <= 1:
                messagebox.showerror("Error", f"Private key x must satisfy: 1 < x < p-1. x={x}, p={p}")
                return
            
            # Calculate public key y = g^x mod p
            y = pow(g, x, p)
            self.y.set(y)
            
            # Display keys
            self.public_key_display.delete(1.0, tk.END)
            self.public_key_display.insert(tk.END, f"({p}, {g}, {y})")
            
            self.private_key_display.delete(1.0, tk.END)
            self.private_key_display.insert(tk.END, f"{x}")
            
            # Validasi tambahan: verifikasi bahwa g < p
            if g >= p:
                messagebox.showerror("Validation Error", f"CRITICAL: Generator g ({g}) must be less than p ({p})!")
                return
            
            # Display calculation process for key generation
            self.key_calc_display.delete(1.0, tk.END)
            calc_text = "=" * 70 + "\n"
            calc_text += "KEY GENERATION CALCULATION PROCESS\n"
            calc_text += "=" * 70 + "\n\n"
            calc_text += f"Step 1: Select prime number p = {p}\n"
            calc_text += f"Step 2: Find generator g = {g} (g < p ✓)\n"
            calc_text += f"Step 3: Select private key x = {x} (1 < x < p-1 ✓)\n"
            calc_text += f"Step 4: Calculate public key y = g^x mod p\n"
            calc_text += f"        y = {g}^{x} mod {p}\n"
            
            # Calculate step by step for demonstration
            if x <= 10:  # Only show detailed calculation for small x
                calc_text += f"        Calculation:\n"
                result = 1
                for i in range(1, x + 1):
                    result = (result * g) % p
                    calc_text += f"        {g}^{i} mod {p} = {result}\n"
            else:
                calc_text += f"        {g}^{x} mod {p} = {y}\n"
            
            calc_text += f"\nStep 5: Final Results:\n"
            calc_text += f"        Public Key: (p={p}, g={g}, y={y})\n"
            calc_text += f"        Private Key: x={x}\n"
            calc_text += "\n" + "=" * 70 + "\n"
            self.key_calc_display.insert(tk.END, calc_text)
            
            # Copy to encryption tab
            self.encrypt_p_entry.delete(0, tk.END)
            self.encrypt_p_entry.insert(0, str(p))
            self.encrypt_g_entry.delete(0, tk.END)
            self.encrypt_g_entry.insert(0, str(g))
            self.encrypt_y_entry.delete(0, tk.END)
            self.encrypt_y_entry.insert(0, str(y))
            
            # Copy to decryption tab
            self.decrypt_x_entry.delete(0, tk.END)
            self.decrypt_x_entry.insert(0, str(x))
            self.decrypt_p_entry.delete(0, tk.END)
            self.decrypt_p_entry.insert(0, str(p))
            
            # Tampilkan pesan sukses
            messagebox.showinfo("Success", f"Keys generated successfully!\n\nPublic Key: (p={p}, g={g}, y={y})\nPrivate Key: x={x}\n\nNote: g ({g}) < p ({p}) is satisfied.")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate keys: {str(e)}")
    
    def encrypt_message(self):
        """Encrypt a message using ElGamal with detailed calculation display"""
        try:
            # Clear calculation display
            self.encrypt_calc_display.delete(1.0, tk.END)
            
            # Get inputs
            message = self.message_entry.get(1.0, tk.END).strip()
            if not message:
                messagebox.showwarning("Warning", "Please enter a message to encrypt!")
                return
            
            # Validasi input kunci publik
            try:
                p = int(self.encrypt_p_entry.get())
                g = int(self.encrypt_g_entry.get())
                y = int(self.encrypt_y_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid public key values! Please enter numeric values.")
                return
            
            # Validasi dasar
            if p <= 1:
                messagebox.showerror("Error", "p must be a prime number > 1")
                return
            
            if not self.is_prime(p):
                messagebox.showerror("Error", "p must be a prime number!")
                return
            
            # Validasi penting: g harus < p
            if g >= p:
                messagebox.showerror("Error", f"Generator g must be less than prime p. g={g}, p={p}")
                return
            
            if g <= 1:
                messagebox.showerror("Error", f"Generator g must be greater than 1. g={g}")
                return
            
            if y <= 0:
                messagebox.showerror("Error", "Invalid public key y value!")
                return
            
            # Get k value
            k_str = self.encrypt_k_entry.get()
            if not k_str:
                messagebox.showerror("Error", "Please enter k value! k must satisfy 1 ≤ k ≤ p-2.\nClick 'Generate Random k' or enter manually.")
                return
            
            try:
                k = int(k_str)
            except ValueError:
                messagebox.showerror("Error", "k must be an integer!")
                return
            
            # Validasi k: 1 ≤ k ≤ p-2
            if k < 1 or k > p-2:
                messagebox.showerror("Error", f"k must satisfy 1 ≤ k ≤ p-2.\nk={k}, p={p}, p-2={p-2}")
                return
            
            # Validasi: pesan harus dapat dikonversi ke angka
            message_nums = [ord(char) for char in message]
            
            # Validasi: nilai ASCII harus < p (untuk memastikan enkripsi bekerja dengan benar)
            for i, m in enumerate(message_nums):
                if m >= p:
                    char = message[i]
                    messagebox.showerror("Error", 
                        f"Character '{char}' (ASCII={m}) has value >= p={p}.\n"
                        f"This may cause issues with encryption.\n"
                        f"Please use a larger prime p or remove character '{char}'.")
                    return
            
            # Validasi: pesan tidak boleh terlalu panjang (untuk demo)
            if len(message) > 100:
                messagebox.showwarning("Warning", "Message is too long for demo purposes. Truncating to 100 characters.")
                message = message[:100]
                message_nums = [ord(char) for char in message]
            
            # Display calculation header
            calc_text = "=" * 70 + "\n"
            calc_text += "ENCRYPTION CALCULATION PROCESS (Step by Step)\n"
            calc_text += "=" * 70 + "\n\n"
            calc_text += f"Encryption Parameters:\n"
            calc_text += f"  Prime p = {p}\n"
            calc_text += f"  Generator g = {g}\n"
            calc_text += f"  Public key y = {y}\n"
            calc_text += f"  Random k = {k} (1 ≤ {k} ≤ {p}-2 ✓)\n"
            calc_text += f"  Message: '{message}' (Length: {len(message)} characters)\n\n"
            calc_text += "=" * 70 + "\n"
            
            # Calculate y^k mod p once since it's the same for all characters
            y_power_k = pow(y, k, p)
            
            # Encrypt each character
            ciphertext = []
            for idx, (char, m) in enumerate(zip(message, message_nums)):
                calc_text += f"\nCharacter {idx+1}: '{char}' (ASCII = {m})\n"
                calc_text += "-" * 40 + "\n"
                
                # Calculate c1 = g^k mod p
                c1 = pow(g, k, p)
                calc_text += f"Step 1: Calculate c1 = g^k mod p\n"
                calc_text += f"        c1 = {g}^{k} mod {p}\n"
                
                # Show step-by-step calculation for small k
                if k <= 10:
                    result = 1
                    for i in range(1, k + 1):
                        result = (result * g) % p
                        calc_text += f"        {g}^{i} mod {p} = {result}\n"
                calc_text += f"        c1 = {c1}\n\n"
                
                # Calculate c2 = m * y^k mod p
                c2 = (m * y_power_k) % p
                calc_text += f"Step 2: Calculate c2 = m * y^k mod p\n"
                calc_text += f"        First calculate y^k mod p:\n"
                
                # Show step-by-step calculation for y^k if k is small
                if k <= 10:
                    y_result = 1
                    for i in range(1, k + 1):
                        y_result = (y_result * y) % p
                        calc_text += f"        {y}^{i} mod {p} = {y_result}\n"
                    calc_text += f"        So y^k mod p = {y_power_k}\n\n"
                else:
                    calc_text += f"        {y}^{k} mod {p} = {y_power_k}\n\n"
                
                calc_text += f"        Now calculate c2 = m * (y^k mod p) mod p\n"
                calc_text += f"        c2 = {m} * {y_power_k} mod {p}\n"
                calc_text += f"        {m} * {y_power_k} = {m * y_power_k}\n"
                calc_text += f"        {m * y_power_k} mod {p} = {c2}\n\n"
                
                calc_text += f"Step 3: Ciphertext for character '{char}': (c1, c2) = ({c1}, {c2})\n"
                calc_text += "-" * 40 + "\n"
                
                ciphertext.append((c1, c2))
            
            # Update calculation display
            self.encrypt_calc_display.insert(tk.END, calc_text)
            
            # Display ciphertext
            self.ciphertext_display.delete(1.0, tk.END)
            ciphertext_str = " ".join([f"({c1},{c2})" for c1, c2 in ciphertext])
            self.ciphertext_display.insert(tk.END, ciphertext_str)
            
            # Copy to decryption tab
            self.ciphertext_entry.delete(1.0, tk.END)
            self.ciphertext_entry.insert(tk.END, ciphertext_str)
            
            # Tampilkan info
            messagebox.showinfo("Encryption Successful", 
                f"Message encrypted successfully!\n\n"
                f"Original message length: {len(message)} characters\n"
                f"Using prime p={p}, generator g={g} (g < p ✓)\n"
                f"Using k={k} (1 ≤ {k} ≤ {p}-2 ✓)\n"
                f"Generated {len(ciphertext)} ciphertext pairs\n\n"
                f"IMPORTANT: k should be random and different for each encryption in real applications!")
            
        except Exception as e:
            # Tampilkan pesan error yang lebih informatif
            error_msg = str(e)
            if "k" in error_msg.lower():
                error_msg += "\n\nPlease check k value: must satisfy 1 ≤ k ≤ p-2"
            elif "g" in error_msg.lower():
                error_msg += "\n\nPlease check g value: must be less than p"
            elif "p" in error_msg.lower():
                error_msg += "\n\nPlease check p value: must be a prime number"
            
            messagebox.showerror("Encryption Error", f"Encryption failed: {error_msg}")
    
    def mod_inverse(self, a, m):
        """Calculate modular inverse using Extended Euclidean Algorithm"""
        def egcd(a, b):
            if b == 0:
                return (1, 0, a)
            else:
                x, y, g = egcd(b, a % b)
                return (y, x - (a // b) * y, g)
        
        x, y, g = egcd(a, m)
        if g != 1:
            raise Exception('Modular inverse does not exist')
        else:
            return x % m
    
    def decrypt_message(self):
        """Decrypt ciphertext using ElGamal with detailed calculation display"""
        try:
            # Clear calculation display
            self.decrypt_calc_display.delete(1.0, tk.END)
            
            # Get inputs
            ciphertext_str = self.ciphertext_entry.get(1.0, tk.END).strip()
            if not ciphertext_str:
                messagebox.showwarning("Warning", "Please enter ciphertext to decrypt!")
                return
            
            try:
                x = int(self.decrypt_x_entry.get())
                p = int(self.decrypt_p_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid key values! Please enter numeric values.")
                return
            
            # Validasi dasar
            if x <= 0 or p <= 1:
                messagebox.showerror("Error", "Invalid private key or prime number!")
                return
            
            if not self.is_prime(p):
                messagebox.showerror("Error", "p must be a prime number!")
                return
            
            # Validasi: x harus 1 < x < p-1
            if x >= p-1 or x <= 1:
                messagebox.showerror("Error", f"Private key x must satisfy: 1 < x < p-1. x={x}, p={p}")
                return
            
            # Parse ciphertext
            ciphertext_pairs = []
            # Remove parentheses and split
            clean_str = ciphertext_str.replace("(", "").replace(")", "")
            pairs = clean_str.split()
            
            for pair in pairs:
                if "," in pair:
                    c1_str, c2_str = pair.split(",")
                    try:
                        c1 = int(c1_str)
                        c2 = int(c2_str)
                        # Validasi: c1 dan c2 harus < p
                        if c1 >= p or c2 >= p:
                            messagebox.showerror("Error", 
                                f"Ciphertext values must be less than p={p}. Found c1={c1}, c2={c2}")
                            return
                        ciphertext_pairs.append((c1, c2))
                    except ValueError:
                        messagebox.showerror("Error", f"Invalid ciphertext pair: {pair}")
                        return
            
            if not ciphertext_pairs:
                messagebox.showerror("Error", "No valid ciphertext pairs found!")
                return
            
            # Display calculation header
            calc_text = "=" * 70 + "\n"
            calc_text += "DECRYPTION CALCULATION PROCESS (Step by Step)\n"
            calc_text += "=" * 70 + "\n\n"
            calc_text += f"Decryption Parameters:\n"
            calc_text += f"  Prime p = {p}\n"
            calc_text += f"  Private key x = {x} (1 < {x} < {p}-1 ✓)\n"
            calc_text += f"  Number of ciphertext pairs: {len(ciphertext_pairs)}\n\n"
            calc_text += "=" * 70 + "\n"
            
            # Decrypt each pair
            decrypted_nums = []
            for idx, (c1, c2) in enumerate(ciphertext_pairs):
                calc_text += f"\nCiphertext pair {idx+1}: (c1, c2) = ({c1}, {c2})\n"
                calc_text += "-" * 40 + "\n"
                
                try:
                    # Calculate s = c1^x mod p
                    calc_text += f"Step 1: Calculate s = c1^x mod p\n"
                    calc_text += f"        s = {c1}^{x} mod {p}\n"
                    
                    s = pow(c1, x, p)
                    
                    # Show step-by-step calculation for small x
                    if x <= 10:
                        result = 1
                        for i in range(1, x + 1):
                            result = (result * c1) % p
                            calc_text += f"        {c1}^{i} mod {p} = {result}\n"
                    
                    calc_text += f"        s = {s}\n\n"
                    
                    # Find modular inverse of s mod p
                    calc_text += f"Step 2: Find modular inverse s_inv of s mod p\n"
                    calc_text += f"        Find s_inv such that: {s} * s_inv ≡ 1 mod {p}\n"
                    
                    try:
                        s_inv = self.mod_inverse(s, p)
                        calc_text += f"        Testing values:\n"
                        
                        # Try to find inverse by brute force for display (only for small p)
                        found = False
                        if p < 100:
                            for i in range(1, p):
                                if (s * i) % p == 1:
                                    calc_text += f"        {s} * {i} mod {p} = {(s * i) % p}"
                                    if i == s_inv:
                                        calc_text += f" ✓ (Found! s_inv = {i})\n"
                                    else:
                                        calc_text += f"\n"
                                    if i == s_inv:
                                        found = True
                                        break
                            
                            if not found:
                                calc_text += f"        Using Extended Euclidean Algorithm: s_inv = {s_inv}\n"
                        else:
                            calc_text += f"        Using Extended Euclidean Algorithm: s_inv = {s_inv}\n"
                        
                        calc_text += f"        s_inv = {s_inv}\n\n"
                        
                    except:
                        calc_text += f"        ERROR: Cannot find modular inverse for {s} mod {p}\n"
                        calc_text += f"        This might indicate invalid keys or corrupted ciphertext.\n"
                        messagebox.showerror("Error", 
                            f"Cannot find modular inverse for s={s} mod p={p}.\n"
                            f"This might indicate invalid keys or corrupted ciphertext.")
                        return
                    
                    # Calculate m = c2 * s_inv mod p
                    calc_text += f"Step 3: Calculate m = c2 * s_inv mod p\n"
                    calc_text += f"        m = {c2} * {s_inv} mod {p}\n"
                    calc_text += f"        {c2} * {s_inv} = {c2 * s_inv}\n"
                    
                    m = (c2 * s_inv) % p
                    calc_text += f"        {c2 * s_inv} mod {p} = {m}\n\n"
                    
                    # Check if m is valid ASCII
                    calc_text += f"Step 4: Convert m to character\n"
                    calc_text += f"        m = {m}\n"
                    
                    if 0 <= m <= 255:
                        char = chr(m)
                        calc_text += f"        Character with ASCII {m} = '{char}'\n"
                    else:
                        char = '?'
                        calc_text += f"        WARNING: {m} is outside ASCII range (0-255)\n"
                        calc_text += f"        Using placeholder '?'\n"
                    
                    calc_text += f"\nDecrypted character {idx+1}: '{char}'\n"
                    calc_text += "-" * 40 + "\n"
                    
                    decrypted_nums.append(m)
                    
                except Exception as e:
                    calc_text += f"\nERROR decrypting pair {idx+1}: {str(e)}\n"
                    calc_text += "-" * 40 + "\n"
                    messagebox.showerror("Error", f"Error decrypting pair {idx+1}: {str(e)}")
                    return
            
            # Update calculation display
            self.decrypt_calc_display.insert(tk.END, calc_text)
            
            # Convert numbers back to characters
            try:
                decrypted_message = "".join([chr(num) for num in decrypted_nums])
            except ValueError:
                # Jika ada nilai di luar range ASCII, gunakan placeholder
                decrypted_message = "".join([chr(num) if 0 <= num <= 255 else '?' for num in decrypted_nums])
                messagebox.showwarning("Warning", 
                    "Some decrypted values are outside ASCII range. Non-ASCII characters replaced with '?'.")
            
            # Display decrypted message
            self.decrypted_display.delete(1.0, tk.END)
            self.decrypted_display.insert(tk.END, decrypted_message)
            
            # Tampilkan info
            messagebox.showinfo("Decryption Successful", 
                f"Message decrypted successfully!\n\n"
                f"Decrypted {len(decrypted_nums)} characters\n"
                f"Using private key x={x} (1 < {x} < {p}-1 ✓)\n\n"
                f"See right panel for detailed calculation process.")
            
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")
    
    def run(self):
        self.root.mainloop()

def main():
    root = tk.Tk()
    app = ElGamalGUI(root)
    app.run()

if __name__ == "__main__":
    main()