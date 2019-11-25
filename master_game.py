import sys
from enum import Enum
from GIFImage import GIFImage
from Pet import Pet 
from Pet import PetType
from Buttonify import Buttonify
from RectButton import RectButton
from Meditate import Meditate
import pygame as pg
from RectButton import RectButton
import os
import shutil
import datetime
import time
import random
import wave
import requests
import pyaudio

# import config

if sys.platform.startswith('linux'):
    import RPi.GPIO as GPIO

class Screen(Enum):
    STARTING = 0
    CREDITS = 1
    SELECTION = 2
    EGG = 3
    Q_A = 4
    Q_A1 = 5
    Q_A2 = 6
    Q_A3 = 7
    Q_A4 = 8
    HATCH = 9
    HOME = 100
    FOOD = 101
    WATER = 102
    SLEEP = 103
    FUN = 104
    MEDITATION = 105
    WATER_ACTIVE = 106

    def __lt__(this, other):
        if this.__class__ is other.__class__:
            return this.value < other.value
        return NotImplemented

    def __gt__(this, other):
        if this.__class__ is other.__class__:
            return this.value > other.value
        return NotImplemented

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  # More colours should be added here
ORANGE = (255, 128, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (127, 0, 255)
WIDTH = 800
HEIGHT = 480

FOOD_CHANGE_RATE = -100 / (12 * 60 * 60 * 12) # 100% per (12 f/s * 60s/m * 60 m/h * 12 h to empty)
WATER_CHANGE_RATE = -100 / (12 * 60 * 60 * 6) # 100% per (12 f/s * 60s/m * 60 m/h * 6 h to empty)
SLEEP_CHANGE_RATE = -100 / (12 * 60 * 60 * 16) # 100% per (12 f/s * 60s/m * 60 m/h * 16 h to empty)
STRESS_CHANGE_RATE = 100 / (12 * 60 * 60 * 24) # 100% per (12 f/s * 60s/m * 60 m/h * 24 h to full)

pg.init()
pg.font.init()
init_time = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%B-%d %I:%M:%S.%f"), "%Y-%B-%d %I:%M:%S.%f")
titleFont = pg.font.Font(os.getcwd() + "/VT323-Regular.ttf", 180)
textFont = pg.font.Font(os.getcwd() + "/VT323-Regular.ttf", 60)
smallFont = pg.font.Font(os.getcwd() + "/VT323-Regular.ttf", 40)

pg.mixer.music.load('Bitbasic_-_01_-_An_opener.mp3')
pg.mixer.music.play(-1)

screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)

currGameState = Screen.STARTING
currPet = Pet.init_gifImage(PetType.BALAGIF, "bala")

def update_save():
    global currPet
    global currGameState
    savefile = open(os.getcwd() + "/save/saveFile.txt", "w+")
    savefile.write(str((currPet.petType)) + "\n")
    savefile.write(currPet.name + "\n")
    savefile.write(str(currPet.food) + "\n")
    savefile.write(str(currPet.water) + "\n")
    savefile.write(str(currPet.sleep) + "\n")
    savefile.write(str(currPet.stress) + "\n")
    savefile.write(str(datetime.datetime.now().strftime("%Y-%B-%d %I:%M:%S.%f")) + "\n")
    savefile.close()
 
# Our function on what to do when the button is pressed  
def Shutdown(channel):
    global currPet
    global currGameState
    if currGameState.value > Screen.HATCH.value:
        update_save()
    os.system("sudo shutdown -h now")

