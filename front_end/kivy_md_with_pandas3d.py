from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDButton

KV = """
Screen:
    MDBoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 20

        MDButton:
            id: dropdown_button
            text: app.selected_option
            size_hint: None, None
            size: "200dp", "40dp"
            pos_hint: {"center_x": 0.5}
            on_release: app.menu.open()
            style: "elevated"
"""

class MyApp(MDApp):
    selected_option = StringProperty("Selecione uma opção")

    def build(self):
        self.screen = Builder.load_string(KV)
        self.create_dropdown_menu()
        return self.screen

    def create_dropdown_menu(self):
        menu_items = [
            {"text": "Opção 1", "viewclass": "OneLineListItem", "on_release": lambda x="Opção 1": self.set_item(x)},
            {"text": "Opção 2", "viewclass": "OneLineListItem", "on_release": lambda x="Opção 2": self.set_item(x)},
            {"text": "Opção 3", "viewclass": "OneLineListItem", "on_release": lambda x="Opção 3": self.set_item(x)},
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.dropdown_button,
            items=menu_items,
            width_mult=4,
        )

    def set_item(self, text_item):
        self.selected_option = text_item
        self.menu.dismiss()

MyApp().run()
