import requests
import json
"""
type的类型有：

ZH_CN2EN 中文　»　英语

ZH_CN2JA 中文　»　日语

ZH_CN2KR 中文　»　韩语

ZH_CN2FR 中文　»　法语

ZH_CN2RU 中文　»　俄语

ZH_CN2SP 中文　»　西语

EN2ZH_CN 英语　»　中文

JA2ZH_CN 日语　»　中文

KR2ZH_CN 韩语　»　中文

FR2ZH_CN 法语　»　中文

RU2ZH_CN 俄语　»　中文

SP2ZH_CN 西语　»　中文
"""

def youdao_trans(word,type='AUTO'):
    data = {
            'doctype': 'json',
            'type': type,
            'i': word
        }
    proxy={"http":None,"https":None}
    url = "http://fanyi.youdao.com/translate"
    r = requests.post(url, params=data,proxies=proxy)
    result = r.json()
    return result

if __name__ == '__main__':
    print(youdao_trans('我喜欢你\n你喜欢我吗',type="ZH_CN2RU"))