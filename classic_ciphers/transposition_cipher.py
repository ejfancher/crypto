import math

class nihilists_cipher:
    def __init__(self):
        None

    def key_to_alpha_rank(self, key):
        key = key.lower()
        ord_of_key = []
        for char in key:
            ord_of_key += [ord(char)]
        key_alpa_ranks = []
        for elem1 in ord_of_key:
            my_rank = 0
            for elem2 in ord_of_key:
                if elem1 > elem2:
                    my_rank += 1
            while my_rank in key_alpa_ranks:
                my_rank += 1
            key_alpa_ranks += [my_rank]
        return key_alpa_ranks

    def text_to_box1(self, text, dim):
        box1 = [[0 for i in range(dim)] for k in range(dim)]
        k = 0
        for i in range(dim):
            for j in range(dim):
                if k < len(text):
                    box1[i][j] = text[k]
                else:
                    box1[i][j] = 'z'
                j += 1
                k += 1
            i += 1
        return box1

    def box_to_text(self, box, dim):
        text = ''
        for i in range(dim):
            for j in range(dim):
                text += box[i][j]
                j += 1
        return text

    def encrypt(self, plaintext, key):
        dim = len(key)
        key = key.lower()
        plaintext = plaintext.replace(' ','')
        if math.pow(dim, dim) < len(plaintext):
            print('For the nihilist\'s cifer, the plaintext can only be the length of the key squared number of characters')
            return
        key_alpha_ranks = self.key_to_alpha_rank(key)
        box1 = self.text_to_box1(plaintext, dim)
        box2 = [[0 for i in range(dim)] for k in range(dim)]

        for i in range(dim):
            for j in range(dim):
                box2[key_alpha_ranks.index(i)][key_alpha_ranks.index(j)] = box1[i][j]
                j += 1
            i += 1
        ciphertext = self.box_to_text(box2, dim)
        return ciphertext

    def decrypt(self, ciphertext, key):
        dim = len(key)
        key = key.lower()
        box2 = [[0 for i in range(dim)] for k in range(dim)]
        key_alpha_ranks = self.key_to_alpha_rank(key)
        box1 = self.text_to_box1(ciphertext, dim)
        for i in range(dim):
            for j in range(dim):
                box2[key_alpha_ranks[i]][key_alpha_ranks[j]] = box1[i][j]
                j += 1
            i += 1
        plaintext = self.box_to_text(box2, dim)
        return plaintext