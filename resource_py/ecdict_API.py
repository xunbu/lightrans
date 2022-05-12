import requests,json,re
def ecdict_search(word='',mode='query'):
    if not re.match(r"[\s?a-zA-Z+]",word):
        return {'error':'word is not English'}
    proxies = {"http": None, "https": None}
    url = 'https://xunbu.cc/ecdict/search'
    headers={'Content-Type': 'application/json'}
    data = json.dumps({'word':word,'mode':mode})
    print(data)
    response = requests.post(url, data=data,headers=headers,proxies=proxies)
    response_json=response.json()
    return response_json