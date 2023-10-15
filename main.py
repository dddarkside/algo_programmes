from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

class Screen_Main(Screen):
    def __init__(self, name='main'):
        super().__init__(name=name)
        txt = Label(text = "hi")
        btn = Button(text = "Начать")
        btn.on_press = self.next
        self.name_in = TextInput(multiline = False)
        box = BoxLayout(orientation = "vertical")

        box.add_widget(txt)
        box.add_widget(self.name_in)
        box.add_widget(btn)
        self.add_widget(box)

    def next(self):
        global name
        name = self.name_in.text

        self.manager.transition.direction = 'left'
        self.manager.current = 'Egor'


class Screen_Egor(Screen):
    pass
class Screen_Nikita(Screen):
    pass
class Screen_CDmitry(Screen):
    pass
class Screen_Maksim(Screen):
    pass
class Screen_Artem(Screen):
    pass
class Screen_EDmitry(Screen):
    pass


class Main(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen_Main())
        sm.add_widget(Screen_Egor())
        sm.add_widget(Screen_Nikita())
        sm.add_widget(Screen_CDmitry())
        sm.add_widget(Screen_Maksim())
        sm.add_widget(Screen_Artem())
        sm.add_widget(Screen_EDmitry())

        return sm

app = Main()
app.run()