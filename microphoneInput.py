import wave
import requests
import pyaudio

#getting audio for stuff

chunk = 8192
sample_format = pyaudio.paInt16
channels = 2
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
