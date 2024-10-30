from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty


class FormScreen(GridLayout):

    def __init__(self, **kwargs):
        super(FormScreen, self).__init__(**kwargs)
        self.cols = 6
        self.add_widget(Label(text='Nome Voluntário'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)


        self.add_widget(Label(text='Sexo'))
        self.sex = TextInput(multiline=False)
        self.add_widget(self.sex)

        self.add_widget(Label(text='Idade'))
        self.age = TextInput(multiline=False)
        self.add_widget(self.age)

        self.add_widget(Label(text='Etnia'))
        self.race = TextInput(multiline=False)
        self.add_widget(self.race)

        self.add_widget(Label(text='Altura (cm)'))
        self.altura = TextInput(multiline=False)
        self.add_widget(self.altura)

        self.add_widget(Label(text='Peso (cm)'))
        self.peso = TextInput(multiline=False)
        self.add_widget(self.peso)

        self.add_widget(Button(text='btn 1'))
        cb = CustomBtn()
        cb.bind(pressed=self.btn_pressed)
    
    def btn_pressed(self, instance, pos):
        print('pos: printed from root widget: {pos}'.format(pos=pos))


class CustomBtn(Widget):

    pressed = ListProperty([0, 0])

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            # we consumed the touch. return False here to propagate
            # the touch further to the children.
            return True
        return super(CustomBtn, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        print('pressed at {pos}'.format(pos=pos))
        
class BodyScanner3DApp(App):

    def build(self):
        return FormScreen()


if __name__ == '__main__':
    BodyScanner3DApp().run()