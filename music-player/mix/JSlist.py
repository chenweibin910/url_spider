# -*- coding:UTF-8 -*-
import json
import os
import re
import time
# import eyed3
# from eyed3 import mp3,utils,plugins,id3
import random
from pypinyin import lazy_pinyin
from mutagen.mp3 import MP3

# songFile = MP3("path")
# title = str(songFile.tags['TIT2'])
# artist = str(songFile.tags['TPE1'])
'''
{
    mp3:'mix/汪苏泷 - 专属味道.mp3',
    title:'专属味道',
    artist:'汪苏泷',
    rating:4,
    duration:'03:33',
    cover:'mix/1.png'
}
'''
FILE_NAME = "myplaylist.js"


def read_data():
    file_list = os.listdir(os.getcwd())
    if FILE_NAME not in file_list:
        os.system("echo =[]>>%s" % FILE_NAME)

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        tmp_str = f.read().split('=')[1].strip().replace(';', '')
        js_list = eval(rep(tmp_str))
    if not js_list:
        js_list = [
            {
                'mp3': 'mix/汪苏泷 - 专属味道.mp3',
                'title': '专属味道',
                'artist': '汪苏泷',
                'cover': 'mix/1.png',
                'rating': 4,
                'duration': '03:33'
            }
        ]
    return js_list


def rep(str):
    return str.replace('mp3:', '"mp3":').replace('title', '"title"').replace('artist', '"artist"'). \
        replace('rating', '"rating"').replace('duration', '"duration"').replace('cover', '"cover"')


def write_data(js_list):
    file_list = os.listdir(os.getcwd())
    new_add = []
    for file in file_list:
        if os.path.isdir(file) or not re.match(r'.+[mp3]$', file):
            continue
        if file.split('-')[0].strip() in str(js_list):
            continue
        if str(file).endswith("1.mp3"):
            continue
        new_add.append(file)
    for item in js_list:
        if item['mp3'].strip("mix/") not in file_list:
            del (js_list[js_list.index(item)])

    for file in new_add:
        newdic = {key: '' for key in js_list[0].keys()}
        total_time = int(MP3(file).info.length)
        min, sec = divmod(total_time, 60)
        duration = str(min) + ":" + "{:02d}".format(sec)
        newdic.update(
            {'mp3': 'mix/' + file,
             'title': file.split(r'.mp3')[0],
             'artist': file.split(r'.mp3')[0].split('-')[0],
             'cover': 'mix/1.png',
             'rating': 4,
             'duration': duration
             }
        )
        js_list.append(newdic)

    js_list.sort(key=lambda x: lazy_pinyin(x["title"]))
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        f.write('var myPlaylist = ' + dis_rep(str(js_list)) + ';')


def dis_rep(str):
    return str.replace("'mp3'", 'mp3').replace("'title'", 'title').replace("'artist'", 'artist'). \
        replace("'rating'", 'rating').replace("'duration'", 'duration').replace("'cover'", 'cover')


if __name__ == '__main__':
    js_list = read_data()
    # print(len(js_list))
    write_data(js_list)
    js_list = read_data()
    print("更新后歌曲数量：", len(js_list))
    # print(os.listdir(os.getcwd()))
