#!/usr/bin/env python3

from collections import namedtuple
from urllib import request
from pprint import pprint
from main import main
from database import write
from colorama import Fore, Back, Style


namedtuples = []

def mainRun():
    hit_sum = 0
    miss_sum = 0 
    inputs = []

    #search variables from main.py
    received_letters, requested_letters, hit_counter, test_duration, test_start_time, test_end_time, accuracy, hit_time, miss_time, duration = main()
    
    #calculate of type average duration 
    if len(received_letters) == 0:
        type_average_duration = 0
    else:
        type_average_duration = round(test_duration/len(received_letters),3)

    #calculate of type_miss_average_duration and type_hit_average_duration
    if len(hit_time) == len(received_letters):
        type_hit_average_duration = type_average_duration
        type_miss_average_duration = 0

    elif len(miss_time) == len(received_letters):
        type_miss_average_duration = type_average_duration
        type_hit_average_duration = 0
        
    else:
        for x in range(len(hit_time)):
            valor_tempo_certas = hit_time[x]
            hit_sum = valor_tempo_certas + hit_sum
            type_hit_average_duration = hit_sum/len(hit_time)


        for i in range(len(miss_time)):
            valor_tempo_erradas = miss_time[i]
            miss_sum = valor_tempo_erradas + miss_sum
            type_miss_average_duration = miss_sum/len(miss_time)
        
    #dictionary to which the values ​​will be indexed
    my_dict = {'accuracy': accuracy,
    'inputs': [],
    'number_of_hits': hit_counter,
    'number_of_types': len(received_letters),
    'test_duration': round(test_duration,3),
    'test_end': test_end_time, 
    'test_start': test_start_time,   
    'type_average_duration': type_average_duration,   
    'type_hit_average_duration': round(type_hit_average_duration,3)  ,   
    'type_miss_average_duration': round(type_miss_average_duration,3)}      
    
    #index 3 variables for input (requested letter,received letter and duration of answering) 
    for x in range(len(requested_letters)):

        namedtuples = (requested_letters[x], received_letters[x], duration[x])
        inputs.append(namedtuples)
          
    my_dict['inputs'] = inputs
    pprint(my_dict)
    write(hit_counter, test_duration)
    return 
    
    
if __name__ == '__main__':
    
    mainRun()