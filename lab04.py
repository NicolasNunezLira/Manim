#!/usr/bin/env python

from manimlib.imports import *
from scipy import interpolate

class InterpolacionFirst(GraphScene):
	CONFIG = {
		"x_max" : 3,
		"x_min" : -1,
		"y_max" : 350,
		"y_min" : -50,
		"axes_color" : "White",
		"y_axis_label" : "$P$",
		"x_axis_label" : "$T$",
		"x_tick_frequency" : 1,
		"y_tick_frequency" : 50
		}

	def construct(self):
		
		eq1 = TexMobject("\\mbox{d}u = c_v \\mbox{d}T + \\left[ T \\left( \\frac{\\partial P}{\\partial T} \\right)_v - P \\right]\\mbox{d}v")
		self.play(Write(eq1))
		self.wait()
		self.play(Uncreate(eq1))
		self.wait(1)
		
		eq2 = TexMobject("1 = \\frac{0+2}{2}")
		eq3 = TexMobject("P_{T = 1}","= \\frac{P_{T = 0} + P_{T = 2}}{2}")
		self.play(Write(eq2))
		self.wait()
		self.play(ReplacementTransform(eq2,eq3))
		self.wait()
		self.play(Transform(eq3,TexMobject("P_{T = 1}", "= \\frac{293.01 + 314.84}{2}")))
		self.wait()
		self.play(Transform(eq3,TexMobject("P_{T = 1}", "\\approx 303.93")))
		self.wait()
		self.play(FadeOut(eq3))
		self.setup_axes(animate=True)
		x = np.array([0,2])
		y = np.array([293.01,314.84])
		p = []
		t = []
		for i in range(0,len(x)):
			p.append(Dot(color = "#30BCED").move_to(self.coords_to_point(x[i],y[i])))
			self.play(ShowCreation(p[i]),run_time=0.6)

		self.wait(1)
		
		graph = []
		textL = []

		for i in range(0,len(x)-1):
			pp = np.polyfit(x,y,i+1)
			graph.append(self.get_graph(lambda x : np.polyval(pp,x),color = "Yellow",
					x_min = 0,x_max = 2))
			if i == 0:
				self.play(ShowCreation(graph[i]))
				self.wait()
			else:
				self.play(ReplacementTransform(graph[i-1],graph[i]))
				self.wait()
		newdot = Dot(color = "#FC5130").move_to(self.coords_to_point(1,303.93))
		nd_lab = TexMobject("P_{\\text{sat}} =").scale(0.6).next_to(newdot,UP)
		
		decimal = DecimalNumber(303.93,num_decimal_places=2,unit=None).scale(0.6)
		decimal.next_to(nd_lab,RIGHT)
		def update_label(obj):
			obj.next_to(newdot,UP)
		def update_num(obj):
			obj.next_to(nd_lab,RIGHT)
			yy = self.point_to_coords(newdot.get_center())
			obj.set_value(yy[1])
		nd_lab.add_updater(update_label)
		decimal.add_updater(update_num)
		self.play(ShowCreation(newdot))
		self.play(Write(nd_lab),Write(decimal))
		self.play(newdot.move_to,self.coords_to_point(x[0],y[0]))
		self.play(MoveAlongPath(newdot,graph[-1]),run_time = 2)
		self.wait(1)

