def caesar_cipher(raw_text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = alphabet[26-key:]+alphabet[0:(26-key)]
    cipher_text = ""

    for i in range(len(raw_text)):
        char = raw_text[i]
        idx = alphabet.find(char.upper())
        if idx == -1:
            cipher_text = cipher_text + char
        elif char.islower():
            cipher_text = cipher_text + shifted_alphabet[idx].lower()
        else:
            cipher_text = cipher_text + shifted_alphabet[idx] 

    return(cipher_text)

print("Enter your plaintext: ")
plain_text = str(input())
print(caesar_cipher(plain_text,6))
print(caesar_cipher(caesar_cipher(plain_text,6), 26-6))