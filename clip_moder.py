#!/usr/bin/python
# -*- coding: utf-8 -*-
import Tkinter
import sys


_eng_chars = u'''~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?'''
_rus_chars = u'''ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,'''


def transliteration(trans_table):
    window = Tkinter.Tk()
    buffer = window.clipboard_get()
    if buffer == '':
        raise EmptyBufferError("Buffer mustn't be empty")
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append(u''.join([trans_table.get(c, c) for c in buffer]))
    window.destroy()


class WrongParameterError(ValueError):
    pass


class EmptyBufferError(ValueError):
    pass


def main():
    args = sys.argv[1:]
    if args == [] or args[0] != '-r' and args[0] != '-e':
        raise WrongParameterError('must be called like [clip_moder.py -e/-r]')
    if args[0] == '-e':
        trans_table = dict(zip(_rus_chars, _eng_chars))
    elif args[0] == '-r':
        trans_table = dict(zip(_eng_chars, _rus_chars))
    else:
        trans_table = {}

    transliteration(trans_table)


if __name__ == '__main__':
    main()