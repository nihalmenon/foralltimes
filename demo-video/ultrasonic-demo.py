from manim import *
import scipy.signal
import numpy as np

class Ultrasonic(Scene):
    def construct(self):
        beam_time = 0.65
        # enter sensor objects
        enter_sensor = VGroup()
        enter_box = Square(2, stroke_color= GREEN, fill_color = GREEN, fill_opacity=0.5)
        enter_text = Text("Enter", should_center=True)
        enter_sensor.add(enter_box)

        # exit sensor objects
        exit_sensor = VGroup()
        exit_box = Square(2, stroke_color= RED, fill_color = RED, fill_opacity=0.5)
        exit_text = Text("Exit", should_center=True)
        exit_sensor.add(exit_box)
        
        # wall
        wall = Line(start= UP*4, end=DOWN*4)

        # displays sensors and shifts them
        self.play(Create(exit_sensor), Create(enter_sensor))
        self.play(enter_sensor.animate.shift(LEFT * 4.5).scale(0.6).shift(UP * 2), exit_sensor.animate.shift(LEFT * 4.5).scale(0.6).shift(DOWN * 2))
    
        # creates text
        enter_text.move_to(enter_box).scale(0.5)
        exit_text.move_to(exit_box).scale(0.5)
        
        # displays text
        self.play(Create(exit_text), Create(enter_text))
        self.play(Wiggle(enter_text))
        self.play(Wiggle(exit_text))


        # displays wall
        self.play(Create(wall))
        self.play(wall.animate.shift(RIGHT * 4.5))
        

        # creates beams and trace
        beam1 = Dot(enter_sensor.get_right())
        beam2 = Dot(exit_sensor.get_right())    
        trace1 = TracedPath(beam1.get_center, dissipating_time=0.5, stroke_opacity=[0, 1])
        trace2 = TracedPath(beam2.get_center, dissipating_time=0.5, stroke_opacity=[0, 1])

        # displays beam
        self.add(trace1, trace2, beam1, beam2)
        self.play(Create(beam1), Create(beam2))
        self.play(Create(trace1), Create(trace2))

        # plays pulse animation
        for i in range(0, 4):
            self.play(beam1.animate.shift(8.2 * RIGHT), beam2.animate.shift(8.2*RIGHT), run_time=beam_time)
            self.play(beam1.animate.shift(8.2 * LEFT), beam2.animate.shift(8.2*LEFT), run_time=beam_time)
        
        # hides beams
        self.play(FadeOut(beam1), FadeOut(beam2))
       
        # creates person 
        person = Circle(color=PURPLE, fill_color=PURPLE, fill_opacity=0.5)

        # displays person
        self.play(GrowFromCenter(person))
        self.play(person.animate.shift(UP * 3.5).scale(0.4))


        # pulse animation
        for i in range(0, 2):
            self.play(beam1.animate.shift(8.2 * RIGHT), beam2.animate.shift(8.2*RIGHT), run_time=beam_time)
            self.play(beam1.animate.shift(8.2 * LEFT), beam2.animate.shift(8.2*LEFT), run_time=beam_time)

        # person collides with beam
        self.play(person.animate.shift(1.5 * DOWN), beam1.animate.shift(3.5 * RIGHT), beam2.animate.shift(3.5*RIGHT), run_time=beam_time)
        self.play(beam1.animate.shift(3.5* LEFT), beam2.animate.shift(3.5*LEFT), run_time=beam_time)
       
        # alerts enter sensor
        self.play(Indicate(enter_text, color=RED))
        self.add_sound('alert.wav')
        

        # waits for person to leave
        for i in range(0, 2):
            self.play(beam1.animate.shift(3.5 * RIGHT), run_time=beam_time)
            self.play(beam1.animate.shift(3.5* LEFT), run_time=beam_time)

        #person leaves
        self.play(person.animate.shift(2 * DOWN), beam1.animate.shift(8.2 * RIGHT),run_time = beam_time)
        self.play(beam1.animate.shift(8.2 * LEFT), run_time=beam_time) 

        # camera takes a picture
        self.play(Indicate(enter_text, color=RED))
        camera = Rectangle(height=2, width=7)
        self.add_sound('camera.wav')
        self.play(Create(camera))   
        self.play(Circumscribe(camera))
        self.play(FadeOut(camera))

        # alerts exit sensor
        self.play(Indicate(exit_text, color=WHITE))

        # plays pulse animation only on exit sensor
        for i in range(0, 2):
            self.play(beam2.animate.shift(8.2 * RIGHT), run_time=beam_time)
            self.play(beam2.animate.shift(8.2* LEFT), run_time=beam_time)
        
        # person collides with exit sensor
        self.play(person.animate.shift(2 * DOWN), beam2.animate.shift(3.5 * RIGHT), run_time=beam_time)
        self.play(beam2.animate.shift(3.5 * LEFT), run_time=beam_time) 

        # alerts exit sensor
        self.play(Indicate(exit_text, color=WHITE))


        # waits for person to leave
        for i in range(0, 2):
            self.play(beam2.animate.shift(3.5 * RIGHT), run_time=beam_time)
            self.play(beam2.animate.shift(3.5* LEFT), run_time=beam_time)

        # person leaves
        self.play(person.animate.shift(1.5 * DOWN), beam2.animate.shift(8.2 * RIGHT), run_time=beam_time)
        self.play(beam2.animate.shift(8.2 * LEFT), run_time=beam_time) 

        
        self.play(Indicate(exit_text, color=WHITE))
        # pulse animation
        for i in range(0, 2):
            self.play(beam1.animate.shift(8.2 * RIGHT), beam2.animate.shift(8.2*RIGHT), run_time=beam_time)
            self.play(beam1.animate.shift(8.2 * LEFT), beam2.animate.shift(8.2*LEFT), run_time=beam_time)

        self.play(FadeOut(person), FadeOut(enter_sensor), FadeOut(exit_sensor), FadeOut(wall), FadeOut(beam1), FadeOut(beam2), FadeOut(exit_text), FadeOut(enter_text))
        