
command line interface: 

python3.7 driver.py [-e for encyrpt/-d for decrypt] [-k [key] all but caesars need this] text caesar|trans|simple|poly|beaufort

(also can use --help)




ciphers:
Caesar cipher: Caesar cipher
source: Lecture

encryption/decryption function inputs:       
    plain/ciphertext: of any length

encryption/decryption function outputs:      
    cipher/plaintext



Transposition cipher: The Nihilist's Cipher
source: https://github.com/CryptoUSF/Course-Material/blob/master/references/books/1911%20-%20Manual%20of%20Cryptography.pdf

encryption/decryption function inputs:       
    plain/ciphertext: can be at longest len(key)^2 chars long
    key: try to keep it relatively close to, but still greater than: log2(len(plaintext)) 

encryption/decryption function outputs:      
    cipher/plaintext



Simple substitution cipher: The Wolseley or Sudan Cipher 
source: https://github.com/CryptoUSF/Course-Material/blob/master/references/books/1911%20-%20Manual%20of%20Cryptography.pdf

encryption/decryption function inputs:
    plain/ciphertext: Text of any length.
    key: any length

encryption/decryption function outputs: 
    cipher/plaintext



Poly-alphabetic cipher: Vigenere cipher
source: Lecture

encryption/decryption function inputs:
    plain/ciphertext: Text of any length.
    key: any length

encryption/decryption function outputs: 
    cipher/plaintext



5th cipher: Beaufort cipher
source: https://github.com/CryptoUSF/Course-Material/blob/master/references/books/1911%20-%20Manual%20of%20Cryptography.pdf

encryption/decryption function inputs:
    plain/ciphertext: any length
    key: len(key) >= len(cipher/plaintext )

encryption/decryption function outputs:
    cipher/plaintext 



All tested thoroughly for their ability to encrypt and decrypt text of the english alphabet with spaces.
