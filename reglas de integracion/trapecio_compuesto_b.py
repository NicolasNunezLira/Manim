"""
***************************************************************************
    trapecio_compuesto_b.py
    ---------------------
    Date                 : May 2020
    Author               : Víctor Osores
***************************************************************************
*                                                                         *
* Este script genera una animación que muestra la regla de integración    *
* numérica de los trapecios.                                              *
*                                                                         *
* python3 ./manim.py trapecio_compuesto_b.py -pmn 1      (720p)           *
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
a = 1.5
b = 6.0

# Número de subintervalos en [a,b]
n = 3 
dx = (b-a)/n

class trapecio_compuesto_b(GraphScene):
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

        self.play(
        	ShowCreation(graph),
            Write(tex),
            run_time = 2
        )

        x=np.zeros(n+1)
        x_int=np.zeros(n)
        dic_label={}
        for i in range(n+1):
            x[i] = a+i*dx
        
        dic_h={}    
        for i in range(n):
            aa=x[i]
            bb=x[i+1]
            dic_label[i] = 'x_{}'.format(i)
            self.func = lambda x: (self.p1(bb)-self.p1(aa))/(bb-aa)*(x-aa)+self.p1(aa)
            graphb = self.get_graph(self.func, color = BLUE,x_min=x[i],x_max=x[i+1])
            vert1=self.get_vertical_line_to_graph(x[i],graphb,color=BLUE)
            vert2=self.get_vertical_line_to_graph(x[i+1],graphb,color=BLUE)
            graph_area = self.get_area(graphb, x[i], x[i+1])
            self.play(
                ShowCreation(graphb),
                ShowCreation(graph_area),
                ShowCreation(vert1),
                ShowCreation(vert2),
                run_time = 1
            )

        integral = TexMobject("\\int_a^b f(x) dx=\\sum_{i=1}^n \\int_{x_{i-1}}^{x_{i}}f(x)=:I_T(f)",color = BLUE) 
        integral.scale(0.7) 
        integral.next_to(self.coords_to_point(2.8, 40), UP)

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
        end_label_x = x_max
        step_x = 1
        
        init_label_y = 5
        end_label_y = y_max
        step_y = 5

        x=np.zeros(n+1)
        dic_label={}
        for i in range(n+1):
            x[i] = a+i*dx
            dic_label[i] = 'x_{}'.format(i)
            
        self.x_axis_labels = VGroup() 
        for i in range(n+1):
            tex = TexMobject(dic_label[i]) 
            tex.scale(0.7) 
            tex.next_to(self.coords_to_point(x[i], 0), DOWN) 
            self.x_axis_labels.add(tex)

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
