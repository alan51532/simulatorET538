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
from kivy.uix.progressbar import ProgressBar
from kivy.animation import Animation


##
##Config.set('graphics', 'resizable', '0')
##
##Config.set('graphics', 'width', '300')
##Config.set('graphics', 'height', '400')



Window.size = (300, 400)
##Window.resizable = False
Window.clearcolor = (23/255, 65/255, 112/255, 1)
Window.title = "спонсор "


class MyKivyApp(App):
    def __init__(self, **kwargs):
         super(MyKivyApp, self).__init__(**kwargs)
         self.radio_enabled = False  # добавлено
         self.current_frequency = 0


    def start_animation(self):
        anim = Animation(value=50) + Animation(value=100, duration=1)
        anim.repeat = True
        anim.start(self.pb)

    def on_button_click(self, instance):
     if not self.radio_enabled:  # Если рация выключена
         ##        time.sleep(1)
        self.img.source = 'C:\\Users\Антон\Desktop\ПИТОН\симулятор\z-1.png'
        self.sound1 = SoundLoader.load('C:\\Users\Антон\Desktop\ПИТОН\симулятор\Rec0.wav')
        self.sound1.play()
        self.start_animation() #запуск индикатора 
        
        time.sleep(5)
        self.sound = SoundLoader.load('C:\\aud2.wav')
        self.sound.play()
        self.radio_enabled = True
        


        
     else:  # Если рация включена
        self.sound1.stop()  # Остановите воспроизведение звука
        self.img.source = 'C:\\Users\Антон\Desktop\ПИТОН\симулятор\z.png'  # Верните изображение в начальное состояние
      
        # Остановить звуки в методах chast
        if hasattr(self, 'sound2'):
            self.sound2.stop()
        if hasattr(self, 'sound2_2'):
            self.sound2_2.stop()
        if hasattr(self, 'sound3'):
            self.sound3.stop()
        if hasattr(self, 'sound3_2'):
            self.sound3_2.stop()
        if hasattr(self, 'sound44'):
            self.sound44.stop()

            
        self.current_frequency = 0
        
        self.radio_enabled = False


    def on_button_click2(self, instance):
        if hasattr(self, 'sound'):
         self.sound.stop()
        if hasattr(self, 'sound'):
         self.sound.stop()
        if not self.radio_enabled:  
            return
        
        self.current_frequency += 1
        print(self.current_frequency)
        if self.current_frequency == 1:
             self.chast2(instance)
        elif self.current_frequency == 2:
             self.chast3(instance)
        elif self.current_frequency == 3:
             self.chast4(instance)
        elif self.current_frequency == 4:
             self.chast5(instance) 
##        elif self.current_frequency == 5:
##             self.chast6(instance) 
##        elif self.current_frequency == 6:
##             self.chast7(instance)
##        elif self.current_frequency == 7:
##             self.chast8(instance)
##        elif self.current_frequency == 8:
##             self.chast9(instance)
##        elif self.current_frequency == 9:
##             self.chast10(instance)
##        elif self.current_frequency == 10:
##             self.chast11(instance) 
##        elif self.current_frequency == 11:
##             self.chast12(instance) 
##        elif self.current_frequency == 12:
##             self.chast13(instance) 
##        elif self.current_frequency == 13:
##             self.chast14(instance) 
##        elif self.current_frequency == 14:
##             self.chast15(instance) 
##        elif self.current_frequency == 15:
##             self.chast16(instance)
##        elif self.current_frequency == 16:
##             self.current_frequency = 0
##     
##     





    def chast2(self, instance):
        if hasattr(self, 'sound2'):
         self.sound.stop()
        if hasattr(self, 'sound2_2'):
         self.sound.stop()

        self.img.source = 'C:\\Users\Антон\Desktop\ПИТОН\симулятор\z-2.png'
        self.sound2 = SoundLoader.load('C:\\z2.wav')
        self.sound2.play()
        
        self.sound2_2 = SoundLoader.load('C:\\razv.wav')
        self.sound2_2.play()

    def chast3(self, instance):
        if hasattr(self, 'sound2'):
         self.sound2.stop()
        if hasattr(self, 'sound2_2'):   
         self.sound2_2.stop()
         
        self.img.source = 'C:\\Users\Антон\Desktop\ПИТОН\симулятор\zz3.png'
        
        self.sound3 = SoundLoader.load('C:\\z3.wav')
        
        self.sound3.play()
        
            
        self.sound3_2 = SoundLoader.load('C:\\Re1.wav')
        self.sound3_2.play()

    def chast4(self, instance):
        if hasattr(self, 'sound3'):
         self.sound2.stop()
        if hasattr(self, 'sound3_2'):
         self.sound2_2.stop()
        self.img.source = 'C:\\Users\Антон\Desktop\ПИТОН\симулятор\z4.png'
        self.sound4 = SoundLoader.load('C:\\A4.wav')
        
        self.sound4.play()
        
          
        time.sleep(1)
        self.sound44 = SoundLoader.load('C:\\oxr.wav')
        self.sound44.play()

    def chast5(self, instance):
         if hasattr(self, 'sound4'):
          self.sound4.stop()
         if hasattr(self, 'sound44'):
          self.sound44.stop()
         
         self.img.source = 'C:\\zz5.png'    
         self.sound5 = SoundLoader.load('C:\\z5.wav')
         self.sound5.play()
    
         self.sound55 = SoundLoader.load('C:\\nem2.wav')
         self.sound55.play()
        
######################################################        
        
    def build(self):
        layout = FloatLayout()
        self.img = Image(source='C:\\Users\Антон\Desktop\ПИТОН\симулятор\z.png')
        layout.add_widget(self.img)

        radio_button = Button(text="",
                              pos_hint={'x': 0.54, 'y': 0.57},
                              size_hint=(0.08, 0.06), background_color=(1, 1, 1, 0.0))
        radio_button.bind(on_press=self.on_button_click)
        layout.add_widget(radio_button)

        radio_button2 = Button(text="",
                              pos_hint={'x': 0.452, 'y': 0.57},
                              size_hint=(0.08, 0.07), background_color=(1, 1, 1, 0.0))
        radio_button2.bind(on_press=self.on_button_click2)
        layout.add_widget(radio_button2)

        self.sound = SoundLoader.load('C:\\Users\Антон\Desktop\ПИТОН\симулятор\spa.wav')
        self.sound.play()

        
        self.pb = ProgressBar(max=100, 
                              pos_hint={'x': 0.1, 'y': 0.1}, 
                              size_hint=(0.8, 0.02))
        layout.add_widget(self.pb)
##        self.start_animation()
       

        return layout

if __name__ == '__main__':
    MyKivyApp().run()
