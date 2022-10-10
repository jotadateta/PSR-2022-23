#!/usr/bin/env python3
import argparse


def main():
    #-h
    parser=argparse.ArgumentParser(
        description='''Definition of test mode ''')
    parser.add_argument('-utm', '--use_time_mode', type=int, required=False,
        help=" Max number of secs for time mode or maximum number of inputs for number of inputs mode.")
    parser.add_argument('-mv', '--max_value', type=int, required=False, 
        help=" Max number of seconds for time mode or maximum number of inputs for number of inputs mode.")
    args=parser.parse_args()


    # para saber como se chamam
    # print(args)
    # print(args.use_time_mode)
    # print(args.max_value)
    
if __name__ == '__main__':
    main()
