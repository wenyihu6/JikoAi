import requests

url = "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize"

headers = {
    'Content-Type': "audio/flac",
    'Authorization': "Basic -",
    'User-Agent': "PostmanRuntime/7.19.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "-",
    'Host': "stream.watsonplatform.net",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "285928",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, headers=headers)

print(response.text)
