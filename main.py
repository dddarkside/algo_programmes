from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout


class Screen_Artem(Screen):
    def __init__(self, name = 'Artem'):
        super().__init__(name = name)
        box = BoxLayout(orientation = 'vertical')
        pic = Image(source = '1.jpg')
        box.add_widget(pic)
        
        txt = Label(text = 'День добрый, люди молодые! Зовут меня Artemом и родом я из Moscowы. Будуюший предпринематель!) Fourth year на алгоритмике. ')
        btn = Button(text = 'Начать', size_hint=(.5,1), alignment='center')
        btn.on_press = self.next
        self._in = TextInput(multiline = False)

        

        box.add_widget(txt)
        box.add_widget(self._in)
        box.add_widget(btn)
        self.add_widget(box)

    def next(self):
        global name
        name = self.name_in.text

        self.manager.transition.direction = 'left'
        self.manager.current = '7'





class Main(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen_Artem())


        return sm

app = Main()
app.run()