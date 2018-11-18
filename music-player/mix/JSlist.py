# -*- coding:UTF-8 -*-
import json
import execjs
import os
import re
import time
# import eyed3
# from eyed3 import mp3,utils,plugins,id3
import random

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


def openFile():

    fileList = os.listdir(os.getcwd())
    if not 'myplaylist.js' in fileList:
        os.system('echo =[]>>myplaylist.js')

    with open('myplaylist.js', 'r', encoding='utf-8') as file_obj:
        res = execjs.compile(file_obj.read())._source
        tmp_str = res.split('=')[1].strip().replace(';', '')
        tmp_str = rep(tmp_str)
        js_list = eval(tmp_str)
        file_obj.close()
        if not js_list:
            js_list = [{'mp3': 'mix/汪苏泷 - 专属味道.mp3', 'title': '专属味道', 'artist': '汪苏泷', 'cover': 'mix/1.png', 'rating': 4,
                    'duration': '03:33'},
                   {'mp3': 'mix/july - in love.mp3', 'title': 'in love', 'artist': 'july', 'cover': 'mix/1.png',
                    'rating': 4,
                    'duration': '03:53'},
                   {'mp3': 'mix/sara、孙子涵 - 请安静的忘记我.mp3', 'title': '请安静的忘记我', 'artist': 'sara、孙子涵', 'cover': 'mix/1.png',
                    'rating': 4, 'duration': '04:07'},
                   {'mp3': 'mix/马頔 - 南山南.mp3', 'title': '马頔 - 南山南', 'artist': '马頔', 'cover': 'mix/1.png', 'rating': 4,
                    'duration': '05:24'}]
        return js_list


def rep(str):
    return str.replace('mp3:', '"mp3":').replace('title', '"title"').replace('artist', '"artist"').replace(
        'rating', '"rating"').replace('duration', '"duration"').replace('cover', '"cover"')


def writeFlie(js_list):

    fileList = os.listdir(os.getcwd())
    addList = []
    for file in fileList:
        if not os.path.isdir(file) and re.match(r'.+[mp3]$', file):
            if file.split('-')[0].strip() in str(js_list):
                continue
            addList.append(file)
    for file in addList:
        newdic = {key: '' for key in js_list[0].keys()}
        newdic.update(
                    {'mp3': 'mix/' + file,
                     'title': file.split(r'.mp3')[0],
                     'artist': file.split(r'.mp3')[0].split('-')[0],
                     'cover': 'mix/1.png',
                     'rating': 4,
                     'duration': '0' + str(int(random.randrange(1, 5, 1))) + ':' + str(int(random.randrange(10, 60, 1)))
                     }
                )
        js_list.append(newdic)

    with open('myplaylist.js', 'w', encoding='utf-8') as f:
        f.write('var myPlaylist = ' + dis_rep(str(js_list)) + ';')
        f.close()

def dis_rep(str):
    return str.replace("'mp3'", 'mp3').replace("'title'", 'title').replace("'artist'", 'artist').replace(
        "'rating'", 'rating').replace("'duration'", 'duration').replace("'cover'", 'cover')


if __name__ == '__main__':
    # print(openFile())
    # os.listdir((repr(__file__)))
    # list = (os.listdir(os.path.dirname((__file__))))
    # print(list)
    # file_list = []
    # for file in list:
    #     if not os.path.isdir(file) and re.match(r'.+[mp3]$', file):
    #         file_list.append(file)
    # info = os.stat(r'郁可唯 - 时间煮雨.mp3')
    # print(time.localtime(info.st_size))
    '''test：os.stat_result(st_mode=33206, st_ino=10696049115251803, st_dev=2752502229, st_nlink=1, st_uid=0, st_gid=0,
                   st_size=0, st_atime=1537008946, st_mtime=1537008946, st_ctime=1537008946)'''

    '''时间煮雨：os.stat_result(st_mode=33206, st_ino=8725724278277217, st_dev=2752502229, st_nlink=1, st_uid=0, st_gid=0, 
    st_size=3969971, st_atime=1537016898, st_mtime=1393319218, st_ctime=1537016898)'''
    # tag = eyed3.core.Tag()
    # eyed3.core.load("郁可唯 - 时间煮雨.mp3")
    # print(tag._getArtist(),tag._getAlbum(),tag._getTitle())
    list = [{'mp3': 'mix/汪苏泷 - 专属味道."mp3"', 'title': '专属味道', 'artist': '汪苏泷', 'cover': 'mix/1.png', 'rating': 4,
             'duration': '03:33'},
            {'mp3': 'mix/july - in love."mp3"', 'title': 'in love', 'artist': 'july', 'cover': 'mix/1.png', 'rating': 4,
             'duration': '03:53'},
            {'mp3': 'mix/sara、孙子涵 - 请安静的忘记我."mp3"', 'title': '请安静的忘记我', 'artist': 'sara、孙子涵', 'cover': 'mix/1.png',
             'rating': 4, 'duration': '04:07'},
            {'mp3': 'mix/马頔 - 南山南."mp3"', 'title': '马頔 - 南山南', 'artist': '马頔', 'cover': 'mix/1.png', 'rating': 4,
             'duration': '05:24'}]
    # dic = list[0]
    # print(dic)
    # newdic = {key: '' for key in dic.keys()}
    # print(newdic)
    # newdic.update(
    #     {'mp3': 'mix/' + file_list[0],
    #      'title': file_list[0].split(r'.mp3')[0],
    #      'artist': file_list[0].split(r'.mp3')[0].split('-')[0],
    #      'cover': 'mix/1.png',
    #      'rating': 4,
    #      'duration': '0' + str(int(random.randrange(1, 5, 1))) + ':' + str(int(random.randrange(10, 60, 1)))
    #      }
    # )
    # list.append(newdic)
    # print(newdic)
    # tex = 'var myPlaylist = ' + dis_rep(str(list)) + ';'
    # f = open('myplaylist.js', 'w', encoding='utf-8')
    # f.write(tex)
    list = openFile()
    print (list)
    writeFlie(list)
    list = openFile()
    print((list))
    print( os.listdir(os.getcwd()))
    
