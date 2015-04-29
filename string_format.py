__author__ = 'Dann'
import re
import sys


def main():
    args = sys.argv[1:]
    if args[0] == '--to_format':
        original = args[1]
    else:
        print 'usage: [--to_format what_to_format]'
        sys.exit(1)

    divided = re.split('\.|\s|_|", "|,', original)
    ready_to_merge = []
    for word in divided:
        ready_to_merge.append(word.lower())
    result_string = '_'.join(ready_to_merge)
    print result_string


if __name__ == '__main__':
    main()