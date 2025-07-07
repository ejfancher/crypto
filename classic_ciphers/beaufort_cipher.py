class beaufort_cipher:
    def __init__(self):
        return

    def encrypt(self, plaintext, key):
        if len(key) < len(plaintext):
            print("key must be longer than plaintext")
            return
        key = key.upper().replace(" ", "")
        plaintext = plaintext.upper().replace(" ", "")
        ciphertext = ""

        for i in range(len(plaintext)):
            ciphertext += chr(
                (((ord(key[i]) - 65) - (ord(plaintext[i])) - 65) % 26) + 65
            )
            i += 1
        return ciphertext

    def decrypt(self, ciphertext, key):
        if len(key) < len(ciphertext):
            print("key must be longer than ciphertext")
            return
        key = key.upper().replace(" ", "")
        plaintext = ""

        for i in range(len(ciphertext)):
            plaintext += chr(
                (((ord(key[i]) - 65) - (ord(ciphertext[i]) - 65)) % 26) + 65
            )
            i += 1

        return plaintext
