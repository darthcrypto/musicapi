#!/bin/env/python

import os
import sys
import argparse

#create the parser
my_parser = argparse.ArgumentParser(description='List the content of a folder')

#add the arguments
my_parser.add_argument('Path',
                        metavar='path',
                        type=str,
                        help='the path to list')
#execute the parse_args() method
args = my_parser.parse_args()

'''
if len(sys.argv) > 2:
    print("You have specified too many arguments")
    sys.exit()

if len(sys.argv) < 2:
    print("You need to specify the path to be listed")
    sys.exit()
'''

input_path = args.path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))
