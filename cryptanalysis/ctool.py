#!/usr/bin/env python
import numpy as np
import argparse

class ctool:

    def __init__(self):
        pass

    def get_char_frequencies(self, text):
        """
        Get the frequency distribution of all english language alphabetic characters in a text

        :param text: a text string
        :return: a string representing the frequency distribution
        """
        alpha_index = np.zeros(128, dtype=np.int16)
        for char in text:
            if ord(char) > 127:
                continue
            alpha_index[ord(char)] += 1
        out_str = ''
        for i in range(128):
            if alpha_index[i] != 0 and chr(i).isalpha():
                out_str += chr(i) + ':' + str(alpha_index[i])+', '
        return out_str

    def get_ngram_frequencies(self, text, n, alpha_only=True):
        """
        Get the frequency distribution of ngrams in a text

        :param text: the text as a string
        :param n: the length of the ngram
        :param alpha_only: whether or not to find english alphabetic ngrams only
        :return: a string representing the frequency distribution of ngrams of specified length in the text
        """
        BMAX = len(text)
        if n > BMAX:
            print("cannot find ngrams of length greater than the text")
            return
        ngs = ['' for i in range(BMAX)]     # list of unique ngrams scanned
        ngc = np.array([-1 for i in range(BMAX)], dtype=np.int16)   # for int A, ngc[A] is the number of ngs[A]'s found
        for i in range(len(text)-n+1):
            ngram = text[i:i + n]
            if alpha_only and not ngram.isalpha():
                continue
            for j in range(BMAX):
                if ngs[j] == ngram:
                    ngc[j] += 1
                    break
                elif ngs[j] == '':
                    ngs[j] = ngram
                    ngc[j] = 1
                    break
        out_str = ''
        for i in range(len(ngs)):
            if ngc[i] == -1:
                break
            cur_ind = ngc.argmax()
            out_str += str(ngs[cur_ind]) + ':' + str(ngc[cur_ind])+', '
            ngc[cur_ind] = -2
        return out_str

    def get_possible_periods(self, text, print_repeat=False):
        """
        search for repeats of ngrams in the text to help identify a period which could help identify the length
        of the keyword used if the ciphertext was produced by periodic polyalpabetic cipher

        :param text: the text to be analyzed as a string
        :param print_repeat: whether or not to return information on the repeats that are found
        :return: a string composed of info about suggested periods and possibly info about the repeats that are found
        """
        out_str1, out_str2 = '', ''
        repeat_info, lpr = [], []
        ri_row = 0
        text = text

        for cut_sz in range(len(text)/2, 1, -1):
            cut_history = np.empty(shape=(0, 2), dtype=object)
            for offset in range(cut_sz):
                start_ind = offset
                while start_ind+(cut_sz-1) < len(text):
                    cur_cut = text[start_ind:(start_ind + cut_sz)]
                    if cur_cut in cut_history:
                        match_start_ind = cut_history[np.where(cut_history == cur_cut)[0][0]][1]
                        period = max(start_ind, match_start_ind) - min(start_ind, match_start_ind)
                        if period not in lpr:
                            lpr += [period]
                        if print_repeat:
                            repeat_info += [[cur_cut, start_ind, str(np.take(cut_history,
                                        np.where(cut_history == cur_cut)[0][0], axis=0)[0]), match_start_ind, period]]
                            ri_row += 1
                    cut_history = np.append(cut_history, np.array([[cur_cut, start_ind]], dtype=object), axis=0)
                    start_ind += cut_sz

        print_history = []
        for i in range(ri_row):
            if repeat_info[i][1] < repeat_info[i][3]:
                if [repeat_info[i][1], repeat_info[i][3]] not in print_history:
                    out_str2 += ('\t' + repeat_info[i][0] + ' (start ind: ' + str(repeat_info[i][1]) + ') : ' \
                              + repeat_info[i][2] + ' (start ind: ' \
                              + str(repeat_info[i][3]) + ') suggests ' + str(repeat_info[i][4])) + '\n'
                    print_history += [[repeat_info[i][1], repeat_info[i][3]]]
            else:
                if [repeat_info[i][3], repeat_info[i][1]] not in print_history:
                    out_str2 += ('\t' + repeat_info[i][2] + \
                              ' (start ind: ' + str(repeat_info[i][3]) + ') : ' + repeat_info[i][0] + ' (start ind: ' \
                              + str(repeat_info[i][1]) + ') suggests ' + str(repeat_info[i][4])) + '\n'
                    print_history += [[repeat_info[i][3], repeat_info[i][1]]]
        out_str1 = 'likely multiples of the period length: ' + str(lpr)
        return out_str1 + '\n' + out_str2


def main():
    """
    Provide the argument input capabilities and act as the driver for the program
    """
    get = argparse.ArgumentParser()
    get.add_argument("file", help="path of file containing the text to be analyzed (relative to the directory ctool.py is in)")
    get.add_argument("-c", help="display frequency distrubution of characters in the file", action="store_true")
    get.add_argument("-n", help="enter the length of ngram after this option to display the frequency distrubution of "
                                "such ngrams in the text")
    get.add_argument("-p", help="display possible periods based on repeats found in the text", action="store_true")
    get.add_argument("-d", help="supplementary to -p, display detailed information on the repeats found",
                     action="store_true")
    args = get.parse_args()
    if (args.d and not args.p) or (not args.file):
        print("invalid input")
        return
    file = open(args.file, 'r')
    text = file.read().replace(' ','').replace('\t','').replace('\n','').upper()
    functionality = ctool()
    if args.c:
        print(functionality.get_char_frequencies(text)+'\n')
    if args.n:
        print(functionality.get_ngram_frequencies(text, int(args.n))+'\n')
    if args.p and not args.d:
        print(functionality.get_possible_periods(text)+'\n')
    if args.p and args.d:
        print(functionality.get_possible_periods(text, True))

if __name__ == '__main__':
    main()