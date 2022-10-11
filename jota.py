#!/usr/bin/env python3

#jota

from collections import namedtuple
from urllib import request
from input import *
from pprint import pprint
from main import main

number_of_hits = 12
number_of_types = 4
test_duration = 0.3213
test_end = "Terça"
test_start = "Terça mais logo"
type_average_duration = 0.3133
type_hit_average_duration = 0.0
type_miss_average_duration = 3123.0

namedtuples = []

def main_jota():
    inputs = []
    received_letters, requested_letters = main()
    print(received_letters)
    
    #print('received' + str(received_letters) + 'requested' + str(requested_letters)) 
    
    #dicionario ao qual se vai indexar os valores
    my_dict = {'accuracy': [],
    'inputs': [],
    'number_of_hits': [],
    'number_of_types': [],
    'test_duration': [],
    'test_end': [],
    'test_start': [],
    'type_average_duration': [],
    'type_hit_average_duration': [],
    'type_miss_average_duration': []}
    
    
    duration = 32.42
    
    print(len(requested_letters))
    
    for x in range(len(requested_letters)):

        duration += 4

        namedtuples = (requested_letters[x], received_letters[x], duration)
        inputs.append(namedtuples)
        
        
        
    ##################################################
    my_dict['inputs'] = inputs
    #print(inputs[0])
    
    ###metodo para o print normal#####
    # Iterate over the keys in dictionary, access value & print line by line
    #for key in namedtuples:
    #    print(key, ' : ', namedtuples[key])
    
    
    
    pprint(my_dict)
    
    
    
if __name__ == '__main__':
    
    main_jota()