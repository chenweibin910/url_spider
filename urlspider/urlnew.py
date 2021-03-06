# -*- coding:UTF-8 -*-
import logging
import os
import re
import sys
import threading
import time
import traceback
import urllib.request

import requests
from PIL import Image
from fake_useragent import UserAgent
from lxml import html

ua = UserAgent()
global progress


class urlfind(object):

    def __init__(self, url='https://movie.douban.com/', path=r'E:\temp'):
        # 默认路径
        self.path = path
        # 网站
        self.url = url
        # 所需爬取文本正则表达式
        self.text_path = r'//li[@class="title"]//a/text()'
        # 所需查找图片正则表达式
        self.reg = r'src="(https[^"]+?\.jpg)"'
        # 日志
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=logging.INFO)
        self.printLog('')
        handler = logging.FileHandler("%s\log\log.txt" % self.path)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s -%(name)s-%(levelname)s- %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_request(self, text_path, jpg_reg):
        """
        :param url:需要爬数据的网址
        :param text_path:截取所需文本正则表达式
        :param jpg_reg: 截取所需图片正则表达式
        :return:返回 得到的图片的列表，爬取到的文本
        """
        self.printLog(tips='url = %s' % self.url, flag=True)
        # 需要爬数据的网址
        # url = 'https://movie.douban.com/'
        try:
            headers = {'User-Agent': ua.chrome}
            page = requests.get(self.url, headers=headers)
            tree = html.fromstring(page.text)
            text_result = tree.xpath(text_path)

            # 读取网页源码
            # html_1 = urllib.request.urlopen(url).read()
            html_1 = page.text
            self.printLog(tips='conect to the url success.')

            # reg = r'src="(https[^"]+?\.jpg)"'
            img_re = re.compile(jpg_reg)
            # 找到所有对应格式的图片的地址，返回列表
            img_list = re.findall(img_re, str(html_1))
            self.printLog(tips='find all photo url success.')
            return img_list, text_result

        except ConnectionError as e:
            # print('%s connection have some error,please check the network.' % e)
            self.printLog(tips='%s connection have some error,please check the network.' % e, flag=True)
            return None

    def path_del_create(self):
        """
        :param path:工作目录
        :param dest_path:最终输出拼接图片目录
        :return: True
        """
        dest_path = self.path + r'\new'
        # 移除目录  path = r'E:\temp'
        cmd = r'rd /s/q %s' % self.path
        # 新建目录
        cmd_tmp = r'md %s' % dest_path
        # 新建图片文件
        cmd_cre = r'type nul> %s\1.jpg' % self.path
        # 如果目录存在，则删除目录及目录下所有文件
        try:
            # if os.path.exists(path):
            #     # os.rmdir(path)
            #     os.system(cmd)
            #     printLog('The path is already exisit.del...')
            #     printLog('del %s success.' % path)
            # 建立目录
            if not os.path.exists(dest_path):
                os.system(cmd_tmp)
                self.printLog('create %s success' % dest_path)
            # 新建图片
            os.system(cmd_cre)
            self.printLog(r'create %s\1.jpg success.' % self.path)
        except Exception as e:
            # print('%s create path failed.' % e)
            self.printLog('%s create path failed.' % e, True)
            return False

        return True

    def downloadAndSave_pic(self, img_list):
        """
        :param path:
        :param img_list:
        :param url:
        :return:
        """
        global progress
        progress = 0
        # 替换路径字符串转义、多余字符
        if not self.path:
            return False
        path = self.path.replace("\\", "/")
        # 存储所有图片命名，以 1.jpg 开始
        pic_name = 1
        # 若列表和路径为空，
        if not (img_list and path):
            self.printLog('list or path is null,please check.', True)
            return False
        # 存储找到的所有图片到目录中，并以阿拉伯数字命名
        self.printLog('download photo file from find photo url.please wait....', True)
        for img in img_list:
            try:
                urllib.request.urlretrieve(img, '%s/%s.jpg' % (path, pic_name))
                pic_name += 1
                progress = float(img_list.index(img) / len(img_list) * 100)
            except Exception as e:
                self.printLog('downlaod jpg failed  %s.jpg' % pic_name)
                self.printLog('%s' % str(e).replace('<', '(').replace(">", ')'))
                continue

        if len(img_list) == pic_name - 1:
            self.printLog('download all find photo success.', True)
        return True

    def get_picPathList(self):
        """
        :param path: 存储路径
        :return:
        """
        # 替换路径字符串转义、多余字符
        if not self.path:
            return False
        path = self.path.replace("\\", "/")
        # 所有图片所在的完整路径的字符串的列表
        imPathList = []
        self.printLog('find all photo`s path,and join to list...', True)
        # 读取所有已存储的图片的路径加文件名 字符串，并保存到列表中
        for file in os.listdir(path):
            if not os.path.isdir(file):
                if file.endswith('.jpg'):
                    imPathList.append(os.path.join(path, file))
        self.printLog('success.', True)

        return imPathList

    def unionPic(self, dest_path, imPathList):
        """
        :param path: 图片存储路径
        :param dest_path: 新建图片存储路径
        :param imPathList: 所有图片所在的完整路径的字符串的列表
        # :param index_list: 路径字符串，路径首字母的下标 组成的列表
        :return:
        """
        # 替换路径字符串转义、多余字符
        if not self.path:
            return False
        path = self.path.replace("\\", "/")

        pic = '%s/1.jpg' % path
        self.printLog('open photo %s' % pic)
        # 打开第一张抓取的照片，获取其像素大小,大小约为270x377
        im_old = Image.open(pic)
        width, height = im_old.size
        # 一张图片贴上10*2 张下载下来的图片
        size_width = width * 10
        size_height = height * 2
        self.printLog('create new jpg file width = %s height = %s' % (size_width, size_height))
        # 新建大小约为2700x754的白底图片，并保存
        im_new = Image.new('RGB', (size_width, size_height))
        # 保存到目的路径
        im_new.save('%s/0.jpg' % dest_path)
        # 新建的图片的像素大小
        new_width, new_height = im_new.size
        # 贴图时用的临时下标
        temp_index = 0
        # 遍历所需要的图片并贴图在新的图片上
        for left in range(0, new_width, width):
            for top in range(0, new_height, height):
                imgPath = imPathList[temp_index]
                im = Image.open(imgPath)
                # 贴图
                im_new.paste(im, (left, top))
                self.printLog('paste %s to new jpg success.' % imgPath)
                temp_index += 1
        # 保存最终图片
        im_new.save('%s/0.jpg' % dest_path)
        self.printLog('save %s/0.jpg success.' % dest_path)

        return im_new

    def printLog(self, tips='', flag=False):
        """
        保存日志文件
        :param dest_path: 路径
        :return:
        """
        # cmd_cre = r'type log:> %s\log.log' % self.path + '\\log'
        t = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime())
        cmd_log = r'echo %s%s>>log.log' % (t, tips)
        path = self.path + '\\log'
        try:
            if flag:
                print(tips)
            if not os.path.exists(path):
                os.mkdir(path)
            self.logger.info(tips)
            os.chdir(path)
            os.popen(cmd_log)
            os.popen('exit')
        except Exception as e:
            print('except occur when save log: %s' % e)

        return True

    def run(self, *args, **kwargs):
        try:
            self.path = input('input workspace:\t')
            if self.path:
                print('input path is %s' % self.path)
                if not re.match(r'[a-zA-Z]{1}:[\\a-zA-Z0-9_]+', self.path):
                    exp = 'input path format error.'
                    self.printLog(exp)
                    raise (Exception, exp)
            startTime = time.time()
            if not self.path:
                self.printLog('input is null,use default path.', True)
                self.path = r'E:\temp'
            dest_path = self.path + r'\new'
            self.printLog('workspace = %s' % self.path, True)
            img_list, text_find = self.get_request(self.text_path, self.reg)

            rst = self.path_del_create()
            if not rst:
                exp = 'update %s failed.' % self.path
                self.printLog(exp, True)
                raise (Exception, exp)
            rst = self.downloadAndSave_pic(img_list)
            if not rst:
                exp = 'download flie error.'
                self.printLog(exp, True)
                raise (Exception, exp)

            imPathList = self.get_picPathList()

            image = self.unionPic(dest_path, imPathList)

            if not image:
                exp = 'image is null.'
                self.printLog(exp)
                raise Exception(exp)
            image.show()
            self.printLog('open destination photo success.', True)
            # 打印爬到的文本
            self.printLog('正在热映电影：%s' % text_find, True)
            self.printLog('main run time:%s' % str(time.time() - startTime))
        except Exception as exp:
            self.printLog('exception :%s' % exp, True)

        return True


