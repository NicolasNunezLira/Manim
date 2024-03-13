"""
***************************************************************************
    punto_medio_b.py
    ---------------------
    Date                 : May 2020
    Author               : Víctor Osores
***************************************************************************
*                                                                         *
* Este script genera una animación que muestra la de integración numérica *
* del punto medio elemental.                                              *
*                                                                         *
* python3 ./manim.py punto_medio_b.py -pmn 1       (720p)                 *
*                                                                         *
***************************************************************************
"""

__author__ = 'Víctor Osores'
__date__ = 'May 2020'

from manimlib.imports import *
import numpy as np

y_max = 50
x_max = 7

# Dominio de integracion [a,b]
a = 2
b = 6
class punto_medio_b(GraphScene):
    CONFIG = {
        "y_max" : y_max,
        "y_min" : 0,
        "x_max" : x_max,
        "x_min" : 0,
        "y_tick_frequency" : 5,
		"x_tick_frequency" : 1,
        "axes_color" : BLUE,
        "x_axis_label" : None,
        "y_axis_label" : None,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": BLUE,
        "area_opacity": 0.4,
        "num_rects": 100,
        "num_graph_anchor_points" : 3000,
    }

    def p1(self,x):
        return 20.0*np.sin((2*np.pi/20.0)*x)+15.0

    def construct(self):
        self.setup_axes()
        graph = self.get_graph(self.p1, color = GREEN,x_min=a-1.0)
        self.func = lambda x: 34.021
        graphb = self.get_graph(self.func, color = BLUE,x_min=a,x_max=b)
        vert1=self.get_vertical_line_to_graph(a,graphb,color=BLUE)
        vert2=self.get_vertical_line_to_graph(b,graphb,color=BLUE)
        graph_area = self.get_area(graphb, a, b)

        tex = TexMobject('f(x)',color = GREEN) 
        tex.scale(0.7) 
        tex.next_to(self.coords_to_point(5, 35), UP)

        self.play(
        	ShowCreation(graph),
            ShowCreation(vert1),
            ShowCreation(vert2),
            Write(tex),
            run_time = 2
        )
        self.play(
            ShowCreation(graphb),
            ShowCreation(graph_area),
            run_time= 1
        )

        integral = TexMobject("\\int_a^b f(x)dx\\approx (b-a)f \\left(\\frac{a+b}{2}\\right)=:I_0(f)",color = BLUE) 
        integral.scale(0.7) 
        integral.next_to(self.coords_to_point(3, 40), UP)

        self.play(
            Write(integral),
            run_time = 2
        )
        self.wait()

        
    def setup_axes(self):
        GraphScene.setup_axes(self) 
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)
        self.x_axis.set_color(RED)
        self.y_axis.set_color(RED)

        self.y_axis.label_direction = LEFT*1.5
        init_label_x = 1
        end_label_x = 7
        step_x = 1
        #   For y
        init_label_y = 5
        end_label_y = 50
        step_y = 5
        values_x = [
            (1,""),
            (2,"a"),
            (4,"\\frac{a+b}{2}"),
            (6,"b"),
            (7,"")
        ]
        self.x_axis_labels = VGroup() # Create a group named x_axis_labels
        #   pos.   tex.
        for x_val, x_tex in values_x:
            tex = TexMobject(x_tex) # Convert string to tex
            tex.scale(0.7) 
            tex.next_to(self.coords_to_point(x_val, 0), DOWN) #Put tex on the position
            self.x_axis_labels.add(tex) #Add tex in graph

        self.play(
            *[Write(objeto)
            for objeto in [
                    self.y_axis,
                    self.x_axis,
                    self.x_axis_labels
                ]
            ],
            run_time=3
        )
