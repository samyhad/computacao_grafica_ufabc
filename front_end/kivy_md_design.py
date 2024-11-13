from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton
from kivymd.uix.progressindicator.progressindicator import MDCircularProgressIndicator
from kivymd.uix.segmentedbutton import (
    MDSegmentedButton,
    MDSegmentedButtonItem,
    MDSegmentButtonLabel,
)
from kivymd.uix.segmentedbutton import MDSegmentedButton, MDSegmentedButtonItem
from kivymd.uix.menu import MDDropdownMenu


KV = """
MDBoxLayout:
    orientation: "vertical"

    GridLayout:
        cols: 1
        rows: 3

        # Primeira linha
        GridLayout:
            cols: 1
            size_hint_y: 0.1
            MDBoxLayout:
                orientation: "vertical"
                padding: [20, 40, 20, 20]  # Espaçamento ao redor
                MDLabel:
                    text: "3D Scanner"
                    font_style: "Display"
                    role: "small"
                    bold: True
                    font_name: "Poppins"
                    theme_text_color: "Custom"
                    text_color: "#A91079"
        # Segunda linha: 2 colunas
        GridLayout:
            cols: 2
            size_hint_y: 0.8
            padding: 20
            spacing: 20

            # Primeira coluna da segunda linha
            CustomMDCard:
                orientation: "vertical"
                padding: 15
                md_bg_color: 1, 1, 1, 1  # Cor branca constante
                elevation: 4
                radius: [15, 15, 15, 15]
                MDBoxLayout:
                    orientation: "vertical"
                    spacing: 30  # Espaçamento entre os elementos
                    size_hint_y: None
                    height: self.minimum_height  # Ajusta a altura ao conteúdo
                    MDTextField:
                        mode: "filled"
                        MDTextFieldHintText:
                            text: "Nome do voluntário"
                        MDTextFieldMaxLengthText:
                            max_text_length: 10
                    MDTextField:
                        mode: "filled"
                        MDTextFieldHintText:
                            text: "Idade"
                        MDTextFieldMaxLengthText:
                            max_text_length: 10
                    MDTextField:
                        mode: "filled"
                        MDTextFieldHintText:
                            text: "Altura (cm)"
                        MDTextFieldMaxLengthText:
                            max_text_length: 10
                    MDTextField:
                        mode: "filled"
                        MDTextFieldHintText:
                            text: "Peso (gramas)"
                        MDTextFieldMaxLengthText:
                            max_text_length: 10
                    MDSegmentedButton:
                        size_hint_x: 1  # Faz com que ocupe toda a largura do card
                        height: "40dp"  # Define a altura do botão segmentado
                        #pos_hint: {"center_x": 0.5}  # Centraliza horizontalmente dentro do card

                        #pos_hint: {"center_x": 0.2, "center_y": 0.5}
                        #size_hint: None, None
                        #size: "50dp", "40dp"  # Ajuste manual do tamanho, opcional
                        MDSegmentedButtonItem:
                            font_style: "Caption"
                            MDSegmentButtonLabel:
                                text: "Feminino"
                        MDSegmentedButtonItem:
                            font_style: "Caption"
                            MDSegmentButtonLabel:
                                text: "Masculino"
                        MDSegmentedButtonItem:
                            font_style: "Caption"
                            MDSegmentButtonLabel:
                                text: "Intersexo"
                    MDDropDownItem:
                        pos_hint: {"center_x": .5, "center_y": .5}
                        on_release: app.open_menu(self)

                        MDDropDownItemText:
                            id: drop_text
                            text: "Etnia do voluntário"

            MDBoxLayout:
                orientation: "vertical"
                padding: [20, 40, 20, 300]  # Espaçamento ao redor
                MDCircularProgressIndicator:
                    size_hint: None, None
                    size: "48dp", "48dp"
                    pos_hint: {'center_x': .5, 'center_y': 1}
            
        # Terceira linha: Única coluna, com altura máxima de 30px
        GridLayout:
            cols: 1
            size_hint_y: 0.1
            height: "30dp"  # Ajuste de altura fixo

            MDBoxLayout:
                padding: "350dp"
                spacing: 10
                orientation: "horizontal"  
                size_hint: None, None
                size: "200dp", "40dp"  # Tamanho fixo do botão
                pos_hint: {"center_x": 0.9, "center_y": 0.5}

                MDButton:
                    #text: "Imprimir"
                    size_hint: None, None
                    width: "200dp"  # Defini uma largura fixa para o botão
                    height: "40dp"  # Defini a altura do botão
                    pos_hint: {"center_x": 10, "center_y": 0.5}
                    style: "elevated"
                    pos_hint: {"center_x": .9, "center_y": .5}

                    MDButtonIcon:
                        icon: "plus"

                    MDButtonText:
                        text: "Imprimir"
            
"""

class CustomMDCard(MDCard):
    def on_enter(self, *args):
        self.md_bg_color = (1, 1, 1, 1)

    def on_leave(self, *args):
        self.md_bg_color = (1, 1, 1, 1)

    def on_release(self, *args):
        self.md_bg_color = (1, 1, 1, 1)

    def on_touch_down(self, touch):
        self.md_bg_color = (1, 1, 1, 1)
        
        if self.collide_point(*touch.pos):
            super().on_touch_down(touch) 
            return True
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        self.md_bg_color = (1, 1, 1, 1)
        return super().on_touch_up(touch)

    def on_touch_move(self, touch):
        self.md_bg_color = (1, 1, 1, 1)
        return super().on_touch_move(touch)



class MyApp(MDApp):
    def open_menu(self, item):
        menu_items = [
            {
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.menu_callback(x),
            } for i in ['Branco','Indígena', 'Negro', 'Pardo']
        ]
        MDDropdownMenu(caller=item, items=menu_items).open()

    def menu_callback(self, text_item):
        self.root.ids.drop_text.text = text_item

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        return Builder.load_string(KV)

MyApp().run()
