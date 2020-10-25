import datetime
import requests
import kivy
from bs4 import BeautifulSoup
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from playsound import playsound

kivy.require("1.9.0")

def assigntime2():
    time2 = True

source = requests.get('https://www.muslimpro.com/en/Prayer-times-London-United-Kingdom-2643743').text

soup = BeautifulSoup(source, 'lxml')

prayertime = soup.find('div', class_="prayer-daily-table d-inline-flex pt-4 px-2")

all_prayer_time = prayertime.findAll('span', {'class':'jam-solat'})

fajr = all_prayer_time[0].text

fajr1 = fajr.split(':')

fajrHL = fajr1[0]

if fajrHL[0] == '0':
    fajrHL = fajrHL[1]

fajrML = fajr1 [1]

FajrHL = int(fajrHL)

FajrML = int(fajrML)

zuhr =  all_prayer_time[2].text

zuhr1 = zuhr.split(':')

zuhrHL = zuhr1[0]

zuhrML = zuhr1[1]

if zuhrML[0] == '0':
    zuhrML = zuhrML[1]

ZuhrHL = int(zuhrHL)

ZuhrML = int(zuhrML)

asr = all_prayer_time[3].text

asr1 = asr.split(':')

AsrHL = asr1[0]

AsrML = asr1[1]

maghrip = all_prayer_time[4].text

maghrip1 = maghrip.split(':')

MaghripHL = maghrip1[0]

MaghripML = maghrip1[1]

isha = all_prayer_time[5].text

isha1 = isha.split(':')

IshaHL = isha1[0]

IshaML = isha1[1]

FajrHL = 13
FajrML = 17

class firstpage(GridLayout):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=2

        self.add_widget(Label(text='What is your name?   :'))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text='Which country are you from?'))
        self.add_widget(Label(text='Which country are you from?'))

        self.edinburgh = Button(text='EDINBURGH')
        self.edinburgh.bind(on_press=self.edinburgh1)
        self.add_widget(self.edinburgh)

        self.london = Button(text='LONDON')
        self.london.bind(on_press=self.london1)
        self.add_widget(self.london)

        self.submit = Button(text='SUBMIT')
        self.submit.bind(on_press=self.hello)
        self.add_widget(self.submit)

        self.submit1 = Button(text='SUBMIT')
        self.submit1.bind(on_press=self.hello)
        self.add_widget(self.submit1)

    def edinburgh1(self, instance):
        global country
        country = 'edinburgh'

    def london1(self, instance):
        global country
        country = 'london'

    def hello(self, instance):
        name = self.name
        haha.screen_manager.current = 'azanpage'

class azanpage(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=5
        self.theteem = True
        self.thetime = True
        self.true = False

        self.add_widget(Label(text=''))

        self.startazan = Button(text='START AZAN APP')
        self.startazan.bind(on_press=self.startazantime)
        self.add_widget(self.startazan)

    def startazantime(self, instance):

        variable = datetime.datetime.now().hour - FajrHL
        variable2 = datetime.datetime.now().minute - FajrML

        if variable > -1 and variable2 > -1:
            self.thetime = True
            self.theteem = True
        else:
            self.thetime =  False
            self.theteem = False
            self.zuhrtimeYER

        if self.thetime and self.theteem ==  True:
            variableYE = variable * 3600
            variableYE2 = variable2 * 60
            self.true = True

            variableYE3 = variableYE + variableYE2

            if self.true == True:
                Clock.schedule_once(self.fajrtimeye, variableYE3)

    def fajrtimeye(self,instance):
        playsound('heheboi.mp3')

    def zuhrtimeYER(self,instance):
        variable = datetime.datetime.now().hour - ZuhrHL
        variable2 = datetime.datetime.now().minute - ZuhrML
        if variable > -1 and variable2 > -1:
            self.thetime = True
            self.theteem = True
        else:
            self.thetime =  False
            self.theteem = False
            self.asrtimeYER

        if self.thetime and self.theteem ==  True:
            variableYE = variable * 3600
            variableYE2 = variable2 * 60
            self.true = True

            variableYE3 = variableYE + variableYE2

            if self.true == True:
                Clock.schedule_once(self.zuhrtimeye, variableYE3)

    def zuhrtimeeye(self,instance):
        playsound('heheboi.mp3')

    def asrtimeYER(self,instance):
        variable = datetime.datetime.now().hour - AsrHL
        variable2 = datetime.datetime.now().minute - AsrML
        if variable > -1 and variable2 > -1:
            self.thetime = True
            self.theteem = True
        else:
            self.thetime =  False
            self.theteem = False
            self.maghriptimeYER

        if self.thetime and self.theteem ==  True:
            variableYE = variable * 3600
            variableYE2 = variable2 * 60
            self.true = True

            variableYE3 = variableYE + variableYE2

            if self.true == True:
                Clock.schedule_once(self.asrtimeye, variableYE3)

    def asrtimeeye(self,instance):
        playsound('heheboi.mp3')

    def maghriptimeYER(self,instance):
        variable = datetime.datetime.now().hour - MaghripHL
        variable2 = datetime.datetime.now().minute - MaghripML
        if variable > -1 and variable2 > -1:
            self.thetime = True
            self.theteem = True
        else:
            self.thetime =  False
            self.theteem = False
            self.ishatimeYER

        if self.thetime and self.theteem ==  True:
            variableYE = variable * 3600
            variableYE2 = variable2 * 60
            self.true = True

            variableYE3 = variableYE + variableYE2

            if self.true == True:
                Clock.schedule_once(self.maghriptimeye, variableYE3)

    def maghriptimeeye(self,instance):
        playsound('heheboi.mp3')

    def ishatimeYER(self,instance):
        variable = datetime.datetime.now().hour - IshaHL
        variable2 = datetime.datetime.now().minute - IshaML
        if variable > -1 and variable2 > -1:
            self.thetime = True
            self.theteem = True
        else:
            self.thetime =  False
            self.theteem = False
            self.startazantime

        if self.thetime and self.theteem ==  True:
            variableYE = variable * 3600
            variableYE2 = variable2 * 60
            self.true = True

            variableYE3 = variableYE + variableYE2

            if self.true == True:
                Clock.schedule_once(self.ishatimeeye, variableYE3)

    def ishatimeeye(self,instance):
        playsound('heheboi.mp3')

class appp(App):

    def build(self):
        self.screen_manager = ScreenManager()

        self.first_page = firstpage()
        screen = Screen(name="countrypage")
        screen.add_widget(self.first_page)
        self.screen_manager.add_widget(screen)

        self.azan_page = azanpage()
        screen = Screen(name="azanpage")
        screen.add_widget(self.azan_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == '__main__':
    haha = appp()
    haha.run()