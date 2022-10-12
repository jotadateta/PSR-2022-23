#!/usr/bin/env python3

def write(hit_counter, test_duration):
    f = open("records.txt", "a")
    f.write("Valor obtido de acertos " + str(hit_counter) + " com o tempo de " + str(round(test_duration,3)))
    f.write("\n")
    f.close()

