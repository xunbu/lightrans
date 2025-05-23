import configparser
from resource_py.utils import config_file_path
class Account():
    customAPI_url=''
    customAPI_key=''
    customAPI_model_id=''
    zhipu_key=''
    zhipu_model_id=''
    appid=''
    appkey=''
    client_id=''
    client_secret=''

    hotkey_select='ctrl+F1'
    hotkey_input='ctrl+enter'
    hotkey_ocr='ctrl+F2'

    engine= 'youdaozhiyun'

    domain='默认'

    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read(config_file_path, encoding='utf-8')#若文件不存在也会返回值
        self.init_ids_keys()
        self.init_hotkey()
        self.init_engin()
        self.init_domain()



    def init_ids_keys(self):
        flag=False
        if self.config.has_section("customAPI"):
            self.customAPI_url=self.config.get('customAPI','url')
            self.customAPI_key=self.config.get('customAPI','key')
            self.customAPI_model_id=self.config.get('customAPI','model_id')
        else:
            flag=True
            self.config.add_section('customAPI')
            self.config.set('customAPI', 'url', self.customAPI_url)
            self.config.set('customAPI', 'key', self.customAPI_key)
            self.config.set('customAPI', 'model_id', self.customAPI_model_id)
        if self.config.has_section("zhipu"):
            self.zhipu_key=self.config.get('zhipu','key')
            self.zhipu_model_id=self.config.get('zhipu','model_id')
        else:
            flag=True
            self.config.add_section('zhipu')
            self.config.set('zhipu', 'key', self.zhipu_key)
            self.config.set('zhipu', 'model_id', self.zhipu_model_id)
        if self.config.has_section('百度翻译'):
            self.appid = self.config.get('百度翻译', 'id')
            self.appkey = self.config.get('百度翻译', 'key')
        else:
            flag=True
            self.config.add_section('百度翻译')
            self.config.set('百度翻译', 'id', self.appid)
            self.config.set('百度翻译', 'key', self.appkey)
        if  self.config.has_section('百度OCR'):
            self.client_id =self.config.get('百度OCR', 'id')
            self.client_secret = self.config.get('百度OCR', 'key')
        else:
            flag=True
            self.config.add_section('百度OCR')
            self.config.set('百度OCR', 'id', self.client_id)
            self.config.set('百度OCR', 'key', self.client_secret)     
        if flag:
            self.config.write(open(config_file_path, 'w', encoding='utf-8'))

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

    def init_domain(self):
        if self.config.has_section('垂直翻译'):
            self.domain=self.config.get('垂直翻译', 'baidu_domain')
        else:
            self._domain2ini()

    def setidkey(self,keys_dict):
        self.customAPI_url,self.customAPI_key,self.customAPI_model_id=keys_dict["customAPI_url"],keys_dict["customAPI_key"],keys_dict["customAPI_model_id"]       
        self.zhipu_key,self.zhipu_model_id=keys_dict["zhipu_key"],keys_dict["zhipu_model_id"]
        self.appid,self.appkey=keys_dict["baidu_id"],keys_dict["baidu_key"]
        self.client_id,self.client_secret=keys_dict["ocr_id"],keys_dict["ocr_key"]
        self.config.set('customAPI', 'url', self.customAPI_url)
        self.config.set('customAPI', 'key', self.customAPI_key)
        self.config.set('customAPI', 'model_id', self.customAPI_model_id)
        self.config.set('zhipu', 'key', self.zhipu_key)
        self.config.set('zhipu', 'model_id', self.zhipu_model_id)
        self.config.set('百度翻译', 'id', self.appid)
        self.config.set('百度翻译', 'key', self.appkey)
        self.config.set('百度OCR', 'id', self.client_id)
        self.config.set('百度OCR', 'key', self.client_secret)
        self.config.write(open(config_file_path, 'w', encoding='utf-8'))

    def sethotkey(self,args):
        # *args=(hotkey_select,hotkey_input,hotkey_ocr)
        self.hotkey_select,self.hotkey_input,self.hotkey_ocr=args
        self._hotket2ini()

    def setengine(self,arg:str):
        self.engine=arg
        self._engine2ini()

    def setdomain(self,arg:str):
        self.domain=arg
        self._domain2ini()

        

    def _hotket2ini(self):
        if not self.config.has_section('热键'):
            self.config.add_section('热键')
        self.config.set('热键','select',self.hotkey_select)
        self.config.set('热键','ocr',self.hotkey_ocr)
        self.config.set('热键','input',self.hotkey_input)
        self.config.write(open(config_file_path, 'w',encoding='utf-8'))

    def _engine2ini(self):
        if not self.config.has_section('翻译引擎'):
            self.config.add_section('翻译引擎')
        self.config.set('翻译引擎','engine', self.engine)
        self.config.write(open(config_file_path, 'w', encoding='utf-8'))

    def _domain2ini(self):
        if not self.config.has_section('垂直翻译'):
            self.config.add_section('垂直翻译')
        self.config.set('垂直翻译', 'baidu_domain', self.domain)
        self.config.write(open(config_file_path, 'w', encoding='utf-8'))


if __name__ == '__main__':
    A=Account()
    print(A.customAPI_url,A.customAPI_key,A.customAPI_model_id)
    print([A.appid,A.appkey,A.client_id,A.client_secret,A.hotkey_select,A.hotkey_ocr,A.hotkey_input])