from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    encrypted_image = Image.new("RGB", image.size)

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            # Simple encryption: add key (modulo 256 to stay in range)
            encrypted_pixel = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )
            encrypted_image.putpixel((x, y), encrypted_pixel)

    encrypted_image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    decrypted_image = Image.new("RGB", image.size)

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            # Reverse the encryption
            decrypted_pixel = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )
            decrypted_image.putpixel((x, y), decrypted_pixel)

    decrypted_image.save(output_path)
    print(f"Decrypted image saved as {output_path}")

def main():
    print("=== Image Encryption Tool ===")
    mode = input("Choose mode: (E)ncrypt or (D)ecrypt: ").strip().upper()
    input_file = input("Enter image file path: ").strip()
    key = int(input("Enter numeric key (1–255): ").strip())
    
    if mode == "E":
        output_file = os.path.splitext(input_file)[0] + "_encrypted.png"
        encrypt_image(input_file, output_file, key)
    elif mode == "D":
        output_file = os.path.splitext(input_file)[0] + "_decrypted.png"
        decrypt_image(input_file, output_file, key)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
