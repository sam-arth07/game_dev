import tkinter as tk

class PlayComponent(object):
    def __init__(self,canvas,item):
        self.item = item
        self.canvas = canvas

    def move(self,x,y):
        self.canvas.move(self.item,x,y)

    def position(self):
        return self.canvas.coords(self.item)

    def delete(self):
        self.canvas.dele(self.item)

class Paddle(PlayComponent):
    def __init__(self, canvas, x, y):
        self.height = 5
        self.width = 100
        self.ball = None
        item = canvas.create_rectangle(x-self.width/2,
                                       y-self.height/2,
                                       x+self.width/2,
                                       y+self.height/2,
                                       fill = 'green')

        super(Paddle,self).__init__(canvas, item)

        def set_ball(self, ball):
            self.ball = ball

        def move(self,dist):
            coord = self.position()
            width = self.canvas.winfo_width()
            if coord[2] +dist <= width and coord[0] +dist >= 0:
                super(Paddle, self).move(dist, 0)
                if self.ball is not None:
                    self.ball.move(dist, 0)                            

class Game(tk.Frame):
    def __init__(self,master):
        super(Game,self).__init__(master)

        self.width = 1000
        self.height = 500

        self.canvas = tk.Canvas(self, bg ="cornsilk",
                                width = self.width,
                                height = self.height)
        self.canvas.pack()
        self.pack()

        self.items = {}
        self.paddle = Paddle(self.canvas, self.width/2,450)
        self.items[self.paddle.item] = self.paddle
        
        self.hud = None
        self.init_game()
        self.canvas.focus_set()
        self.canvas.bind('<Left>',lambda _:self.paddle.move(-30,0))
        self.canvas.bind('<Right>',lambda _:self.paddle.move(30,0))

    def start_game(self):
        self.canvas.unbind("<space>")
        self.paddle.ball = None

    def init_game(self):
        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("BRICK BREAKER")
    game = Game(root)
    game.mainloop()

