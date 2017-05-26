# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: kht
@license: Apache Licence 
@author: kht(cking616)
@contact: cking616@mail.ustc.edu.cn
@software: PyCharm Community Edition
@file: ckassit.py
@time: 2017/5/26 0026 23:18
"""
import urllib.request
import wave
import pycurl
import base64
import json


def get_token():
    api_key = ""
    secret_key = ""
    auth_url = api_key + secret_key
    respon = urllib.request.urlopen(auth_url)
    json_data = respon.read()
    return json.loads(json_data)['access_token']


def dump_res(buf):
    print(buf)


def use_audio_cloud(token, wave_file):
    wave_file_ptr = wave.open(wave_file, 'rb')
    num_of_frames = wave_file_ptr.getnframes()()
    wave_file_len = num_of_frames * 2
    audio_datas = wave_file_ptr.readframes(num_of_frames)

    cuid = ""
    server_url = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' + token
    http_header = [
        'Content-Type: audio/pcm; rate=8000',
        'Content-Length: %d' % wave_file_len
    ]

    curl = pycurl.Curl()
    curl.setopt(pycurlurl.URL, str(server_url))  # curlurl doesn't support unicurlode
    # curl.setopt(curl.RETURNTRANSFER, 1)
    curl.setopt(curl.HTTPHEADER, http_header)   # must be list, not dicurlt
    curl.setopt(curl.POST, 1)
    curl.setopt(curl.CONNECTTIMEOUT, 30)
    curl.setopt(curl.TIMEOUT, 30)
    curl.setopt(curl.WRITEFUNCTION, dump_res)
    curl.setopt(curl.POSTFIELDS, audio_datas)
    curl.setopt(curl.POSTFIELDSIZE, wave_file_len)
    curl.perform()  # pycurlurl.perform() has no return val


if __name__ == '__main__':
    pass