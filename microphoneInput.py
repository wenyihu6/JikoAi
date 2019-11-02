import wave
import requests
import pyaudio

#getting audio for stuff

chunk = 8192
sample_format = pyaudio.paInt16
#two channels for Windows, one channel for Mac
channels = 1
fs = 44100
seconds = 10
filename = 'command.wav'
p = pyaudio.PyAudio()

print(p.get_default_output_device_info())

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                input_device_index=0,
                frames_per_buffer=chunk,
                input=True)

print("starting recording")
frames = []
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

print("stopping recording")
filewriting = wave.open(filename, 'wb')
filewriting.setnchannels(channels)
filewriting.setsampwidth(p.get_sample_size(sample_format))
filewriting.setframerate(fs)
filewriting.writeframes(b''.join(frames))
filewriting.close()

url = "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize"

headers = {
    'Content-Type': "audio/wav",
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

data = open('command.wav', 'rb')

response = requests.post(url, data, headers=headers)

print(response.text)