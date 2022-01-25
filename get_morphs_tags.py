#!/usr/bin/env python3
# coding: utf-8

import sys

def get_morphs_tags(tagged):
    l = []
    t = ()
    s = ''
    for i in range(len(tagged)):
        if len(t) == 0:
            if tagged[i] == '/' and tagged[i+1] == '/':
                t = ('/', )
            elif i > 0 and tagged[i] == '/' and tagged[i-1] == '+':
                t = ('+', )
                s = ''
            elif tagged[i] == '/':
                t = (s, )
                s = ''
            else:
                s += tagged[i]
        elif len(t) == 1:
            if t[0] == '/' and tagged[i] == '/':
                continue
            elif tagged[i] == '+':
                t += (s, )
                l.append(t)
                s = ''
                t = ()
            elif i == len(tagged) - 1:
                s += tagged[i]
                t += (s, )
                l.append(t)
                s = ''
                t = ()
            else:
                s += tagged[i]
    return l    

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print( "[Usage]", sys.argv[0], "in-file", file=sys.stderr)
        sys.exit()

    with open(sys.argv[1]) as fin:

        for line in fin.readlines():

            # 2 column format
            segments = line.split('\t')

            if len(segments) < 2: 
                continue

            # result : list of tuples
            result = get_morphs_tags(segments[1].rstrip())
        
            for morph, tag in result:
                print(morph, tag, sep='\t')