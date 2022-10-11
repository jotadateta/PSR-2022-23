#!/usr/bin/env python3



def write(counter_hits):
    f = open("records.txt", "a")
    f.write("Valor obtido de acertos " + str(counter_hits))
    f.write("\n")
    f.close()

#open and read the file after the appending:
#f = open("records.txt", "r")
#print(f.read()) 