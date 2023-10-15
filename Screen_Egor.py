from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image


class Screen_Egor(Screen):
    def __init__(self, name = 'Egor'):
        super().__init__(name=name)
        txt = Label(text = 'Здарова Хлопцы, my name is Egor and you have already known it! Занимаюсь волейболом и эндуро-мотокроссом, учусь в школе 1557 в "Предпрофессиональный IT класс". Дальше будут кнопочки можете пожмякать <З', size_hint = (2, 4))
        box = BoxLayout(orientation = 'vertical')
        pic = Image(source = "1.jpg")

        box.add_widget(txt)
        box.add_widget(pic)
        self.add_widget(box)



class Main(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen_Egor())

        return sm


app = Main()
app.run()