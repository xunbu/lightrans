from account import Account
from openai import OpenAI, base_url, api_key


def openai_trans(query,from_lang=None,to_lang="中文"):
    account=Account()
    base_url=account.openai_url
    api_key=account.openai_key
    client = OpenAI(base_url=base_url,api_key="xx" if api_key =="" else api_key)

    try:
        response = client.chat.completions.create(
            model=account.openai_model_id,
            messages=[
                {
                    "role": "system",
                    "content": f"You are a professional translator specializing in {to_lang}. Only return the translated text, no explanations or extra content."
                },
                {"role": "user", "content": query},
            ],
            temperature=0.1,  # 减少随机性，确保稳定翻译
        )
        translated_text = response.choices[0].message.content.strip()
        successreturn = {'from': from_lang, 'to': to_lang, "trans_result": [{'src': query, 'dst': translated_text}], 'speakUrl':None, 'tSpeakUrl': None}
        return successreturn
    except Exception as e:
        errorreturn = {'error_code': str(e)}
        return errorreturn





if __name__ == '__main__':
    print(openai_trans("i love you"))