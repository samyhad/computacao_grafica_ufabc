# from kivy.lang import Builder
# from kivymd.app import MDApp
# from kivymd.uix.dialog import (
#     MDDialog,
#     MDDialogIcon,
#     MDDialogHeadlineText,
#     MDDialogSupportingText,
#     MDDialogButtonContainer,
#     MDDialogContentContainer,
# )
# from kivymd.uix.divider import MDDivider
# from kivymd.uix.button import MDButton, MDButtonText
# from kivymd.uix.list import (
#     MDListItem,
#     MDListItemLeadingIcon,
#     MDListItemSupportingText,
# )
# from kivy.uix.widget import Widget

# KV = '''
# MDScreen:
#     id: screen
#     md_bg_color: self.theme_cls.backgroundColor

#     MDBoxLayout:
#         orientation: 'vertical'
#         spacing: 20
#         padding: 20

#         MDTextField:
#             id: nome
#             hint_text: "Nome do voluntário"

#         MDTextField:
#             id: idade
#             hint_text: "Idade"

#         MDTextField:
#             id: altura
#             hint_text: "Altura (cm)"

#         MDTextField:
#             id: peso
#             hint_text: "Peso (gramas)"

#         MDButton:
#             text: "Imprimir"
#             pos_hint: {'center_x': .5}
#             on_release: app.show_form_dialog()
# '''

# class FormApp(MDApp):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.nome = ""
#         self.idade = 0
#         self.peso = 0
#         self.altura = 0
#         self.idade_formatado = ""
#         self.peso_formatado = ""
#         self.altura_formatado = ""
#         self.sexo = ""
#         self.etnia = ""
#         self.volumeModelo3D = 0
#         self.volumeModelo3D_formatado = ""
#         self.gorduraCorporal = 0
#         self.gorduraCorporal_formatado = ""
        
    
#     def build(self):
#         return Builder.load_string(KV)

#     def calcular_gordura(self):        
#         volumePulmao = (((0.0472*(self.altura))+(0.000009*self.peso))-5.92)*1000
#         Densidade = self.peso/(self.volumeModelo3D-volumePulmao)
#         if(self.etnia == "Afro-americano"):
#             self.gorduraCorporal = (437 / Densidade) - 393
#         elif(self.etnia == "Afrodescendente"):
#             self.gorduraCorporal = (437 / Densidade) - 392
#         elif(self.etnia == "Asiático"):
#             self.gorduraCorporal = (503 / Densidade) - 462
#         else:
#             self.gorduraCorporal = (495 / Densidade) - 450

#         self.gorduraCorporal = round(self.gorduraCorporal, 2)
#         self.gorduraCorporal_formatado = str(self.gorduraCorporal)+"%"

#     def show_form_dialog(self):
#         # Obtém os valores preenchidos
#         #nome = self.root.ids.nome.text
#         idade = self.root.ids.idade.text
#         altura = self.root.ids.altura.text
#         peso = self.root.ids.peso.text

#         self.nome = self.root.ids.nome.text
#         self.idade = self.root.ids.idade.text
#         self.peso = self.root.ids.peso.text
#         self.altura = self.root.ids.altura.text
#         self.idade_formatado =  self.root.ids.idade.text + " anos"
#         self.peso_formatado = self.root.ids.peso.text + " kg"
#         self.altura_formatado = self.root.ids.altura.text + " cm"
#         self.sexo = ""
#         self.etnia = ""
#         self.volumeModelo3D = 0
#         self.volumeModelo3D_formatado = ""
#         self.gorduraCorporal = 0
#         self.gorduraCorporal_formatado = ""

#         # Cria e exibe o popup
#         MDDialog(
#             MDDialogIcon(
#                 icon="account",
#             ),
#             MDDialogHeadlineText(
#                 text="Informações do Voluntário",
#             ),
#             MDDialogSupportingText(
#                 text=(
#                     f"Nome: {nome}\n"
#                     f"Idade: {idade}\n"
#                     f"Altura: {altura} cm\n"
#                     f"Peso: {peso} gramas"
#                 ),
#             ),
#             MDDialogButtonContainer(
#                 Widget(),
#                 MDButton(
#                     MDButtonText(text="Fechar"),
#                     style="text",
#                     on_release=lambda x: self.dialog.dismiss(),  # Fecha o diálogo
#                 ),
#                 spacing="8dp",
#             ),
#         ).open()

# FormApp().run()

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
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
            MDCard:
                orientation: "vertical"
                padding: 15
                md_bg_color: 1, 1, 1, 1 
                elevation: 4
                radius: [15, 15, 15, 15]
                MDBoxLayout:
                    orientation: "vertical"
                    spacing: 20
                    size_hint_y: None
                    height: self.minimum_height 

                    MDTextField:
                        id: nome
                        hint_text: "Nome do voluntário"
                        mode: "filled"

                    MDTextField:
                        id: idade
                        hint_text: "Idade"
                        mode: "filled"

                    MDTextField:
                        id: altura
                        hint_text: "Altura (cm)"
                        mode: "filled"

                    MDTextField:
                        id: peso
                        hint_text: "Peso (gramas)"
                        mode: "filled"

                    MDSegmentedButton:
                        id: sexo
                        size_hint_x: 1  
                        height: "40dp"  
                        MDSegmentedButtonItem:
                            text: "Feminino"
                        MDSegmentedButtonItem:
                            text: "Masculino"

                    MDDropDownItem:
                        id: etnia
                        pos_hint: {"center_x": 0.5, "center_y": .5}
                        size_hint_x: 1  
                        on_release: app.open_menu(self)
                        text: "Etnia do voluntário"

            # Segunda coluna da segunda linha
            MDCard:
                orientation: "vertical"
                padding: 15
                md_bg_color: 1, 1, 1, 1 
                elevation: 4
                radius: [15, 15, 15, 15]
                MDBoxLayout:
                    orientation: "vertical"
                    padding: [20, 40, 20, 250]  
                    MDRaisedButton:
                        text: "Ações futuras"
                        pos_hint: {"center_x": 0.5}

        # Terceira linha
        MDBoxLayout:
            padding: "20dp"
            size_hint_y: 0.1
            MDRaisedButton:
                text: "Resultados"
                pos_hint: {"center_x": 0.5}
                on_release: app.show_form_dialog()
"""

class MyApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        return Builder.load_string(KV)

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
        self.root.ids.etnia.text = text_item
        self.menu.dismiss()

    def show_form_dialog(self):
        # Obtém os valores preenchidos
        nome = self.root.ids.nome.text
        idade = self.root.ids.idade.text
        altura = self.root.ids.altura.text
        peso = self.root.ids.peso.text
        sexo = [item.text for item in self.root.ids.sexo.children if item.active][0]
        etnia = self.root.ids.etnia.text

        # Mostra o diálogo
        if not self.dialog:
            self.dialog = MDDialog(
                title="Informações do Voluntário",
                text=(
                    f"Nome: {nome}\n"
                    f"Idade: {idade} anos\n"
                    f"Altura: {altura} cm\n"
                    f"Peso: {peso} g\n"
                    f"Sexo: {sexo}\n"
                    f"Etnia: {etnia}"
                ),
                buttons=[
                    MDFlatButton(
                        text="Fechar",
                        on_release=lambda _: self.dialog.dismiss()
                    )
                ],
            )
        self.dialog.open()

MyApp().run()