class InterpolacionSecond(GraphScene):
	CONFIG = {
		"x_max" : 100,
		"x_min" : 0,
		"y_max" : 30,
		"y_min" : 0	,
		"axes_color" : "White",
		"y_axis_label" : "$y$",
		"x_tick_frequency" : 10,
		"y_tick_frequency" : 5,
		}

	def construct(self):
		self.setup_axes()
		x = np.array([0,20,40,60,80,100])
		y = np.array([0.89,1.40,2.51,5.37,17.4,24.2])
		p = []
		t = []
		for i in range(0,len(x)):
			p.append(Dot(color = "Blue").move_to(self.coords_to_point(x[i],y[i])))
			str = "(%d,%.2f)" % (x[i],y[i])
			t.append(TexMobject(str,color="Yellow").scale(0.6).next_to(p[i],UP))
			self.play(ShowCreation(p[i]),Write(t[i]),run_time=0.6)

		self.wait(1)
		self.play(Uncreate(VGroup(*t)))
		
		graph = 5*[None]
		textL = 5*[None]

		for i in range(0,5):
			pp = np.polyfit(x[0:i+2],y[0:i+2],i+1)
			graph[i] = self.get_graph(lambda x : np.polyval(pp,x),color = BLUE,
					x_min = 0,x_max = 100)
			text = "Interpolaci\\'on con $p \\in \\mathbb{P}_%d$" % (i+1)
			textL[i] = TextMobject(text,color="Yellow").move_to(TOP+DOWN)
			if i == 0:
				self.play(ShowCreation(graph[i]),ShowCreation(textL[i]))
				self.wait()
			else:
				self.play(ReplacementTransform(graph[i-1],graph[i]),
					ReplacementTransform(textL[i-1],textL[i]))
				self.wait()

		spline = interpolate.splrep(x,y)
		sgraph = self.get_graph(lambda s : interpolate.splev(s,spline),
			x_min = 0 , x_max = 100,color = "Red")
		stext = TextMobject("Spline cubica",color = "Yellow").move_to(TOP+DOWN)
		self.play(ReplacementTransform(graph[4],sgraph),
			ReplacementTransform(textL[4],stext))
		self.wait()

class InterpolacionThird(GraphScene):
	CONFIG = {
		"x_max" : 10,
		"x_min" : 0,
		"y_max" : 20,
		"y_min" : 0	,
		"axes_color" : "White",
		"y_axis_label" : "$y$",
		"x_tick_frequency" : 1,
		"y_tick_frequency" : 2,
		}

	def construct(self):
		self.setup_axes(animate=True)
		x = np.array([2, 4, 6, 8])
		y = np.array([2, 7, 8, 10])
		p = []
		t = []
		for i in range(0,len(x)):
			p.append(Dot(color = "#30BCED").move_to(self.coords_to_point(x[i],y[i])))
			self.play(ShowCreation(p[i]),run_time=0.6)

		self.wait(1)
		
		graph = []
		textL = []

		for i in range(0,len(x)-1):
			pp = np.polyfit(x,y,i+1)
			graph.append(self.get_graph(lambda x : np.polyval(pp,x),color = "Yellow",
					x_min = 0,x_max = 10))
			if i == 0:
				self.play(ShowCreation(graph[i]))
				self.wait()
			else:
				self.play(ReplacementTransform(graph[i-1],graph[i]))
				self.wait()
		self.play(Uncreate(graph[-1]))
				
		pnew = []
		ynew = 2*x
		for i in range(0,len(x)):
			pnew.append(Dot(color = "#30BCED").move_to(self.coords_to_point(x[i],ynew[i])))
			self.play(Transform(p[i],pnew[i]),run_time=0.2)
		pp = np.polyfit(x,ynew,len(x)-1)
		graph.append(self.get_graph(lambda x : np.polyval(pp,x),color = "Yellow",
					x_min = 0,x_max = 10))
		self.play(ShowCreation(graph[-1]))
		self.wait()
		
		ynew = np.append(ynew,30)
		x = np.append(x,10)
		pp = np.polyfit(x,ynew,len(x)-1)
		graph.append(self.get_graph(lambda x : np.polyval(pp,x),color = "Yellow",
					x_min = 0,x_max = 10))
		self.play(ReplacementTransform(graph[-2],graph[-1]))
		self.wait()
		
		ynew[-1] = -1
		pp = np.polyfit(x,ynew,len(x)-1)
		graph.append(self.get_graph(lambda x : np.polyval(pp,x),color = "Yellow",
					x_min = 0,x_max = 10))
		self.play(ReplacementTransform(graph[-2],graph[-1]))
		self.wait()
	
