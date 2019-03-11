import os
from datetime import datetime
from live_download import *
from audio_to_text import *

DOWNLOAD_PATH=r'E:\TEST\AudioDownload'


if __name__ == "__main__":
    print('开始下载直播音频')
    now_str = datetime.now().strftime(r'%Y%m%d%H%M%S')
    download_file = os.path.join(DOWNLOAD_PATH,now_str+'.mp3')
    download_live_audio(BBC_LIVE_URL,download_file,256)
    print('直播音频下载完毕,路径: '+download_file)
    print('开始转换音频 '+download_file)
    convert_file = os.path.join(DOWNLOAD_PATH,'temp',now_str+'.pcm')
    convert_xunfei_pcm(download_file,convert_file)
    print('音频转换完毕,路径: '+convert_file)
    print('开始识别音频')
    res = audio_to_text(convert_file)
    print(res.content.decode('utf-8'))
    