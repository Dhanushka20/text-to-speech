import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from gtts import gTTS
import os
import tempfile
import subprocess

# Function to convert text to speech and play it for testing
def text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Text field is empty.")
        return

    lang = languages[language_var.get()]
    if lang == "Select Language":
        messagebox.showerror("Error", "Please select a language.")
        return

    try:
        # Generate the speech
        tts = gTTS(text=text, lang=lang)

        # Save the speech to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            tts.save(temp_audio.name)
            temp_audio_path = temp_audio.name

        # Play the speech using the appropriate system command
        if os.name == 'nt':  # For Windows
            os.system(f'start {temp_audio_path}')
        elif os.name == 'posix':  # For Unix-based systems (Linux, macOS)
            subprocess.call(['mpg123', temp_audio_path])
        else:
            messagebox.showerror("Error", "Unsupported OS.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to convert text to speech and save to file
def save_audio():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Text field is empty.")
        return

    lang = languages[language_var.get()]
    if lang == "Select Language":
        messagebox.showerror("Error", "Please select a language.")
        return

    try:
        # Generate the speech
        tts = gTTS(text=text, lang=lang)

        # Ask user for file save location
        file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            # Save the speech to file
            tts.save(file_path)
            messagebox.showinfo("Success", "Audio saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Setting up the main application window
app = tk.Tk()
app.title("Text to Speech Application")
app.geometry("400x300")

# Label for the text entry
text_label = tk.Label(app, text="Enter Text:")
text_label.pack(pady=10)

# Text entry field
text_entry = tk.Text(app, height=5, width=40)
text_entry.pack(pady=5)

# Dropdown menu for language selection
language_var = tk.StringVar(value="Select Language")
languages = {"Select Language": None, "English": "en", "Sinhala": "si", "Tamil": "ta"}

language_menu = ttk.OptionMenu(app, language_var, *languages.keys())
language_menu.pack(pady=10)

# Button to trigger text-to-speech conversion and test speech
test_button = tk.Button(app, text="Test Speech", command=text_to_speech)
test_button.pack(pady=10)

# Button to trigger text-to-speech conversion and save audio
save_button = tk.Button(app, text="Save Audio", command=save_audio)
save_button.pack(pady=10)

# Run the application
app.mainloop()
