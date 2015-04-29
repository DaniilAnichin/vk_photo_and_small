import os
import sys
import shutil
import urllib


photo_urls = ['https://pp.vk.me/c621631/v621631609/26513/pv_gR0CaCgw.jpg',
              'https://pp.vk.me/c621631/v621631609/2651d/IGTlqfdBHwI.jpg',
              'https://pp.vk.me/c621631/v621631609/26527/fXUhYSwaHh0.jpg',
              'https://pp.vk.me/c621631/v621631609/26531/FzCrfcOxsfU.jpg',
              'https://pp.vk.me/c621631/v621631609/2653b/QcyY2hb_MlY.jpg',
              'https://pp.vk.me/c621631/v621631609/26545/k5RLwBUpX_Y.jpg',
              'https://pp.vk.me/c621631/v621631609/2654f/rVEzNEiG3FM.jpg',
              'https://pp.vk.me/c621631/v621631609/26559/OEdggXHcqPQ.jpg',
              'https://pp.vk.me/c621631/v621631609/26563/GN9zkGvIU8s.jpg',
              'https://pp.vk.me/c621631/v621631609/2656d/6eg4WWJHF1E.jpg',
              'https://pp.vk.me/c621631/v621631609/26577/PFcZGIYmFwY.jpg',
              'https://pp.vk.me/c621631/v621631609/26581/kIQSOYx5U6A.jpg',
              'https://pp.vk.me/c621631/v621631609/2658b/aJbR-36GV94.jpg',
              'https://pp.vk.me/c621631/v621631609/26595/v6399EakZYY.jpg',
              'https://pp.vk.me/c621631/v621631609/2659f/4LizyFOsYKo.jpg',
              'https://pp.vk.me/c621631/v621631609/265a9/WEgnCidRVpU.jpg',
              'https://pp.vk.me/c621631/v621631609/265b3/BDnaIQTW-wM.jpg',
              'https://pp.vk.me/c621631/v621631609/265bd/HY4Pgv8waRg.jpg']

this_name = 'Mir_IAR_'


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
    args = sys.argv[1:]
    down_dir = args[0]

    download_images(photo_urls, down_dir, this_name)


if __name__ == '__main__':
    main()