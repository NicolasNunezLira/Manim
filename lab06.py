#!/usr/bin/env python

from manimlib.imports import *
from scipy import interpolate

class Piston(GraphScene):
	CONFIG = {  
		"H": 2,  # Box in C + [-W/2, W/2] x [-H/2, H/2]
		"n_particles": 10,
		"m1": 1,
		"r1": 0.05,
		"max_v": 5,
		"random_seed": 2,
		"graph_origin": 2.5*DOWN+4*LEFT,
		"y_max" : 1500,
        "y_min" : 0,
        "x_max" : 1.5,
        "x_min" : 0,
        "y_tick_frequency" : 300,
        "x_tick_frequency" : 0.25,
		"y_axis_height": 3,
		"y_labeled_nums": range(0,1500,300),
		"x_labeled_nums": list(np.arange(0,1.5,.25)),
		"x_label_decimal": 2,
        "axes_color" : BLUE,
		"y_axis_label" : "$p$",
		"x_axis_label" : "$V$"
	}
	def construct(self):
		# Cilindro (parte izquierda)
		l = []
		l.append(Line(UP,DOWN))
		l.append(Line(DOWN,DOWN+2*RIGHT))
		l.append(Line(UP,UP+2*RIGHT))
		l.append(Line(ORIGIN,2*LEFT))
		L = VGroup(*l)
		
		# Disco (parte derecha)
		r = []
		v = 0.5;
		r.append(Line(v*RIGHT+.95*UP,v*RIGHT+.95*DOWN))
		r.append(Line(v*RIGHT,(v+1)*RIGHT))
		R = VGroup(*r)
		
		# Piston
		P = VGroup(R,L)
		
		# Le pasamos el disco y la base del cilindro a self para usarla en update_particle
		self.R = R[1]
		self.L = L[0]
		
		# Animaciones
		self.play(ShowCreation(L),ShowCreation(R))
		self.add_particles()
		self.wait(15)
		self.play(P.shift,3*LEFT+2*UP,run_time=1)
		self.wait(2)
		
		# Texto
		eq = TexMobject("W = ", " ", "F", "\Delta x").move_to(2*UP+2.5*RIGHT)
		eq2 = TexMobject("W = ", "\int_{x_i}^{x_f}", " ", "F","\mbox{d}x").move_to(eq.get_center())
		eq3 = TexMobject("W = ", "\int_{x_i}^{x_f}", "\int_{A(x)}", "p", "\mbox{d}A\mbox{d}x").move_to(eq.get_center())
		eq4 = TexMobject("W = ", "\int_{V_i}^{V_f}", " ", "p(V)", "\mbox{d}V").move_to(eq.get_center())

		self.play(Write(eq))
		self.wait(7)
		self.play(ReplacementTransform(eq,eq2))
		self.wait(15)
		self.play(ReplacementTransform(eq2,eq3))
		self.wait(8)
		self.play(ReplacementTransform(eq3,eq4))
		self.play(ShowCreation(SurroundingRectangle(eq4)))
		self.wait(16)
		self.setup_axes(animate=True)
		self.wait(3)
		
		# Puntos
		V_vals = np.array([0.5, 0.6, 0.72, 0.84, 0.96, 1.08, 1.25])
		p_vals = np.array([1400, 1248, 1100, 945, 802, 653, 500])
		
		pv = []
		labels = []
		for i in range(0,len(V_vals)):
			pv.append(Dot(color = "#30bced").scale(0.5).move_to(self.coords_to_point(V_vals[i],p_vals[i])))
			str = "(%.2f,%.0f)" % (V_vals[i],p_vals[i])
			labels.append(TexMobject(str,color="#fff07c").scale(0.4).next_to(pv[i],0.4*UP+0.3*RIGHT))
		
		self.play(ShowCreation(pv[0]),Write(labels[0]))
		for i in range(1,len(V_vals)):
			self.play(R.shift,(V_vals[i] - V_vals[i-1])*RIGHT)
			self.play(ShowCreation(pv[i]),Write(labels[i]))
		self.wait(2)
		
		spline = interpolate.splrep(V_vals,p_vals)		
		s_graph = self.get_graph(lambda s : interpolate.splev(s,spline), x_min = 0.5 , x_max = 1.25,color = "#fff07c")
		s_area = self.get_area(s_graph,0.5,1.25)
		
		self.play(ShowCreation(s_graph),ShowCreation(s_area))
		self.wait(3)
		
	def add_particles(self):
		m1 = self.m1
		r1 = self.r1
		H = self.H
		C = (self.R.get_left() + self.L.get_right())/2
		W = (self.R.get_left() - self.L.get_right())
		max_v = self.max_v
		n_particles = self.n_particles

		lil_particles = VGroup(*[
			self.get_particle(m1, r1, H, W, C, max_v)
			for k in range(n_particles)
		])

		all_particles = VGroup(*lil_particles)
		all_particles.add_updater(self.update_particles)

		self.add(all_particles)
		self.particles = all_particles

	def get_particle(self, m, r, H, W, C, max_v):
		dot = Dot(radius=r)
		dot.set_fill("#30bced", 0.7)
		dot.mass = m
		dot.radius = r
		dot.center = C + op.add(
			np.random.uniform(-W + r, W - r) * RIGHT,
			np.random.uniform(-H + r, H - r) * UP
		)
		dot.move_to(dot.center)
		dot.velocity = rotate_vector(
			np.random.uniform(0, max_v) * RIGHT,
			np.random.uniform(0, TAU),
		)
		return dot

	def update_particles(self, particles, dt):
		for p1 in particles:
			p1.center += p1.velocity * dt

			# Check particle collisions
			buff = 0.02
			for p2 in particles:
				if p1 is p2:
					continue
				v = p2.center - p1.center
				dist = get_norm(v)
				r_sum = p1.radius + p2.radius
				diff = dist - r_sum
				if diff < 0:
					unit_v = v / dist
					p1.center += (diff - buff) * unit_v / 2
					p2.center += -(diff - buff) * unit_v / 2
					u1 = p1.velocity
					u2 = p2.velocity
					m1 = p1.mass
					m2 = p2.mass
					v1 = (
						(m2 * (u2 - u1) + m1 * u1 + m2 * u2) /
						(m1 + m2)
					)
					v2 = (
						(m1 * (u1 - u2) + m1 * u1 + m2 * u2) /
						(m1 + m2)
					)
					p1.velocity = v1
					p2.velocity = v2

			# Check edge collisions
			r1 = p1.radius
			c1 = p1.center
			C = (self.R.get_left() + self.L.get_right())/2
			W = (self.R.get_left() - self.L.get_right())
			D = [W[0], self.H]
			for i in [0, 1]:
				if abs(c1[i] - C[i]) + r1 > D[i]/2:
					c1[i] = C[i] + np.sign(c1[i] - C[i]) * (D[i]/2 - r1)
					p1.velocity[i] *= -1 * op.mul(
						np.sign(p1.velocity[i]),
						np.sign(c1[i] - C[i])
					)
					
		for p in particles:
			p.move_to(p.center)
		return particles