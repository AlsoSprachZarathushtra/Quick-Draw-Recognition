

import tkinter as tk
from PIL import Image, ImageDraw
from predict import Predictor

width = 512
height = 512

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.predictor = Predictor()
        self.x = self.y = 0
        self.canvas = tk.Canvas(self, width=width, height=height, cursor="cross")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.previous_x = None
        self.previous_y = None
        self.canvas.bind("<B1-Motion>", self.on_button_move)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.canvas.bind("<Button-3>",self.reset)
        # create draw stuff
        self.memImage = Image.new("L", (width, height), "white") #fill with white
        self.draw = ImageDraw.Draw(self.memImage)
        
#        self.after(500, func=self.train)

    def on_button_press(self, event):
        self.x = event.x
        self.y = event.y

    def on_button_move(self, event):

        if self.previous_x is None and self.previous_y is None:
            self.previous_x = event.x
            self.previous_y = event.y
        else:
            self.canvas.create_line((self.previous_x,self.previous_y),(event.x,event.y), width=10, fill='black')
            self.draw.line([self.previous_x, self.previous_y, event.x, event.y],fill='black',width=10)
            self.previous_x = event.x
            self.previous_y = event.y
#            kernel_size = 5
#            self.canvas.create_rectangle(event.x-kernel_size, event.y-kernel_size, event.x+kernel_size, event.y+kernel_size, fill="black")
#            self.draw.rectangle([event.x-kernel_size, event.y-kernel_size, event.x+kernel_size, event.y+kernel_size], fill="black")
       
    def on_button_release(self, event):
        #x0,y0 = (self.x, self.y)
        #x1,y1 = (event.x, event.y)
        self.memImage.save("tmp.png")
        result = self.predictor.predict(self.memImage)
        print(result)
        self.previous_x = None
        self.previous_y = None
        # reset canvas n stuff
        
    def reset(self,event):
        self.memImage = Image.new("L", (width, height), "white") #fill with white
        self.draw = ImageDraw.Draw(self.memImage)
        self.canvas.delete("all")
        #self.canvas.create_rectangle(x0,y0,x1,y1, fill="black")
           
    
    def task(self):
        self.after(2000, func=self.task)  # reschedule event in 2 seconds

app = Application()
app.mainloop()
