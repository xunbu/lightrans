from resource_py.Baidu_Text_transAPI import baidu_trans
from resource_py.Youdao_Text_transAPI import youdao_trans
from resource_py.Youdao_Text_transAPI_zhiyun import youdao_zhiyun_trans
from resource_py.ErrorRecoder import errorrecoder
from resource_py.Baidu_Text_transAPI_Reptile import d
"""
将多种翻译统一为百度格式(语言选择/json等)
考虑到语言列表不完整，故只做部分转换
有道智云翻译文档:https://ai.youdao.com/DOCSIRMA/html/%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E7%BF%BB%E8%AF%91/API%E6%96%87%E6%A1%A3/%E6%96%87%E6%9C%AC%E7%BF%BB%E8%AF%91%E6%9C%8D%E5%8A%A1/%E6%96%87%E6%9C%AC%E7%BF%BB%E8%AF%91%E6%9C%8D%E5%8A%A1-API%E6%96%87%E6%A1%A3.html#section-9
"""
baidulang=["auto","zh","en","fra","jp","kor","ru","spa","cht"]
youdaolang=["AUTO","AUTO","ZH_CN2EN","ZH_CN2FR","ZH_CN2JA","ZH_CN2KR","ZH_CN2RU","ZH_CN2SP","AUTO"]
youdaozhiyunlang=["auto","zh-CHS","en","fr","ja","ko","ru","es","zh-CHT"]


baidu2youdao_dict=dict(zip(baidulang,youdaolang))
youdao2baidu_dict=dict(zip(youdaolang,baidulang))

baidu2youdaozhiyun_dict=dict(zip(baidulang,youdaozhiyunlang))
youdaozhiyun2baidu_dict=dict(zip(youdaozhiyunlang,baidulang))

#百度爬虫会报998错误码
#百度{'error_code': '52003', 'error_msg': 'UNAUTHORIZED USER'}
#有道{'errorCode': 50}
#百度爬虫{'trans_result': {'data': [{'dst': '我爱你', 'prefixWrap': 0, 'result': '', 'src': 'i love you '}, {'dst': '你爱我吗', 'prefixWrap': 0, 'result': '', 'src': 'do you love me'}], 'from': 'en', 'status': 0, 'to': 'zh', 'type': 2, 'phonetic': [{'src_str': '我', 'trg_str': 'wǒ'}, {'src_str': '爱', 'trg_str': 'ài'}, {'src_str': '你', 'trg_str': 'nǐ'}, {'src_str': '\n', 'trg_str': ' '}, {'src_str': '你', 'trg_str': 'nǐ'}, {'src_str': '爱', 'trg_str': 'ài'}, {'src_str': '我', 'trg_str': 'wǒ'}, {'src_str': '吗', 'trg_str': 'ma'}]}, 'liju_result': {'double': '', 'single': ''}, 'logid': 392615987}
#百度{'from': 'en', 'to': 'zh', 'trans_result': [{'src': 'I love you', 'dst': '我爱你'}, {'src': 'do you love me', 'dst': '你爱我吗'}]}
#有道{'type': 'ZH_CN2EN', 'errorCode': 0, 'elapsedTime': 10, 'translateResult': [[{'src': '我喜欢你', 'tgt': 'I like you'}], [{'src': '你喜欢我吗', 'tgt': 'Do you like me'}]]}


def fanyi_text(word:str,engine:str='youdao',from_lang:str='auto',to_lang:str='zh')->dict:
    successreturn={'from':None,'to':None,'trans_result':None,'speakUrl':None,'tSpeakUrl':None}
    errorreturn={'error_code':None}
    errorflag=0
    if engine=='baidu':
        result=baidu_trans(word,from_lang,to_lang)
        if 'error_code' in result:
            errorflag=1
            errorrecoder.adderror(f"百度翻译错误码:{result['error_code']}")
            errorreturn['error_code']=result['error_code']
        else:
            successreturn['from'],successreturn['to'],successreturn['trans_result']=result['from'],result['to'],result['trans_result']
    elif engine =='baiduReptile':
        result=d.baidu_trans_reptile(word,from_lang,to_lang)
        if 'error_code' in result:
            errorflag=1
            errorrecoder.adderror(f"百度Reptile错误码:{result['error_code']}")
            errorreturn['error_code']=result['error_code']
        else:
            ls_temp=[]
            for value in result['trans_result']['data']:
                ls_temp.append({'src':value['src'],'dst':value['dst']})
            successreturn['trans_result']=ls_temp

    elif engine=='youdao':
        from_lang,to_lang=baidu2youdao_dict[from_lang],baidu2youdao_dict[to_lang]
        result=youdao_trans(word,to_lang)
        if result['errorCode']!=0:
            errorrecoder.adderror(f"有道翻译错误码:{result['errorCode']}")
            errorflag=1
            errorreturn['error_code']=result['errorCode']
        else:
            index_temp=result['type'].index('2')
            from_temp,to_temp=result['type'][:index_temp],result['type'][index_temp+1:]
            if from_temp in youdao2baidu_dict:
                successreturn['from']=youdao2baidu_dict[from_temp]
            else:
                successreturn['from']=from_temp
            if to_temp in youdao2baidu_dict:
                successreturn['to']=youdao2baidu_dict[to_temp]
            else:
                successreturn['to']=to_temp

            ls_temp=[]
            for value in result['translateResult']:
                dict_temp={'src':value[0]['src'],'dst':value[0]['tgt']}
                ls_temp.append(dict_temp)
            successreturn['trans_result']=ls_temp

    elif engine=='youdaozhiyun':
        from_lang, to_lang = baidu2youdaozhiyun_dict[from_lang], baidu2youdaozhiyun_dict[to_lang]
        result=youdao_zhiyun_trans(word,from_lang,to_lang)
        if 'error_code' in result:
            errorflag=1
            errorreturn['error_code']=result['error_code']
        else:
            successreturn['from'],successreturn['to'],successreturn['trans_result']=result['from'],result['to'],result['trans_result']
            successreturn['speakUrl'], successreturn['tSpeakUrl']=result['speakUrl'],result['tSpeakUrl']
    else:
        raise "engine error"

    if errorflag==1:
        print(errorreturn)
        return errorreturn
    else:
        return successreturn


if __name__ == '__main__':
    print(fanyi_text('我今天想要\n开开心心的化个妆',engine='youdao',to_lang='en'))
    print(fanyi_text('我今天想要\n开开心心的化个妆', engine='youdaozhiyun', to_lang='en'))
    print(fanyi_text('我今天想要\n开开心心的化个妆', engine='baiduReptile', to_lang='en'))
    print(fanyi_text('我今天想要\n开开心心的化个妆', engine='baidu', to_lang='en'))