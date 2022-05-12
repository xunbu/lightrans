import requests
from resource_py.ErrorRecoder import errorrecoder
'''
中文	zh-CHS
中文繁体	zh-CHT
英文	en
日文	ja
韩文	ko
法文	fr
西班牙文	es
葡萄牙文	pt
意大利文	it
俄文	ru
越南文	vi
粤语 yue
'''

'''
统一接口，实现百度json格式
{'from': 'en', 'to': 'zh', 'trans_result': [{'src': 'I love you', 'dst': '我爱你'}, {'src': 'do you love me', 'dst': '你爱我吗'}]}
'''
def youdao_zhiyun_trans(text:str,from_lang:str='auto',to_lang:str='auto')->dict:
    result={'from':None,'to':None,'trans_result':None,'speakUrl':None,'tSpeakUrl':None}
    url = r"https://aidemo.youdao.com/trans"
    proxy = {"http": None, "https": None}
    data = {"q": text, "from":from_lang, "to":to_lang,"strict":True}
    resp = requests.post(url, data,proxies=proxy).json()
    if resp['errorCode']!='0':
        errorrecoder.adderror(f"有道智云错误码:{resp['errorCode']}")
        return {'error_code':resp['errorCode']}
    else:
        if 'speakUrl' in resp:
            result['speakUrl']=resp['speakUrl']
        if 'tSpeakUrl' in resp:
            result['tSpeakUrl'] = resp['tSpeakUrl']
        #2的index
        idx2=resp['l'].index('2')
        result['from'],result['to']=resp['l'][:idx2],resp['l'][idx2+1:]
    if resp['isWord']==True:
        tempdir = {'src': resp['returnPhrase'][0], 'dst': resp['translation'][0]}
        # tempdir={'src':resp['returnPhrase'][0],'dst':','.join(resp['web'][0]['value'])}
        result['trans_result']=[tempdir]
    elif resp['isWord']==False:
        query=resp['query'].strip().split('\n')
        translaion=resp['translation'][0].strip().split('\n')
        templs=[]
        for src,dst in zip(query,translaion):
            templs.append({'src':src,'dst':dst})
        result['trans_result']=templs
    return result

    # print(resp.json())
    # print(resp.json()['speakUrl'].replace("voice=4","voice=3"))
    # print(resp.json()['tSpeakUrl'].replace("voice=4","voice=3"))

if __name__ == '__main__':
    text="""你好"""
    print(youdao_zhiyun_trans(text,to_lang='fr'))