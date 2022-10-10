#!/usr/bin/env python3
import argparse


parser=argparse.ArgumentParser(
    description='''Definition of test mode ''')
parser.add_argument('-utm', '--use_time_mode', action='store_true',
    help=" Max number of secs for time mode or maximum number of inputs for number of inputs mode.")
parser.add_argument('-mv MAX_VALUE', '--max_value MAX_VALUE', action='store_true', 
    help=" Max number of seconds for time mode or maximum number of inputs for number of inputs mode.")
args=parser.parse_args()



print(args)
print(args.max_value)
# args.use_time_mode


def main():
   ""
    
if __name__ == '__main__':
    main()
