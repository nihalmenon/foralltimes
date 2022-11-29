from manim import *
import scipy.signal
import numpy as np

class Ultrasonic(Scene):
    def construct(self):
        enter_sensor = VGroup()
        enter_box = Square(2, stroke_color= GREEN, fill_color = GREEN, fill_opacity=0.5)
        enter_text = Text("Enter", should_center=True)
        enter_sensor.add(enter_box)


        exit_sensor = VGroup()
        exit_box = Square(2, stroke_color= RED, fill_color = RED, fill_opacity=0.5)
        exit_text = Text("Exit", should_center=True)
        exit_sensor.add(exit_box)
        
        
        wall = Line(start= UP*4, end=DOWN*4)

        self.play(Create(exit_sensor), Create(enter_sensor))
        self.wait(1)
        self.play(enter_sensor.animate.shift(LEFT * 4.5).scale(0.6).shift(UP * 2.5), exit_sensor.animate.shift(LEFT * 4.5).scale(0.6).shift(DOWN * 2.5))
    

        enter_text.move_to(enter_box).scale(0.5)
        exit_text.move_to(exit_box).scale(0.5)
        
        self.play(Create(exit_text), Create(enter_text))
        self.play(Indicate(enter_text).scale(0.75))
        self.play(Indicate(exit_text).scale(0.75))


        self.play(Create(wall))
        self.play(wall.animate.shift(RIGHT * 4.5))
        

        beam1 = Dot(enter_sensor.get_right())
        beam2 = Dot(exit_sensor.get_right())
        
        trace1 = TracedPath(beam1.get_center, dissipating_time=0.5, stroke_opacity=[0, 1])
        trace2 = TracedPath(beam2.get_center, dissipating_time=0.5, stroke_opacity=[0, 1])

        
        self.add(trace1, trace2, beam1, beam2)
        self.play(Create(beam1), Create(beam2))
        self.play(Create(trace1), Create(trace2))

        for i in range(0, 5):
            self.play(beam1.animate.shift(8.2 * RIGHT), beam2.animate.shift(8.2*RIGHT), run_time=1)
            self.play(beam1.animate.shift(8.2 * LEFT), beam2.animate.shift(8.2*LEFT), run_time=1)
        

        self.wait()
        