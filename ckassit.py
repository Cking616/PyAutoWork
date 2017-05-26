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
import json


def get_token():
    api_key = "VvYvv9WevLS67TV56onVAIDn"
    secret_key = "e0628ea2b2823974cfd72d636d5ae740"
    auth_url = ("https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" +
                api_key + "&client_secret=" + secret_key)
    res = urllib.request.urlopen(auth_url)
    json_data = res.read()
    json_data = json_data.decode('utf-8')
    return json.loads(json_data)['access_token']


def dump_res(buf):
    print(buf)


def use_audio_cloud(token, wave_file):
    wave_file_ptr = wave.open(wave_file, 'rb')
    num_of_frames = wave_file_ptr.getnframes()()
    wave_file_len = num_of_frames * 2
    audio_data = wave_file_ptr.readframes(num_of_frames)

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
    curl.setopt(curl.POSTFIELDS, audio_data)
    curl.setopt(curl.POSTFIELDSIZE, wave_file_len)
    curl.perform()  # pycurlurl.perform() has no return val


if __name__ == '__main__':
    token = get_token()
    print(token)

