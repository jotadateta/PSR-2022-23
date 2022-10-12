#!/usr/bin/env python3

#imports

import argparse
from collections import namedtuple
import string
import random
import sys
from time import time, ctime
from urllib import request
from colorama import Fore, Back, Style
from readchar import readkey, key


# function to test if number is positive
def posInt(s: str) -> int:          
    
    try:
        v = int(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f'expected integer, got {s!r}')
    if v <= 0:
        raise argparse.ArgumentTypeError(f'expected positive integer, got {v}')
    return v

# function to define the output letters 
def outputLetter(output_list):               
    output_list = []
    for x in range(97,123):
        letter = chr(x)
        output_list.append(letter)
    return output_list


#main function
def main():

    received_letters = [] #list of received letters
    requested_letters = [] #list of requested letters 
    duration = [] #Duration of the minigame
    hit_time = []  #time of corrected answers
    miss_time = [] #time of incorrected answers
    
    
    # Definition of arguments for the inputs 
    
    parser=argparse.ArgumentParser(
        description = '''Definition of test mode ''') 
    parser.add_argument('-utm', '--use_time_mode', action='store_true', 
        help = " Mode: Time")
    parser.add_argument('-mv', '--max_value',nargs='?', const=10, type=posInt, required=True,
        help = " Input number.")
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()   
    
    print(str(args.max_value))
    
   
    
    # Initial print
    print(Style.BRIGHT + Fore.RED + 'PARI '+Style.RESET_ALL+"Typing Test, group 5, October 2022")

    # detect which mode is active and assosiate the arguments
    if args.use_time_mode == True:
        if str(args.max_value) == 'None':
            print('ERROR: Insert a -mv (MAX_NUMBER)')
            sys.exit(1)
        else:
            print('Test running up to '+Style.BRIGHT + Fore.GREEN + str(args.max_value) + ' seconds'+Style.RESET_ALL)
    else:
        print('Test running up to '+Style.BRIGHT + Fore.GREEN+ str(args.max_value) + ' inputs'+Style.RESET_ALL)

    
    # Standby, waiting for the user to press any key 
    print(Style.BRIGHT + Fore.BLUE+'Press any key to start the test'+Style.RESET_ALL)   
    readkey()
    
    
    # timmers and counters
    start_time = time()
    test_start_time = ctime()
    number_characters = -1
    hit_counter = 0
    
    
    # condition for the time mode
    if args.use_time_mode == True:
        #Creation of while loop to control the break
        while True:

            end_time = time()
            diferenca = end_time - start_time  #counts time for each
            
            if diferenca <= int(args.max_value):

                # minigame concept 
                requested = random.choice(outputLetter(''))  
                print('Type letter '+ Fore.YELLOW + requested + Style.RESET_ALL)
                received = readkey()

                # break if user press spacebar 
                if received == chr(32): 
                    test_end_time = ctime()
                    break
                else:
                                
                    # correct answer 
                    if requested == received:
                        print('You typed ' + Fore.GREEN + received + Style.RESET_ALL)
                        hit_counter += 1
                        hit_end_time = time()
                        tempo_certo = hit_end_time-end_time
                        duration.append(round(tempo_certo,3))
                        hit_time.append(tempo_certo)
                    # incorrect answer
                    else:
                        print('You typed ' + Fore.RED + received + Style.RESET_ALL)
                        end_time_errado = time()
                        tempo_errado = end_time_errado-end_time
                        duration.append(round(tempo_errado,3))
                        miss_time.append(tempo_errado)
            else:
                # when you stop playing because of time 
                print(Style.BRIGHT + Fore.RED + str(round(diferenca,3)) + Style.RESET_ALL + ' segundos. Passou o limite de ' + Style.BRIGHT + Fore.GREEN + str(args.max_value) + Style.RESET_ALL + ' segundos.')
                test_end_time = ctime()
                break
            
            received_letters.append(received)
            requested_letters.append(requested)

    # condition for the max value game 
    else:
        #Creation of while loop to control the break
        while True:
            end_time = time()
            diferenca = end_time - start_time 
        
            number_characters += 1 #counter of characters answered
            
            if number_characters < int(args.max_value):

                #minigame concept
                requested = random.choice(outputLetter(''))  
                print('Type letter ' + Fore.YELLOW + requested + Style.RESET_ALL)
                received = readkey()
                
                # break if user press spacebar 
                if received == chr(32):
                    test_end_time = ctime() 
                    break
                else:
                    
                    # correct answer
                    if requested == received:
                        print('You typed ' + Fore.GREEN + received + Style.RESET_ALL)
                        hit_counter += 1
                        hit_end_time = time()
                        tempo_certo = hit_end_time - end_time
                        duration.append(round(tempo_certo,3))
                        hit_time.append(tempo_certo)
                    # incorrect answer
                    else:
                        print('You typed ' + Fore.RED + received + Style.RESET_ALL)
                        end_time_errado = time()
                        tempo_errado  = end_time_errado - end_time
                        duration.append(round(tempo_errado,3))
                        miss_time.append(tempo_errado)
            else:
                # when you stop playing because of time  
                print(Style.BRIGHT + Fore.RED + str(number_characters) + Style.RESET_ALL + ' characters. Reached the limit of ' + Style.BRIGHT + Fore.GREEN + str(args.max_value) + Style.RESET_ALL + ' characters.')
                test_end_time = ctime()
                break
            
            received_letters.append(received)
            requested_letters.append(requested)

    #determine accuracy. if it had no right answers accuracy = 0
    if len(requested_letters) == 0:
        accuracy = 0
    else:
        accuracy = round(hit_counter/len(requested_letters),3)

    return received_letters, requested_letters, hit_counter,diferenca ,test_start_time,test_end_time, accuracy, hit_time, miss_time, duration
        
    
if __name__ == '__main__':
    main()
