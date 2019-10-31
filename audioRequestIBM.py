#request section for the audio processing

url = "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize"

headers = {
    'Content-Type': "audio/flac",
    'Authorization': "Basic YXBpa2V5OmswOV9hV0I3Rmxma3hrS050TjdaQjhwUUdqMTI2ZTRJUlJwNVJ4VTNGYWwz",
    'User-Agent': "PostmanRuntime/7.19.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "cd590707-f657-4057-9c69-b326f568ae1d,44ad2c13-0c6b-4bbb-943f-539869afe4d8",
    'Host': "stream.watsonplatform.net",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "285928",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

data = open('C:\\Users\\Sims\\Downloads\\IBMWatsonTest.flac', 'rb')

response = requests.post(url, data, headers=headers)

print(response.text)

#what to do with the responses and stuff