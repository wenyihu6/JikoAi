# jiko-ai
🐈 A creative final project for SE101 (cohort 2024) - the first-year concepts course for Software Engineering @ the University of Waterloo. jiko-ai is a virtual pet, styled after Tamagotchi™, in which the user is encouraged to not only look after their creatures, but after themselves too. Through activities like medition and affirmations, both the pet and the user can grow together!
### Credits
The audio processing of this project relies heavily on [IBM's Speech-To-Text Service](https://www.ibm.com/ca-en/marketplace/speech-to-text), and a majority of the game code was written using the pygame library (see Dependencies/Imports). 

Other sites and resources that were integral to the building of the project include:

#### Dependencies/Imports
* [pygame](https://pypi.org/project/pygame/) - for building multimedia applications like games
* [pillow](https://pypi.org/project/Pillow/) - an imaging library
* [requests](https://pypi.org/project/requests/) - for being able to make API calls to IBM Watson
* json - part of the standard Python library for dealing with this format
* [pyaudio](https://pypi.org/project/PyAudio/) - for handling audio I/O
* wave - part of the standard Python library to interface with the WAV format

#### Useful Links
Some links we accessed for the project include: 
* for helping set up the wifi on the Raspberry Pi from Adafruit: [Setting up Wifi by Hand](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/setting-up-wifi-with-occidentalis); a .conf file that we used that we made from this is made available at [@simcard0000's gists](https://gist.github.com/simcard0000)
* this [Stack Overflow question: How to make buttons in python pygame](https://stackoverflow.com/questions/10168447/how-to-make-buttons-in-python-pygame/10169083) was accessed to help us make our code for creating buttons
* the code for recording and storing the .wav file produced from the audio input is from this [Real Python Tutorial for Playing and Recording Sound in Python](https://realpython.com/playing-and-recording-sound-python/#pyaudio_1)
* the [Text to Speech - IBM Cloud API Docs](https://cloud.ibm.com/apidocs/text-to-speech/text-to-speech) were accessed to learn more about the functions of the API
* python file i/o knowledge was pieced together from tutorials such as this: [File Handling in Python](https://www.geeksforgeeks.org/file-handling-python/)
* for learning how to open a program automatically on startup: [Stack Overflow: Open chromium full screen on startup](https://raspberrypi.stackexchange.com/questions/69204/open-chromium-full-screen-on-start-up)
* the gifImage class used to split a gif into multiple images for reanimation is from this Stack Overflow question as well: [How to Extract Frame From GIF, and Reconstruct the Details of each Frame?](https://stackoverflow.com/questions/47483375/how-to-extract-frame-from-gif-and-reconstruct-the-details-of-each-frame/48670390#48670390)

Authors: Simran Thind (@simcard0000), Cole MacPhail (@colemacphail), Zhengmao Ouyang (@SwuntiiTHICC), Wenyi Hu (@wenyihu3)
