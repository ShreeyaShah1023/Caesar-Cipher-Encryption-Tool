def caesar(text, shift):
    return "".join(
        chr((ord(c) - (65 if c.isupper() else 97) + shift) % 26 + (65 if c.isupper() else 97))
        if c.isalpha() else c for c in text
    )

text = input("Enter message: ")
shift = int(input("Shift value: "))
choice = input("Encrypt or Decrypt (e/d): ").lower()

shift = -shift if choice == "d" else shift
print("Result:", caesar(text, shift))
