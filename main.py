#!/usr/bin/env python3
import argparse
from collections import namedtuple
import string
import random
import time
from urllib import request
from colorama import Fore, Back, Style
from readchar import readkey, key

def int_pos(s: str)  -> int:
    # torna o tipo de numero inteiro positivo

    try:
        v=int(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f'expected integer, got {s!r}')
    if v<=0:
        raise argparse.ArgumentTypeError(f'expected positive integer, got {v}')
    return v


def obter_args(args):
    return args['use_time_mode'], args['max_value']


def main():
    #-h
    parser=argparse.ArgumentParser(
        description='''Definition of test mode ''') 
    parser.add_argument('-utm', '--use_time_mode', action='store_true', 
        help=" Mode: Time")
    parser.add_argument('-mv', '--max_value', type=int_pos, required=False, 
        help=" Input number.")
    args=parser.parse_args()


    use_time_mode, max_value = obter_args(args)
    
    # data= {
    #     'accuracy': 0.0,
    #     'inputs': [],
    #     'number_of_hits': 0,
    #     'number_of_types': 0,
    #     'test_duration': 0.0,
    #     'test_end': '',
    #     'test_start': '',
    #     'type_average_duration': 0.0,
    #     'type_hit_average_duration': 0.0,
    #     'type_miss_average_duration': 0.0
    # }
   
    # para saber como se chamam as variaveis de entrada
        # print(args)
        # print(args.use_time_mode) #string o valor
        # print(args.max_value) #o valor sai em string
    print(vars(args))
    print(Style.BRIGHT + Fore.RED + 'PARI '+Style.RESET_ALL+"Typing Test, group 5, October 2022")

    # detetar o modo se é por tempo ou tentativas.
    if args.use_time_mode==True:
        if str(args.max_value)=='None':
            print('Insert a mv MAX_NUMBER')
        else:
            print('Test runnin up to '+ str(args.max_value) + ' seconds')
    else:
        print('Test runnin up to '+ str(args.max_value) + ' inputs')

    #basta clicar numa tecla para continuar o programa
    print('Press any key to start the test')  
    k = readkey()

    #Input = namedtuple('Input',([requested,received,duration]))
    

    inicial_time = time()
    
    # while loop
    while True:

        #start game time
        count_time = time()

        #gera letra aleatória
        requested =  random.choice(string.ascii_letters)  
        print('Type letter'+ Fore.YELLOW + requested + Style.RESET_ALL)

        #read letter input
        received = readkey()
        if requested == ' ':
            break
        elif requested == received:
            print('You typed ' + Fore.GREEN + received + Style.RESET_ALL)
        else:
            print('You typed ' + Fore.RED + received + Style.RESET_ALL)

        



            









    

    
if __name__ == '__main__':
    main()
