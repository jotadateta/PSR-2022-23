#!/usr/bin/env python3
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


def my_list(my_list):
    my_list=[]
    for x in range(97,123):
        letter=chr(x)
        my_list.append(letter)
    return my_list

   

def main():
    #lista de letras recebidas
    received_letters = []
    request_letters = []
    
    
    #-h
    parser=argparse.ArgumentParser(
        description='''Definition of test mode ''') 
    parser.add_argument('-utm', '--use_time_mode', action='store_true', 
        help=" Mode: Time")
    parser.add_argument('-mv', '--max_value', type=int_pos, required=False, 
        help=" Input number.")
    args=parser.parse_args()   
   
   
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
    #fica a aguardar 
    readkey()
    
    print('teste')
    #variavel aleatoria
    requested =  random.choice(my_list(''))  
    print('Type letter '+ Fore.YELLOW + requested + Style.RESET_ALL)
    received = readkey()
    
    
    start_time=time.time()
    number_inputs=0

    received_letters.append(received)
    request_letters.append(requested)
    # while loop modo de paragem por tempo
    if args.use_time_mode==True:
        while True:
            ##gera letra aleatória
            end_time=time.time()
            diferenca=end_time-start_time

            if received == chr(32): 
                break
            elif diferenca >=int(args.max_value):
                print(Style.BRIGHT + Fore.RED + str(round(diferenca,3))+Style.RESET_ALL+' segundos. Passou o limite de '+Style.BRIGHT + Fore.GREEN +str(args.max_value)+Style.RESET_ALL+' segundos.')
                break
            elif requested == received:
                print('You typed ' + Fore.GREEN + received + Style.RESET_ALL)
            else:
                print('You typed ' + Fore.RED + received + Style.RESET_ALL)
            
            requested =  random.choice(my_list(''))  
            print('Type letter '+ Fore.YELLOW + requested + Style.RESET_ALL)

            ##read letter input
            received = readkey()
            
            received_letters.append(received)
            request_letters.append(requested)
        
        return received_letters, request_letters   
    else:
        while True:
            ##gera letra aleatória
            number_inputs +=1

            if received == chr(32): 
                break
            elif number_inputs >=int(args.max_value):
                print(Style.BRIGHT + Fore.RED + str(round(diferenca,3))+Style.RESET_ALL+' segundos. Passou o limite de '+Style.BRIGHT + Fore.GREEN +str(args.max_value)+Style.RESET_ALL+' segundos.')
                break
            elif requested == received:
                print('You typed ' + Fore.GREEN + received + Style.RESET_ALL)
            else:
                print('You typed ' + Fore.RED + received + Style.RESET_ALL)
            
            requested =  random.choice(my_list(''))  
            print('Type letter '+ Fore.YELLOW + requested + Style.RESET_ALL)

            ##read letter input
            received = readkey()
            
            received_letters.append(received)
            request_letters.append(requested)
            
        return received_letters, request_letters
        
    
       
        

if __name__ == '__main__':
    main()
