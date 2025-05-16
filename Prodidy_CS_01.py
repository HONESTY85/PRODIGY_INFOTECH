import tkinter as tk
from tkinter import filedialog, messagebox

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def brute_force(text):
    results = []
    for s in range(26):
        results.append(f"Shift {s}: {decrypt(text, s)}")
    return "\n".join(results)

def process_file(filename, shift, mode):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()

    if mode == "encrypt":
        output = encrypt(data, shift)
    else:
        output = decrypt(data, shift)

    output_file = filename.replace(".txt", f"_{mode}.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)

    return output_file

# GUI Code
def run_gui():
    def perform_action():
        text = text_input.get("1.0", tk.END).strip()
        mode = mode_var.get()
        shift_val = shift_input.get()

        if mode == "brute":
            result = brute_force(text)
        else:
            if not shift_val.isdigit():
                messagebox.showerror("Error", "Shift must be an integer")
                return
            shift = int(shift_val)
            if mode == "encrypt":
                result = encrypt(text, shift)
            elif mode == "decrypt":
                result = decrypt(text, shift)
        result_output.delete("1.0", tk.END)
        result_output.insert(tk.END, result)

    def handle_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not file_path:
            return
        try:
            shift = int(shift_input.get())
            output_file = process_file(file_path, shift, mode_var.get())
            messagebox.showinfo("Success", f"Processed file saved to:\n{output_file}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Main window
    root = tk.Tk()
    root.title("Caesar Cipher Toolkit")

    tk.Label(root, text="Enter text:").pack()
    text_input = tk.Text(root, height=5, width=50)
    text_input.pack()

    tk.Label(root, text="Shift:").pack()
    shift_input = tk.Entry(root)
    shift_input.pack()

    mode_var = tk.StringVar(value="encrypt")
    tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="encrypt").pack()
    tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="decrypt").pack()
    tk.Radiobutton(root, text="Brute Force Decrypt", variable=mode_var, value="brute").pack()

    tk.Button(root, text="Run", command=perform_action).pack(pady=5)
    tk.Button(root, text="Encrypt/Decrypt File", command=handle_file).pack(pady=5)

    tk.Label(root, text="Result:").pack()
    result_output = tk.Text(root, height=10, width=50)
    result_output.pack()

    root.mainloop()

if __name__ == "__main__":
    run_gui()

