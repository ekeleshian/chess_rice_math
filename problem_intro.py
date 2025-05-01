from manimlib import *


class Introduction(Scene):
    def construct(self):
        title = Text("The Power of Compound Interest")
        title.shift(UP*3.5)

        obj1 = Text("By the end of this lesson, you will be able to:", font_size=28)
        obj2 = Text("   1. Visually understand the power of compounding", font_size=28)
        obj3 = Text("   2. Use the compound interest formula to solve problems", font_size=28)
        obj = VGroup(obj1, obj2, obj3)
        obj.arrange(DOWN, aligned_edge=LEFT)
        obj.shift(UP*2 + LEFT*2.8)
        
        problem_title = Text("The Rice and Chessboard Problem", font_size=36, t2c={"The Rice and Chessboard Problem": BLUE_A}, t2w={"The Rice and Chessboard Problem":BOLD})
        problem_title.shift(UP*0.5)

        pt1_str = "There is a famous legend about the origin of chess.  When the inventor of the game showed it to "
        pt2_str = 'the emperor of India, the emperor was so impressed that he said to the man, "Name your reward!"'
        pt3_str = 'The man responded, "I only wish for this. Give me one grain of rice for the first square of the chessboard,'
        pt4_str = 'two grains for the next square, four for the next, eight for the next, and so on for all 64 squares, with'
        pt5_str = 'each square having double the number of grains as the square before."'
        pt6_str = 'The emperor laughs it off as a meager price for a brilliant invention. Was this a small price to pay after all?'
        pt7_str = "How many grains of rice will there be solely on the 11th square? On the 21st square? On the 64th square?"
        pt1 = Text(pt1_str, font_size=20, t2c = {pt1_str:BLUE_A})
        pt2 = Text(pt2_str, font_size=20, t2c = {pt2_str:BLUE_A})
        pt3 = Text(pt3_str, font_size=20, t2c = {pt3_str: BLUE_A})
        pt4 = Text(pt4_str, font_size=20, t2c = {pt4_str: BLUE_A})
        pt5 = Text(pt5_str, font_size=20, t2c = {pt5_str: BLUE_A})
        pt6 = Text(pt6_str, font_size=20, t2c = {pt6_str: BLUE_A})
        pt7 = Text(pt7_str, font_size=20, t2c = {pt7_str: BLUE_A})
        pt = VGroup(pt1, pt2, pt3, pt4, pt5, pt6, pt7)
        pt.arrange(DOWN, aligned_edge=LEFT)
        pt.shift(DOWN*1.5)

        self.play(Write(title))

        self.wait()
        
        self.play(Write(obj))

        self.wait(10)

        self.play(Write(problem_title))

        self.wait(5)

        self.play(Write(pt, run_time=.1))
        self.wait(60)

        

        

        
        
        
        
        