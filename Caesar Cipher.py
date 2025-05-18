# caesar_cipher.py

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char  # Non-alphabet characters remain unchanged
    return result

if __name__ == "__main__":
    # Sample usage
    plaintext = input("Enter text: ")
    shift = int(input("Enter shift value: "))
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

    result = caesar_cipher(plaintext, shift, mode)
    print(f"Result: {result}")
