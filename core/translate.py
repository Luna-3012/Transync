import requests
import os

def translate_text(text, to_lang, from_lang='auto'):
    api_key = os.getenv("AZURE_TRANSLATOR_KEY")
    region = os.getenv("AZURE_TRANSLATOR_REGION")
    endpoint = os.getenv("AZURE_TRANSLATOR_ENDPOINT")
    if not endpoint:
        endpoint = f"https://{region}.api.cognitive.microsofttranslator.com"

    route = "/translate?api-version=3.0"
    from_param = f"&from={from_lang}" if from_lang and from_lang != 'auto' else ""
    params = f"{from_param}&to={to_lang}"
    url = endpoint + route + params

    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Ocp-Apim-Subscription-Region": region,
        "Content-type": "application/json"
    }

    body = [{"Text": text}]
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    result = response.json()
    return result[0]['translations'][0]['text']
