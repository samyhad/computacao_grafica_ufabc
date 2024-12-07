# Projeto de Computação Gráfica - UFABC 2024.3 - Prof. Mario Gazziro

 - Este projeto tem como finalidade o desenvolvimento de uma interface gráfica capaz de renderizar um objeto 3D obtido à partir do escaneamento de uma pessoa através de sensores específicos. Além da renderização, uma série de atributos são questionados á pessoa usuária através de um formulário intuitivo para que, a partir dos dados preenchidos e do modelo 3D, o programa consiga retornar ao usuário um cálculo de gordura corporal com uma certa precisão aceitável.

## Prototipação



## Arquitetura

## Bibliotecas utilizadas

|Nome|Versao|Linguagem|
|----|------|---------|
|Kivy               |2.3.0|Python 3|
|Kivy-examples      |2.3.0|Python 3|
|Kivy-Garden        |0.1.5|Python 3|
|Panda3D            |1.10.15|Python 3|
|panda3d_kivy       |0.5.2|Python 3|

## Setup do projeto

    apt install python3.10-venv

    python3 -m venv comp_graf

    source comp_graf/bin/activate

    python -m pip install "kivy[base]" kivy_examples

    pip install "kivy[sdl2]"

    pip install panda3d_kivy
