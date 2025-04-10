from manim import *

class Hello(Scene):
    def construct(self):
        texto = Text("Oi, Fernanda!")
        self.play(Write(texto))
        self.wait(2)
