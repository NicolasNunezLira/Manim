#!/usr/bin/env python

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)

	
class FlowNetwork(Scene):
	def construct(self):
		triangle = Polygon(ORIGIN,DL,DR, color = "WHITE")
		dot = Dot(radius = 0.5, color = "WHITE").shift(0.25*DOWN)

		Qin = VGroup(triangle,dot)
		pdrop = TextMobject("$5.2 \\times 10^5$ [Pa]", color = "WHITE").scale(0.7)
		self.play(ShowCreation(triangle), ShowCreation(dot))
		self.add_foreground_mobjects(dot)
		self.play(Qin.to_corner, UL)
		
		pdrop.next_to(triangle,DOWN)
		q = 7*[None]
		texL = 7*[None]
		qName = 7*[None]
		qNN = 7*[None]
		
		q[0] = Line(triangle.get_top(),triangle.get_top()+4*RIGHT, color = "WHITE")
		q[1] = Line(q[0].get_right(),q[0].get_right()+4*RIGHT, color = "WHITE")
		q31 = Line(q[1].get_right(),q[1].get_right()+2*RIGHT, color = "WHITE")
		q32 = Line(q31.get_right(),q31.get_right()+3*DOWN, color = "WHITE")
		q33 = Line(q32.get_bottom(),q32.get_bottom()+2*LEFT, color = "WHITE")
		q[2] = q32
		q[3] = Line(q[1].get_right(),q[1].get_right()+3*DOWN, color = "WHITE")
		q[4] = Line(q[3].get_bottom(),q[3].get_bottom()+4*LEFT, color = "WHITE")
		q[5] = Line(q[0].get_right(),q[0].get_right()+3*DOWN, color = "WHITE")
		q[6] = Line(q[4].get_left(),q[4].get_left()+2*LEFT, color = "WHITE")
		L = np.array([100, 100, 200, 75, 100, 75, 50]);
		posL = [DOWN, DOWN, RIGHT, RIGHT, UP, RIGHT, UP]
		for i in range(len(q)):
			lenstring = "%d [m]" % L[i]
			namestring = "q_%d" % (i+1)
			texL[i] = TextMobject(lenstring, color = "WHITE").scale(0.5)
			texL[i].next_to(q[i],0.2*posL[i])
			qName[i] = TexMobject(namestring, color = "#54c9ff").scale(0.8)
			qName[i].next_to(q[i],-1*posL[i])
			qNN[i] = TexMobject(namestring+"=\\ ??", color = "#54c9ff").scale(0.8)
		q[2] = VGroup(q31,q32,q33)
		qNNGroup = VGroup(*qNN[0:4])
		qNNGroup2 = VGroup(*qNN[-3:])
		qNNGroup.arrange(DOWN,aligned_edge=LEFT)
		qNNGroup2.arrange(DOWN,aligned_edge=LEFT)
		qNNGroup.shift(2.25*DOWN+3.5*LEFT)
		qNNGroup2.next_to(qNNGroup,RIGHT)
		
		anim = []
		for i in range(len(q)):
			anim.append(ReplacementTransform(qName[i].copy(),qNN[i]))
		
		Q = VGroup(*q)
		QNames = VGroup(*qName)
		L = VGroup(*texL)
		self.play(ShowCreation(Q))
		self.wait()
		self.play(Write(L))
		self.play(Write(pdrop))
		self.wait(1)
		self.play(Write(QNames))
		self.wait()
		pump = VGroup(Q,pdrop)
		
		sevenEq = VGroup(qNNGroup,qNNGroup2)
		texEq = TextMobject("7 ecuaciones", color = "#54c9ff").next_to(sevenEq,RIGHT)
		texEq.shift(2*RIGHT)
		self.play(*anim)
		self.wait()
		self.play(ReplacementTransform(sevenEq,texEq))
		self.wait()
		self.play(FadeOut(texEq))
		self.wait()
		
		

		S = 7*[None]
		SName = 7*[None]
		equation = 7*[None]

		S[0] = VGroup(q[0],q[1],q[5])
		S[1] = VGroup(q[1],q31,q[3])
		S[2] = VGroup(q33,q[3],q[4])
		S[3] = VGroup(q[4],q[5],q[6])
		S[4] = VGroup(q[2],q[3])
		S[5] = VGroup(q[1],q[3],q[4],q[5])
		S[6] = VGroup(q[0],q[5],q[6])
		
		SName[0] = VGroup(qName[0],qName[1],qName[5])
		SName[1] = VGroup(qName[1],qName[2],qName[3])
		SName[2] = VGroup(qName[2],qName[3],qName[4])
		SName[3] = VGroup(qName[4],qName[5],qName[6])
		SName[4] = VGroup(texL[2],qName[2],texL[3],qName[3])
		SName[5] = VGroup(texL[1],qName[1],texL[3],qName[3],texL[4],qName[4],texL[5],qName[5])
		SName[6] = VGroup(texL[0],qName[0],texL[5],qName[5],texL[6],qName[6])
		posNode = [q[0].get_right(), q[1].get_right(), q[3].get_bottom(), q[5].get_bottom()]

		eqscale = .8
		equation[0] = TexMobject("q_1","- q_2","- q_6","= 0", color = "#ff5454").scale(eqscale)
		equation[0].shift(1*DOWN+4*LEFT)
		equation[1] = TexMobject("q_2","- q_3","- q_4","= 0", color = "#ff5454").scale(eqscale)
		equation[1].shift(1.6*DOWN+4*LEFT)
		equation[2] = TexMobject("q_3","+ q_4","- q_5","= 0", color = "#ff5454").scale(eqscale)
		equation[2].shift(2.2*DOWN+4*LEFT)
		equation[3] = TexMobject("q_5","+ q_6","- q_7","= 0", color = "#ff5454").scale(eqscale)
		equation[3].shift(2.8*DOWN+4*LEFT)
		equation[4] = TexMobject("200", "q_3^2","-75", "q_4^2","= 0", color = "#57ff54").scale(eqscale)
		equation[4].shift(1*DOWN+4*RIGHT)
		equation[5] = TexMobject("100", "q_2^2","+75", "q_4^2","+100", "q_5^2","-75", "q_6^2","= 0", color = "#57ff54").scale(eqscale)
		equation[5].shift(1.9*DOWN)
		equation[5].align_to(equation[4],RIGHT)
		equation[6] = TexMobject("100", "q_1^2","+75", "q_6^2", "+50", "q_7^2","=", "5.2 \\times 10^5 \\frac{\\pi^2 (0.2)^5}{8(0.02)(998)}", color = "#57ff54").scale(eqscale)
		equation[6].shift(2.8*DOWN)
		equation[6].align_to(equation[4],RIGHT)
		
		leneq = np.array([4, 8, 6])
		colores = ["#FF0000","#FF0000","#FF0000","#FF0000","#00FF00","#00FF00","#00FF00"]
		for i in range(len(S)-1):
			if i < 4:
				node = Dot(posNode[i],color="#ff5454")
				self.play(ShowCreation(node),run_time = 0.25)
				self.add_foreground_mobjects(node)
				self.play(S[i].set_color,colores[i],run_time = 0.25)
				self.play(
					ReplacementTransform(SName[i][0].copy(),equation[i][0]),
					ReplacementTransform(SName[i][1].copy(),equation[i][1]),
					ReplacementTransform(SName[i][2].copy(),equation[i][2]),
					Write(equation[i][-1]))
				self.play(S[i].set_color,"#FFFFFF",Uncreate(node),run_time = 0.5)
			else:
				self.play(S[i].set_color,colores[i], run_time = 0.5)
				anims = []
				for j in range(leneq[i-4]):
					anims.append(ReplacementTransform(SName[i][j].copy(),equation[i][j]))
				anims.append(Write(equation[i][-1]))
				self.play(*anims)
				self.play(S[i].set_color,"#FFFFFF",run_time = 0.5)   

		self.play(S[6].set_color,colores[6],run_time = 0.5)
		self.play(ReplacementTransform(SName[6].copy(),VGroup(equation[6][0:-1])),ReplacementTransform(pdrop.copy(),VGroup(equation[6][-1])))
		self.play(S[6].set_color,"#FFFFFF",run_time = 0.5)
		self.wait()
		
		tubes = VGroup(*q,Qin)
		txt = VGroup(*texL,pdrop,*qName)
		self.play(FadeOut(txt),Uncreate(tubes))
		self.wait()
		equations = VGroup(*equation)
		self.play(equations.move_to,ORIGIN)
		eq_color_change = []
		aligneqs = []
		for i in range(len(equation)):
			eq_color_change.append(ApplyMethod(equations[i].set_color,"#FFFFFF"))
			aligneqs.append(ApplyMethod(equations[i].align_to,4*LEFT,LEFT))
		self.play(*eq_color_change)
		self.play(equations.arrange, DOWN)
		neweq = TexMobject("- 5.2 \\times 10^5 \\frac{\\pi^2 (0.2)^5}{8(0.02)(998)}","=0", color = "#FFFFFF").scale(eqscale)
		neweq.move_to(equations[-1][6])
		neweq.align_to(equations[-1][6],LEFT)
		self.play(Transform(equations[-1][-2:],neweq))
		#self.play(*aligneqs)
		
		tex1 = TexMobject("F : \\mathbb{R}^7 \\to \\mathbb{R}^7").shift(3*UP+2.5*LEFT)
		self.play(Write(tex1),run_time = 0.5)
		tex2 = TexMobject(",\\qquad \\quad \\vec{q} := (q_1,q_2,\\ldots,q_7)").next_to(tex1,RIGHT)
		self.play(Write(tex2),run_time = 0.5)
		tex3 = TexMobject("F(\\vec{q}) =(0,0,\\ldots,0)^T").shift(UP)
		self.play(Transform(equations,tex3))
		rect = SurroundingRectangle(tex3, color = "YELLOW")
		tex4 = TexMobject("\\vec{q}_{k+1} = \\vec{q}_k - J_F(\\vec{q}_k)^{-1}F(\\vec{q}_k)").next_to(tex3,DOWN)
		tex4.shift(DOWN)
		self.play(ShowCreation(rect))
		self.wait(1)
		self.play(Write(tex4))
		self.wait()
