from turtle import Turtle

# create and move a paddle
# width = 20, height = 100, x_pos = 350, y_pos = 0
# create a paddle turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        # paddleの垂直方向を5倍にする。
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # move the paddle up and down
    # yの範囲が250と‐250: スクリーンの高さは 600 ピクセルであり、
    # パドルの高さが 100 ピクセルなので、上端の座標は 600/2 - 100/2 = 250 となります。
    # 同様に、下端の座標は -250 となります。
    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < 240:
            self.sety(new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > -240:
            self.sety(new_y)
