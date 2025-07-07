class poly_alphabetic_cipher:
    def __init__(self):
        None

    def encrypt(self, plaintext, key):
        key = key.upper().replace(" ", "")
        plaintext = plaintext.upper().replace(" ", "")
        ciphertext = ""
        j = 0
        for i in range(len(plaintext)):
            ciphertext += chr(
                (((ord(key[j]) - 65) + (ord(plaintext[i])) - 65) % 26) + 65
            )
            i += 1
            j += 1
            if j >= len(key):
                j = 0
        return ciphertext

    def decrypt(self, ciphertext, key):
        key = key.upper().replace(" ", "")
        plaintext = ""
        j = 0
        for i in range(len(ciphertext)):
            plaintext += chr(
                (((ord(ciphertext[i]) - 65) - (ord(key[j]) - 65)) % 26) + 65
            )
            i += 1
            j += 1
            if j >= len(key):
                j = 0
        return plaintext
