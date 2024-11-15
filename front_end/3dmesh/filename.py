from math import pi, sin, cos
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

loadPrcFileData("", "load-file-type p3assimp")


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Desabilitar os controles padrão da câmera
        self.disableMouse()

        # Carregar o modelo da orquídea
        model = self.loader.load_model('orchid-flower/source/Orchid_highpoly/Orchid_Highpoly.obj')
        model.reparent_to(self.render)

        # Ajustar o modelo para a escala desejada
        model.set_scale(0.5)  # Ajuste a escala conforme necessário

        # Centralizar o modelo na cena
        model.set_pos(0, 0, 0)

        model.setHpr(0, 90, 0) 

        # Calcular as dimensões do modelo
        model_bounds = model.get_tight_bounds()
        size = model_bounds[1] - model_bounds[0]
        max_size = max(size[0], size[1], size[2])

        # Ajustar a posição inicial da câmera para enquadrar o modelo
        self.camera.set_pos(0, max_size * 2, max_size)
        self.camera.look_at(model)

        # Tentar carregar a textura manualmente
        texture = self.loader.load_texture('orchid-flower/source/Orchid_highpoly/Orchid_Highpoly.jpg')
        model.set_texture(texture)

        # Adicionar a tarefa de rotação da câmera
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

    # Definir a tarefa para girar a câmera ao redor do modelo
    def spinCameraTask(self, task):
        angleDegrees = task.time * 20.0  # Velocidade de rotação ajustável
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.look_at(0, 0, 0)  # Mantém a câmera olhando para o centro
        return Task.cont


app = MyApp()
app.run()
