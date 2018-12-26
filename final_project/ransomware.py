#!/usr/bin/env python3.7

"""
Name: Evan Fancher
Assignment: Final Project
Description: provides encryption with RSA public key cryptography as
well as encryption and decryption with AES in CTR mode
"""

import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import argparse
import codecs

class AES_CTR:
    def encrypt(self, file, key):
        content = open(file, 'r')
        data = content.read()

        cipher = AES.new(key, AES.MODE_CTR)
        ct_bytes = cipher.encrypt(bytes(data, 'iso-8859-1'))

        content = open(file, 'wb')
        content.write(codecs.encode(ct_bytes, 'hex')+b' ')
        content.close()
        return cipher.nonce

    def decrypt(self, file, key, nonce):
        content = open(file, 'r')
        text = bytes.fromhex(content.read())

        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
        pt = cipher.decrypt(text)

        content = open(file, 'wb')
        content.write(pt)

class RSA_ENCRYPT:
    def encrypt(self, ptFile, publicKey):
        pt = open(ptFile, "r")
        data = pt.read().encode("utf-8")

        file_out = open(ptFile, "wb")
        recipient_key = RSA.import_key(publicKey)

        session_key = get_random_bytes(16)

        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)

        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)

        [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]


def main():
    aes_cipher = AES_CTR()
    rsa = RSA_ENCRYPT()

    get = argparse.ArgumentParser()
    get.add_argument("file", help="w/ the text to *cipher")
    get.add_argument("key", nargs='?', help="the key")
    get.add_argument("nonce", nargs='?', help="the nonce")
    get.add_argument("-aes", help="encrypt", action="store_true")
    get.add_argument("-rsa", help="encrypt", action="store_true")
    get.add_argument("-e", help="encrypt", action="store_true")
    get.add_argument("-d", help="decrypt", action="store_true")

    args = get.parse_args()

    if args.aes and args.e:
        key = os.urandom(16)
        nonce = aes_cipher.encrypt(args.file, key)
        file = open('sym_key', "w+")
        file.write(key.hex()+' '+nonce.hex())
    elif args.aes and args.d:
        aes_cipher.decrypt(args.file, bytes.fromhex(args.key), bytes.fromhex(args.nonce))
    elif args.file!='' and args.key!='' and args.rsa:
        rsa.encrypt(args.file, codecs.decode(args.key, encoding='hex'))


if __name__ == '__main__':
    main()
