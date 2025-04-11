from manim import *

class Hello(Scene):
    def construct(self):
        # Configurações iniciais
        self.camera.background_color = WHITE
        color_pink = "#FF69B4"

        # Criação do texto
        texto_stroke = Text(
            "Oi, Fernanda!",
            stroke_color=color_pink,
            stroke_width=2.5,  # Largura da borda
            fill_opacity=0   # Sem preenchimento inicial
        )

        texto_fill = Text(
            "Oi, Fernanda!",
            color=color_pink,
            stroke_width=0,  # Sem borda
            fill_opacity=1   # Com preenchimento
        )

        # Animação para desenhar as bordas e depois preencher o texto
        self.play(Write(texto_stroke))  # Desenha as bordas
        self.play(Transform(texto_stroke, texto_fill))  # Transforma para o texto preenchido
        self.wait(2)