def toggle_voice(channel):
    global currGameState
    global currPet
    #getting audio for stuff

    chunk = 8192
    sample_format = pyaudio.paInt16
    #two channels for Windows, one channel for Mac/Linux
    channels = 1
    fs = 44100
    seconds = 2
    filename = 'command.wav'
    p = pyaudio.PyAudio()

    #print(p.get_default_output_device_info())

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
        'Authorization': config.auth_token,
        'User-Agent': "PostmanRuntime/7.19.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': config.postman_token,
        'Host': "stream.watsonplatform.net",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "285928",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    data = open('command.wav', 'rb')

    response = requests.post(url, data, headers=headers)
    cleanResponse = response.json()

    print(response.text)
    words = cleanResponse['results'][0]['alternatives'][0]['transcript']
    print(words)

    if ((words == 'begin ' or words == 'start ') and currGameState == Screen.STARTING):
        currGameState = Screen.SELECTION
    if (words == 'credits ' and currGameState == Screen.STARTING):
        currGameState = Screen.CREDITS
    if (words == 'new game ' and currGameState == Screen.SELECTION):
        currGameState = Screen.Q_A
    if (words == 'load game ' and currGameState == Screen.SELECTION):
        currPet.setCoords(WIDTH / 2, HEIGHT / 2)
        currGameState = Screen.HOME
    if (words == 'let\'s go ' and currGameState == Screen.Q_A):
        currGameState = Screen.Q_A1
    if ((words == 'not often ' or words == 'sometimes ' or words == 'often ')
        and currGameState == Screen.Q_A1):
        currGameState = Screen.Q_A2
    if ((words == 'disagree ' or words == 'not sure ' or words == 'agree ')):
        if (currGameState == Screen.Q_A2):
            currGameState = Screen.Q_A3
        if (currGameState == Screen.Q_A3):
            currGameState = Screen.Q_A4
        if (currGameState == Screen.Q_A4):
            currGameState = Screen.HOME
            currPet.setCoords(WIDTH / 2, HEIGHT / 2)
    if (currGameState == Screen.HOME):
        if (words == 'food '):
            currGameState = Screen.FOOD
        if (words == 'water '):
            currGameState = Screen.WATER
        if (words == 'sleep '):
            currGameState = Screen.SLEEP
        if (words == 'play '):
            currGameState = Screen.FUN
    if (currGameState == Screen.SLEEP):
        if (words == 'meditation '):
            currGameState = Screen.MEDITIATION
    if (words == 'exit '):
        os.system("sudo shutdown -h now")
    if (words == 'done ' and (currGameState == Screen.FOOD or currGameState == Screen.WATER or 
    currGameState == Screen.SLEEP or currGameState == Screen.MEDITATION or currGameState == Screen.FUN)):
        currGameState = Screen.HOME
        currPet.setCoords(WIDTH / 2, HEIGHT / 2)

if sys.platform.startswith('linux'):
    GPIO.setmode(GPIO.BOARD)  
    GPIO.setup(29, GPIO.IN, pull_up_down = GPIO.PUD_UP) #Power
    GPIO.add_event_detect(29, GPIO.FALLING, callback = Shutdown, bouncetime = 5000)  
    GPIO.setup(33, GPIO.IN, pull_up_down = GPIO.PUD_UP) #Voice
    GPIO.add_event_detect(33, GPIO.FALLING, callback = toggle_voice, bouncetime = 250)  

