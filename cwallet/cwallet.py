#!/usr/bin/env python3.7

import codecs
import ecdsa
import os
import hashlib
import sys

class wallet:
    def __init__(self):
        private_key = ''
        compressed_public_key = ''
        public_key = b''
        bitcoin_address = b''
        coordinate_vector = []

    def gen_private_key(self):
        private_key = os.urandom(32)
        return private_key.hex()

    def get_public_key(self, private_key):
        private_key = bytes.fromhex(private_key)
        key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1).verifying_key
        key_bytes = key.to_string()
        self.coordinate_vector = [key_bytes[0:32], key_bytes[32:64]]
        key_hex = codecs.encode(key_bytes, 'hex')
        self.public_key = b'04' + key_hex

    def create_compressed_public_key(self):
        last_byte_on_y = self.coordinate_vector[1][-1:]
        last_byte_on_y = int.from_bytes(last_byte_on_y, byteorder='big')
        x = int.from_bytes(self.coordinate_vector[0], byteorder='big')
        if last_byte_on_y % 2 == 0:
            compressed_public_key = bytes.fromhex(hex(x + 0x02)[2:])
        else:
            compressed_public_key = bytes.fromhex(hex(x + 0x03)[2:])
        self.compressed_public_key = compressed_public_key.hex()
        return compressed_public_key.hex()

    def create_bitcoin_address(self):
        public_key = self.compressed_public_key
        public_key_bytes = codecs.decode(public_key, 'hex')
        # Run SHA-256 for the public key
        sha256_bpk = hashlib.sha256(public_key_bytes)
        sha256_bpk_digest = sha256_bpk.digest()
        # Run RIPEMD-160 for the SHA-256
        ripemd160_bpk = hashlib.new('ripemd160')
        ripemd160_bpk.update(sha256_bpk_digest)
        ripemd160_bpk_digest = ripemd160_bpk.digest()
        ripemd160_bpk_hex = codecs.encode(ripemd160_bpk_digest, 'hex')
        mainnetpk = b'00' + ripemd160_bpk_hex
        checksum = self.get_checksum(ripemd160_bpk_hex)
        self.bitcoin_address = mainnetpk + checksum
        return self.bitcoin_address

    def get_checksum(self, public_key):
        # Double SHA256 to get checksum
        sha256_nbpk = hashlib.sha256(public_key)
        sha256_nbpk_digest = sha256_nbpk.digest()
        sha256_2_nbpk = hashlib.sha256(sha256_nbpk_digest)
        sha256_2_nbpk_digest = sha256_2_nbpk.digest()
        sha256_2_hex = codecs.encode(sha256_2_nbpk_digest, 'hex')
        checksum = sha256_2_hex[:8]
        return checksum

    def base58(self, address_hex):
        alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
        b58_string = ''
        # Get the number of leading zeros
        leading_zeros = len(address_hex) - len(address_hex.lstrip('0'))
        # Convert hex to decimal
        address_int = int(address_hex, 16)
        # Append digits to the start of string
        while address_int > 0:
            digit = address_int % 58
            digit_char = alphabet[digit]
            b58_string = digit_char + b58_string
            address_int //= 58
        # Add ‘1’ for each 2 leading zeros
        ones = leading_zeros // 2
        for one in range(ones):
            b58_string = '1' + b58_string
        return b58_string

    def __repr__(self):
        return self.base58(str(self.bitcoin_address)[2:-1])


def main():
    wl = wallet()

    if len(sys.argv) == 1:
        print(wl.gen_private_key())
    if len(sys.argv) == 2:
        private_key = sys.argv[1]
        wl.get_public_key(private_key)
        wl.create_compressed_public_key()
        wl.create_bitcoin_address()
        print(wl)


if __name__=='__main__':
    main()


