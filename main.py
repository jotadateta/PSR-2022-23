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




def int_pos(s: str)  -> int:
    
    # function to make the number positive

    try:
        v=int(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f'expected integer, got {s!r}')
    if v<=0:
        raise argparse.ArgumentTypeError(f'expected positive integer, got {v}')
    return v


# defenition of the list of outputs avaible for the minigame
def my_list(my_list):
    my_list=[]
    for x in range(97,123):
        letter=chr(x)
        my_list.append(letter)
    return my_list


#main function
def main():

    
    received_letters = [] #list of received letters
    
    request_letters = [] #list of minigame letters requested
    
    duracao=[] #Duration of the minigame
    
    tempo_das_certas=[]  #time of corrected answers
    
    tempo_das_erradas=[] #time of incorrected answers
    
    
    # Definition of arguments fo the inputs 
    
    parser=argparse.ArgumentParser(
        description='''Definition of test mode ''') 
    parser.add_argument('-utm', '--use_time_mode', action='store_true', 
        help=" Mode: Time")
    parser.add_argument('-mv', '--max_value', type=int_pos, required=False, 
        help=" Input number.")
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args=parser.parse_args()   
    
    print(str(args.max_value))
    
   
    # Just for testing (ignore)
        # print(args)
        # print(args.use_time_mode) 
        # print(args.max_value) 
        #print(vars(args))      ########################## Perguntar ao carlos porque converte para um dicionario
    
    # Initial print
    print(Style.BRIGHT + Fore.RED + 'PARI '+Style.RESET_ALL+"Typing Test, group 5, October 2022")

    # detect wich mode is active and assosiate the arguments
    
    if args.use_time_mode==True:
        if str(args.max_value)=='None':
            print('ERROR: Insert a -mv (MAX_NUMBER)')
            sys.exit(1)
        else:
            print('Test runnin up to '+Style.BRIGHT + Fore.GREEN + str(args.max_value) + ' seconds'+Style.RESET_ALL)
    else:
        print('Test runnin up to '+Style.BRIGHT + Fore.GREEN+ str(args.max_value) + ' inputs'+Style.RESET_ALL)

    
    # Standby, waiting for the user to press any key 
    print('Press any key to start the test')   
    readkey()
    
    
    # random variable ( just for testing 
    # requested =  random.choice(my_list(''))  
    # print('Type letter '+ Fore.YELLOW + requested + Style.RESET_ALL)
    # received = readkey()
    
    
    
    # timmers functions
    start_time=time()
    start_c=ctime()
    number_characters=-1
    counter_points = 0
    
    #print(str(start_time))


    # first try but after we make other file because of the different menbers working in the project
    # received_letters.append(received)
    # request_letters.append(requested)
    
# Creation of while loop to control the break 
    # condition for the time mode
    if args.use_time_mode==True:
        while True:
                
            end_time =time()
            diferenca = end_time - start_time  
            
            if diferenca <= int(args.max_value):

                # minigame concept 
                requested =  random.choice(my_list(''))  
                print('Type letter '+ Fore.YELLOW + requested + Style.RESET_ALL)
                received = readkey()

                # break if user press spacebar 
                if received == chr(32): 
                    tempo_final=ctime()
                    break
                else:
                    #print(Style.BRIGHT + Fore.RED + str(round(diferenca,3))+Style.RESET_ALL+' segundos. Passou o limite de '+Style.BRIGHT + Fore.GREEN +str(args.max_value)+Style.RESET_ALL+' segundos.')
                    
                    # correct answer 
                    if requested == received:
                        print('You typed ' + Fore.GREEN + received + Style.RESET_ALL)
                        counter_points += 1
                        end_time_certo=time()
                        tempo_certo=end_time_certo-end_time
                        duracao.append(round(tempo_certo,3))
                        tempo_das_certas.append(tempo_certo)
                    # incorrect answer
                    else:
                        print('You typed ' + Fore.RED + received + Style.RESET_ALL)
                        end_time_errado=time()
                        tempo_errado=end_time_errado-end_time
                        duracao.append(round(tempo_errado,3))
                        tempo_das_erradas.append(tempo_errado)
            else:
                # activate when you went of the loop for the time 
                print(Style.BRIGHT + Fore.RED + str(round(diferenca,3))+Style.RESET_ALL+' segundos. Passou o limite de '+Style.BRIGHT + Fore.GREEN +str(args.max_value)+Style.RESET_ALL+' segundos.')
                tempo_final=ctime()
                break
            
            
            received_letters.append(received)
            request_letters.append(requested)
    # condition for the max value game 
    else:
        while True:
            end_time = time()
            diferenca = end_time - start_time 
        
            number_characters +=1 
            
            if number_characters < int(args.max_value):

                #minigame concept
                requested =  random.choice(my_list(''))  
                print('Type letter '+ Fore.YELLOW + requested + Style.RESET_ALL)
                received = readkey()

                if received == chr(32):
                    tempo_final=ctime() 
                    break
                else:
                    #print(Style.BRIGHT + Fore.RED + str(round(diferenca,3))+Style.RESET_ALL+' segundos. Passou o limite de '+Style.BRIGHT + Fore.GREEN +str(args.max_value)+Style.RESET_ALL+' segundos.')
                    if requested == received:
                        print('You typed ' + Fore.GREEN + received + Style.RESET_ALL)
                        counter_points += 1
                        end_time_certo=time()
                        tempo_certo=end_time_certo-end_time
                        duracao.append(round(tempo_certo,3))
                        tempo_das_certas.append(tempo_certo)
                    else:
                        print('You typed ' + Fore.RED + received + Style.RESET_ALL)
                        end_time_errado=time()
                        tempo_errado=end_time_errado-end_time
                        duracao.append(round(tempo_errado,3))
                        tempo_das_erradas.append(tempo_errado)
            else:
                print(Style.BRIGHT + Fore.RED + str(number_characters)+Style.RESET_ALL+' caracters. Atingiu o limite de '+Style.BRIGHT + Fore.GREEN +str(args.max_value)+Style.RESET_ALL+' caracters.')
                tempo_final=ctime()
                break
            
            
            received_letters.append(received)
            request_letters.append(requested)
    if len(request_letters)==0:
        accuracy=0
    else:
        accuracy = counter_points/len(request_letters)
            #type_average_duration = round(diferenca/ len(received_letters),3)
    return received_letters, request_letters, counter_points, diferenca,start_c,tempo_final, accuracy, tempo_das_certas, tempo_das_erradas, duracao
        

    
            

if __name__ == '__main__':
    main()
