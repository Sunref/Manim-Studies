from manim import *

class ManimLogo(Scene):
    def construct(self):
        # Configurações iniciais
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        text_color = "#525893"

        # Criação dos elementos do logo
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)

        circle = Circle(color=logo_green, fill_color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_color=logo_red, fill_opacity=1).shift(RIGHT)

        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)

        # Adiciona o logo à cena
        self.play(DrawBorderThenFill(triangle))  # Desenha e preenche o triângulo
        self.play(DrawBorderThenFill(square))  # Desenha e preenche o quadrado
        self.play(DrawBorderThenFill(circle))  # Desenha e preenche o círculo
        self.play(Write(ds_m))  # Desenha o "M"
        self.wait(1)

        # Criação do texto "studies" com bordas (stroke)
        text_stroke = Text(
            "studies",
            color=logo_black,
            stroke_width=5,  # Largura das bordas
            fill_opacity=0   # Torna o preenchimento transparente inicialmente
        ).scale(2).shift(2 * DOWN)  # Ajusta o tamanho e a posição

        # Criação do texto preenchido
        text_fill = Text(
            "studies",
            color=logo_black,
            stroke_width=0,  # Sem bordas
            fill_opacity=1   # Preenchimento opaco
        ).scale(2).shift(2 * DOWN)  # Ajusta o tamanho e a posição

        # Animação para desenhar as bordas e depois preencher o texto
        self.play(Write(text_stroke))  # Desenha as bordas
        self.play(Transform(text_stroke, text_fill))  # Transforma para o texto preenchido
        self.wait(2)
