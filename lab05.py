#!/usr/bin/env python

from manimlib.imports import *
import numpy as np
from scipy import interpolate

# d :  0.25    1.00    1.50    2.50    7.50
# p : -10.8    13.5    16.4    28.7    51.3
# ---- p = a + b * log_10(d)--------------

Cyan = "#30bced"
Violet = "#44344F"
Green = "#AAF683"
Orange = "#FC5130"

class Introduccion(GraphScene):
	CONFIG = {
		"x_max" : 8,
		"x_min" : 0,
		"y_max" : 52,
		"y_min" : -12,
		"axes_color" : "White",
		"x_axis_label" : "$d$",
		"y_axis_label" : "$p$",
		"x_tick_frequency" : 1,
		"y_tick_frequency" : 10,
		}

	def construct(self):
		# ========== Datos Iniciales ============================
		title = TextMobject("Datos",color = Orange).move_to(TOP+2*DOWN)
		text1 = TextMobject("Dosis de Vitamina A(mg)",color = Violet).move_to(3*LEFT)
		text2 = TextMobject(":(0.25,1.00,1.50,2.50,7.50)",color = YELLOW).next_to(text1,RIGHT)
		text3 = TextMobject("Peso ganado(gr)",color = Violet).next_to(text1,DOWN)
		text4 = TextMobject(":(-10.8,13.5,16.4,28.7,51.3)",color = YELLOW).next_to(text2,DOWN)
		self.play(ShowCreation(title),ShowCreation(text1),ShowCreation(text2),ShowCreation(text3),ShowCreation(text4))
		self.wait(3)
		self.play(Uncreate(text1),Uncreate(text3),Uncreate(text2),Uncreate(text4))
		# ==========Creacion grafico 1======================
		d = np.array([0.25,1.00,1.50,2.50,7.50])
		p = np.array([-10.8,13.5,16.4,28.7,51.3])
		P = 5*[None]
		T = 5*[None]
		POS = [RIGHT,DOWN,UP,UP,UP]
		title1 = TextMobject("Datos",color = Orange).move_to(TOP+DOWN)
		self.play(ReplacementTransform(title,title1))
		self.setup_axes()
		anims = []
		for i in range(0,5):
			P[i] = Dot(color = Violet).move_to(self.coords_to_point(d[i],p[i]))
			T[i] = "(%.1f,%.1f)" % (d[i],p[i])
			T[i] = TextMobject(T[i],color = Cyan).next_to(P[i],POS[i])
			anims.append(ShowCreation(P[i]))
			anims.append(ShowCreation(T[i]))
		self.play(*anims)
		# ======== Minimos cuadrados ==============
		self.wait(2)
		self.play(Uncreate(T[0]),Uncreate(T[1]),Uncreate(T[2]),Uncreate(T[3]),Uncreate(T[4]))
		title2 = TextMobject("Modelo : $p = a + b\log_{10}(d)$",color = Orange).move_to(TOP+DOWN)
		error = TexMobject(
			"e",							#0
			"= \\sqrt{ \\sum_{i = 1}^5(", 	#1
			"p_i",							#2
			"-",							#3
			"p(",							#4
			"d_i",							#5
			")",							#6
			")^2}="						    #7
			).move_to(DOWN+2*RIGHT).scale(.8)
		error[0].set_color(YELLOW)
		error[1].set_color(WHITE)
		error[2].set_color(BLUE)
		error[3].set_color(WHITE)
		error[4].set_color(Orange)
		error[5].set_color(BLUE)
		error[6].set_color(Orange)
		error[7].set_color(WHITE)
		self.play(ReplacementTransform(title1,title2))
		self.wait(3)
		a = np.array([9,10,11,12,13,14,15,16])
		b = np.array([39,40,41,42,43,44,45,46])
		graph = 8*[None]
		lab = 8*[None]
		vert = 8*[None]
		errlab = 8*[None]
		for i in range(0,8):
			lab[i] = "Modelo : $p = %i + %i \log_{10}(d)$" %(a[i],b[i])
			lab[i] = TextMobject(lab[i],color = Orange).move_to(TOP+DOWN)
			graph[i] = self.get_graph(lambda x: a[i] + b[i]*np.log10(x),xmin = 0,x_max = 8,label = lab,color = Orange)
			vert[i] = 5*[None]
			err = 0
			for j in range(0,5):
				x = self.coords_to_point(d[j],p[j])
				y = self.coords_to_point(d[j],a[i] + b[i]*np.log10(d[j]))
				err += (a[i] + b[i]*np.log10(d[j]) - p[j])**2
				vert[i][j] = Line(x,y,color=YELLOW)
			errlab[i] = TexMobject("%f" %(np.sqrt(err)),color = YELLOW).next_to(error,RIGHT)
			if i == 0:
				self.play(ShowCreation(graph[i]),ReplacementTransform(title2,lab[i]),ShowCreation(error),ShowCreation(errlab[i]))
				self.play(ShowCreation(vert[i][0]),ShowCreation(vert[i][1]),ShowCreation(vert[i][2]),ShowCreation(vert[i][3]),ShowCreation(vert[i][4]))
			else:
				self.play(ReplacementTransform(graph[i-1],graph[i]),ReplacementTransform(lab[i-1],lab[i]),
					ReplacementTransform(vert[i-1][0],vert[i][0]),ReplacementTransform(vert[i-1][1],vert[i][1]),
					ReplacementTransform(vert[i-1][2],vert[i][2]),ReplacementTransform(vert[i-1][3],vert[i][3]),
					ReplacementTransform(vert[i-1][4],vert[i][4]),ReplacementTransform(errlab[i-1],errlab[i]))


	def setup_axes(self):
		GraphScene.setup_axes(self)
		init_label_x = 0
		end_label_x = 8
		step_x = 1
		init_label_y = -12
		end_label_y = 52
		step_y = 10
		self.x_axis.label_direction = DOWN
		self.y_axis.label_direction = LEFT
		self.x_axis.add_numbers(*range(init_label_x,
		    end_label_x+step_x,step_x))
		self.y_axis.add_numbers(*range(init_label_y,
		    end_label_y+step_y,step_y))
		self.play(ShowCreation(self.x_axis),ShowCreation(self.y_axis))


