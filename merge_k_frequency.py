#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 복수의 빈도 파일을 병합하는 프로그램

import sys
import heapq

###############################################################################
def merge_k_sorted_freq(input_files):
    '''
    input_files : list of input filenames (frequency files; 2 column format)
    '''
    fins = []
    k = len(input_files)
    heap = []
    finished = [False for _ in range(k)] # [False] * k

    for i in range(k):
        fins.append(open(input_files[i]))
        line = fins[i].readline().rstrip().split('\t')
        heapq.heappush(heap, [line[0], int(line[1]), i])

    curr = heapq.heappop(heap)
    line = fins[curr[2]].readline().rstrip().split('\t')
    heapq.heappush(heap, [line[0], int(line[1]), curr[2]])

    while False in finished:

        temp = heapq.heappop(heap)

        if temp[0] == curr[0]:
            curr[1] += temp[1]
            curr[2] = temp[2]
        else:
            print(curr[0], curr[1], sep = '\t')
            curr = temp

        line = fins[curr[2]].readline().rstrip().split('\t')

        if len(line) == 2:
            heapq.heappush(heap, [line[0], int(line[1]), curr[2]])
        else:
            finished[curr[2]] = True
            continue

    print(curr[0], curr[1], sep = '\t')

    for i in range(k):
        fins[i].close()

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()

    merge_k_sorted_freq( sys.argv[1:])