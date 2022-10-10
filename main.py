#!/usr/bin/env python3
import argparse

def int_pos(s: str)  -> int:
    try:
        v=int(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f'expected integer, got {s!r}')
    if v<=0:
        raise argparse.ArgumentTypeError(f'expected positive integer, got {v}')
    return v


def main():
    #-h
    parser=argparse.ArgumentParser(
        description='''Definition of test mode ''') 
    parser.add_argument('-utm', '--use_time_mode', type=int_pos, 
        help=" Max number of seconds.")
    parser.add_argument('-mv', '--max_value', type=int_pos, required=False, 
        help=" maximum number of inputs.")
    args=parser.parse_args()


    # para saber como se chamam

    # print(args)
    print(args.use_time_mode)
    print(args.max_value)


if __name__ == '__main__':
    main()
