from manimlib.imports import *

#    __                  _   _                 
#   / _|_   _ _ __   ___| |_(_) ___  _ __  ___ 
#  | |_| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
#  |  _| |_| | | | | (__| |_| | (_) | | | \__ \
#  |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/

# This function returns data from .csv to an array
def get_coords_from_csv(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            x,y = row
            coord = [float(x),float(y)]
            coords.append(coord)
    csvFile.close()
    return coords
# LEARN MORE HERE:
# https://www.youtube.com/watch?v=Xi52tx6phRU


#        _         _                  _   
#   __ _| |__  ___| |_ _ __ __ _  ___| |_ 
#  / _` | '_ \/ __| __| '__/ _` |/ __| __|
# | (_| | |_) \__ \ |_| | | (_| | (__| |_ 
#  \__,_|_.__/|___/\__|_|  \__,_|\___|\__|
#   ___  ___ ___ _ __   ___  ___ 
#  / __|/ __/ _ \ '_ \ / _ \/ __|
#  \__ \ (_|  __/ | | |  __/\__ \
#  |___/\___\___|_| |_|\___||___/
# Abstract scenes



class IntroLeastSquares(GraphScene):
    CONFIG = {
    "x_min" : -2,
    "x_max" : 2,
    "y_min" : -2,
    "y_max" : 2,
    "graph_origin" : ORIGIN ,
    "function_color" : RED ,
    "axes_color" : GREEN,
    "x_labeled_nums" :range(-2,3,1), 
    "y_labeled_nums" :range(-1,2,1),    
    }

     # Covert the data coords to the graph points
    def get_points_from_coords(self,coords):
        return [
            # Convert COORDS -> POINTS
            self.coords_to_point(px,py)
            # See manimlib/scene/graph_scene.py
            for px,py in coords
        ]
         # Return the dots of a set of points
    def get_dots_from_coords(self,coords,radius=0.15):
        points = self.get_points_from_coords(coords)
        dots = VGroup(*[
            Dot(radius=radius).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots
   

    def construct(self):

        intro_text = TextMobject('Mínimos Cuadrados', color = BLUE)
        intro_text2 = TextMobject('Idea Principal', color = RED)
        intro_text2.next_to(intro_text,2*DOWN)

        self.play(Write(intro_text))
        self.play(Write(intro_text2))
        self.wait(1)
        self.play(FadeOut(intro_text),FadeOut(intro_text2))

        self.setup_axes(animate=True)
        func_graph1=self.get_graph(self.p1,self.function_color)
  
        x1 = [-1, 1]
        y1 = [-1,1]
        coords1= [[px,py] for px,py in zip(x1,y1)]
        points1 = self.get_points_from_coords(coords1)
        dots1 = self.get_dots_from_coords(coords1)
       
        # Create TextMobjects
        first_text = TextMobject('A dos puntos distintos')
        first_text.scale(0.8)
        first_text.to_edge(2*DOWN+3*RIGHT)
        second_text = TextMobject('los interpola un polinomio de grado a lo más 1', color= RED)
        second_text.scale(0.8)
        second_text.to_edge(DOWN+3*RIGHT)        

        self.wait(1)
        self.add(dots1)
        self.play(Write(first_text))
        self.play(FadeOut(first_text))
        self.wait(1)        
        self.play(ShowCreation(func_graph1))
        self.play(Write(second_text))
        self.wait(1)
        self.play(FadeOut(dots1),FadeOut(func_graph1),FadeOut(second_text))

   
        # Create TextMobjects
        first_text = TextMobject('A tres puntos distintos')
        first_text.scale(0.8)
        first_text.to_edge(2*DOWN+3*RIGHT)
        second_text = TextMobject('los interpola un polinomio de grado a lo más 2', color= RED)
        second_text.scale(0.8)
        second_text.to_edge(DOWN+3*RIGHT)        

        func_graph2=self.get_graph(self.p2,self.function_color)
       
        x2 = [-1, 0, 1]
        y2 = [ 0,-1,0 ]
        coords2= [[px,py] for px,py in zip(x2,y2)]
        points2 = self.get_points_from_coords(coords2)
        dots2 = self.get_dots_from_coords(coords2)

        self.wait(1)
        self.add(dots2)
        self.play(Write(first_text))
        self.play(FadeOut(first_text))
        self.wait(1)        
        self.play(ShowCreation(func_graph2))
        self.play(Write(second_text))
        self.wait(3)
        self.play(FadeOut(dots2),FadeOut(func_graph2),FadeOut(second_text))

         # Create TextMobjects
        first_text = TextMobject('A cuatro puntos distintos')
        first_text.scale(0.8)
        first_text.to_edge(2*DOWN+3*RIGHT)
        second_text = TextMobject('los interpola un polinomio de grado a lo más 3', color= RED)
        second_text.scale(0.8)
        second_text.to_edge(DOWN+3*RIGHT)        
    
        func_graph3=self.get_graph(self.p3,self.function_color)
       
        x3 =  [ -1,-1/2,1/2,1]
        y3 = self.p3(x3)
        coords3= [[px,py] for px,py in zip(x3,y3)]
        points3 = self.get_points_from_coords(coords3)
        dots3 = self.get_dots_from_coords(coords3)

        self.wait(1)
        self.add(dots3)
        self.play(Write(first_text))
        self.play(FadeOut(first_text))
        self.wait(1)        
        self.play(ShowCreation(func_graph3))
        self.play(Write(second_text))
        self.wait(1)
        self.play(FadeOut(dots3),FadeOut(func_graph3),FadeOut(second_text))


         # Create TextMobjects
        first_text= TextMobject('¿Qué pasa si tenemos 3 puntos')
        first_text .scale(0.8)
        first_text.to_edge(2*UP+LEFT)
        second_text = TextMobject('y queremos')
        secondB_text = TextMobject('\\textit{ajustar}', color= GREEN)
        secondC_text = TextMobject(' un polinomio de grado 1?', color= RED)
        second_text.scale(0.8)
        second_text.next_to(first_text,DOWN)
        secondB_text.scale(0.8)
        secondB_text.next_to(second_text,DOWN)
        secondC_text.scale(0.8)
        secondC_text.next_to(secondB_text,DOWN)

        third_text= TextMobject('¿Con cuál estas \\textit{infinitas}')
        third_text .scale(0.8)
        third_text.to_edge(3*DOWN+3*RIGHT)
        fourth_text = TextMobject('rectas', color= RED)
        fourth_text.scale(0.8)
        fourth_text.next_to(third_text,DOWN)


        fourthB_text = TextMobject('nos quedamos?')
        fourthB_text.scale(0.8)
        fourthB_text.next_to(fourth_text,DOWN)



        thirdB_text= TextMobject('!Hay \\textit{infinitas}')
        thirdB_text .scale(0.8)
        thirdB_text.to_edge(3*DOWN+3*RIGHT)
        thirdC_text = TextMobject('rectas!', color= RED)
        thirdC_text.scale(0.8)
        thirdC_text.next_to(thirdB_text,DOWN)



        self.wait(1)
        self.add(dots2)
        self.play(Write(first_text))
        self.play(Write(second_text))
        self.play(Write(secondB_text))
        self.play(Write(secondC_text))
  


        self.play(Write(thirdB_text))
        self.play(Write(thirdC_text))
   


        #func_graph1a=self.get_graph(self.p1a,self.function_color)
        #self.play(ShowCreation(func_graph1a))
        #self.wait(1)
        #self.play(FadeOut(func_graph1a)) 

        #func_graph1b=self.get_graph(self.p1b,self.function_color)
        #self.play(ShowCreation(func_graph1b))
        #self.wait(1)
        #self.play(FadeOut(func_graph1b)) 

        #func_graph1c=self.get_graph(self.p1c,self.function_color)
        #self.play(ShowCreation(func_graph1c))
        #self.wait(1)
        #self.play(FadeOut(func_graph1c))         

        #self.play(FadeOut(thirdB_text),FadeOut(thirdC_text)) 

        vec = np.array([-10,-4,-2, -1,-1/2, -1/8, 0,1/8,1/2,1, 2,4,10])
        for m in vec:
            func_graph1general=self.get_graph2(self.p1general,m,self.function_color)
            self.play(WriteC(func_graph1general))
            self.play(FadeOut(func_graph1general)) 

        for mm in range(-10,10,3):
            m = mm/10 
            func_graph1general=self.get_graph2(self.p1general2,m,self.function_color)
            self.play(WriteC(func_graph1general))
            self.play(FadeOut(func_graph1general)) 
            
            
        self.play(FadeOut(thirdB_text),FadeOut(thirdC_text)) 
        #self.play(ShowCreation(func_graph1),ShowCreation(func_graph1a),ShowCreation(func_graph1b),ShowCreation(func_graph1c))
        self.play(Write(third_text))
        self.play(Write(fourth_text))
        self.play(Write(fourthB_text))
       
       
    def p1(self,x):
        return x
    def p2(self,x):
        return x**2-1    
    def p3(self,x):
        return np.power(x,3)    
    def p1a(self,x):
        return -x
    def p1b(self,x):
        return 1/2
        return -x
    def p1c(self,x):
        return -1/2
    def p1general(self,x,m):
        return m*x   
    def p1general2(self,x,m):
        return m   




class GraphFromData(GraphScene):

     # Covert the data coords to the graph points
    def get_points_from_coords(self,coords):
        return [
            # Convert COORDS -> POINTS
            self.coords_to_point(px,py)
            # See manimlib/scene/graph_scene.py
            for px,py in coords
        ]

    # Return the dots of a set of points
    def get_dots_from_coords(self,coords,radius=0.1):
        points = self.get_points_from_coords(coords)
        dots = VGroup(*[
            Dot(radius=radius).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots

#       _                         
#   ___| | __ _ ___ ___  ___  ___ 
#  / __| |/ _` / __/ __|/ _ \/ __|
# | (__| | (_| \__ \__ \  __/\__ \
#  \___|_|\__,_|___/___/\___||___/
# This classes returns graphs
class DiscreteGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners(set_of_points)

class SmoothGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_smoothly(set_of_points)

#   ___  ___ ___ _ __   ___  ___ 
#  / __|/ __/ _ \ '_ \ / _ \/ __|
#  \__ \ (_|  __/ | | |  __/\__ \
#  |___/\___\___|_| |_|\___||___/
# Graph with set of points
class CustomGraph1(GraphFromData):
    def construct(self):
        self.setup_axes()
        coords = get_coords_from_csv("custom_graphs/data")
        dots = self.get_dots_from_coords(coords)
        self.add(dots)

# Discrete Graph
class CustomGraph2(GraphFromData):
    def construct(self):
        self.setup_axes()
        # Get coords
        # coords = get_coords_from_csv("custom_graphs/data")
        x = [0, 1]
        y = [2, 2]
        coords = [[px,py] for px,py in zip(x,y)]
        points = self.get_points_from_coords(coords)
        # Set graph
        #graph = DiscreteGraphFromSetPoints(points,color=ORANGE)
        # Set dots
        dots = self.get_dots_from_coords(coords)
        self.add(dots)
        #self.play(ShowCreation(graph,run_time=4))
        self.wait(3)

# Smooth graph
class CustomGraph3(GraphFromData):
    CONFIG = {
        "y_max": 25,
    }
    def construct(self):
        self.setup_axes()
        x = [0 , 1, 2, 3,  4,  5,  6,  7]
        y = [0 , 1, 4, 9, 16, 25, 20, 10]

        coords = [[px,py] for px,py in zip(x,y)]
        # |
        # V
        points = self.get_points_from_coords(coords)
        
        graph = SmoothGraphFromSetPoints(points,color=GREEN)
        dots = self.get_dots_from_coords(coords)

        self.add(graph,dots)

# But, we can do the same thing with a simple SCENE
class CustomGraph4(Scene):
    def construct(self):
        axes = Axes()
        x = [0 , 1, 2, 3,  4, 5,  6]
        y = [0 , 1, 0, -1, 0,  1, 0]

        coords = [[px,py] for px,py in zip(x,y)]
        # |
        # V
        points = self.get_points_from_coords(axes,coords)

        dots = self.get_dots_from_coords(axes,coords)
        graph = SmoothGraphFromSetPoints(points,color=GREEN)

        self.add(axes,graph,dots)

    def get_points_from_coords(self,axes,coords):
        return [axes.coords_to_point(px,py)
            for px,py in coords
            ]

    # Return the dots of a set of points
    def get_dots_from_coords(self,axes,coords,radius=0.1):
        points = self.get_points_from_coords(axes,coords)
        dots = VGroup(*[
            Dot(radius=radius).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots

        
#               ____          _____ ____  
#              | __ ) _   _  |_   _| __ ) 
#              |  _ \| | | |   | | |  _ \ 
#              | |_) | |_| |   | | | |_) |
#              |____/ \__, |   |_| |____/ 
#                     |___/   



class LeastSquaresPart1(GraphScene2):
    CONFIG = {
    "x_min" : -2,
    "x_max" : 2,
    "y_min" : -2,
    "y_max" : 2,
    "graph_origin" : ORIGIN ,
    "function_color" : RED ,
    "axes_color" : BLACK,
    }

     # Covert the data coords to the graph points
    def get_points_from_coords(self,coords):
        return [
            # Convert COORDS -> POINTS
            self.coords_to_point(px,py)
            # See manimlib/scene/graph_scene.py
            for px,py in coords
        ]

    # Return the dots of a set of points
    def get_dots_from_coords(self,coords,radius,color):
        points = self.get_points_from_coords(coords)
        dots = VGroup(*[
            Dot(radius=radius,color=color).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots
   

    def construct(self):
        self.setup_axes(animate=False)    
        # First animation
        func_graph1=self.get_graph(self.p1,self.function_color)
       
        x0 = [-1]
        x1 = [0]
        x2 = [1]

        y0 = [0]
        y1 = [-2]
        y2 = [1]  

        coord0= [[px,py] for px,py in zip(x0,y0)]
        coord1= [[px,py] for px,py in zip(x1,y1)]
        coord2= [[px,py] for px,py in zip(x2,y2)]

        
        points0 = self.get_points_from_coords(coord0)
        points1 = self.get_points_from_coords(coord1)
        points2 = self.get_points_from_coords(coord2)


        dots0 = self.get_dots_from_coords(coord0,0.1,WHITE)
        dots1 = self.get_dots_from_coords(coord1,0.1,WHITE)
        dots2 = self.get_dots_from_coords(coord2,0.1,WHITE)

        text_dots0 = TextMobject('$(x_0,y_0)$')
        text_dots0.next_to(dots0,UP)
        text_dots1 = TextMobject('$(x_1,y_1)$')
        text_dots1.next_to(dots1,DOWN)        
        text_dots2 = TextMobject('$(x_2,y_2)$')
        text_dots2.next_to(dots2,UP)

        text_fx = TexMobject('f(','x',')','=','c_0','+','c_1','x')
        text_fx.set_color_by_tex('f',RED)
        text_fx.set_color_by_tex('x',WHITE)
        text_fx.set_color_by_tex(')',RED)
        text_fx.set_color_by_tex('=',BLUE)
        text_fx.set_color_by_tex('+',BLUE)
        text_fx.set_color_by_tex('c',GREEN)

        text_fx.move_to(3*DOWN+4.5*LEFT)          
      

        self.add(dots0,dots1,dots2)
        self.add(text_dots0,text_dots1,text_dots2)  
        self.play(ShowCreation(func_graph1),Write(text_fx))
   
        # Second animation    
        z0 = [self.p1(x0[0])]
        z1 = [self.p1(x1[0])]
        z2 = [self.p1(x2[0])]  
         
        coord0z= [[px,py] for px,py in zip(x0,z0)]
        coord1z= [[px,py] for px,py in zip(x1,z1)]
        coord2z= [[px,py] for px,py in zip(x2,z2)]

        
        points0z = self.get_points_from_coords(coord0z)
        points1z = self.get_points_from_coords(coord1z)
        points2z = self.get_points_from_coords(coord2z)


        dots0z = self.get_dots_from_coords(coord0z,0.1,GREEN)
        dots1z = self.get_dots_from_coords(coord1z,0.1,GREEN)
        dots2z = self.get_dots_from_coords(coord2z,0.1,GREEN)

        text_dots0z = TexMobject('(','x_0','f(','x_0',')',')')
        text_dots0z[4].set_color(RED)
        text_dots0z[5].set_color(GREEN)
        text_dots0z.set_color_by_tex('(', GREEN)
        text_dots0z.set_color_by_tex('f(', RED)
        text_dots0z.set_color_by_tex('y', WHITE)
        text_dots0z.set_color_by_tex('x', WHITE)
        text_dots0z.set_color_by_tex('-', BLUE)
        text_dots0z.next_to(dots0z,DOWN)


        text_dots1z = TexMobject('(','x_1','f(','x_1',')',')')
        text_dots1z[4].set_color(RED)
        text_dots1z[5].set_color(GREEN)
        text_dots1z.set_color_by_tex('(', GREEN)
        text_dots1z.set_color_by_tex('f(', RED)
        text_dots1z.set_color_by_tex('y', WHITE)
        text_dots1z.set_color_by_tex('x', WHITE)
        text_dots1z.set_color_by_tex('-', BLUE)        
        text_dots1z.next_to(dots1z,UP) 


        text_dots2z = TexMobject('(','x_2','f(','x_2',')',')')
        text_dots2z[4].set_color(RED)
        text_dots2z[5].set_color(GREEN)
        text_dots2z.set_color_by_tex('(', GREEN)
        text_dots2z.set_color_by_tex('f(', RED)
        text_dots2z.set_color_by_tex('y', WHITE)
        text_dots2z.set_color_by_tex('x', WHITE)
        text_dots2z.set_color_by_tex('-', BLUE)
        text_dots2z.next_to(dots2z,DOWN)          
      
        self.wait(2)
        self.add(dots0z,dots1z,dots2z)
        self.add(text_dots0z,text_dots1z,text_dots2z)  
        self.play(Write(text_dots0z))


        text_r0=TexMobject('y_0','-','f(','x_0',')','=:r_0')
        text_r0[2].set_color(RED)
        text_r0[4].set_color(RED)
        text_r0.set_color_by_tex('r', BLUE)
        text_r0.set_color_by_tex('y', WHITE)
        text_r0.set_color_by_tex('-', BLUE)


        text_r0.move_to(4.5*LEFT+0.6*DOWN)


        text_r1=TexMobject('r_1:=','y_1','-','f(','x_1',')')
        text_r1[3].set_color(RED)
        text_r1[5].set_color(RED)
        text_r1.set_color_by_tex('r', BLUE)
        text_r1.set_color_by_tex('y', WHITE)
        text_r1.set_color_by_tex('-', BLUE)
        text_r1.move_to(2*DOWN+2*RIGHT)

        text_r2=TexMobject('r_2:=','y_2','-','f(','x_2',')')
        text_r2[3].set_color(RED)
        text_r2[5].set_color(RED)
        text_r2.set_color_by_tex('r', BLUE)
        text_r2.set_color_by_tex('y', WHITE)
        text_r2.set_color_by_tex('-', BLUE)
        text_r2.move_to(1.2*UP+4.5*RIGHT)

        vert_line0 = self.get_vertical_line_to_graph(-1,0,func_graph1,color=BLUE)
        vert_line1 = self.get_vertical_line_to_graph(0,-2,func_graph1,color=BLUE)
        vert_line2 = self.get_vertical_line_to_graph(1,1,func_graph1,color=BLUE)


        self.play(Write(text_r0),Write(text_r1),Write(text_r2),ShowCreation(vert_line0),ShowCreation(vert_line1),ShowCreation(vert_line2))

        self.play(FadeOut(func_graph1),FadeOut(text_fx),\
                  FadeOut(text_dots0),FadeOut(text_dots1),FadeOut(text_dots2),\
                  FadeOut(text_dots0z),FadeOut(text_dots1z),FadeOut(text_dots2z))


        # Third animation   

        #  (x0,y0)

        text_r0new=TexMobject('r_0:=','y_0','-','f(','x_0',')')
        text_r0new[3].set_color(RED)
        text_r0new[5].set_color(RED)
        text_r0new.set_color_by_tex('r', BLUE)
        text_r0new.set_color_by_tex('y', WHITE)
        text_r0new.set_color_by_tex('-', BLUE)        
      
        
        for pos,formula in [(4.5*LEFT+0.6*DOWN,text_r0),(5*LEFT+3*UP,text_r0new)]:
            #formula.scale(size)
            formula.move_to(pos)
        self.wait()
        changes = [
			[(0,1,2,3,4,5),
			# | | | | |
			# v v v v v
			 (1,2,3,4,5,0)],
        ]
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    text_r0[i].copy(),text_r0new[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=1
            )

        #  (x1,y1)
        text_r1new=TexMobject('r_1:=','y_1','-','f(','x_1',')')
        text_r1new[3].set_color(RED)
        text_r1new[5].set_color(RED)
        text_r1new.set_color_by_tex('r', BLUE)
        text_r1new.set_color_by_tex('y', WHITE)
        text_r1new.set_color_by_tex('-', BLUE)        
      
      
        
        for pos,formula in [(2*DOWN+2*RIGHT,text_r1),(5*LEFT+2*UP,text_r1new)]:
            #formula.scale(size)
            formula.move_to(pos)
        changes = [
			[(0,1,2,3,4,5),
			# | | | | |
			# v v v v v
			 (0,1,2,3,4,5)],
        ]
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    text_r1[i].copy(),text_r1new[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=1
            )
           
     #  (x2,y2)
        text_r2new=TexMobject('r_2:=','y_2','-','f(','x_2',')')
        text_r2new[3].set_color(RED)
        text_r2new[5].set_color(RED)
        text_r2new.set_color_by_tex('r', BLUE)
        text_r2new.set_color_by_tex('y', WHITE)
        text_r2new.set_color_by_tex('-', BLUE)    
      
        
        for pos,formula in [(1.2*UP+4.5*RIGHT,text_r2),(5*LEFT+UP,text_r2new)]:
            #formula.scale(size)
            formula.move_to(pos)
        changes = [
			[(0,1,2,3,4,5),
			# | | | | |
			# v v v v v
			 (0,1,2,3,4,5)],
        ]
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    text_r2[i].copy(),text_r2new[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=1
            )

        self.play(FadeOut(text_r0),FadeOut(text_r1),FadeOut(text_r2),\
            FadeOut(vert_line0),FadeOut(vert_line1),FadeOut(vert_line2),\
            FadeOut(dots0z),FadeOut(dots1z),FadeOut(dots2z),\
            FadeOut(dots0),FadeOut(dots1),FadeOut(dots2))    

         # Third animation        
        text_fx = TexMobject('f(','x',')','=','c_0','+','c_1','x')
        text_fx.set_color_by_tex('f',RED)
        text_fx.set_color_by_tex('x',WHITE)
        text_fx.set_color_by_tex(')',RED)
        text_fx.set_color_by_tex('=',BLUE)
        text_fx.set_color_by_tex('+',BLUE)
        text_fx.set_color_by_tex('c',GREEN)
        como = TexMobject('\\textrm{como }',color=WHITE)
        como.next_to(text_fx,LEFT)
        text_fx = VGroup(como,text_fx)
        text_fx.bg=SurroundingRectangle(text_fx,color=RED,fill_color=RED, fill_opacity=0)
        text_fx = VGroup(text_fx.bg,text_fx)

        text_fx.move_to(2*UP+4*RIGHT)      
        self.play(Write(text_fx))
        self.wait(2)

        #  (x0,y0)
        text_r0new3=TexMobject('=','y_0','-','(','c_0','+','c_1', 'x_0',')')
        text_r0new3.set_color_by_tex('=', BLUE)
        text_r0new3.set_color_by_tex('+', BLUE)
        text_r0new3.set_color_by_tex('(', BLUE)
        text_r0new3.set_color_by_tex(')', BLUE)
        text_r0new3.set_color_by_tex('y', WHITE)
        text_r0new3.set_color_by_tex('x', WHITE)
        text_r0new3.set_color_by_tex('-', BLUE)
        text_r0new3.set_color_by_tex('c', GREEN) 
        text_r0new3.move_to(1.2*LEFT+3*UP)
        self.play(Write(text_r0new3))

         #  (x1,y1)
        text_r1new3=TexMobject('=','y_1','-','(','c_0','+','c_1', 'x_1',')')
        text_r1new3.set_color_by_tex('=', BLUE)
        text_r1new3.set_color_by_tex('+', BLUE)
        text_r1new3.set_color_by_tex('(', BLUE)
        text_r1new3.set_color_by_tex(')', BLUE)
        text_r1new3.set_color_by_tex('y', WHITE)
        text_r1new3.set_color_by_tex('x', WHITE)
        text_r1new3.set_color_by_tex('-', BLUE)
        text_r1new3.set_color_by_tex('c', GREEN) 
        text_r1new3.move_to(1.2*LEFT+2*UP)
        self.play(Write(text_r1new3))    

           #  (x2,y2)
        text_r2new3=TexMobject('=','y_2','-','(','c_0','+','c_1', 'x_2',')')
        text_r2new3.set_color_by_tex('=', BLUE)
        text_r2new3.set_color_by_tex('+', BLUE)
        text_r2new3.set_color_by_tex('(', BLUE)
        text_r2new3.set_color_by_tex(')', BLUE)
        text_r2new3.set_color_by_tex('y', WHITE)
        text_r2new3.set_color_by_tex('x', WHITE)
        text_r2new3.set_color_by_tex('-', BLUE)
        text_r2new3.set_color_by_tex('c', GREEN)  
        text_r2new3.move_to(1.2*LEFT+UP)
        self.play(Write(text_r2new3))  

        
    def p1(self,x):
        return -1/3+x*0.5    
  




class LeastSquaresPart2(GraphScene2):
    CONFIG = {
    "x_min" : -2,
    "x_max" : 2,
    "y_min" : -2,
    "y_max" : 2,
    "graph_origin" : ORIGIN ,
    "function_color" : RED ,
    "axes_color" : BLACK,
    }

     # Covert the data coords to the graph points
    def get_points_from_coords(self,coords):
        return [
            # Convert COORDS -> POINTS
            self.coords_to_point(px,py)
            # See manimlib/scene/graph_scene.py
            for px,py in coords
        ]

    # Return the dots of a set of points
    def get_dots_from_coords(self,coords,radius,color):
        points = self.get_points_from_coords(coords)
        dots = VGroup(*[
            Dot(radius=radius,color=color).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots
   

    def construct(self):
        self.setup_axes(animate=False)            


        # Previous animations
        text_fx = TexMobject('f(','x',')','=','c_0','+','c_1','x')
        text_fx.set_color_by_tex('f',RED)
        text_fx.set_color_by_tex('x',WHITE)
        text_fx.set_color_by_tex(')',RED)
        text_fx.set_color_by_tex('=',BLUE)
        text_fx.set_color_by_tex('+',BLUE)
        text_fx.set_color_by_tex('c',GREEN)
        como = TexMobject('\\textrm{como }',color=WHITE)
        como.next_to(text_fx,LEFT)
        text_fx = VGroup(como,text_fx)
        text_fx.bg=SurroundingRectangle(text_fx,color=RED,fill_color=RED, fill_opacity=0)
        text_fx = VGroup(text_fx.bg,text_fx)
        text_fx.move_to(3*DOWN+4.5*LEFT)     
        text_fx.move_to(2*UP+4*RIGHT)     


        #  (x0,y0)
        text_r0new=TexMobject('r_0:=','y_0','-','f(','x_0',')') 
        text_r0new[3].set_color(RED) 
        text_r0new[5].set_color(RED) 
        text_r0new.set_color_by_tex('r', BLUE) 
        text_r0new.set_color_by_tex('y', WHITE) 
        text_r0new.set_color_by_tex('-', BLUE) 
        text_r0new.move_to(5*LEFT+3*UP)

        text_r0new3=TexMobject('=','y_0','-','(','c_0','+','c_1', 'x_0',')') 
        text_r0new3.set_color_by_tex('=', BLUE) 
        text_r0new3.set_color_by_tex('+', BLUE) 
        text_r0new3.set_color_by_tex('(', BLUE) 
        text_r0new3.set_color_by_tex(')', BLUE) 
        text_r0new3.set_color_by_tex('y', WHITE) 
        text_r0new3.set_color_by_tex('x', WHITE) 
        text_r0new3.set_color_by_tex('-', BLUE) 
        text_r0new3.set_color_by_tex('c', GREEN)
        text_r0new3.move_to(1.2*LEFT+3*UP)

        text_r0 = TexMobject('r_0','\phantom{.}',color=BLUE)
        text_r0.move_to(6.545*LEFT+2.95*UP)
        


         #  (x1,y1)

        text_r1new=TexMobject('r_1:=','y_1','-','f(','x_1',')') 
        text_r1new[3].set_color(RED) 
        text_r1new[5].set_color(RED) 
        text_r1new.set_color_by_tex('r', BLUE) 
        text_r1new.set_color_by_tex('y', WHITE) 
        text_r1new.set_color_by_tex('-', BLUE) 
        text_r1new.move_to(5*LEFT+2*UP)

        text_r1new3=TexMobject('=','y_1','-','(','c_0','+','c_1', 'x_1',')') 
        text_r1new3.set_color_by_tex('=', BLUE) 
        text_r1new3.set_color_by_tex('+', BLUE) 
        text_r1new3.set_color_by_tex('(', BLUE) 
        text_r1new3.set_color_by_tex(')', BLUE) 
        text_r1new3.set_color_by_tex('y', WHITE) 
        text_r1new3.set_color_by_tex('x', WHITE) 
        text_r1new3.set_color_by_tex('-', BLUE) 
        text_r1new3.set_color_by_tex('c', GREEN) 
        text_r1new3.move_to(1.2*LEFT+2*UP)

        text_r1 = TexMobject('r_1','\phantom{.}',color=BLUE)
        text_r1.move_to(6.545*LEFT+1.95*UP)

           #  (x2,y2)

        text_r2new=TexMobject('r_2:=','y_2','-','f(','x_2',')') 
        text_r2new[3].set_color(RED) 
        text_r2new[5].set_color(RED) 
        text_r2new.set_color_by_tex('r', BLUE) 
        text_r2new.set_color_by_tex('y', WHITE) 
        text_r2new.set_color_by_tex('-', BLUE) 
        text_r2new.move_to(5*LEFT+UP)

        text_r2new3=TexMobject('=','y_2','-','(','c_0','+','c_1', 'x_2',')') 
        text_r2new3.set_color_by_tex('=', BLUE)
        text_r2new3.set_color_by_tex('+', BLUE) 
        text_r2new3.set_color_by_tex('(', BLUE) 
        text_r2new3.set_color_by_tex(')', BLUE) 
        text_r2new3.set_color_by_tex('y', WHITE) 
        text_r2new3.set_color_by_tex('x', WHITE) 
        text_r2new3.set_color_by_tex('-', BLUE) 
        text_r2new3.set_color_by_tex('c', GREEN) 
        text_r2new3.move_to(1.2*LEFT+UP) 

        text_r2 = TexMobject('r_2','\phantom{.}',color=BLUE)
        text_r2.move_to(6.545*LEFT+0.95*UP)    

        self.play(WriteC(text_fx),\
            WriteC(text_r0new),WriteC(text_r0new3),WriteC(text_r0),\
            WriteC(text_r1new),WriteC(text_r1new3),WriteC(text_r1),\
            WriteC(text_r2new),WriteC(text_r2new3),WriteC(text_r2)) 


        # New animation.

        #  (x0,y0)

        text_r0newpos = TexMobject('r_0','\phantom{.}',color=BLUE)
        np=text_r0newpos.move_to(6.545*LEFT+1.4*DOWN)



        for pos,formula in [(6.545*LEFT+2.95*UP,text_r0),(np,text_r0newpos)]:
            #formula.scale(size)
            formula.move_to(pos)
        changes = [
			[(0,1),
			# | | | | |
			# v v v v v
			 (0,1)],
        ]
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    text_r0[i].copy(),text_r0newpos[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=1
            )

        #  (x1,y1)

        text_r1newpos = TexMobject('r_1','\phantom{.}',color=BLUE)
        text_r1newpos.move_to(6.545*LEFT+2*DOWN)


        for pos,formula in [(6.545*LEFT+1.95*UP,text_r1),(6.545*LEFT+2*DOWN,text_r1newpos)]:
            #formula.scale(size)
            formula.move_to(pos)
        changes = [
			[(0,1),
			# | | | | |
			# v v v v v
			 (0,1)],
        ]
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    text_r1[i].copy(),text_r1newpos[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=1
            )

        #  (x2,y2)

        text_r2newpos = TexMobject('r_2','\phantom{.}',color=BLUE)
        text_r2newpos.move_to(6.545*LEFT+2.6*DOWN)


        for pos,formula in [(6.545*LEFT+0.95*UP,text_r2),(6.545*LEFT+2.6*DOWN,text_r2newpos)]:
            #formula.scale(size)
            formula.move_to(pos)
        changes = [
			[(0,1),
			# | | | | |
			# v v v v v
			 (0,1)],
        ]
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    text_r2[i].copy(),text_r2newpos[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=1
            )    

        ################################################################################################
        r =([['r_0'],['r_1'],['r_2']]) 
        rM = matrix_to_mobject(r)
        rM.set_color(BLUE)
        rM.move_to(6*LEFT+2*DOWN)
        rM.scale(0.8)
        self.play(FadeOut(text_r0newpos),FadeOut(text_r1newpos),FadeOut(text_r2newpos))
        self.play(Write(rM)) 

        eq = TexMobject('=',color=BLUE)
        eq.next_to(rM)  
        self.play(Write(eq))   
        ################################################################################################

        #  (x0,y0)

        text_y0 = TexMobject('y_0','\phantom{.}',color=WHITE)
        text_y0.move_to(2.1*LEFT+2.95*UP)

        text_y0newpos = TexMobject('y_0','\phantom{.}',color=WHITE)
        ss=text_y0newpos.next_to(4.45*LEFT+1.4*DOWN)
      


        for pos,formula in [(2.1*LEFT+2.95*UP,text_y0),(ss,text_y0newpos)]:
            #formula.scale(size)
            formula.move_to(pos)
        changes = [
			[(0,1),
			# | | | | |
			# v v v v v
			 (0,1)],
        ]
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    text_y0[i].copy(),text_y0newpos[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=1
            )

        #  (x1,y1)

        text_y1 = TexMobject('y_1','\phantom{.}',color=WHITE)
        text_y1.move_to(2.1*LEFT+1.95*UP)

        text_y1newpos = TexMobject('y_1','\phantom{.}',color=WHITE)
        ss=text_y1newpos.next_to(4.5*LEFT+2*DOWN)
      


        for pos,formula in [(2.2*LEFT+1.95*UP,text_y1),(ss,text_y1newpos)]:
            #formula.scale(size)
            formula.move_to(pos)
        changes = [
			[(0,1),
			# | | | | |
			# v v v v v
			 (0,1)],
        ]
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    text_y1[i].copy(),text_y1newpos[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=1
            )

        #  (x2,y2)

        text_y2 = TexMobject('y_2','\phantom{.}',color=WHITE)
        text_y2.move_to(2.1*LEFT+1.95*UP)

        text_y2newpos = TexMobject('y_2','\phantom{.}',color=WHITE)
        ss=text_y2newpos.next_to(4.5*LEFT+2.7*DOWN)
      


        for pos,formula in [(2.1*LEFT+1.95*UP,text_y2),(ss,text_y2newpos)]:
            #formula.scale(size)
            formula.move_to(pos)
        changes = [
			[(0,1),
			# | | | | |
			# v v v v v
			 (0,1)],
        ]
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    text_y2[i].copy(),text_y2newpos[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=1
            )

        ################################################################################################
        y =([['y_0'],['y_1'],['y_2']]) 
        yM = matrix_to_mobject(y)
        yM.set_color(WHITE)
        yM.move_to(4*LEFT+2*DOWN)
        yM.scale(0.8)
        self.play(FadeOut(text_y0newpos),FadeOut(text_y1newpos),FadeOut(text_y2newpos))
        self.play(Write(yM)) 

        plus = TexMobject('-',color=BLUE)
        plus.next_to(yM)  
        self.play(Write(plus))   
        ################################################################################################



       #  (x0,y0)

        text_c0 = TexMobject('c_0','+','c_1','x_0')
        text_c0.set_color_by_tex('c',GREEN)
        text_c0[1].set_color(BLUE)
        text_c0.set_color_by_tex('x',WHITE)

        tt = text_c0.move_to(0.5*LEFT+3*UP)

        text_c0newpos = text_c0.copy()
        bb=text_c0newpos.next_to(2.25*LEFT+1.4*DOWN)
      


        for pos,formula in [(tt,text_c0),(bb,text_c0newpos)]:
            #formula.scale(size)
            formula.move_to(pos)
        changes = [
			[(0,1,2,3),
			# | | | | |
			# v v v v v
			 (0,1,2,3)],
        ]
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    text_c0[i].copy(),text_c0newpos[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=1
            )

   #  (x1,y1)

        text_c1 = TexMobject('c_0','+','c_1','x_1')
        text_c1.set_color_by_tex('c',GREEN)
        text_c1[1].set_color(BLUE)
        text_c1.set_color_by_tex('x',WHITE)
        tt = text_c1.move_to(0.5*LEFT+2*UP)

        text_c1newpos = text_c1.copy()
        bb=text_c1newpos.next_to(2.25*LEFT+2*DOWN)
      


        for pos,formula in [(tt,text_c1),(bb,text_c1newpos)]:
            #formula.scale(size)
            formula.move_to(pos)
        changes = [
			[(0,1,2,3),
			# | | | | |
			# v v v v v
			 (0,1,2,3)],
        ]
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    text_c1[i].copy(),text_c1newpos[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=1
            )

  #  (x2,y2)
        text_c2 = TexMobject('c_0','+','c_1','x_2')
        text_c2.set_color_by_tex('c',GREEN)
        text_c2[1].set_color(BLUE)
        text_c2.set_color_by_tex('x',WHITE)
        tt = text_c2.move_to(0.5*LEFT+UP)

        text_c2newpos = text_c2.copy()
        bb=text_c2newpos.next_to(2.25*LEFT+2.6*DOWN)
      

        for pos,formula in [(tt,text_c2),(bb,text_c2newpos)]:
            #formula.scale(size)
            formula.move_to(pos)
        changes = [
			[(0,1,2,3),
			# | | | | |
			# v v v v v
			 (0,1,2,3)],
        ]
        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    text_c2[i].copy(),text_c2newpos[j]
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                run_time=1
            )

        ################################################################################################
        r =([['c_0+c_1x_0'],['c_0+c_1x_1'],['c_0+c_1x_2']]) 
        rC = matrix_to_mobject(r)
        rC.scale(0.8)
        rC.set_color(GREEN)
        posC = rC.move_to(1.3*LEFT+2*DOWN)
        self.play(FadeOut(text_c0newpos),FadeOut(text_c1newpos),FadeOut(text_c2newpos))
        self.play(Write(rC))  

        ################################################################################################ 
        eq = TexMobject('=',color=BLUE)
        eq.next_to(rC)  
        self.play(Write(eq))
        yM2 = yM.copy()   
        yM2.next_to(eq)
        self.play(Write(yM2))  

        plus = TexMobject('-',color=GREEN)
        plus.next_to(yM2)  
        self.play(Write(plus))
        r2 = [[1, 'x_0'],[1, 'x_1'],[1, 'x_2']]
        rC2 = matrix_to_mobject(r2)
        rC2.scale(0.8)
        rC2.set_color(WHITE)
        rC2.next_to(plus)  
        self.play(Write(rC2))   

        vec = [['c_0'],['c_1']]
        vecC = matrix_to_mobject(vec)
        vecC.set_color(GREEN)
        vecC.next_to(rC2)   
        vecC.scale(0.8)
        self.play(Write(vecC))  

        self.play(FadeOut(text_fx),\
            FadeOut(text_r0new),FadeOut(text_r0new3),FadeOut(text_r0),\
            FadeOut(text_r1new),FadeOut(text_r1new3),FadeOut(text_r1),\
            FadeOut(text_r2new),FadeOut(text_r2new3),FadeOut(text_r2)) 


         # New animation
        rB = Brace(rM,direction = UP,color = BLUE)
        rB_text = rB.get_text('$\\vec{r}$')
        rB_text.set_color(BLUE)
        self.play(Write(rB),Write(rB_text))         
        
        yM2B = Brace(yM2,direction = UP,color = WHITE)
        yM2B_text = yM2B.get_text('$\\vec{y}$')
        yM2B_text.set_color(WHITE)
        self.play(Write(yM2B),Write(yM2B_text))         
               
        rC2B = Brace(rC2,direction = UP,color = GREEN)
        rC2B_text = rC2B.get_text('$\mathbf{A}$')
        rC2B_text.set_color(WHITE)
        self.play(Write(rC2B),Write(rC2B_text))  

        vecCB = Brace(vecC,direction = UP,color = GREEN)
        vecCB_text = vecCB.get_text('$\\vec{c}$')
        vecCB_text.set_color(GREEN)
        self.play(Write(vecCB),Write(vecCB_text))             

        ###################################################
        rvec = rB_text.copy()
        rvec.move_to(3*UP+1.5*LEFT)
        eq22 = eq.copy()
        eq22.next_to(rvec)
        self.play(ReplacementTransform(rB_text.copy(),rvec),Write(eq22))

        yvec = yM2B_text.copy()
        yvec.next_to(eq22)
        plus2=plus.copy()
        plus2.next_to(yvec)
        self.play(ReplacementTransform(yM2B_text.copy(),yvec),Write(plus2))

        A = rC2B_text.copy()
        A.next_to(plus2)
        self.play(ReplacementTransform(rC2B_text.copy(),A))       
        
        cvec = vecCB_text.copy()
        cvec.next_to(A,0.2*RIGHT)
        self.play(ReplacementTransform(vecCB_text.copy(),cvec))       
                
        vecAc = TexMobject('\\mathbf{A}','\\vec{c}')
        vecAc[1].set_color(GREEN)
        vecAc[0].set_color(WHITE)
        vecAc.next_to(plus2)
        self.play(FadeOut(A),FadeOut(cvec),Write(vecAc))                



class LeastSquaresPart3(GraphScene2):
    CONFIG = {
    "x_min" : -2,
    "x_max" : 2,
    "y_min" : -2,
    "y_max" : 2,
    "graph_origin" : ORIGIN ,
    "function_color" : RED ,
    "axes_color" : BLACK,
    }

     # Covert the data coords to the graph points
    def get_points_from_coords(self,coords):
        return [
            # Convert COORDS -> POINTS
            self.coords_to_point(px,py)
            # See manimlib/scene/graph_scene.py
            for px,py in coords
        ]

    # Return the dots of a set of points
    def get_dots_from_coords(self,coords,radius,color):
        points = self.get_points_from_coords(coords)
        dots = VGroup(*[
            Dot(radius=radius,color=color).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots
   


    def construct(self):
        self.setup_axes(animate=False)      
        func_graph1=self.get_graph(self.p1,self.function_color)

        # Previous animations
        rvec = TexMobject('\\vec{r}')
        rvec.set_color(BLUE)
        rvec.move_to(3*UP+1.5*LEFT)

        eq = TexMobject('=',color=BLUE)
        eq.next_to(rvec)

        yvec = TexMobject('\\vec{y}')
        yvec.next_to(eq)

        minus = TexMobject('-',color=BLUE) 
        minus.next_to(yvec)

        vecAc = TexMobject('\\mathbf{A}','\\vec{c}')
        vecAc[1].set_color(GREEN)
        vecAc[0].set_color(WHITE)
        vecAc.next_to(minus)

        self.play(WriteC(rvec),WriteC(eq),WriteC(yvec),WriteC(minus),WriteC(vecAc))

        self.play(FadeOut(rvec))
        rvec = TexMobject('\\vec{r}\,','(\\vec{c})')
        rvec.set_color_by_tex('vec{r}', BLUE)
        rvec.set_color_by_tex('vec{c}', GREEN)
        rvec.move_to(3*UP+1.7*LEFT)
        self.play(WriteC(rvec))


        self.play(FadeOut(rvec),FadeOut(eq),FadeOut(yvec),FadeOut(minus),FadeOut(vecAc))
        rvec = TexMobject('||\\vec{r}\,','(\\vec{c})\,','||')
        rvec.set_color_by_tex('|\\vec{r}', BLUE)
        rvec.set_color_by_tex('vec{c}', GREEN)
        rvec.set_color_by_tex('||', BLUE)
        rvec.move_to(3*UP+1.7*LEFT)

        eq = TexMobject('=',color=BLUE)
        eq.next_to(rvec)

        yvec = TexMobject('||','\\vec{y}')
        yvec.set_color_by_tex('vec{y}',WHITE)
        yvec.set_color_by_tex('||',BLUE)
        yvec.next_to(eq)

        minus = TexMobject('-',color=BLUE) 
        minus.next_to(yvec)

        vecAc = TexMobject('\\mathbf{A}','\\vec{c}','||')
        vecAc[1].set_color(GREEN)
        vecAc[0].set_color(WHITE)
        vecAc[2].set_color(BLUE)
        vecAc.next_to(minus)

        
        self.play(WriteC(rvec),WriteC(eq),WriteC(yvec),WriteC(minus),WriteC(vecAc))


        rvec2 = TexMobject('||\\vec{r}\,','(\\vec{c})\,','||_2')
        rvec2.set_color_by_tex('vec{r}', BLUE)
        rvec2.set_color_by_tex('vec{c}', GREEN)
        rvec2.set_color_by_tex('_2', BLUE)
        rvec2.move_to(2*UP+1.7*LEFT)

        eq2 = TexMobject('=',color=BLUE)
        eq2.next_to(rvec2)

        yvec2 = TexMobject('||','\\vec{y}')
        yvec2.set_color_by_tex('vec{y}',WHITE)
        yvec2.set_color_by_tex('||',BLUE)
        yvec2.next_to(eq2)

        minus2 = TexMobject('-',color=BLUE) 
        minus2.next_to(yvec2)

        vecAc2 = TexMobject('\\mathbf{A}','\\vec{c}','||_2')
        vecAc2[1].set_color(GREEN)
        vecAc2[0].set_color(WHITE)
        vecAc2[2].set_color(BLUE)
        vecAc2.next_to(minus2)

        self.play(WriteC(rvec2),WriteC(eq2),WriteC(yvec2),WriteC(minus2),WriteC(vecAc2))





        rvec22 = TexMobject('||\\vec{r}\,','(\\vec{c})\,','||_2^2')
        rvec22.set_color_by_tex('||\\vec{r}\,', BLUE)
        rvec22.set_color_by_tex('(\\vec{c})\,', GREEN)
        rvec22.set_color_by_tex('_2', BLUE)
        rvec22.move_to(UP+1.7*LEFT)

        eq22 = TexMobject('=',color=BLUE)
        eq22.next_to(rvec22)

        yvec22 = TexMobject('||','\\vec{y}')
        yvec22.set_color_by_tex('vec{y}',WHITE)
        yvec22.set_color_by_tex('||',BLUE)
        yvec22.next_to(eq22)

        minus22 = TexMobject('-',color=BLUE) 
        minus22.next_to(yvec22)

        vecAc22 = TexMobject('\\mathbf{A}','\\vec{c}','||_2^2')
        vecAc22[1].set_color(GREEN)
        vecAc22[0].set_color(WHITE)
        vecAc22[2].set_color(BLUE)
        vecAc22.next_to(minus22)

        self.play(WriteC(rvec22),WriteC(eq22),WriteC(yvec22),WriteC(minus22),WriteC(vecAc22))

        self.play(FadeOut(rvec),FadeOut(eq),FadeOut(yvec),FadeOut(minus),FadeOut(vecAc))
        self.play(FadeOut(rvec2),FadeOut(eq2),FadeOut(yvec2),FadeOut(minus2),FadeOut(vecAc2))

        rvec22newpos = rvec22.copy()
        rvec22newpos.move_to(3*UP+6.1*LEFT)

        eq22newpos = eq22.copy()
        eq22newpos.next_to(rvec22newpos)

        yvec22newpos = yvec22.copy()
        yvec22newpos.next_to(eq22newpos)

        minus22newpos = minus22.copy()
        minus22newpos.next_to(yvec22newpos)

        vecAc22newpos = vecAc22.copy()
        vecAc22newpos.next_to(minus22newpos)      

        self.play(ReplacementTransform(rvec22.copy(),rvec22newpos),\
            ReplacementTransform(eq22.copy(),eq22newpos),\
            ReplacementTransform(yvec22.copy(),yvec22newpos),\
            ReplacementTransform(minus22.copy(),minus22newpos),\
            ReplacementTransform(vecAc22.copy(),vecAc22newpos))
        self.play(FadeOut(rvec22),FadeOut(eq22),FadeOut(yvec22),FadeOut(minus22),FadeOut(vecAc22))



        ##############################################################################


        vert_line0 = self.get_vertical_line_to_graph(-1,0,func_graph1,color=BLUE)
        vert_line1 = self.get_vertical_line_to_graph(0,-2,func_graph1,color=BLUE)
        vert_line2 = self.get_vertical_line_to_graph(1,1,func_graph1,color=BLUE)

        text_r0 = TexMobject('r_0','\phantom{.}',color=BLUE) 
        text_r0.next_to(vert_line0)
        text_r1 = TexMobject('r_1','\phantom{.}',color=BLUE) 
        text_r1.next_to(vert_line1)
        text_r2 = TexMobject('r_2','\phantom{.}',color=BLUE) 
        text_r2.next_to(vert_line2)


        x0 = [-1]
        x1 = [0]
        x2 = [1]

        y0 = [0]
        y1 = [-2]
        y2 = [1]  

        coord0= [[px,py] for px,py in zip(x0,y0)]
        coord1= [[px,py] for px,py in zip(x1,y1)]
        coord2= [[px,py] for px,py in zip(x2,y2)]

        
        points0 = self.get_points_from_coords(coord0)
        points1 = self.get_points_from_coords(coord1)
        points2 = self.get_points_from_coords(coord2)


        dots0 = self.get_dots_from_coords(coord0,0.1,WHITE)
        dots1 = self.get_dots_from_coords(coord1,0.1,WHITE)
        dots2 = self.get_dots_from_coords(coord2,0.1,WHITE)

        text_dots0 = TextMobject('$(x_0,y_0)$')
        text_dots0.next_to(dots0,UP)
        text_dots1 = TextMobject('$(x_1,y_1)$')
        text_dots1.next_to(dots1,DOWN)        
        text_dots2 = TextMobject('$(x_2,y_2)$')
        text_dots2.next_to(dots2,UP)


        self.add(dots0,dots1,dots2)
        self.add(text_dots0,text_dots1,text_dots2)  
        self.play(ShowCreation(func_graph1))

        self.play(WriteC(text_r0),WriteC(text_r1),WriteC(text_r2),\
            ShowCreation(vert_line0),ShowCreation(vert_line1),ShowCreation(vert_line2))



        rvec22newpos2 = rvec22newpos.copy()
        rvec22newpos2.move_to(5*RIGHT+2.5*DOWN)

        minR = TexMobject('\\min_{\\vec{c}\in \\mathbb{R}^2}')
        minR.set_color(GREEN)
        minR.move_to(3.5*RIGHT+2.6*DOWN)        

        self.play(ReplacementTransform(rvec22newpos.copy(),rvec22newpos2))

        self.play(Write(minR))



        ##############################################################################
        self.wait(2)


        rr = Brace(rvec22newpos2,direction = UP,color = BLUE)
        rr_text = rr.get_tex('r_0^2+r_1^2+r_2^2')
        rr_text.set_color(BLUE)
        rr_text.scale(0.8)
        self.play(Write(rr),Write(rr_text))         


        rB = Brace(rr_text,direction = UP,color = BLUE)
        rB_text = rB.get_tex('J(','\\vec{c}','\,)')
        rB_text.set_color_by_tex('J',BLUE)
        rB_text.set_color_by_tex('\\vec{c}',GREEN)
        rB_text.set_color_by_tex(')',BLUE)
        rB_text.scale(0.8)
        self.play(Write(rB),Write(rB_text))      

        self.play(FadeOut(text_r0),FadeOut(text_r1),FadeOut(text_r2),\
            FadeOut(vert_line0),FadeOut(vert_line1),FadeOut(vert_line2),FadeOut(func_graph1),\
            FadeOut(text_dots0),FadeOut(text_dots1),FadeOut(text_dots2),FadeOut(dots0),FadeOut(dots1),FadeOut(dots2) )
        self.play(FadeOut(rvec22newpos),FadeOut(rvec22newpos),FadeOut(eq22newpos),FadeOut(yvec22newpos),FadeOut(minus22newpos),FadeOut(vecAc22newpos))    
        ##############################################################################

        text1 = TextMobject('Puntos críticos:',color=RED)
        text1.to_edge(UL)
        gradJ = TexMobject('\\nabla{J}=\\vec{0}',color=BLUE) 
        gradJ.to_edge(UP)
        self.play(Write(text1))
        self.play(Write(gradJ))

        MJ =([['\\dfrac{\\partial{J}}{\\partial c_0}'],['\phantom{3}'],['\\dfrac{\\partial{J}}{\\partial c_1}']]) 
        MJ = matrix_to_mobject(MJ)
        MJ.set_color(BLUE)
        MJ.move_to(1.6*UP+LEFT)
        MJ.scale(0.8)
        MJnew = MJ.copy()
        posMJnew = 1.6*UP+6.2*LEFT
        MJnew.move_to(posMJnew)

        eq.move_to(1.6*UP+0.2*RIGHT)
        eq.set_color(BLUE)
        eq.scale(0.8)
        eqnew=eq.copy()
        poseqnew = 1.6*UP+5.2*LEFT
        eqnew.move_to(poseqnew)

        Zero =([['0'],['\phantom{.}'],['0']]) 
        Zero = matrix_to_mobject(Zero)
        Zero.set_color(BLUE)
        Zero.move_to(1.6*UP+1.3*RIGHT)
        Zero.scale(0.8)
        Zeronew = Zero.copy()
        posZeronew = 1.6*UP+4.5*LEFT
        Zeronew.move_to(posZeronew)


        self.play(Write(MJ),Write(eq),Write(Zero))


        Pc0 = TexMobject('\\dfrac{\\partial{J}}{\\partial c_0} = 2r_0\\dfrac{\partial r_0}{\partial c_0}\
            + 2r_1\\dfrac{\partial r_1}{\partial c_0}+ 2r_2\\dfrac{\partial r_2}{\partial c_0}')
        Pc0.set_color(WHITE)
        Pc0.move_to(3.3*LEFT+1.5*DOWN)
        Pc0.scale(0.8)        
        self.play(Write(Pc0))

        Pc1 = TexMobject('\\dfrac{\\partial{J}}{\\partial c_1} = 2r_0\\dfrac{\partial r_0}{\partial c_1}\
            + 2r_1\\dfrac{\partial r_1}{\partial c_1}+ 2r_2\\dfrac{\partial r_2}{\partial c_1}')
        Pc1.set_color(WHITE)
        Pc1.move_to(3.3*LEFT+3*DOWN)
        Pc1.scale(0.8)
        self.play(Write(Pc1))

        self.play(FadeOut(rB),FadeOut(rB_text),FadeOut(rr_text),FadeOut(minR),FadeOut(rr),FadeOut(rvec22newpos2))

        r0 = TexMobject('r_0=','y_0','-','f(','x_0',')') 
        r0[3].set_color(RED) 
        r0[5].set_color(RED) 
        r0.set_color_by_tex('r', BLUE) 
        r0.set_color_by_tex('y', WHITE) 
        r0.set_color_by_tex('-', BLUE) 
        r0.scale(0.8)
        r0.bg=SurroundingRectangle(r0,color=RED,fill_color=RED, fill_opacity=0)
        r0_group=VGroup(r0,r0.bg)
        r0_group.move_to(0.5*DOWN+2*RIGHT)

        self.play(Write(r0_group))

        T1c0 = TexMobject('= 2r_0','(-1)')
        T1c0.set_color_by_tex('r_0',BLUE)
        T1c0.set_color_by_tex('-1',WHITE)
        T1c0.move_to(RIGHT+1.5*DOWN)
        T1c0.scale(0.8)

        self.play(Write(T1c0))

        T1c1 = TexMobject('= 2r_0','(-x_0)')
        T1c1.set_color_by_tex('r_0',BLUE)
        T1c1.set_color_by_tex('x_0',WHITE)
        T1c1.move_to(RIGHT+3*DOWN)
        T1c1.scale(0.8)

        self.play(Write(T1c1))

        self.play(FadeOut(r0_group))

        #############

        r1 = TexMobject('r_1=','y_1','-','f(','x_1',')') 
        r1[3].set_color(RED) 
        r1[5].set_color(RED) 
        r1.set_color_by_tex('r', BLUE) 
        r1.set_color_by_tex('y', WHITE) 
        r1.set_color_by_tex('-', BLUE) 
        r1.scale(0.8)
        r1.bg=SurroundingRectangle(r1,color=RED,fill_color=RED, fill_opacity=0)
        r1_group=VGroup(r1,r1.bg)
        r1_group.move_to(0.5*DOWN+3.5*RIGHT)

        self.play(Write(r1_group))

        T2c0 = TexMobject('+ 2r_1','(-1)')
        T2c0.set_color_by_tex('r_1',BLUE)
        T2c0.set_color_by_tex('-1',WHITE)
        T2c0.move_to(2.9*RIGHT+1.5*DOWN)
        T2c0.scale(0.8)

        self.play(Write(T2c0))

        T2c1 = TexMobject('+ 2r_1','(-x_1)')
        T2c1.set_color_by_tex('r_1',BLUE)
        T2c1.set_color_by_tex('x_1',WHITE)
        T2c1.move_to(3*RIGHT+3*DOWN)
        T2c1.scale(0.8)

        self.play(Write(T2c1))

        self.play(FadeOut(r1_group))

        #############

        r2 = TexMobject('r_2=','y_2','-','f(','x_2',')') 
        r2[3].set_color(RED) 
        r2[5].set_color(RED) 
        r2.set_color_by_tex('r', BLUE) 
        r2.set_color_by_tex('y', WHITE) 
        r2.set_color_by_tex('-', BLUE) 
        r2.scale(0.8)
        r2.bg=SurroundingRectangle(r2,color=RED,fill_color=RED, fill_opacity=0)
        r2_group=VGroup(r2,r2.bg)
        r2_group.move_to(0.5*DOWN+4*RIGHT)

        self.play(Write(r2_group))

        T3c0 = TexMobject('+ 2r_2','(-1)')
        T3c0.set_color_by_tex('r_2',BLUE)
        T3c0.set_color_by_tex('-1',WHITE)
        T3c0.move_to(4.8*RIGHT+1.5*DOWN)
        T3c0.scale(0.8)

        self.play(Write(T3c0))

        T3c1 = TexMobject('+ 2r_2','(-x_2)')
        T3c1.set_color_by_tex('r_2',BLUE)
        T3c1.set_color_by_tex('x_2',WHITE)
        T3c1.move_to(5*RIGHT+3*DOWN)
        T3c1.scale(0.8)

        self.play(Write(T3c1))

        self.play(FadeOut(r2_group))



        #############
        self.play(ReplacementTransform(MJ.copy(),MJnew),ReplacementTransform(eq.copy(),eqnew),ReplacementTransform(Zero.copy(),Zeronew))
        self.play(FadeOut(MJ),FadeOut(eq),FadeOut(Zero))

        iff= TexMobject('\\Leftrightarrow',color=RED)
        iff.next_to(Zeronew)
        iff.scale(0.8)
        self.play(Write(iff))

        MJ1 =([['2r_0(-1)+2r_1(-1)+2r_2(-1)'],['\phantom{3}'],['2r_0(-x_0)+2r_1(-x_1)+2r_2(-x_2)']]) 
        MJ1 = matrix_to_mobject(MJ1)
        MJ1.set_color(BLUE)
        MJ1.move_to(1.6*UP)
        MJ1.scale(0.8)
        eq.move_to(1.6*UP+3.7*RIGHT)
        Zero.move_to(1.6*UP+4.6*RIGHT)
        self.play(Write(MJ1),Write(eq),Write(Zero))

        self.play(FadeOut(Pc0),FadeOut(Pc1),\
            FadeOut(T1c0),FadeOut(T2c0),FadeOut(T3c0),\
            FadeOut(T1c1),FadeOut(T2c1),FadeOut(T3c1))

        At =([['1','1','1'],['x_0','x_1','x_2']]) 
        At = matrix_to_mobject(At)
        At.set_color(WHITE)
        At.scale(0.8)
        At.next_to(MJ1,2*DOWN)

        m2 = TexMobject('-2',color=BLUE)
        m2.next_to(At,LEFT)
        m2.scale(0.8)

        rvec = TexMobject('\\vec{r}',color=BLUE)
        rvec.scale(0.8)
        rvec.next_to(At)

        iff2 = iff.copy()
        iff2.next_to(iff,6*DOWN)

        eq2 = eq.copy()
        eq2.next_to(rvec)
        Zero2 = Zero.copy()
        Zero2.next_to(eq2)


        self.play(Write(At),Write(rvec),Write(m2),Write(iff2),Write(eq2),Write(Zero2))

        AtB = Brace(At,direction = DOWN,color = WHITE)
        AtB_text = AtB.get_text('$\\mathbf{A}^t$')
        AtB_text.scale(0.8)
        AtB_text.set_color(WHITE)
        self.play(Write(AtB),Write(AtB_text))       


        iff3 = iff.copy()
        iff3.next_to(iff,14*DOWN)   

        AtB2_text = AtB_text.copy()
        AtB2_text.next_to(iff3,10*RIGHT)

        rvec2 = rvec.copy()
        rvec2.next_to(AtB2_text)

        eq3 = eq.copy()
        eq3.next_to(rvec2)

        vec0 = TexMobject('\\vec{0}',color=BLUE)
        vec0.scale(0.8)
        vec0.next_to(eq3)

        self.play(Write(AtB2_text),Write(iff3),Write(rvec2),Write(eq3),Write(vec0))



        # Recordemos que
        rvec_old = TexMobject('\\vec{r}')
        rvec_old.set_color(BLUE)
        rvec_old.next_to(vec0,3*RIGHT)
        rvec_old.scale(0.8)

        eq_old = TexMobject('=',color=BLUE)
        eq_old.next_to(rvec_old)
        eq_old.scale(0.8)

        yvec_old = TexMobject('\\vec{y}')
        yvec_old.next_to(eq_old)
        yvec_old.scale(0.8)

        minus_old = TexMobject('-',color=BLUE) 
        minus_old.next_to(yvec_old)
        minus_old.scale(0.8)

        vecAc_old = TexMobject('\\mathbf{A}','\\vec{c}')
        vecAc_old[0].set_color(WHITE)
        vecAc_old[1].set_color(GREEN)
        vecAc_old.next_to(minus_old)
        vecAc_old.scale(0.8)

        res = VGroup(rvec_old,eq_old,yvec_old,minus_old,vecAc_old)
        res2 = VGroup(eq_old,yvec_old,minus_old,vecAc_old)

        res.bg=SurroundingRectangle(res,color=RED,fill_color=RED, fill_opacity=0)
        res_group=VGroup(res,res.bg)
        res_group.next_to(vec0,5*RIGHT)

        self.play(WriteC(res_group))


        iff4 = iff.copy()
        iff4.next_to(iff,18*DOWN)          

        AtA = TexMobject('\\mathbf{A}^t\\mathbf{A}','\\vec{c}')
        AtA[0].set_color(WHITE)
        AtA[1].set_color(GREEN)
        AtA.next_to(iff4,10*RIGHT)
        AtA.scale(0.8)

        eq4 = eq.copy()
        eq4.next_to(AtA)


        Aty = TexMobject('\\mathbf{A}^t','\\vec{y}')
        Aty.set_color_by_tex('A',WHITE)
        Aty.set_color_by_tex('y',WHITE)
        Aty.next_to(eq4)
        Aty.scale(0.8)       


        self.play(FadeOut(res_group))
        self.play(Write(AtA),Write(iff4),Write(eq4),Write(Aty))


    def p1(self,x):
        return -1/3+x*0.5    


class LeastSquaresPart4(GraphScene2):
    CONFIG = {
    "x_min" : -2,
    "x_max" : 2,
    "y_min" : -2,
    "y_max" : 2,
    "graph_origin" : ORIGIN ,
    "function_color" : RED ,
    "axes_color" : BLACK,
    }

     # Covert the data coords to the graph points
    def get_points_from_coords(self,coords):
        return [
            # Convert COORDS -> POINTS
            self.coords_to_point(px,py)
            # See manimlib/scene/graph_scene.py
            for px,py in coords
        ]

    # Return the dots of a set of points
    def get_dots_from_coords(self,coords,radius,color):
        points = self.get_points_from_coords(coords)
        dots = VGroup(*[
            Dot(radius=radius,color=color).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots
   

    def construct(self):
        self.setup_axes(animate=False)    
        # First animation
        func_graph1=self.get_graph(self.p1,self.function_color)
       
        x0 = [-1]
        x1 = [0]
        x2 = [1]

        y0 = [0]
        y1 = [-2]
        y2 = [1]  

        coord0= [[px,py] for px,py in zip(x0,y0)]
        coord1= [[px,py] for px,py in zip(x1,y1)]
        coord2= [[px,py] for px,py in zip(x2,y2)]

        
        points0 = self.get_points_from_coords(coord0)
        points1 = self.get_points_from_coords(coord1)
        points2 = self.get_points_from_coords(coord2)


        dots0 = self.get_dots_from_coords(coord0,0.1,WHITE)
        dots1 = self.get_dots_from_coords(coord1,0.1,WHITE)
        dots2 = self.get_dots_from_coords(coord2,0.1,WHITE)

        text_dots0 = TextMobject('$(x_0,y_0)$')
        text_dots0.next_to(dots0,UP)
        text_dots1 = TextMobject('$(x_1,y_1)$')
        text_dots1.next_to(dots1,DOWN)        
        text_dots2 = TextMobject('$(x_2,y_2)$')
        text_dots2.next_to(dots2,UP)

        text_fx = TexMobject('f(','x',')','=','c_0','+','c_1','x')
        text_fx.set_color_by_tex('f',RED)
        text_fx.set_color_by_tex('x',WHITE)
        text_fx.set_color_by_tex(')',RED)
        text_fx.set_color_by_tex('=',BLUE)
        text_fx.set_color_by_tex('+',BLUE)
        text_fx.set_color_by_tex('c',GREEN)
        text_fx.move_to(3*DOWN+4.5*LEFT)          
      

        todo = VGroup(dots0,dots1,dots2,text_dots0,text_dots1,text_dots2,func_graph1,text_fx)
        todo.scale(0.8)  
        todo.to_edge(UL)
        self.play(Write(todo))


        AtA = TexMobject('\\mathbf{A}^t\\mathbf{A}\,\\vec{c}','=','\\mathbf{A}^t','\\vec{y}')
        AtA.set_color_by_tex('A',WHITE)
        AtA.set_color_by_tex('y',WHITE)
        AtA.set_color_by_tex('=',BLUE)

        AtA.bg=SurroundingRectangle(AtA,color=RED,fill_color=RED, fill_opacity=0)
        AtA=VGroup(AtA,AtA.bg)

        AtA.to_edge(UR)
        AtA.scale(0.8)


        self.play(Write(AtA))


        A = [[1, 'x_0'],[1, 'x_1'],[1, 'x_2']]
        A = matrix_to_mobject(A)
        A.set_color(WHITE)

        eq = TexMobject('=',color=BLUE)  
        eq.next_to(A,LEFT) 
        A_text = TexMobject('\mathbf{A}',color=WHITE)  
        A_text.next_to(eq, LEFT)
        Atotal = VGroup(A_text,eq,A) 
        Atotal.scale(0.8)
        Atotal.next_to(AtA,1.5*DOWN)


        self.play(Write(Atotal))

        eqy = TexMobject('=',color=BLUE)  
        eqy.next_to(Atotal,DOWN)

        y = [['y_0'],['y_1'],['y_2']]
        y = matrix_to_mobject(y)
        y.next_to(eqy,RIGHT)
        y.set_color(WHITE)

        y_text = TexMobject('\\vec{y}',color=WHITE)  
        y_text.next_to(eqy, LEFT)
        ytotal = VGroup(y_text,eqy,y) 
        ytotal.scale(0.8)
        ytotal.next_to(Atotal,1.5*DOWN)
 
        self.play(Write(ytotal)) 


        eqc = TexMobject('=',color=BLUE)  
        eqc.next_to(ytotal,DOWN)

        c = [['c_0'],['c_1']]
        c = matrix_to_mobject(c)
        c.next_to(eqc,RIGHT)
        c.set_color(GREEN)

        c_text = TexMobject('\\vec{c}',color=GREEN)  
        c_text.next_to(eqc, LEFT)
        ctotal = VGroup(c_text,eqc,c) 
        ctotal.scale(0.8)
        ctotal.next_to(ytotal,1.5*DOWN)
 
        self.play(Write(ctotal))         

    def p1(self,x):
        return -1/3+x*0.5    


class LeastSquaresPart0(GraphScene2):
    CONFIG = {
    "x_min" : -2,
    "x_max" : 2,
    "y_min" : -2,
    "y_max" : 2,
    "graph_origin" : ORIGIN ,
    "function_color" : RED ,
    "axes_color" : BLACK,
    }

     # Covert the data coords to the graph points
    def get_points_from_coords(self,coords):
        return [
            # Convert COORDS -> POINTS
            self.coords_to_point(px,py)
            # See manimlib/scene/graph_scene.py
            for px,py in coords
        ]

    # Return the dots of a set of points
    def get_dots_from_coords(self,coords,radius,color):
        points = self.get_points_from_coords(coords)
        dots = VGroup(*[
            Dot(radius=radius,color=color).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots
   

    def construct(self):
        self.setup_axes(animate=False)    
        # First animation
        func_graph1=self.get_graph(self.p1,self.function_color)
       
        x0 = [-1]
        x1 = [0]
        x2 = [1]

        y0 = [0]
        y1 = [-2]
        y2 = [1]  

        coord0= [[px,py] for px,py in zip(x0,y0)]
        coord1= [[px,py] for px,py in zip(x1,y1)]
        coord2= [[px,py] for px,py in zip(x2,y2)]

        
        points0 = self.get_points_from_coords(coord0)
        points1 = self.get_points_from_coords(coord1)
        points2 = self.get_points_from_coords(coord2)


        dots0 = self.get_dots_from_coords(coord0,0.1,WHITE)
        dots1 = self.get_dots_from_coords(coord1,0.1,WHITE)
        dots2 = self.get_dots_from_coords(coord2,0.1,WHITE)

        text_dots0 = TextMobject('$(x_0,y_0)=(-1,0)$')
        text_dots0.next_to(dots0,UP)
        text_dots1 = TextMobject('$(x_1,y_1)=(0,-2)$')
        text_dots1.next_to(dots1,DOWN)        
        text_dots2 = TextMobject('$(x_2,y_2)=(1,1)$')
        text_dots2.next_to(dots2,UP)

        text_fx = TexMobject('f(','x',')','=','c_0','+','c_1','x')
        text_fx.set_color_by_tex('f',RED)
        text_fx.set_color_by_tex('x',WHITE)
        text_fx.set_color_by_tex(')',RED)
        text_fx.set_color_by_tex('=',BLUE)
        text_fx.set_color_by_tex('+',BLUE)
        text_fx.set_color_by_tex('c',GREEN)
        text_fx.move_to(3*DOWN+4.5*LEFT)          
      

        todo = VGroup(dots0,dots1,dots2,text_dots0,text_dots1,text_dots2,func_graph1,text_fx)
        todo.scale(0.8)  
        todo.to_edge(UL)
        self.play(Write(todo))


        eqn0=TexMobject('f(','x_0',')','=','y_0')
        eqn0[0].set_color(RED)
        eqn0[1].set_color(WHITE)
        eqn0[2].set_color(RED)
        eqn0[3].set_color(BLUE)
        eqn0[4].set_color(WHITE)
        eqn0.scale(0.8)

        eqn1=TexMobject('f(','x_1',')','=','y_1')
        eqn1[0].set_color(RED)
        eqn1[1].set_color(WHITE)
        eqn1[2].set_color(RED)
        eqn1[3].set_color(BLUE)
        eqn1[4].set_color(WHITE)
        eqn1.scale(0.8)

        eqn2=TexMobject('f(','x_2',')','=','y_2')
        eqn2[0].set_color(RED)
        eqn2[1].set_color(WHITE)
        eqn2[2].set_color(RED)
        eqn2[3].set_color(BLUE)
        eqn2[4].set_color(WHITE)
        eqn2.scale(0.8)


        pos0 = eqn0.move_to(3*UP+4*RIGHT)
        pos1 = eqn1.next_to(eqn0,DOWN)
        pos2 = eqn2.next_to(eqn1,DOWN)


        fx0 = TexMobject('c_0','+','c_1','x_0','=','y_0')
        fx0[0].set_color(GREEN)
        fx0[1].set_color(BLUE)
        fx0[2].set_color(GREEN)
        fx0[3].set_color(WHITE)
        fx0[4].set_color(BLUE)
        fx0[5].set_color(WHITE) 
        fx0.move_to(pos0)   
        fx0.scale(0.8)    

        fx1 = TexMobject('c_0','+','c_1','x_1','=','y_1')
        fx1[0].set_color(GREEN)
        fx1[1].set_color(BLUE)
        fx1[2].set_color(GREEN)
        fx1[3].set_color(WHITE)
        fx1[4].set_color(BLUE)
        fx1[5].set_color(WHITE)    
        fx1.move_to(pos1) 
        fx1.scale(0.8)    

        fx2 = TexMobject('c_0','+','c_1','x_2','=','y_2')
        fx2[0].set_color(GREEN)
        fx2[1].set_color(BLUE)
        fx2[2].set_color(GREEN)
        fx2[3].set_color(WHITE)
        fx2[4].set_color(BLUE)
        fx2[5].set_color(WHITE) 
        fx2.move_to(pos2)    
        fx2.scale(0.8)    

        

        self.play(Write(eqn0),Write(eqn1),Write(eqn2))      
        self.wait(2)
        self.play(FadeOut(eqn0),ReplacementTransform(eqn0.copy(),fx0))
        self.play(FadeOut(eqn1),ReplacementTransform(eqn1.copy(),fx1))
        self.play(FadeOut(eqn2),ReplacementTransform(eqn2.copy(),fx2))  
        self.wait(2)        



        A = [[1, 'x_0'],[1, 'x_1'],[1, 'x_2']]
        A = matrix_to_mobject(A)
        A.set_color(WHITE)
        A.scale(0.8)
        A.next_to(fx2,2.5*DOWN+2*LEFT)

        Aval = [[1, -1],[1, 0],[1, 1]]
        Aval = matrix_to_mobject(Aval)
        Aval.set_color(WHITE)
        Aval.scale(0.8)
        Aval.next_to(fx2,2.5*DOWN+2*LEFT)    

        c = [['c_0'],['c_1']]
        c = matrix_to_mobject(c)
        c.set_color(GREEN)
        c.next_to(A)
        c.scale(0.8)        

        eq = TexMobject('=',color=BLUE)  
        eq.next_to(c,RIGHT) 

        y = [['y_0'],['y_1'],['y_2']]
        y = matrix_to_mobject(y)
        y.scale(0.8)
        y.next_to(eq,RIGHT)
        y.set_color(WHITE)

        yval = [['0'],['-2'],['1']]
        yval = matrix_to_mobject(yval)
        yval.scale(0.8)
        yval.next_to(eq,RIGHT)
        yval.set_color(WHITE)

        self.play(Write(A),Write(c),Write(eq),Write(y)) 

        self.play(FadeOut(A),ReplacementTransform(A.copy(),Aval))
        self.play(FadeOut(y),ReplacementTransform(y.copy(),yval))
    
        brAval0 = Brace(Aval,direction = DOWN,color = WHITE)
        Aval_text = brAval0.get_text('$\\mathbf{A}$')
        Aval_text.set_color(WHITE)

        bry = Brace(yval,direction = DOWN,color = WHITE)
        bry_text = bry.get_text('$\\vec{y}$')
        bry_text.set_color(WHITE)

        brc = Brace(c,direction = DOWN,color = GREEN)
        brc_text = brc.get_text('$\\vec{c}$')
        brc_text.set_color(GREEN)

        self.play(Write(brAval0),Write(Aval_text),Write(brc),Write(brc_text),Write(bry),Write(bry_text)) 

        Atotal = TexMobject('\mathbf{A}',color=WHITE) 
        Atotal.next_to(eq, LEFT) 
        Atotal.next_to(brc_text,3.5*DOWN+9*LEFT)
      
        ctotal = TexMobject('\\vec{c}',color=GREEN) 
        ctotal.next_to(Atotal) 

        eqc = TexMobject('=',color=BLUE) 
        eqc.next_to(ctotal)

        ytotal = TexMobject('\\vec{y}',color=WHITE) 
        ytotal.next_to(eqc) 

        sis = VGroup(Atotal,ctotal,eqc,ytotal)
        sis.bg=SurroundingRectangle(sis,color=RED,fill_color=RED, fill_opacity=0) 
        
        self.play(Write(sis),Write(sis.bg)) 

        brAval = Brace(sis,direction = DOWN,color = WHITE)
        brAval_text = brAval.get_text('Sistema sobredeterinado')
        brAval_text.set_color(WHITE)
        brAval_text.scale(0.7)
        self.play(Write(brAval),Write(brAval_text))

        imp= TexMobject('\\Rightarrow',color=RED)
        imp.next_to(sis,2.5*RIGHT)

        AtA = TexMobject('\\mathbf{A}^t\\mathbf{A}','\\vec{c}','=','\\mathbf{A}^t','\\vec{y}') 
        AtA.set_color_by_tex('A',WHITE) 
        AtA.set_color_by_tex('y',WHITE) 
        AtA.set_color_by_tex('=',BLUE)
        AtA.set_color_by_tex('c',GREEN)
        AtA.next_to(imp,2.5*RIGHT)

        AtA.bg=SurroundingRectangle(AtA,color=RED,fill_color=RED, fill_opacity=0) 
        AtA=VGroup(AtA,AtA.bg)

        self.play(Write(imp),Write(AtA))

        brAtA = Brace(AtA,direction = DOWN,color = WHITE)
        brAtA_text = brAtA.get_text('Ecuaciones normales')
        brAtA_text.set_color(WHITE)
        brAtA_text.scale(0.7)
        self.play(Write(brAtA),Write(brAtA_text))

        self.play(FadeOut(fx0),FadeOut(fx1),FadeOut(fx2))  

        AtA_UP = AtA.copy()
        AtA_UP.to_edge(UP)

        self.play(FadeOut(AtA),FadeOut(imp),FadeOut(brAtA),FadeOut(brAtA_text),\
            FadeOut(brAval),FadeOut(brAval_text),FadeOut(brc),\
            FadeOut(brc_text),FadeOut(bry),FadeOut(bry_text),\
            FadeOut(Aval),FadeOut(Aval_text),FadeOut(yval),FadeOut(c),FadeOut(eq),\
            FadeOut(brAval0),FadeOut(sis.bg),FadeOut(sis))   




        self.play(ReplacementTransform(AtA.copy(),AtA_UP))

        AA = [[3, 0],[0, 2]]
        AA = matrix_to_mobject(AA)
        AA.set_color(WHITE)
        AA.scale(0.8)
        AA.next_to(AtA_UP,2.5*DOWN+2.5*LEFT)

        c.next_to(AA)
        eqc.next_to(c)

        yy = [[-1],[-1]]
        yy = matrix_to_mobject(yy)
        yy.scale(0.8)
        yy.next_to(eqc,RIGHT)
        yy.set_color(WHITE)

        self.play(Write(AA),Write(c),Write(eqc),Write(yy))

        c0 = TexMobject('c_0 = -1/3',color=GREEN) 
        c0.next_to(c,DOWN) 
        c0.scale(0.8)
        c1 = TexMobject('c_1 = 1/2',color=GREEN) 
        c1.next_to(c0,DOWN)
        c1.scale(0.8)
        self.play(Write(c0),Write(c1))

        text_fx0 = TexMobject('f(','x',')','=','-\\frac{1}{3}','+','\\frac{1}{2}','x')
        text_fx0.set_color_by_tex('f',RED)
        text_fx0.set_color_by_tex('x',WHITE)
        text_fx0.set_color_by_tex(')',RED)
        text_fx0.set_color_by_tex('=',BLUE)
        text_fx0.set_color_by_tex('+',BLUE)
        text_fx0.set_color_by_tex('c',GREEN)
        text_fx0.to_edge(DOWN) 

        text_fx0.bg=SurroundingRectangle(text_fx0,color=RED,fill_color=RED, fill_opacity=0) 
        final=VGroup(text_fx0,text_fx0.bg)

        self.play(ReplacementTransform(text_fx.copy(),final))



    def p1(self,x):
        return -1/3+x*0.5    