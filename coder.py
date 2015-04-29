#!/usr/bin/python
import sys

from itertools import cycle


cycle_nums = [i for i in range(39, 60) + [32, 33, 34, 63, 95] + range(65, 91) + range(97, 123)]
cycle_code = []
for i in range(26):
    cycle_code.append(chr(cycle_nums[i]))
    cycle_code.append(chr(cycle_nums[i + 26]))
    cycle_code.append(chr(cycle_nums[i + 52]))


def comparator(value, key):
    return [[ch[0], ch[1]] for ch in zip(value, cycle(key))]


def full_encode(value, key):
    coded_val = [cycle_code.index(v[0]) - cycle_code.index(v[1]) for v in comparator(value, key)]
    return ''.join([cycle_code[num] for num in coded_val])


def full_decode(value, key):
    coded_val = [cycle_code.index(v[0]) + cycle_code.index(v[1]) - 78 for v in comparator(value, key)]
    return ''.join([cycle_code[num] for num in coded_val])


def main():
    args = sys.argv[1:]
    if args[0] == 'from':
        print full_decode(args[1], args[2])
    elif args[0] == 'to':
        print full_encode(args[1], args[2])
    else:
        print 'Nein, nicht heute'


if __name__ == '__main__':
    main()