class Explicacion(Scene):
	def construct(self):
		text0 = TextMobject("Dado los datos",color = "White").move_to(TOP+2*DOWN+2.5*LEFT)
		text1 = TexMobject(
			"(",				#0
			"d_i",				#1
			",",				#2
			"p_i",				#3
			")_{i=0}^{n}"		#4
			,color = Cyan).next_to(text0,RIGHT)
		text1[1].set_color(BLUE)
		text1[3].set_color(BLUE)
		text2 = TextMobject("y el modelo",color = "White").next_to(text1,RIGHT)
		text3 = TexMobject(
			"p(d) = ",				#0
			"a",				#1
			" +",				#2
			" b",				#3
			"\log_{10}(d)"		#4
			,color = Orange).next_to(text1,DOWN)
		text3[1].set_color(Green)
		text3[3].set_color(Green)
		text4 = TextMobject(
			"¿Cuales son los valores de ",		#0
			"$a$",								#1
			" y ",								#2
			"$b$",								#3
			" para que el error"				#4
			,color = "White").next_to(text3,DOWN)
		text4[1].set_color(Green)
		text4[3].set_color(Green)
		text5 = TexMobject(
			"e",							#0
			"= \\sqrt{ \\sum_{i = 1}^5(", 	#1
			"p_i",							#2
			"-",							#3
			"p(",							#4
			"d_i",							#5
			")",							#6
			")^2}"							#7
			,color = "Cyan").next_to(text4,DOWN)
		text5[2].set_color(BLUE)
		text5[4].set_color(Orange)
		text5[5].set_color(BLUE)
		text5[6].set_color(Orange)
		text6 = TextMobject("sea mínimo?",color = "White").next_to(text5,DOWN)
		self.play(ShowCreation(text0),ShowCreation(text1),ShowCreation(text2),ShowCreation(text3),
			ShowCreation(text4),ShowCreation(text5),ShowCreation(text6))
		self.wait(3)

		d = np.array([0.25,1.00,1.50,2.50,7.50])
		p = np.array([-10.8,13.5,16.4,28.7,51.3])
		eq = TexMobject(
			"p(d_{i}) = ",
			"a",
			"+",
			"b",
			"\log_{10}(d_{i}) = p_{i}" ,color = Orange)
		eq[1].set_color(Green)
		eq[3].set_color(Green)
		self.play(Uncreate(text0),Uncreate(text1),Uncreate(text2),Uncreate(text4),
			Uncreate(text5),Uncreate(text6),ReplacementTransform(text3,eq))
		self.wait(3)
		eq1 = 5*[None]
		eq2 = 5*[None]
		anim = []
		anim2 = []
		for i in range(0,5):
			eq1[i] = TexMobject(
				"p(d_{%i}) = " %(i+1),
				"a",
				"+",
				"b",
				"\log_{10}(d_{%i}) = p_{%i}" %(i+1,i+1),color = Orange)
			eq1[i][1].set_color(Green)
			eq1[i][3].set_color(Green)
			eq2[i] = TexMobject(
				"p(%.1f) = " %(d[i]),
				"a",
				"+",
				"b",
				"\log_{10}(%.1f) = %.1f" %(d[i],p[i]),color = Orange)
			eq2[i][1].set_color(Green)
			eq2[i][3].set_color(Green)
			if i == 0:
				eq1[i].move_to(TOP+2*DOWN)
				eq2[i].move_to(TOP+2*DOWN)
			else:
				eq1[i].next_to(eq1[i-1],DOWN)
				eq2[i].next_to(eq2[i-1],DOWN)
		self.play(ReplacementTransform(eq,eq1[2]),ShowCreation(eq1[1]),ShowCreation(eq1[0]),ShowCreation(eq1[3]),ShowCreation(eq1[4]))
		self.wait(3)
		self.play(ReplacementTransform(eq1[0],eq2[0]),ReplacementTransform(eq1[1],eq2[1]),ReplacementTransform(eq1[2],eq2[2]),
			ReplacementTransform(eq1[3],eq2[3]),ReplacementTransform(eq1[4],eq2[4]))
		self.wait(3)
		self.play(Uncreate(eq2[0]),Uncreate(eq2[1]),Uncreate(eq2[2]),Uncreate(eq2[3]),Uncreate(eq2[4]))
		matrix = TexMobject(r"\begin{pmatrix} 1 & \log_{10}(%.1f)\\1 & \log_{10}(%.1f)\\1 & \log_{10}(%.1f)\
				\\1 & \log_{10}(%.1f)\\1 & \log_{10}(%.1f) \end{pmatrix}\quad" %(d[0],d[1],d[2],d[3],d[4]),color=Orange).move_to(2*LEFT)
		inc = TexMobject(r"\begin{pmatrix}a\\b\end{pmatrix}\quad",color = Green).next_to(matrix,RIGHT)
		rhs = TexMobject(r"=\begin{pmatrix} %.1f\\%.1f\\%.1f\\%.1f\\%.1f\end{pmatrix}\quad"%(p[0],p[1],p[2],p[3],p[4]),color = Orange).next_to(inc,RIGHT)
		self.play(ShowCreation(matrix),ShowCreation(inc),ShowCreation(rhs))
		self.wait(3)
		A = TexMobject(r"A_{5\times 2}",color=Orange).next_to(inc,LEFT)
		b = TexMobject(r"=b_{5\times 1}",color=Orange).next_to(inc,RIGHT)
		self.play(ReplacementTransform(matrix,A),ReplacementTransform(rhs,b))
		self.wait(3)
		At = TexMobject(r"A_{2\times 5}^tA_{5\times 2}",color=Orange).next_to(inc,LEFT)
		bt = TexMobject(r"=A_{2\times 5}^tb_{5\times 1}",color=Orange).next_to(inc,RIGHT)
		title = TextMobject("Ecuaciones normales",color=Orange).move_to(TOP+DOWN)
		self.play(ReplacementTransform(A,At),ReplacementTransform(b,bt),ShowCreation(title))
		self.wait(3)
		inc2 = inc.copy().move_to(2*LEFT)
		At2 = TexMobject(r"=\left( A_{2\times 5}^tA_{5\times 2}\right)^{-1}",color=Orange).next_to(inc2,RIGHT)
		bt2 = TexMobject(r"A_{2\times 5}^tb_{5\times 1}",color=Orange).next_to(At2,RIGHT)
		self.play(ReplacementTransform(At,At2),ReplacementTransform(bt,bt2),ReplacementTransform(inc,inc2))
		self.wait(3)
		inc3 = TexMobject(r"x",color = Green)
		command = TexMobject(r">> ",color = WHITE).next_to(inc3,LEFT)
		Ab = TexMobject(r"= A\backslash b;",color = Orange).next_to(inc3,RIGHT)
		title2 = TextMobject("Resolución en Octave",color=Orange).move_to(TOP+DOWN)
		sub = TextMobject("donde ",color = WHITE).move_to(DOWN+LEFT)
		sub2 = TexMobject("x = [a;b]", color = Green).next_to(sub,RIGHT)
		self.play(ReplacementTransform(inc2,inc3),Uncreate(bt2),Uncreate(At2),ShowCreation(command),ShowCreation(Ab),ReplacementTransform(title,title2),
			ShowCreation(sub),ShowCreation(sub2))
		self.wait(3)

