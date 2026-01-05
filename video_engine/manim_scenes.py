from manim import *

class ExplainerScene(Scene):
    def construct(self):
        title = Text("How WebSockets Work", font_size=48)
        self.play(Write(title))
        self.wait(2)

        client = Rectangle(height=1, width=2).shift(LEFT * 3)
        server = Rectangle(height=1, width=2).shift(RIGHT * 3)

        client_text = Text("Client", font_size=24).move_to(client)
        server_text = Text("Server", font_size=24).move_to(server)

        arrow = Arrow(client.get_right(), server.get_left())

        self.play(Create(client), Write(client_text))
        self.play(Create(server), Write(server_text))
        self.play(GrowArrow(arrow))
        self.wait(2)
