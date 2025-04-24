from account import Account
import requests


def zhipu_trans(query, from_lang=None, to_lang="中文"):
    account = Account()
    base_url = r"https://open.bigmodel.cn/api/paas/v4"
    api_key = account.zhipu_key
    model_id = account.zhipu_model_id

    # 构造完整的API请求URL
    # Chat Completions endpoint is usually /v1/chat/completions
    url = f"{base_url}/chat/completions"

    # 设置请求头
    headers = {
        "Content-Type": "application/json",
        # 认证头，使用Bearer token方式，key为空时使用"xx"与原代码逻辑一致
        "Authorization": f"Bearer {'xx' if api_key == '' else api_key}"
    }

    # 构造请求体（payload），格式与openai库的create方法参数类似
    payload = {
        "model": model_id,
        "messages": [
            {
                "role": "system",
                "content": "You are a professional, authentic machine translation engine."
            },
            {
                "role": "user",
                "content": f"translate text input into {to_lang} . If translation is unnecessary (e.g. proper nouns, codes, etc.), return the original text. NO explanations. NO notes.  Text input:{query}"
            },
        ],
        # 可选：设置 temperature 为 0 通常对翻译任务更好，结果更确定
        # "temperature": 0,
    }

    try:
        # 发送POST请求
        response = requests.post(url, headers=headers, json=payload)

        # 检查HTTP响应状态码，如果不是2xx，会抛出HTTPError异常
        response.raise_for_status()

        # 解析JSON响应体
        response_data = response.json()

        # 从响应中提取翻译结果
        # 响应结构通常是 response_data['choices'][0]['message']['content']
        translated_text = response_data['choices'][0]['message']['content'].strip()

        # 构造与原函数一致的成功返回值格式
        successreturn = {
            'from': from_lang,
            'to': to_lang,
            "trans_result": [{'src': query, 'dst': translated_text}],
            'speakUrl': None,
            'tSpeakUrl': None
        }
        return successreturn

    except Exception as e:
        # 捕获其他未预料的异常
        print(f"An unexpected error occurred: {e}")
        errorreturn = {'error_code': f"Unexpected Error: {e}"}
        return errorreturn




if __name__ == '__main__':
    print(openai_trans("i love you"))