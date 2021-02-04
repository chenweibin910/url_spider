#!/usr/bin/python
# coding:utf-8
import os
import sys
from hashlib import md5
from random import choice

import requests
from six.moves import urllib

FakeUserAgents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12",
    "Opera/9.27 (Windows NT 5.2; U; zh-cn)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13",
    "Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 ",
    "Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; F-01D Build/F0001) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13 ",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; ja-jp) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; da-dk) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5 ",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Chrome/ Safari/530.9 ",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"
]


class XiaMi:
    # ua = UserAgent()
    ua = choice(FakeUserAgents)
    DOMAIN = "https://www.xiami.com"

    # 各个API接口地址
    # 每日音乐推荐
    APIDailySongs = "/api/recommend/getDailySongs"
    # 排行榜音乐
    APIBillboardDetail = "/api/billboard/getBillboardDetail"
    # 所有排行榜
    APIBillboardALL = "/api/billboard/getBillboards"
    # 歌曲详情信息
    APISongDetails = "/api/song/getPlayInfo"

    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            "user-agent": self.ua
        }
        self.session.get(self.DOMAIN)

    def _get_api_url(self, api):
        return self.DOMAIN + api

    # 获取每日推荐的30首歌曲
    def get_daily_songs(self):
        url = self._get_api_url(self.APIDailySongs)
        params = {
            "_s": self._get_params__s(self.APIDailySongs)
        }
        result = self.session.get(url=url, params=params).json()
        return self._dispose(result)

    # 获取虾米音乐的音乐排行榜
    def get_billboard_song(self, billboard_id: int = 0):
        '''
        :param billboard_id: 各类型的排行榜
        :return: 排行榜音乐数据
        '''
        if not hasattr(self, "billboard_dict"):
            self._get_billboard_dict_map()

        assert hasattr(self, "billboard_dict"), "billboard_dict获取失败"
        # pprint.pprint(self.billboard_dict)
        if billboard_id == 0:
            billboard_id = input("输入对应ID，获取排行榜信息")
        # assert billboard_id in self.billboard_dict, "billboard_id错误"

        url = self._get_api_url(self.APIBillboardDetail)
        _q = '{\"billboardId\":\"%s\"}' % billboard_id
        params = {
            "_q": _q,
            "_s": self._get_params__s(self.APIBillboardDetail, _q)
        }
        result = self.session.get(url=url, params=params).json()
        return self._dispose(result)

    # 生成一个排行榜对应的字典映射
    def _get_billboard_dict_map(self):
        billboard_dict = {}
        billboards_info = self.get_billboard_all()
        try:
            if billboards_info["code"] == "SUCCESS":
                xiamiBillboards_list = billboards_info["result"]["data"]["xiamiBillboards"]
                for xiamiBillboards in xiamiBillboards_list:
                    # for xiamiBillboard in xiamiBillboards:
                    id = xiamiBillboards["billboardId"]
                    name = xiamiBillboards["name"]
                    billboard_dict[id] = name
                self.billboard_dict = billboard_dict
        except Exception:
            pass

    # 获取所有的排行榜信息
    def get_billboard_all(self):
        url = self._get_api_url(self.APIBillboardALL)
        params = {
            "_s": self._get_params__s(self.APIBillboardALL)
        }
        result = self.session.get(url=url, params=params).json()
        return self._dispose(result)

    # 获取歌曲详情信息
    def get_song_details(self, *song_ids) -> dict:
        '''
        :param song_ids: 歌曲的id，可以为多个
        :return: 歌曲的详情信息
        '''
        assert len(song_ids) != 0, "参数不能为空"

        for song_id in song_ids:
            if not isinstance(song_id, int):
                raise Exception("每个参数必须为整型")

        url = self._get_api_url(self.APISongDetails)
        _q = "{\"songIds\":%s}" % list(song_ids)
        params = {
            "_q": _q,
            "_s": self._get_params__s(self.APISongDetails, _q)
        }
        result = self.session.get(url=url, params=params).json()
        return self._dispose(result)

    # 获取歌曲的下载地址
    def get_song_download_url(self, *song_ids):
        download_url_dict = {}
        song_details = self.get_song_details(*song_ids)
        songPlayInfos = song_details["result"]["data"]["songPlayInfos"]
        for songPlayInfo in songPlayInfos:
            song_download_url = songPlayInfo["playInfos"][0]["listenFile"] or songPlayInfo["playInfos"][1]["listenFile"]
            song_id = songPlayInfo["songId"]
            download_url_dict[song_id] = song_download_url

        print({"歌曲下载地址数量:": len(download_url_dict)})
        return download_url_dict

    # 处理爬虫获取到的数据，这里我就输出值
    def _dispose(self, data):
        # pprint.pprint(data)
        return data

    # 获取加密字符串_s
    def _get_params__s(self, api: str, _q: str = "") -> str:
        '''
        :param api: URL的地址
        :param _q:  需要加密的参数
        :return: 加密字符串
        '''
        xm_sg_tk = self._get_xm_sg_tk()
        data = xm_sg_tk + "_xmMain_" + api + "_" + _q
        return md5(bytes(data, encoding="utf-8")).hexdigest()

    # 获取xm_sg_tk的值，用于对数据加密的参数
    def _get_xm_sg_tk(self) -> str:
        xm_sg_tk = self.session.cookies.get("xm_sg_tk", None)
        assert xm_sg_tk is not None, "xm_sg_tk获取失败"
        return xm_sg_tk.split("_")[0]

    def test(self):
        self.get_daily_songs()
        self._get_xm_sg_tk()
        self.get_billboard_song(332)
        self.get_billboard_all()
        self.get_song_details(1813243760)
        self.get_song_download_url(1813243760)


def download_and_extract(filepath, save_dir):
    """根据给定的URL地址下载文件

    Parameter:
        filepath: list 文件的URL路径地址
        save_dir: str  保存路径
    Return:
        None
    """
    file_list = os.listdir()
    for index, one in enumerate(filepath):
        filename = one["singer"][:50] + " - " + one["name"] + ".mp3"
        filename = filename.replace("/", " ")
        url = one["download_url"]
        if not url:
            continue
        if filename in file_list:
            continue
        save_path = os.path.join(save_dir, filename)
        urllib.request.urlretrieve(url, save_path)
        sys.stdout.write('\r>> Downloading %.1f%%' % (float(index + 1) / float(len(filepath)) * 100.0))
        sys.stdout.flush()
    print('\nSuccessfully downloaded')


if __name__ == '__main__':
    xm = XiaMi()
    # xm.test()
    all_boards = xm.get_billboard_all()["result"]["data"]["xiamiBillboards"]
    billboard = {}
    for board in all_boards:
        billboard.update({board["name"]: board["billboardId"]})
    print(billboard)
    for name, board_id in billboard.items():
        # board_id = 305
        dy_songs = xm.get_billboard_song(board_id)["result"]["data"]["billboard"]
        songs = dy_songs["songs"]
        song_ids = {}
        for song in songs:
            song_id, song_name, singer = song["songId"], song["songName"], song["singers"]
            song_ids.update({
                song_id: {"name": song_name, "singer": singer}
            })
        download_url_dict = xm.get_song_download_url(*song_ids.keys())
        for song_id in list(download_url_dict):
            song_ids[song_id].update({"download_url": download_url_dict[song_id]})
        # print(song_ids)
        # save_dir = ''
        # download_and_extract(list(song_ids.values()), save_dir)
