import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, font
import pyshorteners
import pyperclip
import validators
import qrcode
from io import BytesIO
from PIL import Image, ImageTk
import datetime

class URLShortenerGUI:
    def __init__(self, root):
        self.root = root
        root.title("✨ URL Shortener Pro 🔗🚀")

        # --- Styling ---
        style = ttk.Style(root)
        style.theme_use('clam')  # 'clam' theme is generally modern and clean. Try 'alt' or 'default' too.

        # Define fonts
        self.title_font = font.Font(family="Helvetica", size=14, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=10)
        self.button_font = font.Font(family="Helvetica", size=10, weight="bold")
        self.status_font = font.Font(family="Helvetica", size=10, slant="italic")
        self.history_font = font.Font(family="Helvetica", size=9)

        # --- Colors (Subtle adjustments if needed based on theme) ---
        primary_color = '#f0f0f0' # Light gray background (often default for 'clam')
        secondary_color = '#e0e0e0' # Slightly darker gray for frames
        accent_color = '#4CAF50' # Green accent (you can change this)
        error_color = '#F44336' # Red for errors
        success_color = accent_color

        root.configure(bg=primary_color) # Set root background

        # Configure LabelFrame styles (if you want to customize them further)
        style.configure('TLabelframe', background=primary_color, borderwidth=2, relief='groove')
        style.configure('TLabelframe.Label', font=self.title_font, background=primary_color)

        style.configure('TLabel', background=primary_color, font=self.label_font, foreground='#333') # Darker text color
        style.configure('TButton', font=self.button_font, padding=8) # Button padding
        style.configure('TCombobox', font=self.label_font)
        style.configure('TEntry', font=self.label_font, padding=5)

        # --- Data & Shortener ---
        self.shortener = pyshorteners.Shortener()
        self.available_providers = ['dagd', 'clickru', 'isgd', 'osdb']
        self.history = []

        # --- UI Elements ---
        frame_padding = 15 # Consistent frame padding
        element_padding_x = 10 # Horizontal padding for elements
        element_padding_y = 8  # Vertical padding for elements

        # --- Input Frame ---
        input_frame = ttk.Frame(root, padding=frame_padding, style='TLabelframe') # Apply style here if needed
        input_frame.grid(row=0, column=0, padx=frame_padding, pady=frame_padding, sticky="nsew")

        ttk.Label(input_frame, text="Enter Long URL:", style='TLabel').grid(row=0, column=0, padx=element_padding_x, pady=element_padding_y, sticky="w")
        self.url_entry = ttk.Entry(input_frame, width=50)
        self.url_entry.grid(row=0, column=1, padx=element_padding_x, pady=element_padding_y, columnspan=2, sticky="we")

        ttk.Label(input_frame, text="Provider:", style='TLabel').grid(row=1, column=0, padx=element_padding_x, pady=element_padding_y, sticky="w")
        self.provider_var = tk.StringVar(root)
        self.provider_var.set(self.available_providers[0] if self.available_providers else "isgd")
        self.provider_dropdown = ttk.Combobox(input_frame, textvariable=self.provider_var, values=self.available_providers, state="readonly")
        self.provider_dropdown.grid(row=1, column=1, padx=element_padding_x, pady=element_padding_y, sticky="we")

        self.shorten_button = ttk.Button(input_frame, text="Shorten URL ➡️", command=self.shorten_url, style='TButton')
        self.shorten_button.grid(row=2, column=1, padx=element_padding_x, pady=element_padding_y, sticky="we")
        self.clear_button = ttk.Button(input_frame, text="Clear 🗑️", command=self.clear_input, style='TButton')
        self.clear_button.grid(row=2, column=2, padx=element_padding_x, pady=element_padding_y, sticky="we")

        # --- Output Frame ---
        output_frame = ttk.Frame(root, padding=frame_padding, style='TLabelframe')
        output_frame.grid(row=1, column=0, padx=frame_padding, pady=frame_padding, sticky="nsew")

        ttk.Label(output_frame, text="Shortened URL:", style='TLabel').grid(row=0, column=0, padx=element_padding_x, pady=element_padding_y, sticky="nw")
        self.shortened_url_text = tk.Text(output_frame, height=3, width=50, wrap=tk.WORD, state=tk.DISABLED, font=self.label_font) # Apply font here for Text widget
        self.shortened_url_text.grid(row=0, column=1, padx=element_padding_x, pady=element_padding_y, columnspan=2, sticky="we")
        self.copy_button = ttk.Button(output_frame, text="Copy to Clipboard 📋", command=self.copy_to_clipboard, state=tk.DISABLED, style='TButton')
        self.copy_button.grid(row=1, column=1, padx=element_padding_x, pady=element_padding_y, sticky="we")

        # --- Status Label ---
        self.status_label_var = tk.StringVar()
        self.status_label = ttk.Label(root, textvariable=self.status_label_var, style='TLabel', font=self.status_font) # Apply italic font
        self.status_label.grid(row=2, column=0, columnspan=1, pady=element_padding_y, sticky="ew", padx=frame_padding) # Span less columns

        # --- QR Code Frame ---
        qr_code_frame = ttk.LabelFrame(root, text="QR Code ✨", padding=frame_padding, style='TLabelframe')
        qr_code_frame.grid(row=0, column=1, rowspan=2, padx=frame_padding, pady=frame_padding, sticky="nsew") # Adjusted rowspan

        self.qr_code_image_label = ttk.Label(qr_code_frame, background=primary_color) # Ensure QR code background matches
        self.qr_code_image_label.pack(padx=element_padding_x, pady=element_padding_y)
        self.qr_code_image = None

        # --- History Frame ---
        history_frame = ttk.LabelFrame(root, text="Shortening History 📜", padding=frame_padding, style='TLabelframe')
        history_frame.grid(row=3, column=0, columnspan=2, padx=frame_padding, pady=frame_padding, sticky="nsew") # Span both columns

        self.history_text = scrolledtext.ScrolledText(history_frame, height=5, wrap=tk.WORD, state=tk.DISABLED, font=self.history_font) # Apply smaller history font
        self.history_text.pack(padx=element_padding_x, pady=element_padding_y, fill=tk.BOTH, expand=True)

        self.clear_history_button = ttk.Button(history_frame, text="Clear History 🗑️", command=self.clear_history, style='TButton')
        self.clear_history_button.pack(pady=element_padding_y, anchor="e", padx=element_padding_x)

        # --- "Made by Sufyaan" Line ---
        self.made_by_label = ttk.Label(root, text="Made with ❤️ by Sufyaan", cursor="hand2", style='TLabel') # Apply style here
        self.made_by_label.grid(row=4, column=0, columnspan=2, pady=element_padding_y, sticky="ew", padx=frame_padding) # Span both columns
        self.made_by_label.bind("<Enter>", self.on_made_by_hover)
        self.made_by_label.bind("<Leave>", self.on_made_by_leave)
        self.made_by_label_original_color = self.made_by_label.cget("foreground")

        # --- Configure Grid Weights for responsiveness ---
        root.columnconfigure(0, weight=1) # Input/Output column expands
        root.columnconfigure(1, weight=1) # QR Code column expands
        input_frame.columnconfigure(1, weight=1)
        output_frame.columnconfigure(1, weight=1)
        history_frame.columnconfigure(0, weight=1)


        # --- Initial Clear ---
        self.clear_input() # Ensure initial state is clear

    def shorten_url(self):
        # ... (shorten_url method - same as before) ...
        long_url = self.url_entry.get()
        provider_name = self.provider_var.get().lower()

        if not long_url:
            self.show_status("⚠️ Please enter a URL to shorten.", "error")
            return

        if not validators.url(long_url): # Basic URL validation
            self.show_status("⚠️ Invalid URL format. Please enter a valid URL.", "error")
            return

        self.show_status(f"⏳ Shortening URL using {provider_name.upper()}...", "info")
        self.shorten_button.config(state=tk.DISABLED)
        self.clear_button.config(state=tk.DISABLED)

        try:
            shortened_url = getattr(self.shortener, provider_name).short(long_url)

            self.display_shortened_url(shortened_url)
            self.show_status(f"✅ URL Shortened Successfully using {provider_name.upper()}! ✨", "success")
            self.copy_button.config(state=tk.NORMAL)

            # Generate and display QR code
            self.generate_qr_code(shortened_url)

            # Add to history
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.history.append({"long_url": long_url, "shortened_url": shortened_url, "provider": provider_name.upper(), "timestamp": timestamp})
            self.update_history_display()


        except pyshorteners.exceptions.ShorteningErrorException as e:
            self.show_status(f"❌ Error shortening URL with {provider_name.upper()}: {e}", "error")
            self.display_shortened_url("Error")
            self.clear_qr_code() # Clear QR code on error
        except Exception as e:
            self.show_status(f"❌ An unexpected error occurred: {e}", "error")
            self.display_shortened_url("Error")
            self.clear_qr_code() # Clear QR code on error
        finally:
            self.shorten_button.config(state=tk.NORMAL)
            self.clear_button.config(state=tk.NORMAL)


    def display_shortened_url(self, url):
        self.shortened_url_text.config(state=tk.NORMAL)
        self.shortened_url_text.delete("1.0", tk.END)
        self.shortened_url_text.insert(tk.END, url)
        self.shortened_url_text.config(state=tk.DISABLED)

    def copy_to_clipboard(self):
        # ... (copy_to_clipboard method - same as before) ...
        shortened_url = self.shortened_url_text.get("1.0", tk.END).strip()
        if shortened_url and shortened_url != "Error":
            try:
                pyperclip.copy(shortened_url)
                self.show_status("📋 Shortened URL copied to clipboard! ✅", "info")
            except pyperclip.PyperclipException as e:
                error_message = "❌ Error copying to clipboard: Pyperclip could not find a copy/paste mechanism for your system.\n" \
                                "On Linux, you can run: `sudo apt-get install xclip` or `sudo apt-get install xsel` to install the required tools."
                self.show_status(error_message, "error")
            except Exception as e:
                self.show_status(f"❌ Error copying to clipboard: {e}", "error")
        else:
            self.show_status("⚠️ No shortened URL to copy.", "warning")

    def clear_input(self):
        # ... (clear_input method - same as before) ...
        self.url_entry.delete(0, tk.END)
        self.shortened_url_text.config(state=tk.NORMAL)
        self.shortened_url_text.delete("1.0", tk.END)
        self.shortened_url_text.config(state=tk.DISABLED)
        self.status_label_var.set("")
        self.copy_button.config(state=tk.DISABLED)
        self.clear_qr_code() # Clear QR code when clearing input

    def show_status(self, message, status_type="info"):
        # ... (show_status method - same as before) ...
        self.status_label_var.set(message)
        if status_type == "error":
            self.status_label.config(foreground= "red") # error_color
        elif status_type == "success":
            self.status_label.config(foreground= "green") # success_color
        elif status_type == "warning":
            self.status_label.config(foreground= "orange") # warning_color
        else: # info
            self.status_label.config(foreground= "black") # default color
        self.root.after(3000, self.clear_status)

    def clear_status(self):
        # ... (clear_status method - same as before) ...
        self.status_label_var.set("")
        self.status_label.config(foreground="black")

    def generate_qr_code(self, url):
        # ... (generate_qr_code method - same as before) ...
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Convert PIL Image to Tkinter PhotoImage
        img_tk = ImageTk.PhotoImage(img)
        self.qr_code_image = img_tk # Store it to prevent garbage collection
        self.qr_code_image_label.config(image=img_tk) # Update label

    def clear_qr_code(self):
        # ... (clear_qr_code method - same as before) ...
        self.qr_code_image_label.config(image=None) # Clear image from label
        self.qr_code_image = None

    def update_history_display(self):
        # ... (update_history_display method - same as before) ...
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete("1.0", tk.END)
        for item in reversed(self.history): # Display latest first
            history_entry = f"[{item['timestamp']}] Provider: {item['provider']}, Long URL: {item['long_url']}, Shortened: {item['shortened_url']}\n---\n"
            self.history_text.insert(tk.END, history_entry)
        self.history_text.config(state=tk.DISABLED)

    def clear_history(self):
        # ... (clear_history method - same as before) ...
        self.history = []
        self.update_history_display()

    def on_made_by_hover(self, event):
        # ... (on_made_by_hover method - same as before) ...
        self.made_by_label.config(foreground="blue") # Change color on hover

    def on_made_by_leave(self, event):
        # ... (on_made_by_leave method - same as before) ...
        self.made_by_label.config(foreground=self.made_by_label_original_color) # Restore original color


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("950x650") # Slightly wider and taller
    root.minsize(800, 550)
    URLShortenerGUI(root)
    root.mainloop()