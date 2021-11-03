import os
import re
import math
import string
import sys
import getopt
import numpy as np
import pandas as pd
from scipy import interp
from collections import Counter
from toipa import phonetic
import warnings

# To ignore code warnings at the output. Deactivate this if you modify the code.
warnings.filterwarnings("ignore")


def levenshtein(source, target):
    source_word = range(len(source) + 1)
    target_word = range(len(target) + 1)
    mtable = [[(i if j == 0 else j) for j in target_word] for i in source_word]
    for i in source_word[1:]:
        for j in target_word[1:]:
            deletion_dist = mtable[i - 1][j] + 1
            insertion_dist = mtable[i][j - 1] + 1
            sub_trans_cost = 0 if source[i - 1] == target[j - 1] else 1
            substition_dist = mtable[i - 1][j - 1] + sub_trans_cost
            mtable[i][j] = min(deletion_dist, insertion_dist, substition_dist)
            if i > 1 and j > 1 and source[i - 1] == target[j - 2] \
                    and source[i - 2] == target[j - 1]:
                trans_dist = mtable[i - 2][j - 2] + sub_trans_cost
                mtable[i][j] = min(mtable[i][j], trans_dist)
    distance = mtable[len(source)][len(target)]
    return float(distance) / max(len(source), len(target))


def replacest(text):
    text = text.strip()
    chars = " ˌːˈ\n"
    for symb in text:
        if symb in chars:
            text = text.replace(symb, "")
    return text


def rdlevenshteinphonetics(row):
    t = phonetic(str(row['target']))
    t1 = replacest(t.strip())
    r = phonetic(str(row['response']))
    r1 = replacest(r.strip())
    return levenshtein(t1, r1)


def phonemicdistance(FILE):
    """Calculate phonemic distance"""
    DF = pd.read_csv(FILE)
    DF['target'] = DF.target.str.lower()
    DF['response'] = DF.response.str.lower()
    DF['target'] = DF['target'].str.strip()
    DF['response'] = DF['response'].str.strip()
    EMPTY = DF[DF.response.isna()]
    DF = DF[DF.response.notnull()]
    if DF.empty == False:
        DF['phonological_score'] = DF.apply(rdlevenshteinphonetics, axis=1)
    EMPTY['phonological_score'] = "NA"
    newdf = pd.concat([DF, EMPTY], axis=0)
    return newdf


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('python phonology.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python phonology.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            FILE = arg
            out = phonemicdistance(FILE)
        elif opt in ("-o", "--ofile"):
            outputfile = arg
            out.to_csv(outputfile)
            print("Phonology run without errors. (Remember a phonological distance that is equal to 0 means that the target and the response are the same whereas if it is 1 means that the two words are phonemically dissimilar).")


if __name__ == "__main__":
    main(sys.argv[1:])
