# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document
from account import Account
import requests
import random
import json
from hashlib import md5
from typing import Union

def baidu_trans(query,from_lang='auto',to_lang='zh',domain:Union[str,None]=None):
    account=Account()
# Set your own appid/appkey.
    appid = account.appid
    appkey = account.appkey


    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    from_lang = from_lang
    to_lang =to_lang

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    query = query

    # Generate salt and sign
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    #如果有垂直领域，则添加
    if(domain):
        payload.update(domain=domain)

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()

    # Show response
    return result

if __name__ == '__main__':
    a=baidu_trans('I love you\n do you love me')
    print(a)
