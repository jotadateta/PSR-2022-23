#!/usr/bin/env python3

#jota

from collections import namedtuple
from urllib import request
from pprint import pprint
from main import main


namedtuples = []


def main_jota():
    soma_certas=0
    soma_erradas=0
    inputs = []
    received_letters, requested_letters, counter_points, test_duration, start_c, tempo_final, accuracy, tempo_das_certas, tempo_das_erradas, duracao = main()
    #print("letras recebidas " + str(received_letters))
    #print("certas " + str(counter_points))
    

    type_average_duration=round(test_duration/len(received_letters),3)

    if len(tempo_das_certas)==len(received_letters):
        type_hit_average_duration=type_average_duration
        type_miss_average_duration=0

    elif len(tempo_das_erradas)==len(received_letters):
        type_miss_average_duration=type_average_duration
        type_hit_average_duration=0
        
    else:
        for x in range(len(tempo_das_certas)):
            valor_tempo_certas=tempo_das_certas[x]
            soma_certas = valor_tempo_certas + soma_certas
            type_hit_average_duration=soma_certas/len(tempo_das_certas)


        for i in range(len(tempo_das_erradas)):
            valor_tempo_erradas = tempo_das_erradas[i]
            soma_erradas = valor_tempo_erradas + soma_erradas
            type_miss_average_duration = soma_erradas/len(tempo_das_erradas)
        
    #dicionario ao qual se vai indexar os valores
    my_dict = {'accuracy': accuracy,
    'inputs': [],
    'number_of_hits': counter_points,
    'number_of_types': len(received_letters),
    'test_duration': round(test_duration,3),
    'test_end': [tempo_final],     
    'test_start': [start_c],   
    'type_average_duration': type_average_duration,   
    'type_hit_average_duration': round(type_hit_average_duration,3)  ,   
    'type_miss_average_duration': round(type_miss_average_duration,3)}      
    
    
     
    for x in range(len(requested_letters)):

        namedtuples = (requested_letters[x], received_letters[x], duracao[x])
        inputs.append(namedtuples)
        
        
        
        
        
    ##################################################
    my_dict['inputs'] = inputs
    #print(inputs[0])
      
    pprint(my_dict)
    

    
    
    
if __name__ == '__main__':
    
    main_jota()