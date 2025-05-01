from manimlib import *


class ChessBoard(Scene):
    def construct(self):
        def write_rice_grains(total, start_x, start_y, start_z=0, rotate = False, color=WHITE):
            rice_grains = []
            margin_x = 0.05
            margin_y = 0.15
            margin_z = 0.14
            x_coord = start_x
            y_coord = start_y
            z_coord = start_z
            
            for i in range(total):
                rice_grain = Circle()
                rice_grain.set_fill(color, opacity=1)
                rice_grain.set_stroke(BLACK, width=1)
                rice_grain.stretch(8, dim=1)
                rice_grain.scale(0.01)
                rice_grain.set_x(x_coord)
                if rotate:
                    rice_grain.rotate(PI/3, LEFT)
                x_coord += margin_x
                rice_grain.set_y(y_coord)
                rice_grain.set_z(z_coord)
                
                if ((i + 1) % 8) == 0:
                    x_coord = start_x
                    y_coord += margin_y
                if ((i+1) % 32) == 0:
                    z_coord += margin_z
                    
                rice_grains.append(rice_grain)


            return rice_grains
            
            
        squares = VGroup(*[Square(side_length=0.8, stroke_width=0) for _ in range(8**2)])
        squares.arrange_in_grid(buff=0)
        even_row = True
        odd_row = False
        for i in range(64):
            if even_row:
                if i %2 == 0:
                    squares[i].set_fill(TEAL, opacity=0.5)
                else:
                    squares[i].set_fill(WHITE, opacity=0.5)
            else:
                if i %2 == 1:
                    squares[i].set_fill(TEAL, opacity=0.5)
                else:
                    squares[i].set_fill(WHITE, opacity=0.5)
            if (i + 1) % 8 == 0:
                if even_row:
                    odd_row = True
                    even_row = False
                else:
                    odd_row = False
                    even_row = True
                    
        self.add(squares)
        self.wait(3)
        
        rice_grains_cell_1 = write_rice_grains(1, -3.8, -2.08, rotate=True)
        rice_grains_cell_2 = write_rice_grains(2, -2.9, -2.08, rotate=True)
        rice_grains_cell_3 = write_rice_grains(4, -1.9, -2.08, rotate=True)
        rice_grains_cell_4 = write_rice_grains(8, -0.8, -2.08, rotate=True)
        rice_grains_cell_5 = write_rice_grains(16, 0.4, -2.08, rotate=True)
        rice_grains_cell_6 = write_rice_grains(32, 1.3, -2.08, rotate=True)

        chess_idx = []

        for i in range(56, 64):
            chess_idx.append(i)

        for i in range(48, 56):
            chess_idx.append(i)

        for i in range(40, 48):
            chess_idx.append(i)

        for i in range(32, 40):
            chess_idx.append(i)

        for i in range(24, 32):
            chess_idx.append(i)

        for i in range(16, 24):
            chess_idx.append(i)

        for i in range(8, 16):
            chess_idx.append(i)

        for i in range(0, 8):
            chess_idx.append(i)

        nums = [num for num in range(1,65)]
        texts = []
                
        self.play(Rotate(squares, PI/3, LEFT))

        for i, idx in enumerate(chess_idx):
            text = Text(str(nums[i]), font_size=8)
            sq = squares[idx]
            corner = sq.get_start()
            text.rotate(PI/3, LEFT)
            texts.append(text)
            text.move_to(sq.get_corner(LEFT))
            text.shift(DOWN*.15+RIGHT*0.05)
            if i+1 in [8,16,24,32,40,48,56,64]:
                text.shift(RIGHT*0.1)
            if i+1 in [7,15,23,31,39,47,55,63]:
                text.shift(RIGHT*0.085)
            if i+1 in [6,14,22,30,38,46,54,62]:
                text.shift(RIGHT*0.06)
            if i+1 in [1,9,17,25,33,41,49,57]:
                text.shift(LEFT*0.1)
            
            self.play(Write(text), run_time=0.05)
        self.wait(15)

        c0 = Square(side_length=0.5)
        c0.set_stroke(WHITE, width=2)
        c0.shift(-3*UP+-3*RIGHT)
        t0 = Tex("Square", font_size=14)
        t0.move_to(c0)        
        c1 = Square(side_length=0.5)
        c1.set_stroke(WHITE, width=2)
        c1.move_to(c0.get_bottom(),UP)
        t1 = Tex("Grains", font_size=14)
        t1.move_to(c1)
        self.play(Write(c0, run_time=0.5), Write(t0, run_time=0.5), Write(c1, run_time=0.5), Write(t1, run_time=0.5))

        self.wait(10)
        
        c2 = Square(side_length=0.5)
        c2.set_stroke(WHITE, width=2)
        c2.move_to(c0.get_right(),LEFT)
        t2 = Tex("1", font_size=14)
        t2.move_to(c2)
        self.play(Write(c2, run_time=0.5), Write(t2, run_time=0.5))        
        self.play(squares[56].animate.set_stroke(ORANGE, width=4))
        self.wait(2)
        for rice in rice_grains_cell_1:
            self.add(rice)        
        c3 = Square(side_length=0.5)
        c3.set_stroke(WHITE, width=2)
        c3.move_to(c1.get_right(),LEFT)
        t3 = Tex("1", font_size=14)
        t3.move_to(c3)
        self.wait(2)
        self.play(Write(c3, run_time=0.1), Write(t3, run_time=0.1))

        self.wait()
        
        c4 = Square(side_length=0.5)
        c4.set_stroke(WHITE, width=2)
        c4.move_to(c2.get_right(),LEFT)
        t4 = Tex("2", font_size=14)
        t4.move_to(c4)
        self.play(Write(c4, run_time=0.1), Write(t4, run_time=0.1))
        self.play(squares[57].animate.set_stroke(ORANGE, width=4))
        self.wait(2)
        for rice in rice_grains_cell_2:
            self.add(rice)
        c5 = Square(side_length=0.5)
        c5.set_stroke(WHITE, width=2)
        c5.move_to(c3.get_right(),LEFT)
        t5 = Tex("2", font_size=14)
        t5.move_to(c5)
        self.wait(2)
        self.play(Write(c5, run_time=0.1), Write(t5, run_time=0.1))

        self.wait()

        c6 = Square(side_length=0.5)
        c6.set_stroke(WHITE, width=2)
        c6.move_to(c4.get_right(),LEFT)
        t6 = Tex("3", font_size=14)
        t6.move_to(c6)
        self.play(Write(c6, run_time=0.1), Write(t6, run_time=0.1))        
        self.play(squares[58].animate.set_stroke(ORANGE, width=4))
        self.wait(2)
        for rice in rice_grains_cell_3:
            self.add(rice)            
        c7 = Square(side_length=0.5)
        c7.set_stroke(WHITE, width=2)
        c7.move_to(c5.get_right(),LEFT)
        t7 = Tex("4", font_size=14)
        t7.move_to(c7)
        self.wait()
        self.play(Write(c7, run_time=0.1), Write(t7, run_time=0.1)) 

        self.wait()

        c8 = Square(side_length=0.5)
        c8.set_stroke(WHITE, width=2)
        c8.move_to(c6.get_right(),LEFT)
        t8 = Tex("4", font_size=14)
        t8.move_to(c8)
        self.play(Write(c8, run_time=0.1), Write(t8, run_time=0.1))         
        self.play(squares[59].animate.set_stroke(ORANGE, width=4))
        self.wait()
        for rice in rice_grains_cell_4:
            self.add(rice)
        c9 = Square(side_length=0.5)
        c9.set_stroke(WHITE, width=2)
        c9.move_to(c7.get_right(),LEFT)
        t9 = Tex("8", font_size=14)
        t9.move_to(c9)
        self.wait()
        self.play(Write(c9, run_time=0.1), Write(t9, run_time=0.1))  

        self.wait()

        c10 = Square(side_length=0.5)
        c10.set_stroke(WHITE, width=2)
        c10.move_to(c8.get_right(),LEFT)
        t10 = Tex("5", font_size=14)
        t10.move_to(c10)
        self.play(Write(c10, run_time=0.1), Write(t10, run_time=0.1))  
        self.play(squares[60].animate.set_stroke(ORANGE, width=4))
        self.wait()
        for rice in rice_grains_cell_5:
            self.add(rice)
        c11 = Square(side_length=0.5)
        c11.set_stroke(WHITE, width=2)
        c11.move_to(c9.get_right(),LEFT)
        t11 = Tex("16", font_size=14)
        t11.move_to(c11)
        self.wait()
        self.play(Write(c11, run_time=0.1), Write(t11, run_time=0.1)) 

        self.wait()

        c12 = Square(side_length=0.5)
        c12.set_stroke(WHITE, width=2)
        c12.move_to(c10.get_right(),LEFT)
        t12 = Tex("6", font_size=14)
        t12.move_to(c12)
        self.play(Write(c12, run_time=0.1), Write(t12, run_time=0.1))         
        self.play(squares[61].animate.set_stroke(ORANGE, width=4))
        self.wait()
        for rice in rice_grains_cell_6:
            self.add(rice)
        c13 = Square(side_length=0.5)
        c13.set_stroke(WHITE, width=2)
        c13.move_to(c11.get_right(),LEFT)
        t13 = Tex("32", font_size=14)
        t13.move_to(c13)
        self.wait()
        self.play(Write(c13, run_time=0.1), Write(t13, run_time=0.1)) 

        self.wait()

        rice_grains_cell_7 = write_rice_grains(64, 2.45, -2, start_z=0, rotate=True)

        rice_grains_cell_8 = write_rice_grains(128, 3.6, -2, start_z=0, rotate=True)

        rice_grains_cell_9 = write_rice_grains(256, -3.7, -1.3, start_z=0, rotate=True)

        rice_grains_cell_10 = write_rice_grains(512, -2.7, -1.3, start_z=0, rotate=True)

        rice_grains_cell_11 = write_rice_grains(1024, -1.85, -1.3, start_z=0, rotate=True)

        c14 = Square(side_length=0.5)
        c14.set_stroke(WHITE, width=2)
        c14.move_to(c12.get_right(),LEFT)
        t14 = Tex("7", font_size=14)
        t14.move_to(c14)
        self.play(Write(c14, run_time=0.1), Write(t14, run_time=0.1))         
        self.play(squares[62].animate.set_stroke(ORANGE, width=4))
        self.wait()
        for rice in rice_grains_cell_7:
            self.add(rice)
        c15 = Square(side_length=0.5)
        c15.set_stroke(WHITE, width=2)
        c15.move_to(c13.get_right(),LEFT)
        t15 = Tex("64", font_size=14)
        t15.move_to(c15)
        self.wait()
        self.play(Write(c15, run_time=0.1), Write(t15, run_time=0.1))             

        self.wait()

        c16 = Square(side_length=0.5)
        c16.set_stroke(WHITE, width=2)
        c16.move_to(c14.get_right(),LEFT)
        t16 = Tex("8", font_size=14)
        t16.move_to(c16)
        self.play(Write(c16, run_time=0.1), Write(t16, run_time=0.1))          
        self.play(squares[63].animate.set_stroke(ORANGE, width=4))
        self.wait()
        for rice in rice_grains_cell_8:
            self.add(rice)
        c17 = Square(side_length=0.5)
        c17.set_stroke(WHITE, width=2)
        c17.move_to(c15.get_right(),LEFT)
        t17 = Tex("128", font_size=14)
        t17.move_to(c17)
        self.wait()
        self.play(Write(c17, run_time=0.1), Write(t17, run_time=0.1))          

        self.wait()

        c18 = Square(side_length=0.5)
        c18.set_stroke(WHITE, width=2)
        c18.move_to(c16.get_right(),LEFT)
        t18 = Tex("9", font_size=14)
        t18.move_to(c18)
        self.play(Write(c18, run_time=0.1), Write(t18, run_time=0.1))        
        self.play(squares[48].animate.set_stroke(ORANGE, width=4))
        self.wait()
        for rice in rice_grains_cell_9:
            self.add(rice)
        c19 = Square(side_length=0.5)
        c19.set_stroke(WHITE, width=2)
        c19.move_to(c17.get_right(),LEFT)
        t19 = Tex("256", font_size=14)
        t19.move_to(c19)
        self.wait()
        self.play(Write(c19, run_time=0.1), Write(t19, run_time=0.1))  

        self.wait()

        c20 = Square(side_length=0.5)
        c20.set_stroke(WHITE, width=2)
        c20.move_to(c18.get_right(),LEFT)
        t20 = Tex("10", font_size=14)
        t20.move_to(c20)
        self.play(Write(c20, run_time=0.1), Write(t20, run_time=0.1))          
        self.play(squares[49].animate.set_stroke(ORANGE, width=4))
        self.wait()
        for rice in rice_grains_cell_10:
            self.add(rice)
        c21 = Square(side_length=0.5)
        c21.set_stroke(WHITE, width=2)
        c21.move_to(c19.get_right(),LEFT)
        t21 = Tex("512", font_size=14)
        t21.move_to(c21)
        self.wait()
        self.play(Write(c21, run_time=0.1), Write(t21, run_time=0.1))
        
        texts_to_fade_in_out = VGroup(*texts)
        self.play(FadeOut(texts_to_fade_in_out))

        camera = self.camera
        frame = camera.frame
        frame.save_state()
        squares.scale(1.2)
        self.play(frame.animate.scale(2.5), run_time=2)

        self.wait(5)

        c22 = Square(side_length=0.5)
        c22.set_stroke(WHITE, width=2)
        c22.move_to(c20.get_right(),LEFT)
        t22 = Tex("11", font_size=14)
        t22.move_to(c22)
        self.play(Write(c22, run_time=0.1), Write(t22, run_time=0.1))        
        self.play(squares[50].animate.set_stroke(ORANGE, width=4))
        self.wait(3)
        for rice in rice_grains_cell_11:
            self.add(rice)

        self.play(frame.animate.scale(1.4))
        self.play(frame.animate.shift(UP*6))
        self.wait(7)
        squares.scale(0.83)
        self.play(Restore(frame))
        self.play(FadeIn(texts_to_fade_in_out))
        
        c23 = Square(side_length=0.5)
        c23.set_stroke(WHITE, width=2)
        c23.move_to(c21.get_right(),LEFT)
        t23 = Tex("1024", font_size=14)
        t23.move_to(c23)
        self.play(Write(c23, run_time=0.1), Write(t23, run_time=0.1))

        
        self.wait(16)

        c24 = Square(side_length=0.5)
        c24.set_stroke(WHITE, width=2)
        c24.move_to(c22.get_right(),LEFT)
        t24 = Tex("21", font_size=14)
        t24.move_to(c24)
        self.play(Write(c24, run_time=0.1), Write(t24, run_time=0.1))
        self.play(squares[44].animate.set_stroke(ORANGE, width=4))
        c25 = Square(side_length=0.5)
        c25.set_stroke(WHITE, width=2)
        c25.move_to(c23.get_right(),LEFT)
        t25 = Tex("??", font_size=14)
        t25.move_to(c25)
        self.play(Write(c25, run_time=0.5), Write(t25, run_time=0.5))

        self.wait(15)

        formula = Tex("A = P(1 + r)^t")
        formula.shift(UP*3.5 + RIGHT*2.5)
        def1 = Text("A: Amount", font_size = 24)
        def2 = Text("P: Principal", font_size=24)
        def3 = Text("r: Interest\n   rate (decimal)", font_size=24)
        def4 = Text("t: Time since\n   principal amount", font_size=24)
        def1.move_to(formula.get_right())
        def1.shift(RIGHT*1.5)
        def2.move_to(def1.get_bottom(), UP)
        def2.shift(DOWN*.1+RIGHT*0.05)
        def3.move_to(def2.get_bottom(), UP)
        def3.shift(DOWN*.1 + RIGHT*.30)
        def4.move_to(def3.get_left(), UL)
        def4.shift(DOWN*0.4)
        self.play(Write(formula, run_time=.5), Write(def1, run_time=.5),Write(def2, run_time=.5),Write(def3, run_time=.5),Write(def4, run_time=.5))

        self.wait(60)
        
        eq0 = Tex("=")
        eq0.move_to(formula.get_bottom(), UR)
        eq0.shift(LEFT*0.65 + DOWN*.2)
        self.wait(2)
        self.play(Write(eq0, run_time=.5))
        p0 = Tex("1")
        p0.move_to(formula.get_bottom())
        p0.shift(DOWN*.2+LEFT*.3)
        self.play(Write(p0, run_time=.5))
        r0 = Tex("(1+1)")
        r0.move_to(formula.get_bottom(),UL)
        self.wait(15)
        self.play(Write(r0, run_time=.5))
        time0 = Tex("21-1", font_size=24)
        time0.move_to(formula.get_bottom(), UL)
        time0.shift(RIGHT*1.35)
        self.wait(15)
        self.play(Write(time0, run_time=.1))
        eq1 = Tex("=")
        eq1.move_to(eq0.get_bottom())
        eq1.shift(DOWN*.5)
        self.wait()
        self.play(Write(eq1, run_time=.5))
        p1 = Tex("1")
        p1.move_to(p0.get_bottom())
        p1.shift(DOWN*.4)
        self.play(Write(p1, run_time=.1))
        r1 = Tex("(2)")
        r1.move_to(r0.get_bottom())
        r1.shift(DOWN*.3 + LEFT*.3)
        self.play(Write(r1, run_time=.5))
        time1 = Tex("20", font_size=24)
        time1.move_to(time0.get_bottom(), UR)
        time1.shift(DOWN*.4 + LEFT*.8)
        self.play(Write(time1, run_time=.5))
        eq2 = Tex("=")
        eq2.move_to(eq1.get_bottom())
        eq2.shift(DOWN*.5)
        self.play(Write(eq2, run_time=.5))
        answer1 = Tex("1,048,576", t2c={"1,048,576": YELLOW})
        answer2 = Text("grains of rice", font_size=28)
        answer3 = Text("(approx. 65 kg)", font_size=28)
        answer1.move_to(p1.get_bottom())
        answer1.shift(DOWN*.4 + RIGHT*1.15)
        answer2.move_to(answer1.get_bottom())
        answer2.shift(DOWN*.3)
        answer3.move_to(answer2.get_bottom())
        answer3.shift(DOWN*.3)
        self.wait(3)
        self.play(Write(answer1, run_time=.5), Write(answer2, run_time=.5), Write(answer3, run_time=.5))
        answer_mini = Tex("1,048,576", font_size=9)
        answer_mini.move_to(c25)
        self.wait(2)
        self.play(ReplacementTransform(t25, answer_mini))
        self.play(FadeOut(answer1), FadeOut(answer2), FadeOut(answer3))

        self.wait(15)
        time64 = Tex("64-1", font_size=24)
        time64.move_to(formula.get_bottom(), UL)
        time64.shift(RIGHT*1.35)
        time63 = Tex("63", font_size=24)
        time63.move_to(time0.get_bottom(), UR)
        time63.shift(DOWN*.4+LEFT*.8)

        self.play(ReplacementTransform(time0, time64), ReplacementTransform(time1, time63))

        self.wait(2)

        answer4 = Tex("9.2 * 10^{18}", t2c={"9.2 * 10^{18}": YELLOW})
        answer5 = Text("grains of rice", font_size=28)
        answer6 = Text("(approx. 100 BILLION tons)", font_size=28)
        answer4.move_to(p1.get_bottom())
        answer4.shift(DOWN*.4 + RIGHT*1.15)
        answer5.move_to(answer1.get_bottom())
        answer5.shift(DOWN*.3)
        answer6.move_to(answer2.get_bottom())
        answer6.shift(DOWN*.3)
        self.play(Write(answer4), Write(answer5, run_time=.1), Write(answer6, run_time=.5))        

        
        
            

        

    
            