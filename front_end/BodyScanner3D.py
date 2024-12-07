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
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)
from kivymd.uix.divider import MDDivider
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.list import (
    MDListItem,
    MDListItemLeadingIcon,
    MDListItemSupportingText,
)
from kivy.uix.widget import Widget

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
                        id: nome
                        mode: "filled"
                        MDTextFieldHintText:
                            text: "Nome do voluntário"
                        MDTextFieldMaxLengthText:
                            max_text_length: 10
                    MDTextField:
                        id: idade
                        mode: "filled"
                        MDTextFieldHintText:
                            text: "Idade"
                        MDTextFieldMaxLengthText:
                            max_text_length: 10
                    MDTextField:
                        id: altura
                        mode: "filled"
                        MDTextFieldHintText:
                            text: "Altura (cm)"
                        MDTextFieldMaxLengthText:
                            max_text_length: 10
                    MDTextField:
                        id: peso
                        mode: "filled"
                        MDTextFieldHintText:
                            text: "Peso (gramas)"
                        MDTextFieldMaxLengthText:
                            max_text_length: 10
                    MDSegmentedButton:
                        id: sexo
                        size_hint_x: 1  
                        height: "40dp"
                        MDSegmentedButtonItem:
                            id: Feminino
                            font_style: "Caption"
                            text: 'Feminino'
                            on_release: app.item_selected(self)
                            MDSegmentButtonLabel:
                                text: "Feminino"
                        MDSegmentedButtonItem:
                            id: Masculino
                            font_style: "Caption"
                            text: 'Masculino'
                            on_release: app.item_selected(self)
                            MDSegmentButtonLabel:
                                text: "Masculino"
                    MDDropDownItem:
                        id: etnia
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
                MDBoxLayout: #COLOCAR AS COISAS DO PANDAS3D AQUI
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
                    size_hint: None, None
                    width: "200dp"  
                    height: "40dp"  
                    pos_hint: {"center_x": 10, "center_y": 0.5}
                    style: "elevated"
                    pos_hint: {"center_x": .9, "center_y": .5}
                    on_release: app.show_form_dialog()
                    MDButtonIcon:
                        icon: "plus"

                    MDButtonText:
                        text: "Resultados"
                    
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nome = ""
        self.idade = 0
        self.peso = 0
        self.altura = 0
        self.idade_formatado = ""
        self.peso_formatado = ""
        self.altura_formatado = ""
        self.sexo = ""
        self.etnia = ""
        self.volumeModelo3D = 0
        self.volumeModelo3D_formatado = ""
        self.gorduraCorporal = 0
        self.gorduraCorporal_formatado = ""

    title = "3D Scanner"
    icon = 'ico/scanner-de-rosto.png'
    
    def open_menu(self, item):
        menu_items = [
            {
                "text": i,
                "on_release": lambda x=i: self.menu_callback(x),
            } for i in ["Afro-americano", "Afrodescendente", "Asiático", "Outros"]
        ]
        self.menu = MDDropdownMenu(caller=item, items=menu_items, width_mult=4)
        self.menu.open()

    def menu_callback(self, text_item):
        self.root.ids.drop_text.text = text_item

    def item_selected(self, instance):
        self.sexo = instance.text
        
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        return Builder.load_string(KV)
    
    def calcular_gordura(self):        
        volumePulmao = (((0.0472*(self.altura))+(0.000009*self.peso))-5.92)*1000
        Densidade = self.peso/(self.volumeModelo3D-volumePulmao)
        if(self.etnia == "Afro-americano"):
            self.gorduraCorporal = (437 / Densidade) - 393
        elif(self.etnia == "Afrodescendente"):
            self.gorduraCorporal = (437 / Densidade) - 392
        elif(self.etnia == "Asiático"):
            self.gorduraCorporal = (503 / Densidade) - 462
        else:
            self.gorduraCorporal = (495 / Densidade) - 450

        self.gorduraCorporal = round(self.gorduraCorporal, 2)
        self.gorduraCorporal_formatado = str(self.gorduraCorporal)+"%"

    def show_form_dialog(self):
        # Obtém os valores preenchidos
        self.nome = self.root.ids.nome.text
        self.idade = int(self.root.ids.idade.text)
        self.peso = float(self.root.ids.peso.text)
        self.altura = int(self.root.ids.altura.text)
        self.idade_formatado =  self.root.ids.idade.text + " anos"
        self.peso_formatado = self.root.ids.peso.text + " kg"
        self.altura_formatado = self.root.ids.altura.text + " cm"
        self.etnia = self.root.ids.drop_text.text 
        self.volumeModelo3D = 109869736
        self.calcular_gordura()

        # Cria e exibe o popup
        MDDialog(
            MDDialogIcon(
                icon="account",
            ),
            MDDialogHeadlineText(
                text="Informações do Voluntário",
            ),
            MDDialogSupportingText(
                text=(
                    f"Nome: {self.nome}\n"
                    f"Idade: {self.idade}\n"
                    f"Altura: {self.altura_formatado}\n"
                    f"Peso: {self.peso_formatado}\n"
                    f"Etnia: {self.etnia}\n"
                    f"Sexo: {self.sexo}\n"
                    f"Gordura corporal: {self.gorduraCorporal_formatado}\n"
                    f"Relatório final salvo em: ..."
                ),
            ),
            # MDDialogButtonContainer(
            #     Widget(),
            #     MDButton(
            #         MDButtonText(text="Fechar"),
            #         style="text",
            #         on_release=lambda x: self.dialog.dismiss(),  # Fecha o diálogo
            #     ),
            #     spacing="8dp",
            # ),
        ).open()

MyApp().run()
