from account import Account
from openai import OpenAI


def openai_trans(query,from_lang=None,to_lang="中文"):
    account=Account()
    base_url=account.customAPI_url
    api_key=account.customAPI_key
    client = OpenAI(base_url=base_url,api_key="xx" if api_key =="" else api_key)

    try:
        response = client.chat.completions.create(
            model=account.customAPI_model_id,
            messages=[
                {
                    "role": "system",
                    "content": f"You are a professional, authentic machine translation engine."
                },
                {"role": "user", "content": f"translate text input into {to_lang} . If translation is unnecessary (e.g. proper nouns, codes, etc.), return the original text. NO explanations. NO notes.  Text input:{query}"},
            ],
        )
        translated_text = response.choices[0].message.content.strip()
        successreturn = {'from': from_lang, 'to': to_lang, "trans_result": [{'src': query, 'dst': translated_text}], 'speakUrl':None, 'tSpeakUrl': None}
        return successreturn
    except Exception as e:
        errorreturn = {'error_code': str(e)}
        return errorreturn





if __name__ == '__main__':
    print(openai_trans("i love you"))