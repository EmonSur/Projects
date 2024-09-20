from tkinter import *

root = Tk()
root.title("Lecture Demo")
#root.geometry("900x600")
root.maxsize(930,600)
root.config(bg="skyblue")

left_frame = Frame(root, width=200, height=580, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=10)
left_frame.grid_propagate(False)

right_frame = Frame(root, width=700, height=600, bg='red')
right_frame.grid(row=0, column=1)
right_frame.grid_propagate(False)

lab1 = Label(left_frame, text="Label 1").grid(column=0, row=0)
lab2 = Label(left_frame, text="Label 2").grid(column=0, row=1)


root.mainloop()