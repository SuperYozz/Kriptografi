import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont
import numpy as np
import os

class LSBSteganographyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LSB Steganography - Advanced Visualizer")
        self.root.geometry("1400x900")
        self.root.configure(bg='#1a1a2e')
        
        self.original_image = None
        self.stego_image = None
        self.image_array = None
        self.modified_pixels = []
        self.bit_positions = []
        self.message = ""
        
        # Setup style
        self.setup_styles()
        
        # Create GUI
        self.create_widgets()
        
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Colors
        self.bg_color = '#1a1a2e'
        self.fg_color = '#e6e6e6'
        self.accent_color = '#4cc9f0'
        self.secondary_color = '#4361ee'
        self.warning_color = '#f72585'
        self.success_color = '#4ade80'
        
    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg=self.bg_color)
        header_frame.pack(fill=tk.X, padx=20, pady=10)
        
        title_label = tk.Label(
            header_frame, 
            text="🔐 ADVANCED LSB STEGANOGRAPHY VISUALIZER", 
            font=("Arial", 24, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            header_frame,
            text="Visual Learning Tool with Encoding Location & LSB Process Visualization",
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.fg_color
        )
        subtitle_label.pack()
        
        # Main container
        main_container = tk.Frame(self.root, bg=self.bg_color)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Left panel - Controls
        left_panel = tk.Frame(main_container, bg=self.bg_color, width=350)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)
        
        # Image selection frame
        selection_frame = self.create_frame(left_panel, "📁 IMAGE SELECTION")
        selection_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.img_path_var = tk.StringVar()
        tk.Entry(selection_frame, textvariable=self.img_path_var, 
                font=("Arial", 10), state='readonly', width=30,
                bg='#16213e', fg='white', relief=tk.FLAT).pack(side=tk.LEFT, padx=5, pady=5)
        
        ttk.Button(selection_frame, text="📂 Browse", 
                  command=self.load_image, style="Accent.TButton").pack(side=tk.LEFT, padx=5)
        
        # Message input frame
        message_frame = self.create_frame(left_panel, "✉️ SECRET MESSAGE")
        message_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(message_frame, text="Enter your secret message:", 
                bg='#16213e', fg=self.fg_color, font=("Arial", 9)).pack(anchor=tk.W, padx=10, pady=(5,0))
        
        self.message_text = tk.Text(message_frame, height=4, width=40, 
                                   font=("Arial", 10), bg='#0f3460', fg='white',
                                   relief=tk.FLAT)
        self.message_text.pack(padx=10, pady=5)
        
        # Image info frame
        info_frame = self.create_frame(left_panel, "📊 IMAGE INFORMATION")
        info_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.info_text = tk.Text(info_frame, height=8, width=40, 
                                font=("Consolas", 9), bg='#0f3460', fg='#4cc9f0',
                                relief=tk.FLAT)
        self.info_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Process buttons frame
        process_frame = self.create_frame(left_panel, "⚙️ PROCESSING CONTROLS")
        process_frame.pack(fill=tk.X, pady=(0, 10))
        
        button_container = tk.Frame(process_frame, bg='#16213e')
        button_container.pack(pady=10)
        
        ttk.Button(button_container, text="🔒 ENCODE MESSAGE", 
                  command=self.encode_message, style="Accent.TButton", width=20).pack(pady=5)
        
        ttk.Button(button_container, text="🔓 DECODE MESSAGE", 
                  command=self.decode_message, style="Secondary.TButton", width=20).pack(pady=5)
        
        ttk.Button(button_container, text="📍 SHOW ENCODING AREA", 
                  command=self.show_encoding_area, style="Warning.TButton", width=20).pack(pady=5)
        
        # Right panel - Image display
        right_panel = tk.Frame(main_container, bg=self.bg_color)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Image comparison frame
        img_frame = self.create_frame(right_panel, "🖼️ IMAGE COMPARISON")
        img_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create image containers
        image_container = tk.Frame(img_frame, bg='#16213e')
        image_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Original image frame
        orig_frame = tk.Frame(image_container, bg='#16213e')
        orig_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        tk.Label(orig_frame, text="ORIGINAL IMAGE", bg='#16213e', fg=self.fg_color,
                font=("Arial", 11, "bold")).pack(pady=5)
        
        self.orig_canvas = tk.Canvas(orig_frame, bg='#0f3460', highlightthickness=1,
                                    highlightbackground=self.accent_color)
        self.orig_canvas.pack(fill=tk.BOTH, expand=True)
        
        self.orig_info = tk.Label(orig_frame, text="No image loaded", bg='#16213e',
                                 fg='#888888', font=("Arial", 9))
        self.orig_info.pack(pady=5)
        
        # Stego image frame
        stego_frame = tk.Frame(image_container, bg='#16213e')
        stego_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        tk.Label(stego_frame, text="STEGO IMAGE", bg='#16213e', fg=self.secondary_color,
                font=("Arial", 11, "bold")).pack(pady=5)
        
        self.stego_canvas = tk.Canvas(stego_frame, bg='#0f3460', highlightthickness=1,
                                     highlightbackground=self.secondary_color)
        self.stego_canvas.pack(fill=tk.BOTH, expand=True)
        
        self.stego_info = tk.Label(stego_frame, text="No stego image", bg='#16213e',
                                  fg='#888888', font=("Arial", 9))
        self.stego_info.pack(pady=5)
        
        # Bottom panel - Visualization
        bottom_panel = tk.Frame(self.root, bg=self.bg_color, height=250)
        bottom_panel.pack(fill=tk.BOTH, expand=False, padx=20, pady=(0,10))
        
        # Visualization tabs
        notebook = ttk.Notebook(bottom_panel)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Tab 1: Encoding Process
        encode_tab = tk.Frame(notebook, bg='#16213e')
        notebook.add(encode_tab, text="🔍 ENCODING PROCESS")
        
        self.encode_text = tk.Text(encode_tab, height=10, font=("Consolas", 9),
                                  bg='#0f3460', fg='white', wrap=tk.WORD)
        self.encode_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Tab 2: LSB Binary View
        binary_tab = tk.Frame(notebook, bg='#16213e')
        notebook.add(binary_tab, text="🔢 LSB BINARY VIEW")
        
        self.binary_text = tk.Text(binary_tab, height=10, font=("Consolas", 9),
                                  bg='#0f3460', fg='#4cc9f0', wrap=tk.WORD)
        self.binary_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Tab 3: Statistics
        stats_tab = tk.Frame(notebook, bg='#16213e')
        notebook.add(stats_tab, text="📈 STATISTICS")
        
        self.stats_text = tk.Text(stats_tab, height=10, font=("Arial", 9),
                                 bg='#0f3460', fg='#f72585', wrap=tk.WORD)
        self.stats_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Status bar
        status_frame = tk.Frame(self.root, bg='#0f3460', height=30)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.status_label = tk.Label(status_frame, text="Ready", 
                                    bg='#0f3460', fg=self.secondary_color,
                                    font=("Arial", 10, "bold"))
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        # Configure styles
        self.style.configure("Accent.TButton", 
                           background=self.accent_color,
                           foreground='white',
                           font=("Arial", 10, "bold"),
                           padding=10)
        self.style.configure("Secondary.TButton",
                           background=self.secondary_color,
                           foreground='white',
                           font=("Arial", 10, "bold"),
                           padding=10)
        self.style.configure("Warning.TButton",
                           background=self.warning_color,
                           foreground='white',
                           font=("Arial", 10, "bold"),
                           padding=10)
    
    def create_frame(self, parent, title):
        frame = tk.Frame(parent, bg='#16213e', relief=tk.FLAT)
        
        title_label = tk.Label(frame, text=title, 
                              font=("Arial", 10, "bold"),
                              bg='#0f3460', fg=self.fg_color,
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
                
                # Reset stego image
                self.stego_image = None
                self.modified_pixels = []
                self.bit_positions = []
                
                # Display original image
                self.display_image_on_canvas(self.original_image, self.orig_canvas)
                
                # Display image info
                self.display_image_info()
                
                self.status_label.config(text=f"✓ Image loaded: {os.path.basename(file_path)}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {str(e)}")
    
    def display_image_info(self):
        if self.image_array is not None:
            height, width, channels = self.image_array.shape
            total_pixels = height * width
            total_bits = total_pixels * channels
            max_chars = total_bits // 8
            
            # Calculate approximate file size
            # For 24-bit RGB: width * height * 3 bytes
            file_size_bytes = total_pixels * 3
            file_size_kb = file_size_bytes / 1024
            
            info = f"""╔═══════════════════════════════╗
║        IMAGE INFO         ║
╠═══════════════════════════════╣
║ Dimensions: {width} × {height} px
║ Channels: {channels} (RGB)
║ Total Pixels: {total_pixels:,}
║ Available Bits: {total_bits:,}
║ Max Capacity: {max_chars:,} chars
║ Approx Size: {file_size_kb:.1f} KB
║ Bits per Pixel: 24 bits
╚═══════════════════════════════╝"""
            
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, info)
            self.info_text.config(state=tk.DISABLED)
            
            # Update original image info label
            self.orig_info.config(text=f"Size: {width}×{height} | Pixels: {total_pixels:,} | {file_size_kb:.1f} KB")
    
    def display_image_on_canvas(self, image, canvas):
        canvas.delete("all")
        
        # Get canvas dimensions
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        
        if canvas_width <= 1:  # If canvas not yet drawn
            canvas_width = 400
            canvas_height = 300
        
        # Calculate aspect ratio
        img_width, img_height = image.size
        ratio = min(canvas_width/img_width, canvas_height/img_height)
        new_width = int(img_width * ratio)
        new_height = int(img_height * ratio)
        
        # Resize image
        resized_img = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Convert to PhotoImage
        img_tk = ImageTk.PhotoImage(resized_img)
        
        # Calculate position to center
        x = (canvas_width - new_width) // 2
        y = (canvas_height - new_height) // 2
        
        # Draw image
        canvas.create_image(x, y, anchor=tk.NW, image=img_tk)
        
        # Keep reference
        canvas.image = img_tk
        
        return resized_img
    
    def encode_message(self):
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first!")
            return
        
        self.message = self.message_text.get("1.0", tk.END).strip()
        if not self.message:
            messagebox.showwarning("Warning", "Please enter a secret message!")
            return
        
        try:
            # Reset tracking
            self.modified_pixels = []
            self.bit_positions = []
            
            # Get image dimensions
            height, width, channels = self.image_array.shape
            
            # Convert message to binary with termination marker
            binary_message = ''.join(format(ord(char), '08b') for char in self.message)
            binary_message += '1111111111111110'  # 16-bit termination marker
            
            # Check capacity
            max_bits = height * width * channels
            if len(binary_message) > max_bits:
                messagebox.showerror("Error", 
                    f"Message too long!\n\n"
                    f"Message needs: {len(binary_message)} bits\n"
                    f"Available: {max_bits} bits\n"
                    f"Try shorter message or larger image.")
                return
            
            # Create copy for stego image
            stego_array = self.image_array.copy()
            bit_index = 0
            
            # Clear visualization texts
            self.encode_text.delete(1.0, tk.END)
            self.binary_text.delete(1.0, tk.END)
            self.stats_text.delete(1.0, tk.END)
            
            # Start visualization
            encode_log = "🚀 ENCODING PROCESS STARTED\n"
            encode_log += "="*50 + "\n\n"
            encode_log += f"📝 Message: '{self.message}'\n"
            encode_log += f"📊 Message Length: {len(self.message)} characters\n"
            encode_log += f"🔢 Binary Length: {len(binary_message)} bits (including 16-bit terminator)\n\n"
            encode_log += "📥 Encoding Steps:\n"
            
            # Encode message in LSB
            for y in range(height):
                for x in range(width):
                    for c in range(channels):
                        if bit_index < len(binary_message):
                            original_pixel = stego_array[y, x, c]
                            original_binary = format(original_pixel, '08b')
                            
                            # Get LSB and message bit
                            lsb = original_pixel & 1
                            message_bit = int(binary_message[bit_index])
                            
                            # Modify LSB if different
                            if lsb != message_bit:
                                stego_array[y, x, c] = original_pixel ^ 1
                                
                                # Track modified pixel
                                self.modified_pixels.append((x, y, c))
                                self.bit_positions.append(bit_index)
                                
                                # Log first few modifications
                                if bit_index < 15:
                                    channel_name = ['R', 'G', 'B'][c]
                                    encode_log += (f"  • Pixel({x},{y}) {channel_name}: "
                                                  f"{original_pixel:03d} [{original_binary}] → "
                                                  f"{stego_array[y,x,c]:03d} "
                                                  f"[LSB: {lsb}→{message_bit}]\n")
                            
                            bit_index += 1
                        else:
                            break
                    if bit_index >= len(binary_message):
                        break
                if bit_index >= len(binary_message):
                    break
            
            # Create stego image
            self.stego_image = Image.fromarray(stego_array)
            
            # Display both images
            self.display_image_on_canvas(self.original_image, self.orig_canvas)
            
            # Create highlighted version for stego image
            self.display_stego_with_highlight(stego_array)
            
            # Update stego info with size information
            img_width, img_height = self.stego_image.size
            file_size_kb = (img_width * img_height * 3) / 1024
            
            self.stego_info.config(
                text=f"Size: {img_width}×{img_height} | {file_size_kb:.1f} KB\n"
                     f"Modified Bits: {bit_index:,} | Modified Pixels: {len(self.modified_pixels):,}"
            )
            
            # Add completion log
            encode_log += f"\n✅ ENCODING COMPLETE!\n"
            encode_log += f"📤 Total bits encoded: {bit_index}\n"
            encode_log += f"🎯 Total pixels modified: {len(self.modified_pixels)}\n"
            encode_log += f"📈 Capacity used: {bit_index/max_bits*100:.2f}%\n"
            
            # Update visualization texts
            self.encode_text.insert(tk.END, encode_log)
            
            # Create binary visualization
            binary_visual = "🔢 BINARY REPRESENTATION\n"
            binary_visual += "="*50 + "\n\n"
            binary_visual += f"Message Binary (first 64 bits):\n{binary_message[:64]}...\n\n"
            binary_visual += "First 5 Modified Pixels:\n"
            
            # Show first few pixels' LSB pattern
            for i in range(min(5, len(self.modified_pixels))):
                x, y, c = self.modified_pixels[i]
                original_val = self.image_array[y, x, c]
                stego_val = stego_array[y, x, c]
                channel = ['R', 'G', 'B'][c]
                
                binary_visual += (f"Pixel({x},{y}) {channel}: "
                                f"{original_val:03d}({format(original_val, '08b')}) → "
                                f"{stego_val:03d}({format(stego_val, '08b')})\n")
            
            self.binary_text.insert(tk.END, binary_visual)
            
            # Create statistics
            self.create_statistics(bit_index, max_bits, len(binary_message))
            
            # Save stego image
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
                initialfile="stego_image.png"
            )
            if save_path:
                self.stego_image.save(save_path)
                self.status_label.config(
                    text=f"✓ Stego image saved: {os.path.basename(save_path)} | "
                         f"{bit_index} bits encoded"
                )
                messagebox.showinfo("Success", 
                    f"✅ Message encoded successfully!\n\n"
                    f"📊 Statistics:\n"
                    f"• Message: {len(self.message)} characters\n"
                    f"• Binary: {len(binary_message)} bits\n"
                    f"• Modified bits: {bit_index}\n"
                    f"• Modified pixels: {len(self.modified_pixels)}\n"
                    f"• Capacity used: {bit_index/max_bits*100:.2f}%\n\n"
                    f"💾 Saved as: {os.path.basename(save_path)}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Encoding failed: {str(e)}")
    
    def display_stego_with_highlight(self, stego_array):
        """Display stego image with highlighted encoding area"""
        if self.stego_image is None:
            return
        
        # Create a copy for highlighting
        highlighted_img = self.stego_image.copy()
        draw = ImageDraw.Draw(highlighted_img)
        
        # Highlight modified pixels (limited to first 100 for performance)
        highlight_count = min(100, len(self.modified_pixels))
        for i in range(highlight_count):
            x, y, c = self.modified_pixels[i]
            # Draw a small rectangle around modified pixel
            color = ['#ff0000', '#00ff00', '#0000ff'][c]  # R,G,B colors
            draw.rectangle([x-1, y-1, x+1, y+1], outline=color, width=1)
        
        # Draw a box around the encoding area if we have modified pixels
        if self.modified_pixels:
            xs = [p[0] for p in self.modified_pixels]
            ys = [p[1] for p in self.modified_pixels]
            min_x, max_x = min(xs), max(xs)
            min_y, max_y = min(ys), max(ys)
            
            # Draw encoding area box
            draw.rectangle([min_x, min_y, max_x, max_y], 
                          outline=self.warning_color, 
                          width=2)
            
            # Add text label
            try:
                # Try to use default font
                font = ImageFont.truetype("arial.ttf", 12)
            except:
                # Fallback to default
                font = ImageFont.load_default()
            
            draw.text((min_x + 5, min_y - 20), 
                     f"Encoding Area: {len(self.modified_pixels)} pixels",
                     fill=self.warning_color, font=font)
        
        # Display on canvas
        self.display_image_on_canvas(highlighted_img, self.stego_canvas)
    
    def show_encoding_area(self):
        """Show detailed encoding area information"""
        if not self.modified_pixels:
            messagebox.showinfo("Info", "No encoding data available. Please encode a message first.")
            return
        
        area_window = tk.Toplevel(self.root)
        area_window.title("Encoding Area Details")
        area_window.geometry("600x500")
        area_window.configure(bg=self.bg_color)
        
        tk.Label(area_window, text="📍 ENCODING AREA DETAILS", 
                font=("Arial", 14, "bold"),
                bg=self.bg_color, fg=self.accent_color).pack(pady=10)
        
        # Create text widget
        text_frame = tk.Frame(area_window, bg='#16213e')
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        text_widget = tk.Text(text_frame, wrap=tk.WORD, font=("Consolas", 9),
                             bg='#0f3460', fg='white')
        scrollbar = tk.Scrollbar(text_frame, command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)
        
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Add encoding area info
        info = "="*60 + "\n"
        info += "ENCODING LOCATION DETAILS\n"
        info += "="*60 + "\n\n"
        
        # Calculate area bounds
        xs = [p[0] for p in self.modified_pixels]
        ys = [p[1] for p in self.modified_pixels]
        
        if xs and ys:
            info += f"📏 Area Bounds:\n"
            info += f"   • Top-Left: ({min(xs)}, {min(ys)})\n"
            info += f"   • Bottom-Right: ({max(xs)}, {max(ys)})\n"
            info += f"   • Width: {max(xs)-min(xs)+1} pixels\n"
            info += f"   • Height: {max(ys)-min(ys)+1} pixels\n"
            info += f"   • Total Area: {(max(xs)-min(xs)+1)*(max(ys)-min(ys)+1)} pixels\n\n"
        
        info += f"📊 Modified Pixels: {len(self.modified_pixels)}\n"
        info += f"🔢 Modified Bits: {len(self.bit_positions)}\n\n"
        
        info += "📍 First 20 Modified Pixels:\n"
        info += "-"*50 + "\n"
        
        for i, (x, y, c) in enumerate(self.modified_pixels[:20]):
            channel_name = ['Red', 'Green', 'Blue'][c]
            original_val = self.image_array[y, x, c] if self.image_array is not None else 0
            stego_val = self.stego_image.getpixel((x, y))[c] if self.stego_image else 0
            
            bit_pos = self.bit_positions[i] if i < len(self.bit_positions) else 'N/A'
            info += (f"{i+1:2d}. Pixel({x:3d},{y:3d}) {channel_name:6s}: "
                    f"{original_val:3d} → {stego_val:3d} | "
                    f"Bit Position: {bit_pos}\n")
        
        text_widget.insert(tk.END, info)
        text_widget.config(state=tk.DISABLED)
        
        # Add close button
        close_button = ttk.Button(area_window, text="Close", 
                                 command=area_window.destroy,
                                 style="Accent.TButton")
        close_button.pack(pady=10)
    
    def decode_message(self):
        if self.stego_image is None:
            messagebox.showwarning("Warning", "No stego image available! Please encode a message first or load a stego image.")
            return
        
        try:
            # Create decoding visualization window
            decode_window = tk.Toplevel(self.root)
            decode_window.title("LSB Decoding Process")
            decode_window.geometry("1000x700")
            decode_window.configure(bg=self.bg_color)
            
            # Header
            header = tk.Label(decode_window, text="🔓 LSB DECODING PROCESS VISUALIZATION",
                            font=("Arial", 16, "bold"),
                            bg=self.bg_color, fg=self.secondary_color)
            header.pack(pady=10)
            
            # Create notebook for tabs
            decode_notebook = ttk.Notebook(decode_window)
            decode_notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            # Tab 1: Decoding Steps
            steps_tab = tk.Frame(decode_notebook, bg='#16213e')
            decode_notebook.add(steps_tab, text="📋 Decoding Steps")
            
            steps_text = tk.Text(steps_tab, wrap=tk.WORD, font=("Arial", 10),
                                bg='#0f3460', fg='white')
            steps_scroll = tk.Scrollbar(steps_tab, command=steps_text.yview)
            steps_text.configure(yscrollcommand=steps_scroll.set)
            
            steps_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            steps_scroll.pack(side=tk.RIGHT, fill=tk.Y)
            
            # Tab 2: Binary Extraction
            binary_tab = tk.Frame(decode_notebook, bg='#16213e')
            decode_notebook.add(binary_tab, text="🔢 Binary Extraction")
            
            binary_text = tk.Text(binary_tab, wrap=tk.WORD, font=("Consolas", 9),
                                 bg='#0f3460', fg='#4cc9f0')
            binary_scroll = tk.Scrollbar(binary_tab, command=binary_text.yview)
            binary_text.configure(yscrollcommand=binary_scroll.set)
            
            binary_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            binary_scroll.pack(side=tk.RIGHT, fill=tk.Y)
            
            # Tab 3: Result
            result_tab = tk.Frame(decode_notebook, bg='#16213e')
            decode_notebook.add(result_tab, text="📝 Decoded Message")
            
            result_text = tk.Text(result_tab, wrap=tk.WORD, font=("Arial", 11),
                                 bg='#0f3460', fg=self.success_color)
            result_scroll = tk.Scrollbar(result_tab, command=result_text.yview)
            result_text.configure(yscrollcommand=result_scroll.set)
            
            result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            result_scroll.pack(side=tk.RIGHT, fill=tk.Y)
            
            # Start decoding process
            stego_array = np.array(self.stego_image)
            height, width, channels = stego_array.shape
            
            # Initialize
            steps_text.insert(tk.END, "🚀 STARTING DECODING PROCESS\n")
            steps_text.insert(tk.END, "="*60 + "\n\n")
            steps_text.insert(tk.END, "📊 Image Information:\n")
            steps_text.insert(tk.END, f"  • Size: {width} × {height} pixels\n")
            steps_text.insert(tk.END, f"  • Total bits available: {width*height*channels:,}\n")
            steps_text.insert(tk.END, f"  • Channels: {channels} (RGB)\n\n")
            
            # Extract LSBs from ALL pixels
            steps_text.insert(tk.END, "2️⃣ EXTRACTING LSB BITS FROM IMAGE\n")
            steps_text.insert(tk.END, "-"*60 + "\n")
            
            all_binary_bits = []
            total_bits = width * height * channels
            
            # Progress tracking
            steps_text.insert(tk.END, "Extracting bits...\n")
            steps_text.update()
            
            # Extract all bits
            for y in range(height):
                for x in range(width):
                    for c in range(channels):
                        pixel_value = stego_array[y, x, c]
                        lsb = pixel_value & 1
                        all_binary_bits.append(str(lsb))
            
            full_binary_string = ''.join(all_binary_bits)
            
            steps_text.insert(tk.END, f"✅ Extracted {len(all_binary_bits):,} LSB bits from entire image\n\n")
            
            # Look for termination marker
            steps_text.insert(tk.END, "3️⃣ LOOKING FOR TERMINATION MARKER\n")
            steps_text.insert(tk.END, "-"*60 + "\n")
            
            terminator = '1111111111111110'  # 16-bit termination marker
            message_binary = ""
            terminator_pos = -1
            
            # Search for terminator
            for i in range(0, len(full_binary_string) - 15, 8):
                if full_binary_string[i:i+16] == terminator:
                    terminator_pos = i
                    message_binary = full_binary_string[:i]
                    break
            
            if terminator_pos == -1:
                steps_text.insert(tk.END, "⚠️ Termination marker not found!\n")
                steps_text.insert(tk.END, "   Trying to decode without terminator...\n")
                # Try to decode a reasonable amount of bits
                max_chars_to_decode = min(1000, len(full_binary_string) // 8)
                message_binary = full_binary_string[:max_chars_to_decode * 8]
            else:
                steps_text.insert(tk.END, f"✅ Found termination marker at bit position: {terminator_pos}\n")
                steps_text.insert(tk.END, f"✅ Message binary length: {len(message_binary)} bits\n\n")
            
            # Show binary visualization
            binary_text.insert(tk.END, "🔢 EXTRACTED BINARY DATA (First 200 bits)\n")
            binary_text.insert(tk.END, "="*60 + "\n\n")
            
            # Format binary for display
            display_binary = ""
            for i in range(0, min(200, len(full_binary_string)), 8):
                chunk = full_binary_string[i:i+8]
                display_binary += chunk + " "
                if (i // 8 + 1) % 4 == 0:
                    display_binary += "\n"
            
            binary_text.insert(tk.END, display_binary + "\n\n")
            
            if len(full_binary_string) > 200:
                binary_text.insert(tk.END, f"... and {len(full_binary_string) - 200} more bits\n\n")
            
            # Show termination marker search
            binary_text.insert(tk.END, "🔍 TERMINATION MARKER SEARCH:\n")
            binary_text.insert(tk.END, "-"*60 + "\n")
            binary_text.insert(tk.END, f"Looking for: {terminator}\n")
            
            if terminator_pos != -1:
                binary_text.insert(tk.END, f"✅ Found at position: {terminator_pos}\n")
                # Show context
                start = max(0, terminator_pos - 20)
                end = min(len(full_binary_string), terminator_pos + 36)
                context = full_binary_string[start:end]
                binary_text.insert(tk.END, f"Context: ...{context}...\n")
            else:
                binary_text.insert(tk.END, "❌ Not found in extracted bits\n")
            
            # Convert binary to text
            steps_text.insert(tk.END, "4️⃣ CONVERTING BINARY TO TEXT\n")
            steps_text.insert(tk.END, "-"*60 + "\n")
            
            message = ""
            char_count = 0
            
            for i in range(0, len(message_binary), 8):
                byte = message_binary[i:i+8]
                if len(byte) == 8:
                    try:
                        char_value = int(byte, 2)
                        # Check if it's a printable ASCII character
                        if 32 <= char_value <= 126 or char_value in [10, 13, 9]:  # Printable + newline, return, tab
                            char = chr(char_value)
                            message += char
                            char_count += 1
                            
                            # Show conversion of first 10 characters
                            if char_count <= 10:
                                char_display = char
                                if char == '\n':
                                    char_display = '\\n'
                                elif char == '\t':
                                    char_display = '\\t'
                                elif char == '\r':
                                    char_display = '\\r'
                                
                                steps_text.insert(tk.END, f"  • Byte {char_count:3d}: {byte} → '{char_display}' (ASCII: {char_value:3d})\n")
                        else:
                            # Non-printable character, might be end of message
                            if char_count > 0:
                                break
                    except:
                        break
            
            steps_text.insert(tk.END, f"\n✅ Successfully decoded {char_count} characters\n")
            
            # Display result
            result_text.insert(tk.END, "✅ MESSAGE SUCCESSFULLY DECODED!\n")
            result_text.insert(tk.END, "="*60 + "\n\n")
            
            result_text.insert(tk.END, "📊 DECODING STATISTICS:\n")
            result_text.insert(tk.END, "-"*60 + "\n")
            result_text.insert(tk.END, f"• Total bits extracted: {len(all_binary_bits):,}\n")
            result_text.insert(tk.END, f"• Message bits used: {len(message_binary):,}\n")
            result_text.insert(tk.END, f"• Characters decoded: {char_count:,}\n")
            result_text.insert(tk.END, f"• Termination marker: {'✅ Found' if terminator_pos != -1 else '❌ Not found'}\n")
            if terminator_pos != -1:
                result_text.insert(tk.END, f"• Terminator at bit: {terminator_pos}\n")
            result_text.insert(tk.END, "\n")
            
            result_text.insert(tk.END, "📝 DECODED MESSAGE:\n")
            result_text.insert(tk.END, "="*60 + "\n\n")
            
            if message:
                result_text.insert(tk.END, message)
            else:
                result_text.insert(tk.END, "⚠️ No message could be decoded. Possible issues:\n")
                result_text.insert(tk.END, "1. Image doesn't contain hidden message\n")
                result_text.insert(tk.END, "2. Message was encoded with different method\n")
                result_text.insert(tk.END, "3. The image is not a stego image\n")
            
            # Show visual LSB extraction examples
            steps_text.insert(tk.END, "\n5️⃣ VISUAL LSB EXTRACTION EXAMPLES\n")
            steps_text.insert(tk.END, "-"*60 + "\n")
            
            # Show LSB extraction for first few pixels
            pixel_count = 0
            for y in range(min(2, height)):
                for x in range(min(3, width)):
                    if pixel_count >= 6:
                        break
                    rgb_values = stego_array[y, x]
                    steps_text.insert(tk.END, f"\nPixel({x},{y}): RGB({rgb_values[0]}, {rgb_values[1]}, {rgb_values[2]})\n")
                    for c in range(3):
                        channel_name = ['Red', 'Green', 'Blue'][c]
                        pixel_val = rgb_values[c]
                        binary_val = format(pixel_val, '08b')
                        lsb = pixel_val & 1
                        steps_text.insert(tk.END, f"  {channel_name}: {pixel_val:3d} = {binary_val} → LSB = {lsb}\n")
                    pixel_count += 1
            
            # Disable editing
            steps_text.config(state=tk.DISABLED)
            binary_text.config(state=tk.DISABLED)
            result_text.config(state=tk.DISABLED)
            
            self.status_label.config(text=f"✓ Message decoded: {char_count} characters extracted")
            
        except Exception as e:
            messagebox.showerror("Error", f"Decoding failed: {str(e)}")
    
    def create_statistics(self, encoded_bits, total_bits, message_bits):
        """Create detailed statistics"""
        stats = "📈 ENCODING STATISTICS\n"
        stats += "="*40 + "\n\n"
        
        # Basic stats
        stats += f"🔢 Bits Statistics:\n"
        stats += f"   • Total available bits: {total_bits:,}\n"
        stats += f"   • Message bits (with terminator): {message_bits:,}\n"
        stats += f"   • Bits actually used: {encoded_bits:,}\n"
        stats += f"   • Bits unused: {total_bits - encoded_bits:,}\n\n"
        
        # Percentage stats
        capacity_used = encoded_bits / total_bits * 100
        efficiency = encoded_bits / message_bits * 100
        
        stats += f"📊 Percentage Analysis:\n"
        stats += f"   • Capacity used: {capacity_used:.2f}%\n"
        stats += f"   • Encoding efficiency: {efficiency:.2f}%\n"
        stats += f"   • Available capacity: {100-capacity_used:.2f}%\n\n"
        
        # Pixel statistics
        pixels_modified = len(self.modified_pixels)
        total_pixels = self.image_array.shape[0] * self.image_array.shape[1]
        pixel_percentage = pixels_modified / total_pixels * 100
        
        stats += f"🎯 Pixel Statistics:\n"
        stats += f"   • Total pixels: {total_pixels:,}\n"
        stats += f"   • Modified pixels: {pixels_modified:,}\n"
        stats += f"   • Pixels modified: {pixel_percentage:.4f}%\n"
        stats += f"   • Average bits per pixel: {encoded_bits/total_pixels:.2f}\n\n"
        
        # Channel distribution
        if self.modified_pixels:
            red_count = sum(1 for _, _, c in self.modified_pixels if c == 0)
            green_count = sum(1 for _, _, c in self.modified_pixels if c == 1)
            blue_count = sum(1 for _, _, c in self.modified_pixels if c == 2)
            
            stats += f"🌈 Channel Distribution:\n"
            stats += f"   • Red channel: {red_count:,} modifications\n"
            stats += f"   • Green channel: {green_count:,} modifications\n"
            stats += f"   • Blue channel: {blue_count:,} modifications\n"
        
        self.stats_text.delete(1.0, tk.END)
        self.stats_text.insert(tk.END, stats)
        self.stats_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = LSBSteganographyGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()