class caesar_cipher:
    def __init__(self):
        return None

    def encrypt(self, plain_text, ignore):
        plain_text = plain_text.upper().replace(" ", "")
        cipher_text = ""
        for char in plain_text:
            tf = ord(char) + 3
            if tf > 90:
                tf = 64 + tf - 90
            tf = chr(tf)
            cipher_text += tf
        return cipher_text

    def decrypt(self, cifer_text, ignore):
        plain_text = ""
        for char in cifer_text:
            tf = ord(char) - 3
            if tf < 65:
                tf = 91 - (65 - tf)
            tf = chr(tf)
            plain_text += tf
        return plain_text
