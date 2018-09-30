#!/usr/bin/env python3.7

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import argparse

class RC4:
    def KSA(self, key):
        n = len(key)
        S = list(range(256))
        j = 0
        for i in range(256):
            j = (j + S[i] + key[i % n]) % 256
            S[i], S[j] = S[j], S[i]
        return S

    def gen_keystream(self, S, m):
        i = 0
        j = 0
        KS = [0] * 256
        for b in range(m):
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            KS[b] = S[(S[i] + S[j]) % 256]
        return KS

    def get_keystream(self, key, pt_len):
        S = self.KSA(key)
        return self.gen_keystream(S, pt_len)

    def encrypt(self, key, text, decrypt=False):
        if decrypt:
            text = bytes.fromhex(text)
        else:
            text = [ord(c) for c in text]
        key = [ord(c) for c in key]
        keystream = self.get_keystream(key, len(text))
        res = b''
        for i in range(len(text)):
            val = bytes(chr(text[i] ^ keystream[i]), 'iso-8859-1')
            res += val;
        return res

class AES:
    def encrypt(self, text, key, iv):
        backend = default_backend()
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
        encryptor = cipher.encryptor()
        ct = encryptor.update(bytes(text, 'iso-8859-1')) + encryptor.finalize()
        return ct

    def decrypt(self, text, key, iv):
        backend = default_backend()
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
        decryptor = cipher.decryptor()
        pt = decryptor.update(text) + decryptor.finalize()
        return pt

def main():
    rc4_cipher = RC4()
    aes_cipher = AES()

    get = argparse.ArgumentParser()
    get.add_argument("text", help="the text to *cipher")
    get.add_argument("key", nargs='?', help="the key")
    get.add_argument("iv", nargs='?', help="initial value")
    get.add_argument("-rc4", help="Use RC4 cipher", action="store_true")
    get.add_argument("-aes", help="Use AES", action="store_true")
    get.add_argument("-e", help="encrypt", action="store_true")
    get.add_argument("-d", help="decrypt", action="store_true")

    args = get.parse_args()

    if args.rc4:
        if args.e:
            encrypted = rc4_cipher.encrypt(args.key, args.text)
            print(encrypted.hex())
        elif args.d:
            encrypted = rc4_cipher.encrypt(args.key, args.text, True)
            print(encrypted.decode('utf-8'))
    elif args.aes:
        if args.e:
            for i in range(16 - (len(args.text) % 16)):
                args.text += ' '
            key = os.urandom(32)
            iv = os.urandom(16)
            print('%s %s %s' % (aes_cipher.encrypt(args.text, key, iv).hex(), key.hex(), iv.hex()))
        elif args.d:
            print(aes_cipher.decrypt(bytes.fromhex(args.text), bytes.fromhex(args.key), bytes.fromhex(args.iv)))

if __name__ == '__main__':
    main()
