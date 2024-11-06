from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton, MDButtonText, MDIconButton, MDButtonIcon
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import (
    MDTextField,
    MDTextFieldLeadingIcon,
    MDTextFieldHintText,
    MDTextFieldHelperText,
    MDTextFieldTrailingIcon,
    MDTextFieldMaxLengthText,
)


# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.primary_palette = "Purple"

#         return (
#             MDScreen(
#                 MDTextField(
#                     MDTextFieldHintText(
#                         text="Nome do voluntário",
#                     ),
#                     MDTextFieldMaxLengthText(
#                         max_text_length=200,
#                     ),
#                     mode="outlined",
#                     size_hint_x=None,
#                     width="240dp",
#                     pos_hint={"center_x": 0.5, "center_y": 0.9},
#                 ),
#                 MDTextField(
#                     MDTextFieldHintText(
#                         text="Idade",
#                     ),
#                     MDTextFieldMaxLengthText(
#                         max_text_length=10,
#                     ),
#                     mode="outlined",
#                     size_hint_x=None,
#                     width="240dp",
#                     pos_hint={"center_x": 0.5, "center_y": 0.75},
#                 ),
#                 MDTextField(
#                     MDTextFieldHintText(
#                         text="Altura (cm)",
#                     ),
#                     MDTextFieldMaxLengthText(
#                         max_text_length=10,
#                     ),
#                     mode="outlined",
#                     size_hint_x=None,
#                     width="240dp",
#                     pos_hint={"center_x": 0.5, "center_y": 0.60},
#                 ),
#                 MDTextField(
#                     MDTextFieldHintText(
#                         text="Peso (gramas)",
#                     ),
#                     MDTextFieldMaxLengthText(
#                         max_text_length=10,
#                     ),
#                     mode="outlined",
#                     size_hint_x=None,
#                     width="240dp",
#                     pos_hint={"center_x": 0.5, "center_y": 0.45},
#                 ),
#                 MDButton(
#                     MDButtonText(
#                         text="Imprimir resultados",
#                     ),
#                     MDButtonIcon(
#                         icon="plus",
#                         theme_icon_color="Custom",
#                         icon_color="purple"
#                     ),
#                     pos_hint={"center_x": 0.5, "center_y": 0.1},
#                 ),
#                 MDIconButton(
#                     icon="heart-outline",
#                     style="outlined",
#                     theme_bg_color="Custom",
#                     icon_color="purple",
#                     pos_hint={"center_x": 0.9, "center_y": 0.9},
#                 )
#             )
#         )


# MainApp().run()

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.progressindicator.progressindicator import MDCircularProgressIndicator

class MyApp(MDApp):
    def build(self):
        return MDScreen( 
            MDCard(
                orientation="vertical",
                size_hint=(None, None),
                size=("400dp", "450dp"), 
                pos_hint={"center_x": 0.28, "center_y": 0.5},
                padding="20dp",
                spacing="10dp",
                md_bg_color=(0.9, 0.9, 0.9, 1),  # Cor de fundo fixa do cartão
                radius=[15],
                elevation=0,  # Remove a sombra
                shadow_softness=0,  # Desativa o efeito de hover
            ),
            MDTextField(
                MDTextFieldHintText(
                    text="Nome do voluntário",
                ),
                MDTextFieldMaxLengthText(
                    max_text_length=200,
                ),
                mode="outlined",
                size_hint_x=None,
                width="240dp",
                pos_hint={"center_x": 0.28, "center_y": 0.8},
                line_color_normal='purple'
            ),
            MDTextField(
                MDTextFieldHintText(
                    text="Idade",
                ),
                MDTextFieldMaxLengthText(
                    max_text_length=10,
                ),
                mode="outlined",
                size_hint_x=None,
                width="240dp",
                pos_hint={"center_x": 0.28, "center_y": 0.65},
            ),
            MDTextField(
                MDTextFieldHintText(
                    text="Altura (cm)",
                ),
                MDTextFieldMaxLengthText(
                    max_text_length=10,
                ),
                mode="outlined",
                size_hint_x=None,
                width="240dp",
                pos_hint={"center_x": 0.28, "center_y": 0.50},
            ),
            MDTextField(
                MDTextFieldHintText(
                    text="Peso (gramas)",
                ),
                MDTextFieldMaxLengthText(
                    max_text_length=10,
                ),
                mode="outlined",
                size_hint_x=None,
                width="240dp",
                pos_hint={"center_x": 0.28, "center_y": 0.35},
            ),
            MDButton(
                MDButtonText(
                    text="Imprimir resultados",
                ),
                MDButtonIcon(
                    icon="plus",
                    theme_icon_color="Custom",
                    icon_color="purple"
                ),
                pos_hint={"center_x": 0.28, "center_y": 0.2},
            ),
            MDIconButton(
                icon="heart-outline",
                style="outlined",
                theme_bg_color="Custom",
                icon_color="purple",
                pos_hint={"center_x": 0.9, "center_y": 0.9},
            ),
            MDCircularProgressIndicator(
                size_hint = (None, None),
                size = ( "48dp", "48dp"),
                pos_hint= {'center_x': .75, 'center_y': .5}
            ),
            md_bg_color=(0.18, 0.01, 0.29, 1)
        )

MyApp().run()

