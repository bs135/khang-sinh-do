"""
Module documentation.
"""

import sys
#import os
import pylab
import random
import networkx as nx
import argparse


def get_input():
    print('usage: [--flags options] [inputs] ')


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--flags options] [inputs] ')
        sys.exit(1)


# Main body
if __name__ == '__main__':
    main()
