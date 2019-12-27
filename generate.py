#!/usr/bin/env python3

"""
Generator for Dyck words.

For an explanation see Section 2 and in particular Section 2.1 of:
Skachkova, N., Trost, T. A., Kusmirek, A., & Klakow, D. (2018, November). Closing brackets with recurrent neural networks.
In Proceedings of the 2018 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP (pp. 232-239)
https://www.aclweb.org/anthology/W18-5425.pdf

Author: Thomas A. Trost <ttrost@lsv.uni-saarland.de>
"""

import random
from typing import Dict


def generate(words: int, p: float, parentheses: Dict[str, str], seed: int = None, delim: str = ' ') -> str:
    """
    Generator for Dyck words.
    :param words: number of words to generate
    :param p: probability of adding an opening parenthesis; must be between 0 and 0.5,
        otherwise infinite length words become likely and there is a high risk of overflows
    :param parentheses: dictionary that maps available opening to closing parenthesis, e.g. {'(': ')', '[': ']'}
    :param seed: random seed for initializing random generator for reproducibility
    :param delim: delimiter for connecting the parentheses
    """
    random.seed(seed)
    count = 0
    opening = list(parentheses.keys())
    while count < words:
        count += 1
        dyck_word = random.choice(opening)
        stack = [dyck_word]
        while len(stack) > 0:
            if random.random() < p:
                # open another parenthesis
                choice = random.choice(opening)
                stack.append(choice)
            else:
                # close a parenthesis
                choice = parenthesis[stack.pop()]
            dyck_word += delim + choice
        yield dyck_word


if __name__ == '__main__':

    # get arguments from command line
    import argparse

    def check_positive_int(value):
        """Check if value is a positive integer."""
        int_val = int(value)
        if int_val <= 0:
            raise argparse.ArgumentTypeError("{} is negative or invalid".format(value))
        return int_val

    def check_probability(value):
        """Check if value is a float between 0 and 1 (not inclusive, see paper)"""
        p_val = float(value)
        if not 0. < p_val < .5:
            raise argparse.ArgumentTypeError("{} is not a probability between 0 and 0.5".format(value))
        return p_val

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-w', metavar='NATURAL_NUMBER', required=True, type=check_positive_int,
                        help='number of words to generate')
    parser.add_argument('-p', metavar='FLOAT', required=True, type=check_probability,
                        help='probability for adding an opening parenthesis')
    parser.add_argument('-n', metavar='NATURAL_NUMBER', default=1, type=check_positive_int,
                        help='number of kinds of parentheses')
    parser.add_argument('-s', metavar='INTEGER', type=int, help='random seed')
    parser.add_argument('-d', metavar='STRING', type=str, help='delimiter for separating parenthesis', default=' ')
    args = parser.parse_args()

    # generate dictionary of matching parenthesis
    parenthesis = {'(': ')'} if args.n == 1 else {'({}'.format(i): '){}'.format(i) for i in range(args.n)}

    # generate words and print to stdout
    for word in generate(args.w, args.p, parenthesis, seed=args.s, delim=args.d):
        print(word)
