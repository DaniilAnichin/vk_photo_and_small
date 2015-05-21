import os
import shutil
import urllib
import re


def read_photo_urls(url_file_path):
    url_file = open(url_file_path).read().decode("cp1252")
    regex = re.compile(ur'</div><img src="([^<]*\.jpg)" />')
    mid_log = re.findall(regex, url_file)
    """photo_regexp = re.compile(r'https://cs7053.vk.me')
    url_list = []
    for url in mid_log:
        if photo_regexp.match(url):
            url_list.append(url)
    print 'HTML parsed'"""
    return mid_log


def download_images(url_list, to_dir, root_name):
    if not os.access(to_dir, os.F_OK):
        os.makedirs(to_dir)
    url_num = 1
    print('Progress: ')
    for url in url_list:
        # download photos
        out = open(to_dir + '\%s%d.jpg' % (root_name, url_num), 'wb')
        response = urllib.urlopen(url)
        shutil.copyfileobj(response, out)
        out.close()
        print('Uploaded %d parts;' % url_num)
        url_num += 1
    return


def main():
    down_dir = "d:\Dann\Python\small\DPA"
    file_path = "d:\Dann\Python\small\Download_to\urls.txt"
    this_name = 'Solve_DPA_'
    photo_urls = read_photo_urls(file_path)
    download_images(photo_urls, down_dir, this_name)


if __name__ == '__main__':
    main()