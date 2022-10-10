#!/usr/bin/env python3

from input import *


number_of_hits = 12
number_of_types = 4
test_duration = 0.3213
test_end = "Terça"
test_start = "Terça mais logo"
type_average_duration = 0.3133
type_hit_average_duration = 0.0
type_miss_average_duration = 3123.0


def main():
    
    #dicionario ao qual se vai indexar os valores
    namedtuples = {'accuracy': 0.0,
    'inputs': [],
    'number_of_hits': [],
    'number_of_types': [],
    'test_duration': [],
    'test_end': [],
    'test_start': [],
    'type_average_duration': [],
    'type_hit_average_duration': [],
    'type_miss_average_duration': []}
    
    
    
    # criar a lista de inputs
    requested = 1
    received = 1
    duration = 52.42
    
    inputs = []
    
    for x in range(3):

        
        requested += 1
        received += 2
        duration += 4

        input = Input(requested, received, duration)
        inputs.append(input)
        
        
        
    ##################################################
    namedtuples['inputs'] = inputs
    #print(inputs[0])
    
    
    # Iterate over the keys in dictionary, access value & print line by line
    for key in namedtuples:
        print(key, ' : ', namedtuples[key])
    
    
    #print (namedtuples)
    
    
    
if __name__ == '__main__':
    
    main()