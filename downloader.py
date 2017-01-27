# -*- coding: utf-8 -*- #
import os
import shutil
import urllib
import re


def read_photo_urls(url_file_path):
    # url_file = open(url_file_path).read().decode("cp1252")
    # regex = re.compile(ur'</div><img src="([^<]*\.jpg)" />')
    # mid_log = re.findall(regex, url_file)
    """photo_regexp = re.compile(r'https://cs7053.vk.me')
    url_list = []
    for url in mid_log:
        if photo_regexp.match(url):
            url_list.append(url)
    print 'HTML parsed'"""
    with open(url_file_path, 'r') as out:
        mid_log = map(lambda x: x[:-1], out.readlines())
    return mid_log


def download_images(url_list, to_dir, root_name):
    if not os.access(to_dir, os.F_OK):
        os.makedirs(to_dir)
    url_num = 1
    print('Progress: ')
    for url in url_list:
        # download photos
        out = open(os.path.join(to_dir, '%s%d.jpg' % (root_name, url_num)), 'wb')
        response = urllib.urlopen(url)
        shutil.copyfileobj(response, out)
        out.close()
        print('Uploaded %d parts;' % url_num)
        url_num += 1
    return


def main():
    down_dir = u"/home/anichindaniil/Изображения/Саша ДР"
    file_path = u"/home/anichindaniil/new/Рабочий стол/messages_photo_S.txt"
    this_name = 'Poli_'
    photo_urls = read_photo_urls(file_path)
    download_images(photo_urls, down_dir, this_name)


if __name__ == '__main__':
    main()
