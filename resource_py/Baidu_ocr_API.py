# encoding:utf-8

import httpx
from account import Account
from resource_py.ErrorRecoder import errorrecoder
import base64
import json

def baiduocrAPI(file):
    account=Account()
    print('baiduocrAPI')
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    proxies = {"http": None, "https": None}
    host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={account.client_id}&client_secret={account.client_secret}'
    response = httpx.get(host,proxies=proxies).json()
    print('response1',response)
    if 'access_token' in response:
        access_token=response['access_token']
    else:
        errorrecoder.adderror("百度OCR获取token失败,请检查OCR账号是否填写正确")
        return -1
    '''
    通用文字识别
    '''
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    # request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件
    # f = open('photo1.png', 'rb')

    img = base64.b64encode(file)
    # print(type(img))


    params = {"image":img,'detect_language':'true','paragraph':'true'}
    access_token = access_token
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = httpx.post(request_url, data=params, headers=headers,proxies=proxies)
    print(response.json())
    return response.json()

if __name__ == '__main__':
    from PySide6.QtGui import QGuiApplication
    from PySide6.QtWidgets import QApplication
    from PySide6.QtCore import QBuffer, QIODevice,QByteArray
    import base64
    app = QApplication([])
    clipboard = QGuiApplication.clipboard()
    im = clipboard.image()

    if not im.isNull():
        print('这是一张图片')
        buffer = QBuffer()
        buffer.open(QIODevice.ReadWrite)
        im.save(buffer, 'PNG')
        picture_bytes=bytes(buffer.data())
        a = baiduocrAPI(picture_bytes)
        print(a)
    else:
        print('这不是一张图片')

    app.exec()