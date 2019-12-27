# Dyck Word Generator

Python 3 script for generating random [Dyck words](https://en.wikipedia.org/wiki/Dyck_language). A Dyck word is a balanced string of parentheses.

## Background

This script supplements the paper:  
**Skachkova, N., Trost, T. A., Kusmirek, A., & Klakow, D.** (2018, November). *Closing brackets with recurrent neural networks.*
In Proceedings of the 2018 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP (pp. 232-239)  
https://www.aclweb.org/anthology/W18-5425.pdf

For an explanation of how the words are generated, see Section 2 and in particular Section 2.1.

## Usage

The script can either be used from the command line or it can be imported as a Python module. The options are easily reviewed by invoking the script with the typical help option:

```
python3 generate.py --help
```
