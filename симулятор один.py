from kivy.config import Config
Config.set('graphics', 'resizable', '0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
import random
import time



##Config.set('graphics', 'resizable', '0')
##
##Config.set('graphics', 'width', '100')
##Config.set('graphics', 'height', '100')



Window.size = (300, 400)
##Window.resizable = False
Window.clearcolor = (23/255, 65/255, 112/255, 1)
Window.title = "спонсор "


class MyKivyApp(App):
    def __init__(self, **kwargs):
        super(MyKivyApp, self).__init__(**kwargs)
        self.radio_enabled = False  # добавлено
        self.current_frequency = 0 

    def on_button_click(self, instance):
        self.sound = SoundLoader.load('C:\\kuk\z0.wav')
        self.sound.play()
        time.sleep(2)
        self.img.source = 'C:\\kuk\z-1.png'
        self.radio_enabled = True  # добавлено
        
        self.current_frequency += 1

        

        

    def on_button_click2(self, instance):
        if not self.radio_enabled:  # добавлено
            return  # добавлено

        self.sound = SoundLoader.load('C:\\2.wav')
        self.sound.play()
        self.img.source = 'C:\\kuk\z-2.png'
        
    def build(self):
        layout = FloatLayout()
        self.img = Image(source='C:\\kuk\z.png')
        layout.add_widget(self.img)

        radio_button = Button(text="",
                              pos_hint={'x': 0.55, 'y': 0.59},
                              size_hint=(0.08, 0.06), background_color=(1, 1, 1, 0.0))
        radio_button.bind(on_press=self.on_button_click)
        layout.add_widget(radio_button)

        radio_button2 = Button(text="",
                              pos_hint={'x': 0.472, 'y': 0.59},
                              size_hint=(0.08, 0.07), background_color=(1, 1, 1, 0.1))
        radio_button2.bind(on_press=self.on_button_click2)
        layout.add_widget(radio_button2)

        self.sound = SoundLoader.load('C:\\spa.wav')
        self.sound.play()

        return layout

if __name__ == '__main__':
    MyKivyApp().run()
