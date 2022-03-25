import os,json
class Account():
    appid=''
    appkey=''
    client_id=''
    client_secret=''

    hotkey_select='ctrl+c'
    hotkey_input='ctrl+enter'
    hotkey_ocr='ctrl+alt'

    def __init__(self):
        self.init_ids_keys()
        self.init_hotkey()



    def init_ids_keys(self):
        if os.path.exists('./account.txt'):
            with open('account.txt', 'r') as fp:
                info = fp.read()
            infolist = info.split('\n')
            self.appid = infolist[0][6:]
            self.appkey = infolist[1][7:]
            self.client_id = infolist[2][10:]
            self.client_secret = infolist[3][14:]
            print(
                f'info:appid={self.appid},appkey={self.appkey},client_id={self.client_id},client_secret={self.client_secret}')
        else:
            with open('account.txt','w') as fp:
                fp.write('appid=这里填百度翻译开放平台的APPID\nappkey=这里填百度翻译开放平台的密钥\nclient_id=这里填百度AI开放平台(文字识别)的APIKey\nclient_secret=这里填百度AI开放平台(文字识别)的SecretKey')
            return 0

    def init_hotkey(self):
        if os.path.exists('./hotkey.txt'):
            with open('hotkey.txt', 'r') as fp:
                info = fp.read()
            hotkey_dir=json.loads(info)
            self.hotkey_select=hotkey_dir["hotkey_select"]
            self.hotkey_ocr=hotkey_dir["hotkey_ocr"]
            self.hotkey_input=hotkey_dir["hotkey_input"]
        else:
            self._hotket2txt()


    def sethotkey(self,args):
        # *args=(hotkey_select,hotkey_input,hotkey_ocr)
        self.hotkey_select,self.hotkey_input,self.hotkey_ocr=args
        self._hotket2txt()

    def _hotket2txt(self):
        hotkey_dir = {r"hotkey_select": self.hotkey_select, r"hotkey_ocr": self.hotkey_ocr,
                      r"hotkey_input": self.hotkey_input}
        with open('hotkey.txt', 'w') as fp:
            fp.write(json.dumps(hotkey_dir, indent=4))



if __name__ == '__main__':
    A=Account()
    print(A.hotkey_copynorow)