class Explicacion2(GraphScene):
	CONFIG = {
		"x_max" : 8,
		"x_min" : 0,
		"y_max" : 52,
		"y_min" : -12,
		"axes_color" : "White",
		"x_axis_label" : "$L$",
		"y_axis_label" : "$p$",
		"x_tick_frequency" : 1,
		"y_tick_frequency" : 10,
		}

	def construct(self):

		Q = TextMobject("¿Es esta la única opción?")
		self.play(ShowCreation(Q))
		self.wait(3)
		title = TextMobject("Datos",color = Orange).move_to(TOP+2*DOWN)
		text1 = TextMobject(" Dosis de Vitamina A(mg)",color = Violet).move_to(2.8*LEFT)
		text2 = TextMobject(":(0.25,1.00,1.50,2.50,7.50)",color = YELLOW).next_to(text1,RIGHT)
		text3 = TextMobject("Peso ganado(gr)",color = Violet).next_to(text1,DOWN)
		text4 = TextMobject(":(-10.8,13.5,16.4,28.7,51.3)",color = YELLOW).next_to(text2,DOWN)
		self.play(Uncreate(Q),ShowCreation(title),ShowCreation(text1),ShowCreation(text2),ShowCreation(text3),ShowCreation(text4))
		self.wait(3)
		d = np.array([0.25,1.00,1.50,2.50,7.50])
		p = np.array([-10.8,13.5,16.4,28.7,51.3])
		lgd = np.log10(d)
		text1_3 = TextMobject("(Dosis de Vitamina A(mg))",color = Violet).move_to(2.9*LEFT)
		text1_2 = TexMobject("\log_{10}",color = Violet).next_to(text1_3,LEFT)
		text2_2 = TextMobject(":(%.2f,%.2f,%.2f,%.2f,%.2f)"%(lgd[0],lgd[1],lgd[2],lgd[3],lgd[4]),color = YELLOW).move_to(text2)
		self.play(ReplacementTransform(text1,text1_3),ShowCreation(text1_2),ReplacementTransform(text2,text2_2))
		self.wait(3)
		model = TexMobject(
			"p = ",
			"a ",
			"+",
			" b",
			"\log_{10}(d)",
			color = Orange)
		model[1].set_color(Green)
		model[3].set_color(Green)
		model[4].set_color(YELLOW)
		title2 = TextMobject("Modelo",color = Orange).move_to(TOP+2*DOWN)
		self.play(Uncreate(text4),Uncreate(text3),Uncreate(text1_2),Uncreate(text2_2),Uncreate(text1_3))
		self.play(ShowCreation(model),ReplacementTransform(title,title2))
		self.wait(3)
		model2 = TexMobject(
			"p = ",
			"a ",
			"+",
			" b",
			"L",
			color = Orange)
		model2[1].set_color(Green)
		model2[3].set_color(Green)
		model2[4].set_color(YELLOW)
		sub = TextMobject("donde ",color = WHITE).move_to(DOWN+LEFT)
		sub2 = TexMobject("L = \log_{10}(d)", color = YELLOW).next_to(sub,RIGHT)
		self.play(ReplacementTransform(model,model2),ShowCreation(sub),ShowCreation(sub2))
		self.wait(1.5)
		
		model3 = TexMobject(
			"p = ",
			"b",
			"L^1",
			"+",
			"a",
			"L^0",
			"\in \mathcal{P}_1(\mathbb{R})",
			color = Orange)
		model3[1].set_color(Green)
		model3[2].set_color(YELLOW)
		model3[4].set_color(Green)
		model3[5].set_color(YELLOW)
		self.play(ReplacementTransform(model2,model3))
		self.wait(3)
		command = TexMobject(
			">> ",
			"x",
			"= polyfit(L,p,1);",
			color = Orange)
		command[0].set_color(WHITE)
		command[1].set_color(Green)
		sub3 = TexMobject("x = [b;a]", color = Green).next_to(sub,RIGHT)
		title3 = TextMobject("Resolución en Octave",color = Orange).move_to(TOP+2*DOWN)
		self.play(ReplacementTransform(model3,command),ReplacementTransform(sub2,sub3),ReplacementTransform(title2,title3))
		self.wait(3)

	def setup_axes(self):
		GraphScene.setup_axes(self)
		init_label_x = 0
		end_label_x = 8
		step_x = 1
		init_label_y = -12
		end_label_y = 52
		step_y = 10
		self.x_axis.label_direction = DOWN
		self.y_axis.label_direction = LEFT
		self.x_axis.add_numbers(*range(init_label_x,
		    end_label_x+step_x,step_x))
		self.y_axis.add_numbers(*range(init_label_y,
		    end_label_y+step_y,step_y))
		self.play(ShowCreation(self.x_axis),ShowCreation(self.y_axis))