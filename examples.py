from manimlib import *


class ChessBoard(Scene):
    def construct(self):
        def create_rice_grains(total, start_x, start_y, start_z=0, rotate = False, color=WHITE):
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

        def move_rice_grains(rice_grains):
            new_coords = []
            # cell_delta = [-1, -0.7, -0.5, -0.2, 0, 0.2]
            cell_delta = [-.8, -0.6, -0.4, -0.1, 0.2, 0.4]

            for cell_idx, cell in enumerate(rice_grains):
                prev_x = 0
                start_x = 0
                start_y = -2
                for i, rice in enumerate(cell):
                    if i == 0:
                        start_x = rice.get_x() + cell_delta[cell_idx]
                        new_coords.append([start_x, start_y, 0.5])
                        prev_x = start_x
                    elif (i)%8 == 0:
                        start_y += 0.18
                        new_coords.append([start_x, start_y, 0.5])
                        prev_x = start_x
                    else:
                        new_coords.append([prev_x + 0.05, start_y, 0.5])
                        prev_x += 0.05

            return new_coords
            
            
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
        self.wait()
        rice_grains_cell_1 = create_rice_grains(1, -3.8, -2.08, rotate=True)
        rice_grains_cell_2 = create_rice_grains(2, -2.9, -2.08, rotate=True)
        rice_grains_cell_3 = create_rice_grains(4, -1.9, -2.08, rotate=True)
        rice_grains_cell_4 = create_rice_grains(8, -0.8, -2.08, rotate=True)
        rice_grains_cell_5 = create_rice_grains(16, 0.4, -2.08, rotate=True)
        rice_grains_cell_6 = create_rice_grains(32, 1.3, -2.08, rotate=True)

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
            
            self.play(Write(text), run_time=0.01)


        self.play(squares[56].animate.set_stroke(ORANGE, width=4))
        for rice in rice_grains_cell_1:
            self.add(rice)

        self.wait(2)

        self.play(squares[57].animate.set_stroke(ORANGE, width=4))
        for rice in rice_grains_cell_2:
            self.add(rice)

        self.wait(2)
        
        self.play(squares[58].animate.set_stroke(ORANGE, width=4))
        for rice in rice_grains_cell_3:
            self.add(rice)

        self.wait(2)

        self.play(squares[59].animate.set_stroke(ORANGE, width=4))
        for rice in rice_grains_cell_4:
            self.add(rice)

        self.wait(2)

        self.play(squares[60].animate.set_stroke(ORANGE, width=4))
        for rice in rice_grains_cell_5:
            self.add(rice)

        self.wait(2)

        self.play(squares[61].animate.set_stroke(ORANGE, width=4))
        for rice in rice_grains_cell_6:
            self.add(rice)

        self.wait(2)

        # total_rice = [rice_grains_cell_1] + [rice_grains_cell_2] + [rice_grains_cell_3] + [rice_grains_cell_4] + [rice_grains_cell_5] + [rice_grains_cell_6]
        # new_coords = move_rice_grains(total_rice)
        # total_rice_flat = []
        # for cell in total_rice:
        #     for rice in cell:
        #         total_rice_flat.append(rice)
        # move_animations = [ApplyMethod(VGroup(rice).move_to, direction) for rice, direction in zip(total_rice_flat,new_coords)]

        # self.play(*move_animations)

        # rotate_animations = [ApplyMethod(VGroup(total_rice_flat).rotate, PI/3, LEFT)]

        # self.play(*rotate_animations)

        rice_grains_cell_7 = create_rice_grains(64, 2.45, -2, start_z=0, rotate=True)
        # rice_grains_cell_7 = create_rice_grains(64, 2.3, -2, start_z=0, rotate=True)

        rice_grains_cell_8 = create_rice_grains(128, 3.6, -2, start_z=0, rotate=True)
        # rice_grains_cell_8 = create_rice_grains(128, 3.5, -2, start_z=0, rotate=True)
        
        rice_grains_cell_9 = create_rice_grains(256, -3.7, -1.3, start_z=0, rotate=True, color=YELLOW)
        # rice_grains_cell_9 = create_rice_grains(256, -3.8, -1.3, start_z=0, rotate=True, color=YELLOW)

        rice_grains_cell_10 = create_rice_grains(512, -2.7, -1.3, start_z=0, rotate=True, color=YELLOW)
        # rice_grains_cell_10 = create_rice_grains(512, -2.85, -1.3, start_z=0, rotate=True, color=YELLOW)
        
        rice_grains_cell_11 = create_rice_grains(1024, -1.85, -1.3, start_z=0, rotate=True, color=YELLOW)
        # rice_grains_cell_11 = create_rice_grains(1024, -1.9, -1.3, start_z=0, rotate=True, color=YELLOW)
        
                                                
        for rice in rice_grains_cell_7:
            self.add(rice)
            

        self.wait(2)

        for rice in rice_grains_cell_8:
            self.add(rice)
        
        self.wait()

        for rice in rice_grains_cell_9:
            self.add(rice)

        self.wait()

        for rice in rice_grains_cell_10:
            self.add(rice)

        camera = self.camera
        frame = camera.frame
        frame.save_state()
        squares.scale(1.2)
        self.play(frame.animate.scale(2.5))


        self.wait()
        for rice in rice_grains_cell_11:
            self.add(rice)

        self.play(frame.animate.scale(1.3))
        self.play(frame.animate.shift(UP*4))
        self.wait(2)
        squares.scale(0.85)
        self.play(Restore(frame))
        

        
        self.embed()

    
            