#!/usr/bin/env python3.7

"""
Name: Evan Fancher
Assignment: ECIES
Description: performs RSA public key cryptography
"""

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import codecs
import argparse

class rsa_key_exchange:
    def __init__(self):
        pass

    #The following code generates public key stored in receiver.pem and private key stored in private.pem.
    # These files will be used in the examples below. Every time, it generates different public key and private key pair.
    def gen_keys(self):
        key = RSA.generate(2048)
        private_key = key.export_key()

        public_key = key.publickey().export_key()

        return "RSA PRIVATE KEY:\n"+private_key.hex()+"\n\nRSA PUBLIC KEY:\n"+public_key.hex()


    # The following code encrypts a piece of data for a receiver we have the RSA public key of.
    # The RSA public key is stored in a file called receiver.pem.
    def encrypt(self, ptFile, publicKey):
        pt = open(ptFile, "r")
        data = pt.read().encode("utf-8")

        file_out = open(ptFile, "wb")
        recipient_key = RSA.import_key(publicKey)

        session_key = get_random_bytes(16)

        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)

        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)

        [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]

    # The receiver has the private RSA key. They will use it to decrypt the session key first, and with that the rest of the file:
    def decrypt(self, ctFile, privateKey):
        file_in = open(ctFile, "rb")

        private_key = RSA.import_key(privateKey)

        enc_session_key, nonce, tag, ciphertext = \
            [file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        # Decrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)

        file_out = open(ctFile, "w")
        file_out.write(data.decode("utf-8"))

def main():

    rsa = rsa_key_exchange()

    get = argparse.ArgumentParser()
    get.add_argument("fileName", help="the file to encrypt or decrypt", nargs='?', default="")
    get.add_argument("key", help="the public or private key", nargs='?', default="")
    get.add_argument("-e", help="encrypt", action="store_true")
    get.add_argument("-d", help="decrypt", action="store_true")

    args = get.parse_args()

    if args.fileName!='' and args.key!='' and args.e:
        rsa.encrypt(args.fileName, codecs.decode(args.key, encoding='hex'))
    elif args.fileName!='' and args.key!='' and args.d:
        rsa.decrypt(args.fileName, codecs.decode(args.key, encoding='hex'))
    elif args.fileName=='' and args.key=='' and not args.e and not args.d:
        print(rsa.gen_keys())

if __name__=='__main__':
    main()