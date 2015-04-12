import os
import re
import sys
import shutil
import urllib
import json
import webbrowser
from settings import settings
import vk_auth


def collect_urls(url_file_path):
    url_file = open(url_file_path).read().decode("utf-8")
    urls = []
    requests_list = json.loads(url_file)
    for request in requests_list:
        url = request['url']
        root_name = request['root_name']
        request.pop('url')
        request.pop('root_name')
        data = urllib.urlencode(request)
        result = urllib.urlopen(url, data).read()
        urls.append({'html': result, 'name': root_name})
        with open(r"results.html", "w") as f:
            f.write(result)
        webbrowser.open(r"results.html")
    print 'Collected'
    return urls


def read_photo_urls(urls):
    regex = re.compile(r'</div><img src=(.*)/><div')
    url_dicts = []
    for url in urls:
        html_string = url['html']
        mid_log = regex.findall(html_string)
        url_dicts.append({'img_url': mid_log, 'name': url['name']})
    for url in url_dicts:
        print url
    print 'HTML parsed'
    return url_dicts


def download_images(url_dicts, to_dir):
    if not os.access(to_dir, os.F_OK):
        os.makedirs(to_dir)
    url_num = 1
    print('Progress: ')
    for url_dict in url_dicts:
        # download photos
        root_name = url_dict['name']
        for url in url_dict['img_url']:
            with urllib.urlopen(url) as response, open(to_dir + '\%s%d.jpg' % (root_name, url_num), 'wb') as out:
                shutil.copyfileobj(response, out)
        print('Uploaded %d parts;' % url_num)
        url_num += 1
    return


def main():
    args = sys.argv[1:]
    print 'works? %s' % settings['VK_login']


if __name__ == '__main__':
    main()