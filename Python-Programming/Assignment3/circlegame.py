import tkinter as tk
import random
from datetime import datetime
import time


def mouse_function(event):
    global clickcount
    global starttime
    
    if clickcount == 0:
        randtime = random.randint(10,20)
        time.sleep(randtime) 

        starttime = datetime.now()
        clickcount += 1
        myCanvas.create_oval(randx, randy, randx + 100, randy + 100, fill='red')        
    else:
        endtime = datetime.now()

        if (event.x - randx) > 0 and (event.x - randx) < 100 and (event.y - randy) > 0 and (event.y - randy) < 100:
            print("Hit")
        else:
            print("Miss")

        print(endtime - starttime)

root = tk.Tk()
myCanvas = tk.Canvas(root, bg="white", height=300, width=300)
myCanvas.bind("<Button-1>", mouse_function)

clickcount = 0
starttime = 0
randx = random.randint(0,200)
randy = random.randint(0,200)

myCanvas.pack()
root.mainloop()






