#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from time import sleep
import re
import requests
from tqdm import tqdm


def mkdir(path):
    if os.path.exists(path) is not True:
        os.makedirs(path)


def download_pic(url, path):
    resp = requests.get(url)
    with open(path, 'wb') as code:
        code.write(resp.content)


def download_emoji(emoji, save_path):
    emoji_name = emoji['text']
    emoji_name = emoji_name[1:-1]
    # print(emoji_name)
    path = os.path.join(save_path, f'{emoji_name}.png')
    download_pic(emoji['url'], path)

def download_emoji_live(emoji, save_path):
    # print(emoji)

    emoji_name = emoji['emoji']
    # emoji_name = emoji_name[1:-1]
    # print(emoji_name)
    path = os.path.join(save_path, f'{emoji_name}.png')
    download_pic(emoji['url'], path)


def download_package(package, path):
    # package_name = package['text']
    # save_path = os.path.join(path, package_name)
    mkdir(path)
    all_emote = set(map(lambda e: e['text'][1:-1], package['emote']))
    # print(all_emote)

    downloaded_emote = set(map(lambda e: e[:-4], os.listdir(path)))
    # print(downloaded_emote)

    download_emote_name = all_emote - downloaded_emote
    # print(download_emote_name)

    if len(download_emote_name) == 0:
        return
    going_to_download_emote = filter(lambda e: e['text'][1:-1] in download_emote_name, package['emote'])
    with ThreadPoolExecutor() as executor:
        executor.map(partial(download_emoji, save_path=path), going_to_download_emote)
    sleep(3)

def download_package_live(package, path):
    mkdir(path)

    all_emote = set(map(lambda e: e['emoji'], package['emoticons']))
    # print(all_emote)

    downloaded_emote = set(map(lambda e: e[:-4], os.listdir(path)))
    # print(downloaded_emote)

    download_emote_name = all_emote - downloaded_emote
    # print(download_emote_name)

    if len(download_emote_name) == 0:
        return
    going_to_download_emote = filter(lambda e: e['emoji'] in download_emote_name, package['emoticons'])
    with ThreadPoolExecutor() as executor:
        executor.map(partial(download_emoji_live, save_path=path), going_to_download_emote)
    sleep(3)

def eomjidown():
    with open('emoji.json', 'r', encoding='utf-8') as fp:
        emojis = json.load(fp)
    emoji_packages = emojis['data']['all_packages']
    package_path = 'pic'
    for i in emoji_packages:
         # af = re.match(r'颜文字|2233|小电视|拜年祭|拜年纪|兔|tv|大会员|2020拜年祭|2021拜年纪'
         #            r'星座系列|崩坏|原神|BML|BW|[0-9]|\W+', i['text'], re.M | re.I | re.U)
         # print(af)
#
#         if re.search(r'颜文字|2233|小电视|拜年祭|拜年纪|兔|tv|大会员|2020拜年祭|2021拜年纪|'
#              r'星座系列|崩坏|原神|BML|BW|[0-9]|FPX|RNG|EDG|LNG|LPL|AG|热词|灵笼', i['text'], re.M|re.I|re.U|re.IGNORECASE) == None:
            print(i['id'], i['text'])

    assign = input('请输入需要下载的包\n')
    bar = tqdm(emoji_packages)
    for p in bar:
        expx = str(re.match(assign, p['text'], re.M | re.I | re.U | re.IGNORECASE))
        if expx != 'None':
            bar.set_description(p['text'])
            download_package(p, package_path)
            print(p['text'])

    print('下载完成\n')

def eomjidown_live():
    with open('GetEmoticons.json', 'r', encoding='utf-8') as fp:
        emojis_live = json.load(fp)
    emoji_packages = emojis_live['data']['data']
    package_path = 'pic'
    for i in emoji_packages:
         print(i['pkg_name'])                                        #i['pkg_name']

    assign = input('请输入需要下载的包\n')
    bar = tqdm(emoji_packages)
    for p in bar:
        expx = str(re.match(assign, p['pkg_name'], re.M | re.I | re.U | re.IGNORECASE))
        if expx != 'None':
            bar.set_description(p['pkg_name'])
            download_package_live(p, package_path)
            print(p['pkg_name'])
    print('下载完成\n')