# Transformações geométricas

## Serve para ajustarmos a visão que temos do modelo
### Def: operações de escala, rotação, translação
    Sequência de tranformações para animais objetos
    
    ## Translação
    A translação é realizada adicionando componenetes de deslocamento a um ponto original
    Em notação matricial.
    P = [x, y, z]^T. t = [dx, dy, dz]^t , P' = P + t =  [x+ dx, y + dy, z + dz]


    ## Escala
    Ajustar um objeto em relação ao seu view port, 
    Se vc tem apenas um único objeto, o melhor a se fazer é mexer na câmera
    basta multiplicar por uma matriz diagonal
    P = [x, y, z]^T. s = [[sx,0 ,0][0, sy, 0][0, 0, sz]]^t , P' = P * s* =  [x*sx, y *sy, z*sz]

    onde cada elemento de S exerce um fator de escalonamento para cada elemento da matriz P

    ### Escala uniforme e não uniforme
        Se s = sx = sy = sz
        Se a escalamos com valores negativo obtemos a reflexão (espelhamento) do objeto

    ## Rotação 
        ### O que é uma origem?
        Centro das nossas coordenadas

        A rotação depende de duas informações o centro e o ponto

    
    ## Espaços afins
    Comporta as transformações afins
    obeto + ambiente
    Temos um sistema de referências
    vetores (eixos)
    origem (ponto)

    Nada mais é do que uma combinação linear entre uma rotação e uma translação ou translação e escala (toda combinação de uma operação de mutiplicação matricial e soma)

    Se tivermos um objeto 3d formado por vários pontos e esses pontos formam uma cadeia de triagulos, o vetor é sempre um vetor ortogoinal a esse ponto

O time de engenharia irá disponibilizar uma matriz de transformação afim (obtida pela calibração das câmeras) pro pessoal do backend poder trabalhar


projeção(sombra do elemento no cenário|ambiente)

# Clibração de câmera
https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html

https://learnopencv.com/camera-calibration-using-opencv/

Código: https://github.com/spmallick/learnopencv/tree/master/CameraCalibration
