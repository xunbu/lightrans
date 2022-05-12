import os,json,configparser
class Account():
    appid=''
    appkey=''
    client_id=''
    client_secret=''

    hotkey_select='ctrl+F1'
    hotkey_input='ctrl+enter'
    hotkey_ocr='ctrl+F2'

    engine= 'baiduReptile'

    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read('./account.ini', encoding='utf-8')#若文件不存在也会返回值
        self.init_ids_keys()
        self.init_hotkey()
        self.init_engin()



    def init_ids_keys(self):
        if self.config.has_section('百度翻译') and self.config.has_section('百度OCR'):
            self.appid = self.config.get('百度翻译', 'id')
            self.appkey = self.config.get('百度翻译', 'key')
            self.client_id =self.config.get('百度OCR', 'id')
            self.client_secret = self.config.get('百度OCR', 'key')
            print(f'info:appid={self.appid},appkey={self.appkey},client_id={self.client_id},client_secret={self.client_secret}')
        else:
            self._idkey2ini()
            return 0

    def init_hotkey(self):
        if self.config.has_section('热键'):
            self.hotkey_select=self.config.get('热键', 'select')
            self.hotkey_ocr=self.config.get('热键', 'ocr')
            self.hotkey_input=self.config.get('热键', 'input')
        else:
            self._hotket2ini()

    def init_engin(self):
        if self.config.has_section('翻译引擎'):
            self.engine=self.config.get('翻译引擎', 'engine')
        else:
            self._engine2ini()

    def setidkey(self,args):
        self.appid,self.appkey, self.client_id,self.client_secret = args
        self._idkey2ini()

    def sethotkey(self,args):
        # *args=(hotkey_select,hotkey_input,hotkey_ocr)
        self.hotkey_select,self.hotkey_input,self.hotkey_ocr=args
        self._hotket2ini()

    def setengine(self,arg:str):
        self.engine=arg
        self._engine2ini()

    def _idkey2ini(self):
        if not self.config.has_section('百度翻译'):
            self.config.add_section('百度翻译')
        if not  self.config.has_section('百度OCR'):
            self.config.add_section('百度OCR')
        self.config.set('百度翻译', 'id', self.appid)
        self.config.set('百度翻译', 'key', self.appkey)
        self.config.set('百度OCR', 'id', self.client_id)
        self.config.set('百度OCR', 'key', self.client_secret)
        self.config.write(open('account.ini', 'w', encoding='utf-8'))

    def _hotket2ini(self):
        if not self.config.has_section('热键'):
            self.config.add_section('热键')
        self.config.set('热键','select',self.hotkey_select)
        self.config.set('热键','ocr',self.hotkey_ocr)
        self.config.set('热键','input',self.hotkey_input)
        self.config.write(open('account.ini', 'w',encoding='utf-8'))

    def _engine2ini(self):
        if not self.config.has_section('翻译引擎'):
            self.config.add_section('翻译引擎')
        self.config.set('翻译引擎','engine', self.engine)
        self.config.write(open('account.ini', 'w', encoding='utf-8'))



if __name__ == '__main__':
    A=Account()
    print([A.appid,A.appkey,A.client_id,A.client_secret,A.hotkey_select,A.hotkey_ocr,A.hotkey_input])