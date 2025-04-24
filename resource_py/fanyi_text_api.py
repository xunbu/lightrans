from typing import Union

from .fanyiAPI import *
from resource_py.ErrorRecoder import errorrecoder
"""
将多种翻译统一为百度格式(语言选择/json等)
考虑到语言列表不完整，故只做部分转换
有道智云翻译文档:https://ai.youdao.com/DOCSIRMA/html/%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E7%BF%BB%E8%AF%91/API%E6%96%87%E6%A1%A3/%E6%96%87%E6%9C%AC%E7%BF%BB%E8%AF%91%E6%9C%8D%E5%8A%A1/%E6%96%87%E6%9C%AC%E7%BF%BB%E8%AF%91%E6%9C%8D%E5%8A%A1-API%E6%96%87%E6%A1%A3.html#section-9
"""
baidulang=["auto","zh","en","fra","jp","kor","ru","spa","cht"]
# youdaolang=["AUTO","AUTO","ZH_CN2EN","ZH_CN2FR","ZH_CN2JA","ZH_CN2KR","ZH_CN2RU","ZH_CN2SP","AUTO"]
youdaozhiyunlang=["auto","zh-CHS","en","fr","ja","ko","ru","es","zh-CHT"]
openailang=["auto","Simplified Chinese","English","French","Japanese","Korean","Russian","Spanish","Traditional Chinese"]

# baidu2youdao_dict=dict(zip(baidulang,youdaolang))
# youdao2baidu_dict=dict(zip(youdaolang,baidulang))

baidu2youdaozhiyun_dict=dict(zip(baidulang,youdaozhiyunlang))
# youdaozhiyun2baidu_dict=dict(zip(youdaozhiyunlang,baidulang))

baidu2openai_dict=dict(zip(baidulang,openailang))
# openai2baidu_dict=dict(zip(openailang,baidulang))


baidu_domain_dict={'默认':None,'生物医药':'medicine','金融财经':'finance'}
#百度爬虫会报998错误码
#百度{'error_code': '52003', 'error_msg': 'UNAUTHORIZED USER'}
#有道{'errorCode': 50}
#百度爬虫{'trans_result': {'data': [{'dst': '我爱你', 'prefixWrap': 0, 'result': '', 'src': 'i love you '}, {'dst': '你爱我吗', 'prefixWrap': 0, 'result': '', 'src': 'do you love me'}], 'from': 'en', 'status': 0, 'to': 'zh', 'type': 2, 'phonetic': [{'src_str': '我', 'trg_str': 'wǒ'}, {'src_str': '爱', 'trg_str': 'ài'}, {'src_str': '你', 'trg_str': 'nǐ'}, {'src_str': '\n', 'trg_str': ' '}, {'src_str': '你', 'trg_str': 'nǐ'}, {'src_str': '爱', 'trg_str': 'ài'}, {'src_str': '我', 'trg_str': 'wǒ'}, {'src_str': '吗', 'trg_str': 'ma'}]}, 'liju_result': {'double': '', 'single': ''}, 'logid': 392615987}
#百度{'from': 'en', 'to': 'zh', 'trans_result': [{'src': 'I love you', 'dst': '我爱你'}, {'src': 'do you love me', 'dst': '你爱我吗'}]}
#有道{'type': 'ZH_CN2EN', 'errorCode': 0, 'elapsedTime': 10, 'translateResult': [[{'src': '我喜欢你', 'tgt': 'I like you'}], [{'src': '你喜欢我吗', 'tgt': 'Do you like me'}]]}


def fanyi_text(word:str,engine:str='youdao',from_lang:str='auto',to_lang:str='zh',domain:str='默认')->dict:
    successreturn={'from':None,'to':None,'trans_result':None,'speakUrl':None,'tSpeakUrl':None}
    errorreturn={'error_code':None}
    errorflag=0
    if engine=='baidu':
        result=baidu_trans(word,from_lang,to_lang,baidu_domain_dict[domain])
        if 'error_code' in result:
            errorflag=1
            errorrecoder.adderror(f"百度翻译错误码:{result['error_code']}")
            errorreturn['error_code']=result['error_code']
        else:
            successreturn['from'],successreturn['to'],successreturn['trans_result']=result['from'],result['to'],result['trans_result']

    # elif engine=='youdao':
    #     from_lang,to_lang=baidu2youdao_dict[from_lang],baidu2youdao_dict[to_lang]
    #     result=youdao_trans(word,to_lang)
    #     if result['errorCode']!=0:
    #         errorrecoder.adderror(f"有道翻译错误码:{result['errorCode']}")
    #         errorflag=1
    #         errorreturn['error_code']=result['errorCode']
    #     else:
    #         index_temp=result['type'].index('2')
    #         from_temp,to_temp=result['type'][:index_temp],result['type'][index_temp+1:]
    #         if from_temp in youdao2baidu_dict:
    #             successreturn['from']=youdao2baidu_dict[from_temp]
    #         else:
    #             successreturn['from']=from_temp
    #         if to_temp in youdao2baidu_dict:
    #             successreturn['to']=youdao2baidu_dict[to_temp]
    #         else:
    #             successreturn['to']=to_temp
    #
    #         ls_temp=[]
    #         for value in result['translateResult']:
    #             dict_temp={'src':value[0]['src'],'dst':value[0]['tgt']}
    #             ls_temp.append(dict_temp)
    #         successreturn['trans_result']=ls_temp

    elif engine=='youdaozhiyun':
        from_lang, to_lang = baidu2youdaozhiyun_dict[from_lang], baidu2youdaozhiyun_dict[to_lang]
        result=youdao_zhiyun_trans(word,from_lang,to_lang)
        if 'error_code' in result:
            errorflag=1
            errorreturn['error_code']=result['error_code']
        else:
            successreturn['from'],successreturn['to'],successreturn['trans_result']=result['from'],result['to'],result['trans_result']
            successreturn['speakUrl'], successreturn['tSpeakUrl']=result['speakUrl'],result['tSpeakUrl']
    elif engine=='customAPI':
        from_lang, to_lang = baidu2openai_dict[from_lang], baidu2openai_dict[to_lang]
        result=openai_trans(word,from_lang,to_lang)
        if 'error_code' in result:
            errorflag=1
            errorreturn['error_code']=result['error_code']
        else:
            successreturn['from'],successreturn['to'],successreturn['trans_result']=result['from'],result['to'],result['trans_result']
            successreturn['speakUrl'], successreturn['tSpeakUrl']=result['speakUrl'],result['tSpeakUrl']
    elif engine=='zhipu':
        from_lang, to_lang = baidu2openai_dict[from_lang], baidu2openai_dict[to_lang]
        result=zhipu_trans(word,from_lang,to_lang)
        if 'error_code' in result:
            errorflag=1
            errorreturn['error_code']=result['error_code']
        else:
            successreturn['from'],successreturn['to'],successreturn['trans_result']=result['from'],result['to'],result['trans_result']
            successreturn['speakUrl'], successreturn['tSpeakUrl']=result['speakUrl'],result['tSpeakUrl']
    else:
        raise Exception("engine error")

    if errorflag==1:
        print(errorreturn)
        return errorreturn
    else:
        return successreturn


if __name__ == '__main__':
    print(fanyi_text('我今天想要\n开开心心的化个妆', engine='youdaozhiyun', to_lang='en'))
    print(fanyi_text('我今天想要\n开开心心的化个妆', engine='baidu', to_lang='en'))
    print(fanyi_text('我今天想要\n开开心心的化个妆', engine='openai', to_lang='en'))