def main(*args, **kwargs):
    time.sleep(1)
    print('main thread start!the thread name is:%s\r' % threading.currentThread().getName())
    url = urlfind()
    url.run()
    time.sleep(1)


def mytime(threads):
    startTime = time.time()
    global progress
    url = urlfind()
    url.path_del_create()
    time.sleep(5)
    url.printLog('sub thread start!the thread name is:%s\r' % threading.currentThread().getName())
    progress = 0
    list = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■'
        , '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
    while not threads[0]._is_stopped:
        # url.printLog(time.ctime())
        # time.sleep(5)
        # for progress in range(100):
        #     time.sleep(0.5)
        #     sys.stdout.write("Download progress: %d%%   \r" % (int(time.time() - t)))
        #     sys.stdout.flush()
        # sys.stdout.write(" progress: %d%%   \r" % (int(time.time() - t)))
        if progress != 0:
            for i in range(0, int(progress * len(list) / 100)):
                sys.stdout.write('■')
            sys.stdout.write(' %d%%   \r' % progress)
            if progress == 100:
                break
            # sys.stdout.write("Download progress: %d%%   \r" % progress)
            sys.stdout.flush()
            time.sleep(0.2)
    sys.stdout.write(" progress: %d%%   \r" % (100))
    print('runtime:%ss' % int(time.time() - startTime))


def myThread():
    threads = []

    t = threading.Thread(target=main, args=(0,))
    threads.append(t)

    t = threading.Thread(target=mytime, args=(threads,))
    threads.append(t)

    for t in threads:
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()
        print('%s end!' % t.getName())

    print('all thread end.')
    """
　　setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，
    如果不设置为守护线程程序会被无限挂起。子线程启动后，父线程也继续执行下去，
    当父线程执行完最后一条语句后，没有等待子线程，直接就退出了，同时子线程也一同结束。
    　我们只对上面的程序加了个join()方法，用于等待线程终止。
    join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
    apply(func [, args [, kwargs ]]) 函数用于当函数参数已经存在于一个元组或字典中时，间接地调用函数。
    args是一个包含将要提供给函数的按位置传递的参数的元组。如果省略了args，任何参数都不会被传递，
    kwargs是一个包含关键字参数的字典。
    """


if __name__ == '__main__':
    try:
        myThread()
    except Exception as e:
        print(traceback.format_exc())
        print(e)
    finally:
        os.system("pause")
    # for progress in range(100):
    #     time.sleep(0.1)
    #     sys.stdout.write("Download progress: %d%%   \r" % (progress))
    #     sys.stdout.flush()
