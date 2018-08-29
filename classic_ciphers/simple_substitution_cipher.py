import string

class simple_substitution:
    def __init__(self):
        None

    def get_cipher_alpha(self, key):
        c_alpha = []
        for char in key:
            if char not in c_alpha:
                c_alpha.append(char)
        for char in string.ascii_uppercase:
            if char not in c_alpha:
                c_alpha.append(char)
        return c_alpha

    def encrypt(self, plain_text, key):
        key = key.upper().replace(' ','')
        plain_text = plain_text.upper().replace(' ','')
        cipher_text = ''
        c_alpha = self.get_cipher_alpha(key)
        for char in plain_text:
            ind = 24 - c_alpha.index(char)
            cipher_text += c_alpha[ind]
        return cipher_text

    def decrypt(self, cipher_text, key):
        plain_text = ''
        key = key.upper().replace(' ', '')
        c_alpha = self.get_cipher_alpha(key)
        for char in cipher_text:
            ind = 24 - c_alpha.index(char)
            plain_text += c_alpha[ind]
        return plain_text