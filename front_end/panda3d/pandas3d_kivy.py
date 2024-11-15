# from panda3d_kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.gridlayout import GridLayout

# from direct.showbase.ShowBase import ShowBase

# class Example(App):
#         def build(self):
#             self.button = Button(text='Hello, world!')
#             return self.button
    

# class PandaApp(ShowBase):

#    def __init__(self):
#         ShowBase.__init__(self)
#         self.kivy_app = kivy_app = Example(self)
#         self.kivy_app.run()

# PandaApp().run()

# from panda3d_kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.splitter import Splitter
# from direct.showbase.ShowBase import ShowBase
# from panda3d.core import Point3

# class Example(App):
#     def build(self):
#         # Criando um layout com duas colunas: uma para o modelo e outra para o botão
#         layout = GridLayout(cols=2)

#         # Botão na coluna da direita
#         self.button = Button(text='Hello, world!')
#         layout.add_widget(self.button)

#         # Colocando o layout na interface gráfica
#         return layout

# class PandaApp(ShowBase):

#     def __init__(self):
#         ShowBase.__init__(self)

#         # Carregar o modelo do Panda3D
#         self.scene = self.loader.loadModel("models/environment")
#         self.scene.reparentTo(self.render)
#         self.scene.setScale(0.25, 0.25, 0.25)
#         self.scene.setPos(-8, 42, 0)

#         # Configurando a divisão da tela, para ter o modelo na parte esquerda
#         self.kivy_app = Example(self)
#         self.kivy_app.run()

# PandaApp().run()


# BOTÃO EM CIMA DO CENÁRIO PANDAS3D

from panda3d_kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3, WindowProperties

class Example(App):
    def build(self):
        # Criando um layout com duas colunas: uma para o modelo e outra para o botão
        layout = GridLayout(cols=2)

        # Botão na coluna da direita
        self.button = Button(text='Hello, world!')
        layout.add_widget(self.button)

        # Colocando o layout na interface gráfica
        return layout

class PandaWidget(Widget):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.set_size()

    def set_size(self):
        # Ajusta o tamanho do widget para cobrir a área onde o modelo será renderizado
        self.size = (800, 600)  # Defina o tamanho desejado

class PandaApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Carregar o modelo do Panda3D
        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Ajustando o widget do Panda3D na janela do Kivy
        self.window_props = WindowProperties()
        self.window_props.set_size(800, 600)  # Defina o tamanho do modelo
        self.win.request_properties(self.window_props)

        # Configurando o layout do Kivy
        self.kivy_app = Example(self)
        self.kivy_app.run()

PandaApp().run()



