#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author:washingtown
'''测试下载音频直播到本地'''
import sys
import os
import requests

BBC_LIVE_URL=r'http://bbcwssc.ic.llnwd.net/stream/bbcwssc_mp1_ws-eieuk'

def download_live_audio(url, local_path, size=512):
    '''下载在线音频到本地
    
    :param size:下载文件大小，单位KB'''
    local_dir = os.path.split(local_path)[0]
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)
    buffer_size = 1024
    stream = requests.get(url, stream=True)
    with open(local_path, 'wb') as f:
        for i, chunk in enumerate(stream.iter_content(chunk_size=buffer_size)):
            if i>=size:
                break
            f.write(chunk)

if __name__ == "__main__":
    download_live_audio(BBC_LIVE_URL,r'E:\TEST\AudioDownload\1.wav')