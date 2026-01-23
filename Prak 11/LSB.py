import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as patches
import os

class LSBSteganographyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LSB Steganography - Visual Learning Tool")
        self.root.geometry("1300x800")
        self.root.configure(bg='#2c3e50')
        
        self.original_image = None
        self.stego_image = None
        self.image_array = None
        self.message = ""
        
        # Setup style
        self.setup_styles()
        
        # Create GUI
        self.create_widgets()
        
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Colors
        self.bg_color = '#2c3e50'
        self.fg_color = '#ecf0f1'
        self.accent_color = '#3498db'
        self.secondary_color = '#1abc9c'
        
    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg=self.bg_color)
        header_frame.pack(fill=tk.X, padx=20, pady=10)
        
        title_label = tk.Label(
            header_frame, 
            text="🔐 LSB STEGANOGRAPHY VISUALIZER", 
            font=("Arial", 24, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            header_frame,
            text="Visual Learning Tool for Least Significant Bit Steganography",
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.accent_color
        )
        subtitle_label.pack()
        
        # Main container
        main_container = tk.Frame(self.root, bg=self.bg_color)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Left panel - Controls
        left_panel = tk.Frame(main_container, bg=self.bg_color)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 10))
        
        # Image selection frame
        selection_frame = self.create_frame(left_panel, "📁 Image Selection")
        selection_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.img_path_var = tk.StringVar()
        tk.Entry(selection_frame, textvariable=self.img_path_var, 
                font=("Arial", 10), state='readonly', width=30).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(selection_frame, text="Browse", 
                  command=self.load_image, style="Accent.TButton").pack(side=tk.LEFT, padx=5)
        
        ttk.Button(selection_frame, text="Show Original", 
                  command=self.show_original, style="Secondary.TButton").pack(side=tk.LEFT, padx=5)
        
        # Message input frame
        message_frame = self.create_frame(left_panel, "✉️ Secret Message")
        message_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.message_text = tk.Text(message_frame, height=5, width=40, 
                                   font=("Arial", 10), bg='#34495e', fg='white')
        self.message_text.pack(padx=10, pady=10)
        
        # Process buttons frame
        process_frame = self.create_frame(left_panel, "⚙️ Processing")
        process_frame.pack(fill=tk.X, pady=(0, 10))
        
        button_container = tk.Frame(process_frame, bg='#34495e')
        button_container.pack(pady=10)
        
        ttk.Button(button_container, text="ENCODE", 
                  command=self.encode_message, style="Accent.TButton").pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_container, text="DECODE", 
                  command=self.decode_message, style="Secondary.TButton").pack(side=tk.LEFT, padx=5)
        
        # Info display frame
        info_frame = self.create_frame(left_panel, "📊 Image Information")
        info_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.info_text = tk.Text(info_frame, height=8, width=40, 
                                font=("Arial", 9), bg='#34495e', fg='white')
        self.info_text.pack(padx=10, pady=10)
        
        # Visualization frame
        viz_frame = self.create_frame(left_panel, "👁️ Pixel Visualization")
        viz_frame.pack(fill=tk.BOTH, expand=True)
        
        self.viz_text = tk.Text(viz_frame, height=15, width=40, 
                               font=("Courier", 9), bg='#2c3e50', fg='#1abc9c')
        self.viz_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Right panel - Image display and explanation
        right_panel = tk.Frame(main_container, bg=self.bg_color)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Image display frame
        img_display_frame = self.create_frame(right_panel, "🖼️ Image Display")
        img_display_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Create canvas for images
        self.image_canvas = tk.Canvas(img_display_frame, bg='#34495e', 
                                      highlightthickness=0)
        self.image_canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Explanation frame
        explanation_frame = self.create_frame(right_panel, "📚 LSB Algorithm Steps")
        explanation_frame.pack(fill=tk.BOTH, expand=False)
        
        explanation_text = """
        🔍 LSB (Least Significant Bit) Algorithm Steps:
        
        1️⃣ IMAGE LOADING:
           • Load image and convert to RGB array
           • Each pixel has 3 channels (Red, Green, Blue)
           • Each channel value: 0-255 (8 bits)
        
        2️⃣ MESSAGE PREPARATION:
           • Convert message to binary
           • Add termination markers
        
        3️⃣ CAPACITY CHECK:
           • Calculate available LSB slots
           • Formula: width × height × 3 channels
           • Compare with message size
        
        4️⃣ ENCODING PROCESS:
           • For each bit in message:
             • Select pixel channel
             • Replace LSB (bit 0) with message bit
             • Change is: 255 → 254 or 254 → 255 (1-bit change)
        
        5️⃣ VISUAL EFFECT:
           • Human eye cannot detect changes
           • Maximum change: 1/255 ≈ 0.4% intensity
        
        6️⃣ DECODING:
           • Extract LSB from each pixel
           • Reconstruct binary message
           • Convert back to text
        
        ⚡ Key Features:
           • High capacity (up to 1/8 of image size)
           • Minimal visual distortion
           • Simple but effective
        """
        
        explanation_label = tk.Text(explanation_frame, height=15, 
                                   font=("Arial", 9), bg='#34495e', fg='#ecf0f1',
                                   wrap=tk.WORD, relief=tk.FLAT)
        explanation_label.insert(tk.END, explanation_text)
        explanation_label.config(state=tk.DISABLED)
        explanation_label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Status bar
        status_frame = tk.Frame(self.root, bg='#34495e', height=30)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.status_label = tk.Label(status_frame, text="Ready", 
                                    bg='#34495e', fg=self.secondary_color,
                                    font=("Arial", 10))
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        # Configure styles
        self.style.configure("Accent.TButton", 
                           background=self.accent_color,
                           foreground='white',
                           font=("Arial", 10, "bold"))
        self.style.configure("Secondary.TButton",
                           background=self.secondary_color,
                           foreground='white',
                           font=("Arial", 10, "bold"))
    
    def create_frame(self, parent, title):
        frame = tk.Frame(parent, bg='#34495e', relief=tk.RAISED, borderwidth=2)
        
        title_label = tk.Label(frame, text=title, 
                              font=("Arial", 11, "bold"),
                              bg='#2c3e50', fg=self.fg_color,
                              padx=10, pady=5)
        title_label.pack(fill=tk.X)
        
        return frame
    
    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff")]
        )
        
        if file_path:
            try:
                self.img_path_var.set(os.path.basename(file_path))
                self.original_image = Image.open(file_path).convert('RGB')
                self.image_array = np.array(self.original_image)
                
                # Display image info
                self.display_image_info()
                self.status_label.config(text=f"Image loaded: {self.image_array.shape[1]}x{self.image_array.shape[0]}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {str(e)}")
    
    def display_image_info(self):
        if self.image_array is not None:
            height, width, channels = self.image_array.shape
            total_pixels = height * width
            total_bits = total_pixels * channels
            max_chars = total_bits // 8
            
            info = f"""📐 Image Dimensions:
   Width: {width} pixels
   Height: {height} pixels
   Channels: {channels} (RGB)
   
   Total Pixels: {total_pixels:,}
   Available LSBs: {total_bits:,} bits
   
   Maximum Capacity:
   → {max_chars:,} characters
   → {max_chars//1024:.1f} KB of text
   
   Format: 8-bit per channel
   Type: {self.image_array.dtype}"""
            
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, info)
            self.info_text.config(state=tk.DISABLED)
    
    def show_original(self):
        if self.original_image:
            self.display_images(self.original_image, None, "Original Image")
    
    def encode_message(self):
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first!")
            return
        
        self.message = self.message_text.get("1.0", tk.END).strip()
        if not self.message:
            messagebox.showwarning("Warning", "Please enter a secret message!")
            return
        
        try:
            # Get image dimensions
            height, width, channels = self.image_array.shape
            
            # Convert message to binary
            binary_message = ''.join(format(ord(char), '08b') for char in self.message)
            binary_message += '1111111111111110'  # Termination marker
            
            # Check capacity
            max_bits = height * width * channels
            if len(binary_message) > max_bits:
                messagebox.showerror("Error", 
                    f"Message too long!\n"
                    f"Message needs {len(binary_message)} bits\n"
                    f"Available: {max_bits} bits")
                return
            
            # Create copy for stego image
            stego_array = self.image_array.copy()
            bit_index = 0
            
            # Visualization text
            viz_text = "🔍 ENCODING PROCESS:\n" + "="*40 + "\n\n"
            viz_text += f"Message: '{self.message[:50]}...'\n"
            viz_text += f"Binary: {binary_message[:64]}...\n\n"
            viz_text += "Pixel modifications:\n"
            
            # Encode message in LSB
            for y in range(height):
                for x in range(width):
                    for c in range(channels):
                        if bit_index < len(binary_message):
                            original_pixel = stego_array[y, x, c]
                            # Get LSB
                            lsb = original_pixel & 1
                            # Get message bit
                            message_bit = int(binary_message[bit_index])
                            
                            # Modify LSB if different
                            if lsb != message_bit:
                                stego_array[y, x, c] = original_pixel ^ 1
                                
                                # Add to visualization (first few pixels)
                                if bit_index < 12:  # Show only first 12 bits for clarity
                                    channel_name = ['R', 'G', 'B'][c]
                                    viz_text += (f"Pixel({x},{y}) {channel_name}: "
                                                f"{original_pixel:03d} → {stego_array[y,x,c]:03d} "
                                                f"[LSB: {lsb}→{message_bit}]\n")
                            
                            bit_index += 1
            
            viz_text += f"\n✅ Encoding complete!\n"
            viz_text += f"Modified pixels: {bit_index//3:,}\n"
            viz_text += f"Modified bits: {bit_index:,}\n"
            viz_text += f"Capacity used: {bit_index/max_bits*100:.2f}%"
            
            # Update visualization
            self.viz_text.delete(1.0, tk.END)
            self.viz_text.insert(tk.END, viz_text)
            
            # Create stego image
            self.stego_image = Image.fromarray(stego_array)
            
            # Display both images
            self.display_images(self.original_image, self.stego_image, "Original vs Stego Image")
            
            # Save stego image
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
            )
            if save_path:
                self.stego_image.save(save_path)
                self.status_label.config(text=f"Stego image saved to: {os.path.basename(save_path)}")
                messagebox.showinfo("Success", 
                    f"Message encoded successfully!\n\n"
                    f"Statistics:\n"
                    f"• Message length: {len(self.message)} characters\n"
                    f"• Binary length: {len(binary_message)} bits\n"
                    f"• Modified pixels: {bit_index//3:,}\n"
                    f"• Capacity used: {bit_index/max_bits*100:.2f}%")
            
        except Exception as e:
            messagebox.showerror("Error", f"Encoding failed: {str(e)}")
    
    def decode_message(self):
        if self.stego_image is None:
            messagebox.showwarning("Warning", "Please encode a message first or load a stego image!")
            return
        
        try:
            stego_array = np.array(self.stego_image)
            height, width, channels = stego_array.shape
            
            # Extract LSBs
            binary_bits = []
            for y in range(height):
                for x in range(width):
                    for c in range(channels):
                        pixel_value = stego_array[y, x, c]
                        lsb = pixel_value & 1
                        binary_bits.append(str(lsb))
            
            binary_string = ''.join(binary_bits)
            
            # Find termination marker
            terminator = '1111111111111110'
            if terminator in binary_string:
                binary_string = binary_string[:binary_string.index(terminator)]
            
            # Convert binary to text
            message = ""
            for i in range(0, len(binary_string), 8):
                byte = binary_string[i:i+8]
                if len(byte) == 8:
                    message += chr(int(byte, 2))
            
            # Show decoded message
            self.show_decoded_message(message)
            
        except Exception as e:
            messagebox.showerror("Error", f"Decoding failed: {str(e)}")
    
    def show_decoded_message(self, message):
        decode_window = tk.Toplevel(self.root)
        decode_window.title("Decoded Message")
        decode_window.geometry("500x300")
        decode_window.configure(bg=self.bg_color)
        
        tk.Label(decode_window, text="✅ SECRET MESSAGE DECODED", 
                font=("Arial", 16, "bold"),
                bg=self.bg_color, fg=self.secondary_color).pack(pady=20)
        
        text_frame = tk.Frame(decode_window, bg='#34495e')
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        text_widget = tk.Text(text_frame, wrap=tk.WORD, 
                             font=("Arial", 12), 
                             bg='#2c3e50', fg=self.fg_color,
                             relief=tk.FLAT)
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        text_widget.insert(tk.END, message)
        text_widget.config(state=tk.DISABLED)
        
        tk.Button(decode_window, text="Close", 
                 command=decode_window.destroy,
                 bg=self.accent_color, fg='white',
                 font=("Arial", 10, "bold"),
                 padx=20, pady=5).pack(pady=10)
    
    def display_images(self, original_img, stego_img=None, title=""):
        # Clear canvas
        self.image_canvas.delete("all")
        
        # Calculate positions
        canvas_width = self.image_canvas.winfo_width()
        canvas_height = self.image_canvas.winfo_height()
        
        if canvas_width <= 1:  # If canvas not yet drawn
            canvas_width = 800
            canvas_height = 400
        
        if stego_img:
            # Display both images side by side
            img_width = canvas_width // 2 - 20
            img_height = canvas_height - 40
            
            # Resize images
            orig_resized = original_img.copy()
            orig_resized.thumbnail((img_width, img_height), Image.Resampling.LANCZOS)
            stego_resized = stego_img.copy()
            stego_resized.thumbnail((img_width, img_height), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            orig_tk = ImageTk.PhotoImage(orig_resized)
            stego_tk = ImageTk.PhotoImage(stego_resized)
            
            # Draw original image
            x1 = 10
            y1 = 10
            self.image_canvas.create_image(x1, y1, anchor=tk.NW, image=orig_tk)
            self.image_canvas.create_text(x1 + img_width//2, y1 + img_height + 15, 
                                        text="Original Image", fill='white',
                                        font=("Arial", 10, "bold"))
            
            # Draw stego image
            x2 = canvas_width // 2 + 10
            self.image_canvas.create_image(x2, y1, anchor=tk.NW, image=stego_tk)
            self.image_canvas.create_text(x2 + img_width//2, y1 + img_height + 15, 
                                        text="Stego Image (with hidden message)", 
                                        fill=self.secondary_color,
                                        font=("Arial", 10, "bold"))
            
            # Draw arrow
            arrow_x = canvas_width // 2
            self.image_canvas.create_line(arrow_x-50, img_height//2, 
                                         arrow_x+50, img_height//2,
                                         arrow=tk.LAST, fill=self.accent_color, width=3)
            self.image_canvas.create_text(arrow_x, img_height//2 - 20, 
                                        text="ENCODE", fill=self.accent_color,
                                        font=("Arial", 12, "bold"))
            
            # Keep references
            self.image_canvas.orig_image = orig_tk
            self.image_canvas.stego_image = stego_tk
            
        else:
            # Display single image
            img_width = canvas_width - 40
            img_height = canvas_height - 40
            
            # Resize image
            img_resized = original_img.copy()
            img_resized.thumbnail((img_width, img_height), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            img_tk = ImageTk.PhotoImage(img_resized)
            
            # Draw image
            x = (canvas_width - img_resized.width) // 2
            y = 10
            self.image_canvas.create_image(x, y, anchor=tk.NW, image=img_tk)
            self.image_canvas.create_text(canvas_width//2, y + img_resized.height + 20, 
                                        text="Original Image", fill='white',
                                        font=("Arial", 12, "bold"))
            
            # Keep reference
            self.image_canvas.image = img_tk

def main():
    root = tk.Tk()
    app = LSBSteganographyGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()