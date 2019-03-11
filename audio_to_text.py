#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author:washingtown
'''语音转文字'''
import sys
import os
import hashlib
import base64
import subprocess
import requests
import common

APP_ID = '5c8653a9'
API_KEY = 'e0decf41cb3f13a7635b7ee92cda5379'
TEMP_PATH = r'E:\TEST\AudioDownload\temp'
FFMPEG_PATH = r'G:\工具\提取工具\ffmpeg\bin\ffmpeg.exe'
XUNFEI_API = 'http://api.xfyun.cn/v1/service/v1/iat'

def convert_xunfei_pcm(input_file, output_file):
    if not os.path.exists(input_file):
        print('源文件不存在！')
        return
    out_dir = os.path.split(output_file)[0]
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    cmd = FFMPEG_PATH + ' -y -i '+ input_file +' -acodec pcm_s16le -f s16le -ac 1 -ar 16000 ' + output_file
    print(cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    code = p.wait()
    print(code)

def audio_to_text(audio_path):
    if not os.path.exists(audio_path):
        print('音频文件不存在！')
        return
    audio_bas64 = None
    with open(audio_path,'rb') as f:
        stream =  f.read()
        audio_bas64 = base64.b64encode(stream).decode(encoding='utf-8')
    param = '{"engine_type": "sms-en16k","aue": "raw"}'
    x_param = base64.b64encode(param.encode(encoding='utf-8')).decode(encoding='utf-8')
    timestamp = str(common.utc_timestamp())
    md5 = hashlib.md5()
    md5.update(''.join([API_KEY,timestamp,x_param]).encode(encoding='utf-8'))
    x_checksum = md5.hexdigest()
    print(x_checksum)
    headers={
        'X-Appid':APP_ID,
        'X-CurTime':timestamp,
        'X-Param':x_param,
        'X-CheckSum':x_checksum,
        'Content-Type':'application/x-www-form-urlencoded; charset=utf-8'
    }
    data={
        'audio':audio_bas64
    }
    res = requests.post(XUNFEI_API,data=data,headers=headers)
    return res


if __name__ == "__main__":
    res = audio_to_text(r'E:\TEST\AudioDownload\text.pcm')
    print(res.content.decode('utf-8'))