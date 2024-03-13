"""
***************************************************************************
    trapecio_b.py
    ---------------------
    Date                 : May 2020
    Author               : Víctor Osores
***************************************************************************
*                                                                         *
* Este script genera una animación que muestra la regla de integración    *
* numérica del trapecio elemental.                                        *
*                                                                         *
* python3 ./manim.py trapecio_b.py -pmn 1      (720p)                     *
*                                                                         *
***************************************************************************
"""

__author__ = 'Víctor Osores'
__date__ = 'May 2020'

from manimlib.imports import *
import numpy as np

y_max = 50
x_max = 7

a = 1.5
b = 6
class trapecio_b(GraphScene):
    CONFIG = {
        "y_max" : y_max,
        "y_min" : 0,
        "x_max" : x_max,
        "x_min" : 0,
        "y_tick_frequency" : 5,
		"x_tick_frequency" : 0.5,
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
        graph = self.get_graph(self.p1, color = GREEN,x_min=a-0.5)
        tex = TexMobject('f(x)',color = GREEN) 
        tex.scale(0.7) 
        tex.next_to(self.coords_to_point(5, 35), UP)
        self.func = lambda x: 2.2092*(x-1.5)+24.080
        graphb = self.get_graph(self.func, color = BLUE,x_min=1.5,x_max=6)
        graph_area = self.get_area(graphb, a, b)
        vert1=self.get_vertical_line_to_graph(1.5,graphb,color=BLUE)
        vert2=self.get_vertical_line_to_graph(6,graphb,color=BLUE)
        self.play(
        	ShowCreation(graph),
            ShowCreation(graphb),
            ShowCreation(vert1),
            ShowCreation(vert2),
            ShowCreation(graph_area),
            Write(tex),
            run_time = 2
        )

        integral = TexMobject("\\int_a^b f(x) dx\\approx \\frac{(b-a)}{2}(f(a)+f(b)) =:I_1(f)",color = BLUE) 
        integral.scale(0.7) 
        integral.next_to(self.coords_to_point(3, 40), UP)

        self.play(
            Write(integral),
            run_time = 2
        )
        self.wait()

        
    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self) 
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)
        self.x_axis.set_color(RED)
        self.y_axis.set_color(RED)

        self.y_axis.label_direction = LEFT*1.5

        init_label_x = 1
        end_label_x = x_max
        step_x = 1

        init_label_y = 5
        end_label_y = y_max
        step_y = 5

        values_x = [
            (1.5,"a"),
            (6,"b"),
            (7,"")
        ]
        values_y = [
            (24.080,"f(a)"),
            (34.021,"f(b)"),
            (7,"")
        ]

        self.x_axis_labels = VGroup() 
        self.y_axis_labels = VGroup() 

        for x_val, x_tex in values_x:
            tex = TexMobject(x_tex) 
            tex.scale(0.7) 
            tex.next_to(self.coords_to_point(x_val, 0), DOWN) 
            self.x_axis_labels.add(tex) 
        
        for y_val, y_tex in values_y:
            texy = TexMobject(y_tex) 
            texy.scale(0.7) 
            texy.next_to(self.coords_to_point(0, y_val), LEFT) 
            self.y_axis_labels.add(texy) 

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
