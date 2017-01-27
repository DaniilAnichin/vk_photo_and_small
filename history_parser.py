#!/usr/bin/python3
# -*- coding: utf-8 -*- #
import os
import re
import sys
import shutil
from urllib.request import urlopen


def is_photo_line(line):
    return line.startswith('vk.com/photo') and \
           not 'https://vk.com/images/x_null.gif' in line


def is_audio_line(line):
    return line.startswith('vk.com/audio')


def make_search_query(line):
    """
    Turns vkotp history line into search query
    :param line: line of the history; example:
    # vk.com/audio?id=26280299&audio_id=90272004 : Пятница - Забери
    :return: vk.com search query
    """
    replace_index_start = line.index('audio_id')
    replace_index_end = line.index(' : ', replace_index_start)
    query = line[:replace_index_start] + 'q=' + line[replace_index_end + 3:]
    return query


def get_photos_list(lines):
    """
    This function can separate photo urls from other data in vk chat history
    :param lines: list of the history lines
    :return: list of the photo urls
    """
    photo_lines = list(filter(is_photo_line, lines))
    url_lines = list(map(lambda x: x[x.index(':') + 2:-1], photo_lines))

    return url_lines


def get_audio_list(lines):
    audio_lines = list(filter(is_audio_line, lines))
    search_lines = list(map(make_search_query, audio_lines))
    return search_lines


def get_plain_text(lines):
    """
    This function can make vk history readable
    :param lines: list of the history lines
    :return: list of the plain text lines, pretty-formatted
    """
    author_re = re.compile(r'.*\(\d{2}:\d{2}:\d{2} {2}\d{2}/\d{2}/\d{4}\):')
    is_attachment = False
    plain_lines = []
    level = 0
    for line in lines:
        if is_attachment:
            if line == '\t' * level + ']\n':
                is_attachment = False
            if 'Attachments:[\n' in line:
                plain_lines.append('пересланные вложения')
        else:
            if 'Attachments:[\n' in line:
                level = line.count('\t')
                # Removing blank line and author
                plain_lines.pop()
                plain_lines.pop()
                is_attachment = True
            else:
                if author_re.match(line):
                    # This line tells us about message author, we'll intend it
                    if plain_lines:
                        plain_lines.pop()
                    plain_lines.append(' ' * 4 + line)
                else:
                    plain_lines.append(line)

    return plain_lines


def download_photos(urls, dirname, prefix):
    """
    This function downloads photos one by one into the dirname with names
    like prefix0000
    :param urls: list of the photo urls
    :param dirname: dir to save files
    :param prefix: photo prefix
    :return: None
    """
    print('Started')
    max_len = len(str(len(urls) + 1))
    for i, url in enumerate(urls):
        full_name = os.path.join(dirname, prefix + str(i + 1).zfill(max_len))
        with urlopen(url) as response, open(full_name, 'wb') as out:
            shutil.copyfileobj(response, out)
        print('{0}/{1}'.format(i + 1, len(urls) + 1))
    print('Finished')


functions = {
    'plain': get_plain_text,
    'audio': get_audio_list,
    'photo': get_photos_list
}


def get_part_of(filename, datatype=None):
    """

    :param filename: name of the history file
    :param datatype: some of values: plain, audio, photo
    :return:
    """
    if not datatype:
        for datatype in functions.keys():
            get_part_of(filename, datatype=datatype)
        return

    with open(filename, 'r') as out:
        lines = out.readlines()

    raw_name, extension = os.path.splitext(filename)
    new_name = '_'.join([raw_name, datatype + extension])
    function = functions.get(datatype)
    if not function:
        return
    with open(new_name, 'w') as out:
        out.writelines(function(lines))


def main():
    args = sys.argv[1:]
    filename = args.pop(0)
    datatype = args.pop(0)
    get_part_of(filename=filename, datatype=datatype)


if __name__ == "__main__":
    main()


'''

with open('messages_Полина Никитина(86455230).txt' as out:
with open('messages_Полина Никитина(86455230).txt', 'r') as out:
    start_lines = out.readlines()
len(start_lines)
for i, line in enumerate(start_lines):
    if line.startswith('Attachments:['):
        pass
new_lines = [
]
for i, line in enumerate(start_lines):
    if line.startswith('Attachments:['):
        for line in start_lines[i:]:
            new_lines.append(line)
            if ']' in line:
                break
len(new_lines)
with open('messages_clear_v1.txt', 'w') as out:
    out.writelines(new_lines)
lines = new_lines
new_lines = []
for line in lines:
    if not line.startswith('Attach'):
        if line.startswith(']'):
            new_lines.append('\n')
        else: new_lines.append(line)
with open('messages_clear_v2.txt', 'w') as out:
    out.writelines(new_lines)
lines = new_lines
new_lines = []
for line in lines:
    if line.startswith('vk.com/photo'):
        new_lines.append(line[line.index(':') + 1 : ])
with open('messages_clear_v3.txt', 'w') as out:
    out.writelines(new_lines)
new_lines = []
for line in lines:
    if not line.startswith('vk.com/photo'):
        new_lines.append(line)
with open('messages_no_photo.txt', 'w') as out:
    out.writelines(new_lines)
lines = new_lines
new_lines = []
new_lines = list(filter(lambda x: !x.startswith('vk.com/audio'), lines))
new_lines = list(filter(lambda x: not x.startswith('vk.com/audio'), lines))
len(new_line) - len(lines)
len(new_lines) - len(lines)
with open('messages_no_photo_audio.txt', 'w') as out:
    out.writelines(new_lines)
with open('messages_clear_v3.txt', 'r') as out:
    photo_lines = out.readlines()
normal_lines = list(filter( lambda x: x != ' https://vk.com/images/x_null.gif ))
normal_lines = list(filter( lambda x: x != ' https://vk.com/images/x_null.gif', photo_lines ))
len(photo_lines) - len(normal_lines)
photo_lines[4]
normal_lines = list(filter( lambda x: x != ' https://vk.com/images/x_null.gif\n', photo_lines ))
len(photo_lines) - len(normal_lines)
with open('messages_photo.txt', 'w') as out:
    out.writelines(normal_lines)
clear_lines = list(map( lambda x: x[1:], normal_lines))
with open('messages_photo.txt', 'w') as out:
    out.writelines(clear_lines)
'''
