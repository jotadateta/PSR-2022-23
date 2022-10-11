import argparse
from collections import namedtuple
import string
import random
import time
from urllib import request
from colorama import Fore, Back, Style
from readchar import readkey, key
import time

def int_pos(s: str)  -> int:
    # torna o tipo de numero inteiro positivo

    try:
        v=int(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f'expected integer, got {s!r}')
    if v<=0:
        raise argparse.ArgumentTypeError(f'expected positive integer, got {v}')
    return v


def main():

    #-h
    parser=argparse.ArgumentParser(
        description='''Definition of test mode ''') 
    parser.add_argument('-utm', '--use_time_mode', action='store_true', 
        help=" Mode: Time")
    parser.add_argument('-mv', '--max_value', type=int_pos, required=False, 
        help=" Input number.")
    args=parser.parse_args()
    