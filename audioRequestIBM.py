import requests
import json

url = "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize"

headers = {
    'Content-Type': "audio/flac",
    'Authorization': "Basic YXBpa2V5OjY2Ylk2SmljTUh0LW1SdjJCZk8tYzEwLTJ0U0xweVVTZkRRTlFjU3A5WV90",
    'User-Agent': "PostmanRuntime/7.19.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "507a31da-ffc7-430e-9dad-b8006da32933,270b9439-797f-4e71-bc99-c13feb217166",
    'Host': "stream.watsonplatform.net",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "285928",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

data = open('C:\\Users\\Sims\\Downloads\\IBMWatsonTest.flac', 'rb')

response = requests.post(url, data, headers=headers)

print(response.text)