def main():
    global currPet
    global currGameState

    savefile = open(os.getcwd() + "/save/saveFile.txt", "a+")

    FRAMERATE = 12

    titleBG = GIFImage(os.getcwd() + "/graphicAssets/BgTitle3")
    homeBG = GIFImage(os.getcwd() + "/graphicAssets/BgTitle5")
    homeBG.resize(800, 480)
    qaBG = GIFImage(os.getcwd() + "/graphicAssets/BgTitle4")
    qaBG.resize(800, 480)
    sleepBG = GIFImage(os.getcwd() + "/graphicAssets/SleepBG")
    sleepBG.resize(800, 480)
    waterBG = GIFImage(os.getcwd() + "/graphicAssets/BgWater")
    waterBG.resize(800, 480)
    foodBG = GIFImage(os.getcwd() + "/graphicAssets/BgFood")
    foodBG.resize(800, 480)
    playBG = GIFImage(os.getcwd() + "/graphicAssets/BgPlay")
    playBG.resize(800, 480)

    eggUnhatched = GIFImage(os.getcwd() + "/graphicAssets/EggUnhatched",
                            WIDTH/4 + 80, HEIGHT/2 - 170, 15)
    eggUnhatched.resize(250, 250)

    startButton = Buttonify(os.getcwd() + "/graphicAssets/startButton.png", screen)
    startButton.resize(300, 100)
    startButton.setCoords(100, 300)

    newGameButton = Buttonify(os.getcwd() + "/graphicAssets/NewGame.png", screen)
    newGameButton.resize(320, 110)
    newGameButton.setCoords(75, 180)

    continueGameButton = Buttonify(os.getcwd() + "/graphicAssets/LoadGame.png", screen)
    continueGameButton.resize(300, 100)
    continueGameButton.setCoords(425, 175)

    qa1LeftButton = RectButton(
        WIDTH / 4 - 145, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa1MiddleButton = RectButton(
        WIDTH / 4 + 98, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa1RightButton = RectButton(
        WIDTH / 4 + 340, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)

    qa2LeftButton = RectButton(
        WIDTH / 4 - 145, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa2MiddleButton = RectButton(
        WIDTH / 4 + 98, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa2RightButton = RectButton(
        WIDTH / 4 + 340, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)

    qa3LeftButton = RectButton(
        WIDTH / 4 - 145, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa3MiddleButton = RectButton(
        WIDTH / 4 + 98, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa3RightButton = RectButton(
        WIDTH / 4 + 340, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)

    qa4LeftButton = RectButton(
        WIDTH / 4 - 145, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa4MiddleButton = RectButton(
        WIDTH / 4 + 98, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa4RightButton = RectButton(
        WIDTH / 4 + 340, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)

    HomeFoodButton = RectButton(
        7 * WIDTH / 8, HEIGHT / 16 + 10, 90, 90, screen, BLACK, 180)
    HomeWaterButton = RectButton(
        7 * WIDTH / 8, HEIGHT / 16 + 110, 90, 90, screen, BLACK, 180)
    HomeSleepButton = RectButton(
        7 * WIDTH / 8, HEIGHT / 16 + 210, 90, 90, screen, BLACK, 180)
    HomeStressButton = RectButton(
        7 * WIDTH / 8, HEIGHT / 16 + 310, 90, 90, screen, BLACK, 180)

    sleepAffirmationsButton = RectButton(10, 60, 215, 50, screen, BLACK, 100)
    sleepLogButton = RectButton(80, 10, 215, 50, screen, BLACK, 100)
    sleepMeditateButton = RectButton(100, 100, 215, 50, screen, BLACK, 100)
    sleepBreatheButton = RectButton(200, 200, 215, 50, screen, BLACK, 100)

    backButton = RectButton(10, 10, 215, 50, screen, BLACK, 100)

    creditsButton = RectButton(300, 350, 215, 50, screen, BLACK, 100)

    creditToTitleButton = RectButton(20, 20, 215, 50, screen, BLACK, 100)

    randomButton = RectButton(20, 20, 215, 50, screen, BLACK, 100)

    exitButton = RectButton(20, HEIGHT - 70, 215, 50, screen, BLACK, 100)

    currPet.setCoords(WIDTH / 2, 3 * HEIGHT / 4)
    currPet.setMoveCycleCount(45)

    meditate = Meditate(screen)

    checkin_button = RectButton(20, 20, 215, 50, screen, BLACK, 100)
    checkin_button.getImageRect().center = (WIDTH / 2, HEIGHT / 2)

    water_question_button = RectButton(20, 20, 550, 50, screen, BLACK)
    water_question_button.getImageRect().center = (WIDTH / 2, HEIGHT / 4)

    water_response_button = RectButton(20, 20, 650, 50, screen, BLACK)
    water_response_button.getImageRect().center = (WIDTH / 2, HEIGHT / 4)

    water_drop1 = Buttonify(os.getcwd() + "/graphicAssets/WaterDrop.png", screen)
    water_drop2 = Buttonify(os.getcwd() + "/graphicAssets/WaterDrop.png", screen)
    water_exists1 = True
    water_exists2 = True
    water_drop1.resize(100, 100)
    water_drop2.resize(100, 100)

    petSum = 0
    
    while True:

        clock = pg.time.Clock()

        ev = pg.event.get()
        screen.fill(WHITE)

        if currGameState.value > Screen.HATCH.value:
            currPet.food += FOOD_CHANGE_RATE
            currPet.water += WATER_CHANGE_RATE
            currPet.sleep += SLEEP_CHANGE_RATE
            currPet.stress += STRESS_CHANGE_RATE

            currPet.food = 0 if currPet.food < 0 else 100 if currPet.food > 100 else currPet.food
            currPet.water = 0 if currPet.water < 0 else 100 if currPet.water > 100 else currPet.water
            currPet.sleep = 0 if currPet.sleep < 0 else 100 if currPet.sleep > 100 else currPet.sleep
            currPet.stress = 0 if currPet.stress < 0 else 100 if currPet.stress > 100 else currPet.stress

        if currGameState == Screen.STARTING:

            titleBG.animate(screen)

            title = titleFont.render('JikoAi', True, WHITE) 
            screen.blit(title, (WIDTH / 4 - 15, HEIGHT / 2 - 125))

            subtitle = textFont.render('Click to begin!', True, WHITE)
            screen.blit(subtitle, (WIDTH / 4 + 25, HEIGHT / 2 + 32))

            creditsButton.draw()
            creditsButton.draw_text("Credits")

        elif currGameState == Screen.SELECTION:

            titleBG.animate(screen)

            newGameButton.draw()
            continueGameButton.draw()

        elif currGameState == Screen.HOME:

            homeBG.animate(screen)

            innerFoodBar = pg.Rect(40, 40, 200, 25)
            innerWaterBar = pg.Rect(40, 80, 200, 25)
            innerSleepBar = pg.Rect(40, 120, 200, 25)
            innerStressBar = pg.Rect(40, 160, 200, 25)
            currPet.drawStatBar(screen, innerFoodBar, ORANGE, currPet.food)
            currPet.drawStatBar(screen, innerWaterBar, BLUE, currPet.water)
            currPet.drawStatBar(screen, innerSleepBar, PURPLE, currPet.sleep)
            currPet.drawStatBar(screen, innerStressBar, RED, currPet.stress)
            currPet.draw(screen)

            HomeFoodButton.draw()
            HomeFoodButton.draw_text("food")
            HomeWaterButton.draw()
            HomeWaterButton.draw_text("water")
            HomeSleepButton.draw()
            HomeSleepButton.draw_text("sleep")
            HomeStressButton.draw()
            HomeStressButton.draw_text("play")

            exitButton.draw()
            exitButton.draw_text("EXIT")

            randomButton.draw()
            randomButton.draw_text("RANDOM")
        elif currGameState == Screen.EGG:
            print("FILLER")
        elif currGameState == Screen.HATCH:
            if petSum <= 6:
                currPet = Pet.init_gifImage(PetType.BALAGIF, "bala")
            elif petSum <= 9:
                currPet = Pet.init_gifImage(PetType.MAMAUGIF, "mamau")
            else:
                currPet = Pet.init_gifImage(PetType.TORAGIF, "tora")
            savefile.write(str(currPet.petType.value) + "\n")
            currGameState = Screen.HOME
            currPet.setCoords(WIDTH / 2, HEIGHT / 2)
        elif currGameState == Screen.Q_A:

            homeBG.animate(screen)
            eggUnhatched.animate(screen)

            bgRect = pg.Surface((600, 75))
            bgRect.set_alpha(100)
            bgRect.fill(BLACK)
            screen.blit(bgRect, (WIDTH / 4 - 80, HEIGHT / 2 + 70))

            eggSubtitle = textFont.render('Who will your pet be?', True, WHITE)
            screen.blit(eggSubtitle, (WIDTH / 4 - 30, HEIGHT / 2 + 77))

        elif currGameState == Screen.Q_A1:

            qaBG.animate(screen)

            bgRect = pg.Surface((600, 75))
            bgRect.set_alpha(100)
            bgRect.fill(BLACK)
            screen.blit(bgRect, (WIDTH / 4 - 90, HEIGHT / 2 - 160))

            qTitle = textFont.render('Some questions first!', True, WHITE)
            screen.blit(qTitle, (WIDTH / 4 - 30, HEIGHT / 2 - 157))

            q1Text = textFont.render(
                'Do you often feel stressed?', True, WHITE)

            bgRect1 = pg.Surface((700, 75))
            bgRect1.set_alpha(100)
            bgRect1.fill(BLACK)

            screen.blit(bgRect1, (WIDTH / 4 - 145, HEIGHT / 2 - 35))
            screen.blit(q1Text, (WIDTH / 4 - 110, HEIGHT / 2 - 30))

            bgRect2 = pg.Surface((215, 50))
            bgRect2.set_alpha(100)
            bgRect2.fill(BLACK)

            qa1LeftButton.draw()
            qa1LeftButton.draw_text("Not often")

            qa1MiddleButton.draw()
            qa1MiddleButton.draw_text("Sometimes")

            qa1RightButton.draw()
            qa1RightButton.draw_text("Often")

        elif currGameState == Screen.Q_A2:

            qaBG.animate(screen)

            bgRect = pg.Surface((600, 75))
            bgRect.set_alpha(100)
            bgRect.fill(BLACK)
            screen.blit(bgRect, (WIDTH / 4 - 90, HEIGHT / 2 - 160))

            qTitle = textFont.render('Some questions first!', True, WHITE)
            screen.blit(qTitle, (WIDTH / 4 - 30, HEIGHT / 2 - 157))

            q1Text = textFont.render('I feel good about myself.', True, WHITE)

            bgRect1 = pg.Surface((700, 75))
            bgRect1.set_alpha(100)
            bgRect1.fill(BLACK)

            screen.blit(bgRect1, (WIDTH / 4 - 145, HEIGHT / 2 - 35))
            screen.blit(q1Text, (WIDTH / 4 - 110, HEIGHT / 2 - 30))

            bgRect2 = pg.Surface((215, 50))
            bgRect2.set_alpha(100)
            bgRect2.fill(BLACK)

            qa2LeftButton.draw()
            qa2LeftButton.draw_text("Disagree")

            qa2MiddleButton.draw()
            qa2MiddleButton.draw_text("Not sure")

            qa2RightButton.draw()
            qa2RightButton.draw_text("Agree")

        elif currGameState == Screen.Q_A3:

            qaBG.animate(screen)

            bgRect = pg.Surface((600, 75))
            bgRect.set_alpha(100)
            bgRect.fill(BLACK)
            screen.blit(bgRect, (WIDTH / 4 - 90, HEIGHT / 2 - 160))

            qTitle = textFont.render('Some questions first!', True, WHITE)
            screen.blit(qTitle, (WIDTH / 4 - 30, HEIGHT / 2 - 157))

            q1Text = textFont.render(
                'I have things under control.', True, WHITE)

            bgRect1 = pg.Surface((700, 75))
            bgRect1.set_alpha(100)
            bgRect1.fill(BLACK)

            screen.blit(bgRect1, (WIDTH / 4 - 145, HEIGHT / 2 - 35))
            screen.blit(q1Text, (WIDTH / 4 - 110, HEIGHT / 2 - 30))

            bgRect2 = pg.Surface((215, 50))
            bgRect2.set_alpha(100)
            bgRect2.fill(BLACK)

            qa3LeftButton.draw()
            qa3LeftButton.draw_text("Disagree")

            qa3MiddleButton.draw()
            qa3MiddleButton.draw_text("Not sure")

            qa3RightButton.draw()
            qa3RightButton.draw_text("Agree")

        elif currGameState == Screen.Q_A4:

            qaBG.animate(screen)

            bgRect = pg.Surface((600, 75))
            bgRect.set_alpha(100)
            bgRect.fill(BLACK)
            screen.blit(bgRect, (WIDTH / 4 - 90, HEIGHT / 2 - 160))

            qTitle = textFont.render('Some questions first!', True, WHITE)
            screen.blit(qTitle, (WIDTH / 4 - 30, HEIGHT / 2 - 157))

            q1Text = textFont.render(
                'I take good care of myself.', True, WHITE)

            bgRect1 = pg.Surface((700, 75))
            bgRect1.set_alpha(100)
            bgRect1.fill(BLACK)

            screen.blit(bgRect1, (WIDTH / 4 - 145, HEIGHT / 2 - 35))
            screen.blit(q1Text, (WIDTH / 4 - 110, HEIGHT / 2 - 30))

            bgRect2 = pg.Surface((215, 50))
            bgRect2.set_alpha(100)
            bgRect2.fill(BLACK)

            qa4LeftButton.draw()
            qa4LeftButton.draw_text("Disagree")

            qa4MiddleButton.draw()
            qa4MiddleButton.draw_text("Not sure")

            qa4RightButton.draw()
            qa4RightButton.draw_text("Agree")

        
        elif currGameState == Screen.WATER:
            waterBG.animate(screen)
            backButton.draw()
            backButton.draw_text("Back")
            checkin_button.draw()
            checkin_button.draw_text("CHECK IN")
            water_question_button.draw()
            water_question_button.draw_text("Have you drank anything recently?")
        elif currGameState == Screen.WATER_ACTIVE:

            waterBG.animate(screen)
            backButton.draw()
            backButton.draw_text("Back")
            water_response_button.draw()
            water_response_button.draw_text("Thank you for keeping us both healthy!")

            if water_exists1:
                water_drop1.draw()

            if water_exists2:
                water_drop2.draw()

            currPet.draw(screen)
        elif currGameState == Screen.FUN:
            playBG.animate(screen)
            backButton.draw()
            backButton.draw_text("Back")
        elif currGameState == Screen.SLEEP:
            sleepBG.animate(screen)
            #affirmations
            sleepAffirmationsButton.draw()
            sleepAffirmationsButton.draw_text("Affirmations")
            #meditate
            #sleep
            #breathe
            #back
            backButton.draw()
            backButton.draw_text("Back")
        elif currGameState == Screen.FOOD:
            foodBG.animate(screen)
            backButton.draw()
            backButton.draw_text("Back")
        elif currGameState == Screen.MEDITATION:
            backButton.draw()
            backButton.draw_text("Back")
            sleepBG.animate(screen)
            meditate.setOn()
        elif currGameState == Screen.CREDITS:
            titleBG.animate(screen)
            creditToTitleButton.draw()
            creditToTitleButton.draw_text("Back")

        pg.display.update()

        clock.tick(FRAMERATE)

        for event in ev:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if currGameState == Screen.Q_A:
                    currGameState = Screen.Q_A1
                if currGameState.value > Screen.HATCH.value:
                    savefile.close()
                    update_save() 
                    savefile = open(os.getcwd() + "/save/saveFile.txt", 'a+')
                    print ("saving")
                mouse = pg.mouse.get_pos()
                if creditsButton.getImageRect().collidepoint(mouse) and currGameState == Screen.STARTING:
                    currGameState = Screen.CREDITS
                elif currGameState == Screen.STARTING:
                    currGameState = Screen.SELECTION
                elif newGameButton.getImageRect().collidepoint(mouse) and currGameState == Screen.SELECTION:
                    open(os.getcwd() + "/save/saveFile.txt", 'w').close()
                    currGameState = Screen.Q_A
                elif continueGameButton.getImageRect().collidepoint(mouse) and currGameState == Screen.SELECTION:
                    lines = open(os.getcwd() + "/save/saveFile.txt", "r").read().splitlines()
                    if len(lines) > 5:
                        savePetType = lines[0]
                        if savePetType.__contains__("GIF"):
                            currPet = Pet.init_gifImage(lines[0], lines[1])
                        else:
                            currPet = Pet(lines[0], lines[1])
                        currPet.food = float(lines[2])
                        currPet.water = float(lines[3])
                        currPet.sleep = float(lines[4])
                        currPet.stress = float(lines[5])
                        dtimeT = (init_time - datetime.datetime.strptime(lines[6], "%Y-%B-%d %I:%M:%S.%f"))
                        dtime = dtimeT.seconds
                        print(dtimeT)
                        print(dtime)
                        currPet.food += FOOD_CHANGE_RATE * dtime * FRAMERATE
                        currPet.water += WATER_CHANGE_RATE * dtime * FRAMERATE
                        currPet.sleep += SLEEP_CHANGE_RATE * dtime * FRAMERATE
                        currPet.stress += STRESS_CHANGE_RATE * dtime * FRAMERATE
                        currGameState = Screen.HOME
                        currPet.setCoords(WIDTH / 2, HEIGHT / 2)
                    else:
                        print("Save game not found")
                        open(os.getcwd() + "/save/saveFile.txt", 'w').close()
                        currGameState = Screen.Q_A
                elif qa1LeftButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A1:
                    petSum += 1
                    currGameState = Screen.Q_A2
                elif qa1MiddleButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A1:
                    petSum += 2
                    currGameState = Screen.Q_A2
                elif qa1RightButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A1:
                    petSum += 3
                    currGameState = Screen.Q_A2
                elif qa2LeftButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A2:
                    petSum += 1
                    currGameState = Screen.Q_A3
                elif qa2MiddleButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A2:
                    petSum += 2
                    currGameState = Screen.Q_A3
                elif qa2RightButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A2:
                    petSum += 3
                    currGameState = Screen.Q_A3
                elif qa3LeftButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A3:
                    petSum += 1
                    currGameState = Screen.Q_A4
                elif qa3MiddleButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A3:
                    petSum += 2
                    currGameState = Screen.Q_A4
                elif qa3RightButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A3:
                    petSum += 3
                    currGameState = Screen.Q_A4
                elif qa4LeftButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A4:
                    petSum += 1
                    currGameState = Screen.HATCH
                elif qa4MiddleButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A4:
                    petSum += 2
                    currGameState = Screen.HATCH
                elif qa4RightButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A4:
                    petSum += 3
                    currGameState = Screen.HATCH
                elif currGameState == Screen.HATCH:
                    currGameState = Screen.HOME
                    currPet.setCoords(WIDTH / 2, HEIGHT / 2)
                elif creditToTitleButton.getImageRect().collidepoint(mouse) and currGameState == Screen.CREDITS:
                    currGameState = Screen.STARTING
                elif sleepAffirmationsButton.getImageRect().collidepoint(mouse) and currGameState == Screen.SLEEP:
                    currGameState = Screen.MEDITATION
                elif backButton.getImageRect().collidepoint(mouse) and (currGameState is Screen.FOOD or currGameState is Screen.WATER or currGameState is Screen.WATER_ACTIVE or currGameState is Screen.SLEEP or currGameState is Screen.FUN):
                    currGameState = Screen.HOME
                    currPet.setCoords(WIDTH / 2, HEIGHT / 2)
                elif currGameState == Screen.HOME:
                    if HomeFoodButton.getImageRect().collidepoint(mouse):
                        currGameState = Screen.FOOD
                    elif HomeWaterButton.getImageRect().collidepoint(mouse):
                        currGameState = Screen.WATER
                    elif HomeSleepButton.getImageRect().collidepoint(mouse):
                        currGameState = Screen.SLEEP
                    elif HomeStressButton.getImageRect().collidepoint(mouse):
                        currGameState = Screen.FUN
                    elif exitButton.getImageRect().collidepoint(mouse):
                        update_save()
                        pg.quit()
                        if sys.platform.startswith('linux'):
                            os.system("sudo shutdown -h now")  
                        sys.exit()
                elif currGameState == Screen.WATER:
                    if checkin_button.getImageRect().collidepoint(mouse):
                        water_drop1.getImageRect().center = (random.randint(100, WIDTH - 100), random.randint(100, HEIGHT- 100))
                        water_drop2.getImageRect().center = (random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100))
                        
                        currGameState = Screen.WATER_ACTIVE
                        currPet.setCoords(WIDTH / 2, HEIGHT / 2)
                        water_exists1 = True
                        water_exists2 = True

                elif currGameState is Screen.WATER_ACTIVE:
                    
                    if water_drop1.getImageRect().collidepoint(mouse) and water_exists1:                                   
                        currPet.water += 12
                        if currPet.water > 100:
                            currPet.water = 100
                        water_exists1 = False
                    elif water_drop2.getImageRect().collidepoint(mouse) and water_exists2:
                        currPet.water += 12
                        if currPet.water > 100:
                            currPet.water = 100
                        water_exists2 = False




main()
