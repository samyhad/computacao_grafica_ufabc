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
from kivy.core.window import Window

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
                padding: [20, 50, 20, 20] 
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
                md_bg_color: 1, 1, 1, 1 
                elevation: 4
                radius: [15, 15, 15, 15]
                MDBoxLayout:
                    orientation: "vertical"
                    spacing: 30  # Espaçamento entre os elementos
                    size_hint_y: None
                    height: self.minimum_height 
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
                        size_hint_x: 1  
                        height: "40dp"  
                        #pos_hint: {"center_x": 0.5} 

                        #pos_hint: {"center_x": 0.2, "center_y": 0.5}
                        #size_hint: None, None
                        #size: "50dp", "40dp"  
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
                        pos_hint: {"center_x": 0.5, "center_y": .5}
                        size_hint_x: 1  
                        on_release: app.open_menu(self)
                        font_size: "48sp" 

                        MDDropDownItemText:
                            id: drop_text
                            text: "Etnia do voluntário"
                            font_size: "24sp"  

            CustomMDCard:
                orientation: "vertical"
                padding: 15
                md_bg_color: 1, 1, 1, 1 
                elevation: 4
                radius: [15, 15, 15, 15]
                MDBoxLayout: #COLOCAR AS COISAS O PANDAS3D AQUI
                    orientation: "vertical"
                    padding: [20, 40, 20, 250]  
                    MDCircularProgressIndicator:
                        size_hint: None, None
                        size: "48dp", "48dp"
                        pos_hint: {'center_x': .5, 'center_y': 1}
                    
                
        # Terceira linha: Única coluna, com altura máxima de 30px
        GridLayout:
            cols: 1
            size_hint_y: 0.1
            height: "30dp"  

            MDBoxLayout:
                padding: "350dp"
                spacing: 10
                orientation: "horizontal"  
                size_hint: None, None
                size: "200dp", "40dp"  
                pos_hint: {"center_x": 0.9, "center_y": 0.5}

                MDButton:
                    #text: "Imprimir"
                    size_hint: None, None
                    width: "200dp"  
                    height: "40dp"  
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
    title = "3D Scanner"
    icon = 'ico/scanner-de-rosto.png'
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
