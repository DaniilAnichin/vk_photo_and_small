#!/usr/bin/python
import sys
from datetime import datetime

from itertools import cycle


cycle_nums = [i for i in range(39, 60) + [32, 33, 34, 63, 95] + range(65, 91) + range(97, 123)]
cycle_code = []
for i in range(26):
    cycle_code.append(chr(cycle_nums[i]))
    cycle_code.append(chr(cycle_nums[i + 26]))
    cycle_code.append(chr(cycle_nums[i + 52]))
cycle_code.append('\n')
cycle_code.append('\t')
cycle_code.append('\r')
cycle_code.append('\x85')
cycle_code.append('\x91')
cycle_code.append('\x92')
cycle_code.append('\x93')
cycle_code.append('\x94')
cycle_code.append('\xa0')
cycle_code.append('\x96')
cycle_code.append('\xe7')
cycle_code.append('\xf3')
cycle_code.append('\xe0')
cycle_code.append('\xe9')
cycle_code.append('$')
cycle_code.append('\xf6')
cycle_code.append('\xe4')
len_dict = len(cycle_code)


def comparator(value, key):
    return [[ch[0], ch[1]] for ch in zip(value, cycle(key))]


def full_encode(value, key):
    coded_val = [cycle_code.index(v[0]) - cycle_code.index(v[1]) for v in comparator(value, key)]
    return ''.join([cycle_code[num] for num in coded_val])


def full_decode(value, key):
    coded_val = [cycle_code.index(v[0]) + cycle_code.index(v[1]) - len_dict for v in comparator(value, key)]
    return ''.join([cycle_code[num] for num in coded_val])


def main():
    start_time = datetime.now()
    args = sys.argv[1:]
    args[1] = open(args[1], 'r').read()
    if args[0] == 'from':
        print(full_decode(args[1], args[2]))
    elif args[0] == 'to':
        print(full_encode(args[1], args[2]))
    else:
        print('Nein, nicht heute')
    finish_time = datetime.now()
    print(str(finish_time - start_time))


if __name__ == '__main__':
    main()
