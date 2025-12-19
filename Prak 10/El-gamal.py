import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import math

class ElGamalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ElGamal Cryptography Suite")
        self.root.geometry("900x700")
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
            text="Key Generation, Encryption, and Decryption", 
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
                             text="Note: p harus bilangan prima, g adalah generator dari Zp*, x adalah bilangan acak antara 1 dan p-1",
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
        
    def build_encryption_tab(self, parent):
        # Input frame
        input_frame = tk.Frame(parent, bg='#34495e')
        input_frame.pack(pady=20, padx=20, fill='x')
        
        # Message input
        tk.Label(input_frame, text="Message to Encrypt:", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=0, column=0, sticky='w', pady=5)
        
        self.message_entry = tk.Text(input_frame, height=3, font=("Arial", 11), width=50)
        self.message_entry.grid(row=0, column=1, pady=5, padx=10, columnspan=2)
        
        # Public key inputs
        tk.Label(input_frame, text="Public Key (p):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=1, column=0, sticky='w', pady=5)
        
        self.encrypt_p_entry = tk.Entry(input_frame, font=("Arial", 11), width=30)
        self.encrypt_p_entry.grid(row=1, column=1, pady=5, padx=10)
        
        tk.Label(input_frame, text="Public Key (g):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=2, column=0, sticky='w', pady=5)
        
        self.encrypt_g_entry = tk.Entry(input_frame, font=("Arial", 11), width=30)
        self.encrypt_g_entry.grid(row=2, column=1, pady=5, padx=10)
        
        tk.Label(input_frame, text="Public Key (y):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=3, column=0, sticky='w', pady=5)
        
        self.encrypt_y_entry = tk.Entry(input_frame, font=("Arial", 11), width=30)
        self.encrypt_y_entry.grid(row=3, column=1, pady=5, padx=10)
        
        # Button untuk encrypt
        encrypt_button = tk.Button(input_frame, text="Encrypt Message", command=self.encrypt_message,
                                  bg="#2ecc71", fg="white", font=("Arial", 11, "bold"), width=20)
        encrypt_button.grid(row=4, column=0, columnspan=3, pady=20)
        
        # Output frame
        output_frame = tk.LabelFrame(parent, text="Encryption Results", font=("Arial", 12, "bold"),
                                    fg="#ecf0f1", bg="#34495e", relief=tk.RIDGE)
        output_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Ciphertext display
        tk.Label(output_frame, text="Ciphertext (c1, c2 pairs):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").pack(anchor='w', pady=(10, 5), padx=10)
        
        self.ciphertext_display = scrolledtext.ScrolledText(output_frame, height=6, font=("Consolas", 10), width=80)
        self.ciphertext_display.pack(padx=10, pady=(0, 10))
        
    def build_decryption_tab(self, parent):
        # Input frame
        input_frame = tk.Frame(parent, bg='#34495e')
        input_frame.pack(pady=20, padx=20, fill='x')
        
        # Ciphertext input
        tk.Label(input_frame, text="Ciphertext (c1, c2 pairs):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=0, column=0, sticky='w', pady=5)
        
        self.ciphertext_entry = tk.Text(input_frame, height=3, font=("Arial", 11), width=50)
        self.ciphertext_entry.grid(row=0, column=1, pady=5, padx=10, columnspan=2)
        
        # Private key input
        tk.Label(input_frame, text="Private Key (x):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=1, column=0, sticky='w', pady=5)
        
        self.decrypt_x_entry = tk.Entry(input_frame, font=("Arial", 11), width=30)
        self.decrypt_x_entry.grid(row=1, column=1, pady=5, padx=10)
        
        # Prime p input
        tk.Label(input_frame, text="Prime Number (p):", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").grid(row=2, column=0, sticky='w', pady=5)
        
        self.decrypt_p_entry = tk.Entry(input_frame, font=("Arial", 11), width=30)
        self.decrypt_p_entry.grid(row=2, column=1, pady=5, padx=10)
        
        # Button untuk decrypt
        decrypt_button = tk.Button(input_frame, text="Decrypt Message", command=self.decrypt_message,
                                  bg="#2ecc71", fg="white", font=("Arial", 11, "bold"), width=20)
        decrypt_button.grid(row=3, column=0, columnspan=3, pady=20)
        
        # Output frame
        output_frame = tk.LabelFrame(parent, text="Decryption Results", font=("Arial", 12, "bold"),
                                    fg="#ecf0f1", bg="#34495e", relief=tk.RIDGE)
        output_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Decrypted message display
        tk.Label(output_frame, text="Decrypted Message:", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").pack(anchor='w', pady=(10, 5), padx=10)
        
        self.decrypted_display = scrolledtext.ScrolledText(output_frame, height=6, font=("Consolas", 10), width=80)
        self.decrypted_display.pack(padx=10, pady=(0, 10))
        
    def build_explanation_tab(self, parent):
        # Explanation text
        explanation = """
ELGAMAL CRYPTOGRAPHY ALGORITHM

ElGamal adalah sistem kriptografi asimetris yang dibuat oleh Taher Elgamal pada tahun 1985.
Algoritma ini didasarkan pada pertukaran kunci Diffie-Hellman.

PROSES:

1. KEY GENERATION:
   - Pilih bilangan prima p yang besar
   - Pilih generator g dari grup siklik Zp*
   - Pilih kunci privat x (1 < x < p-1)
   - Hitung kunci publik y = g^x mod p
   - Kunci publik: (p, g, y)
   - Kunci privat: x

2. ENCRYPTION:
   - Untuk setiap karakter m (dikonversi ke angka):
     - Pilih k acak (1 < k < p-1)
     - Hitung c1 = g^k mod p
     - Hitung c2 = m * y^k mod p
   - Ciphertext adalah pasangan (c1, c2) untuk setiap karakter

3. DECRYPTION:
   - Untuk setiap pasangan ciphertext (c1, c2):
     - Hitung s = c1^x mod p
     - Hitung invers modular s_inv dari s mod p
     - Hitung m = c2 * s_inv mod p
     - Konversi m kembali ke karakter

KEUNGGULAN:
- Keamanan bergantung pada kesulitan masalah logaritma diskrit
- Menggunakan kunci acak berbeda untuk setiap enkripsi
- Cocok untuk enkripsi dan tanda tangan digital

CATATAN PROGRAM INI:
- Program ini menggunakan bilangan prima yang telah ditentukan (tidak generate secara dinamis)
- Nilai generator dicari secara brute-force untuk prima kecil
- Untuk keamanan nyata, gunakan library kriptografi yang lebih komprehensif

CONTOH PENGGUNAAN:
1. Generate kunci di tab "Key Generation"
2. Enkripsi pesan di tab "Encryption"
3. Dekripsi ciphertext di tab "Decryption"
"""
        
        text_widget = scrolledtext.ScrolledText(parent, height=25, font=("Arial", 11), width=80, bg='#2c3e50', fg='#ecf0f1')
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
    
    def find_generator_button(self):
        """Button handler untuk mencari generator"""
        p = self.p.get()
        if p <= 2:
            messagebox.showwarning("Warning", "Please enter a prime number first!")
            return
            
        g = self.find_generator(p)
        if g:
            self.g.set(g)
            messagebox.showinfo("Generator Found", f"Generator found: g = {g}")
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
        
        # Test potential generators
        for g in range(2, min(p, 100)):  # Limit search for simplicity
            is_generator = True
            for q in factors:
                if pow(g, (p-1)//q, p) == 1:
                    is_generator = False
                    break
            if is_generator:
                return g
        
        # If no generator found in limited search, try common small generators
        common_generators = [2, 3, 5, 6, 7, 10]
        for g in common_generators:
            if g < p:
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
            
            # Find a generator g
            if self.g.get() == 0:
                g = self.find_generator(p)
                if g is None:
                    messagebox.showerror("Error", "Could not find a generator for p. Try a different prime.")
                    return
                self.g.set(g)
            else:
                g = self.g.get()
            
            # Generate private key if not set
            if self.x.get() == 0:
                self.generate_private_key()
                
            x = self.x.get()
            
            # Calculate public key y = g^x mod p
            y = pow(g, x, p)
            self.y.set(y)
            
            # Display keys
            self.public_key_display.delete(1.0, tk.END)
            self.public_key_display.insert(tk.END, f"({p}, {g}, {y})")
            
            self.private_key_display.delete(1.0, tk.END)
            self.private_key_display.insert(tk.END, f"{x}")
            
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
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate keys: {str(e)}")
    
    def encrypt_message(self):
        """Encrypt a message using ElGamal"""
        try:
            # Get inputs
            message = self.message_entry.get(1.0, tk.END).strip()
            if not message:
                messagebox.showwarning("Warning", "Please enter a message to encrypt!")
                return
                
            p = int(self.encrypt_p_entry.get())
            g = int(self.encrypt_g_entry.get())
            y = int(self.encrypt_y_entry.get())
            
            if p <= 1 or g <= 0 or y <= 0:
                messagebox.showerror("Error", "Invalid public key values!")
                return
            
            # Convert message to numbers
            message_nums = [ord(char) for char in message]
            
            # Encrypt each character
            ciphertext = []
            for m in message_nums:
                # Choose random k
                k = random.randint(2, p-2)
                
                # Calculate c1 and c2
                c1 = pow(g, k, p)
                c2 = (m * pow(y, k, p)) % p
                
                ciphertext.append((c1, c2))
            
            # Display ciphertext
            self.ciphertext_display.delete(1.0, tk.END)
            ciphertext_str = " ".join([f"({c1},{c2})" for c1, c2 in ciphertext])
            self.ciphertext_display.insert(tk.END, ciphertext_str)
            
            # Copy to decryption tab
            self.ciphertext_entry.delete(1.0, tk.END)
            self.ciphertext_entry.insert(tk.END, ciphertext_str)
            
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")
    
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
        """Decrypt ciphertext using ElGamal"""
        try:
            # Get inputs
            ciphertext_str = self.ciphertext_entry.get(1.0, tk.END).strip()
            if not ciphertext_str:
                messagebox.showwarning("Warning", "Please enter ciphertext to decrypt!")
                return
                
            x = int(self.decrypt_x_entry.get())
            p = int(self.decrypt_p_entry.get())
            
            if x <= 0 or p <= 1:
                messagebox.showerror("Error", "Invalid private key or prime number!")
                return
            
            # Parse ciphertext
            ciphertext_pairs = []
            # Remove parentheses and split
            clean_str = ciphertext_str.replace("(", "").replace(")", "")
            pairs = clean_str.split()
            
            for pair in pairs:
                if "," in pair:
                    c1_str, c2_str = pair.split(",")
                    ciphertext_pairs.append((int(c1_str), int(c2_str)))
            
            # Decrypt each pair
            decrypted_nums = []
            for c1, c2 in ciphertext_pairs:
                # Calculate s = c1^x mod p
                s = pow(c1, x, p)
                
                # Find modular inverse of s mod p
                try:
                    s_inv = self.mod_inverse(s, p)
                except:
                    messagebox.showerror("Error", "Cannot find modular inverse. Check your keys.")
                    return
                
                # Calculate m = c2 * s_inv mod p
                m = (c2 * s_inv) % p
                decrypted_nums.append(m)
            
            # Convert numbers back to characters
            decrypted_message = "".join([chr(num) for num in decrypted_nums])
            
            # Display decrypted message
            self.decrypted_display.delete(1.0, tk.END)
            self.decrypted_display.insert(tk.END, decrypted_message)
            
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