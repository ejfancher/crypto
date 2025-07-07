import cesaer_cipher as cc, simple_substitution_cipher as ssc, transposition_cipher as tc, poly_alphabetic_cipher as pac, beaufort_cipher as bc

import argparse


def main():
    get = argparse.ArgumentParser()
    get.add_argument("text", help="the plaintext or ciphertext")
    get.add_argument("-e", help="encrypt the given plaintext", action="store_true")
    get.add_argument("-d", help="decrypt the given ciphertext", action="store_true")
    get.add_argument("-k", help="keyword for the cipher")
    get.add_argument(
        "cipher",
        help="enter 'caesar' for caesar cipher, \
        cipher, 'simple' for simple substitution cipher, 'poly' for poly-alphabetic cipher, \
        'trans' for transposition cipher, 'beaufort' for beaufort cipher",
    )
    args = get.parse_args()
    if args.e and args.d:
        print("Cannot encrypt and decrypt simultaneously")
        return

    cipher = None

    if args.cipher == "caesar":
        cipher = cc.caesar_cipher()
    elif args.cipher == "simple":
        cipher = ssc.simple_substitution()
    elif args.cipher == "poly":
        cipher = pac.poly_alphabetic_cipher()
    elif args.cipher == "trans":
        cipher = tc.nihilists_cipher()
    elif args.cipher == "beaufort":
        cipher = bc.beaufort_cipher()
    if cipher is not None:
        if args.e:
            print(cipher.encrypt(args.text, args.k))
        elif args.d:
            print(cipher.decrypt(args.text, args.k))


if __name__ == "__main__":
    main()
