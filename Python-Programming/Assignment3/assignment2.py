import tkinter as tk
from tkinter import messagebox

class SimplePaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Just a Simple Paint Tool")
        self.controlPanelBg = '#1E1E1E'
        self.textColour = '#D4D4D4'
        self.buttonColours = {
            "Red": "#F44747",
            "Blue": "#569CD6",
            "Yellow": "#DCDCAA"
        }
        self.selectedColour = None
        self.selectedShape = None
        self.controlPanel = tk.Frame(root, bg=self.controlPanelBg, width=200)
        self.controlPanel.grid(row=0, column=0, padx=10, pady=5)
        self.canvasFrame = tk.Frame(root, bg='white', width=600, height=600)
        self.canvasFrame.grid(row=0, column=1, padx=10, pady=5)
        self.canvas = tk.Canvas(self.canvasFrame, bg="white", width=600, height=600)
        self.canvas.bind("<Button-1>", self.onCanvasClick)
        self.canvas.pack()
        self.setupSelectionButtons()
        tk.Button(self.controlPanel, text="Clear Canvas", fg=self.textColour, bg="#C586C0",
                  command=self.clearCanvas).pack(pady=10)
        self.startX = None
        self.startY = None

    def setupSelectionButtons(self):
        tk.Label(self.controlPanel, text="Colour", bg=self.controlPanelBg, fg=self.textColour, font=("Arial", 12)).pack()
        for colourText, colourValue in self.buttonColours.items():
            tk.Button(self.controlPanel, text=colourText, fg=self.textColour, bg=colourValue,
                      command=lambda c=colourText: self.setSelectedColour(c)).pack(fill=tk.X)
        self.colourLabel = tk.Label(self.controlPanel, bg=self.controlPanelBg, fg=self.textColour, text="Selected Colour: None")
        self.colourLabel.pack()
        tk.Label(self.controlPanel, text="Shape", bg=self.controlPanelBg, fg=self.textColour, font=("Arial", 12)).pack()
        for shape in ["Line", "Rectangle", "Oval"]:
            tk.Button(self.controlPanel, text=shape, fg=self.textColour, bg="#4EC9B0",
                      command=lambda s=shape: self.setSelectedShape(s.lower())).pack(fill=tk.X)
        self.shapeLabel = tk.Label(self.controlPanel, bg=self.controlPanelBg, fg=self.textColour, text="Selected Shape: None")
        self.shapeLabel.pack()

    def setSelectedColour(self, colour):
        self.selectedColour = self.buttonColours[colour]
        self.colourLabel.config(text="Selected Colour: %s" % colour)

    def setSelectedShape(self, shape):
        self.selectedShape = shape
        self.shapeLabel.config(text="Selected Shape: %s" % shape)

    def clearCanvas(self):
        self.canvas.delete("all")

    def onCanvasClick(self, event):
        if self.selectedShape is None or self.selectedColour is None:
            messagebox.showerror("Error", "Please select a shape and a colour first.")
            return

        if self.startX is None and self.startY is None:
            self.startX, self.startY = event.x, event.y
        else:
            self.drawShape(self.startX, self.startY, event.x, event.y)
            self.startX, self.startY = None, None

    def drawShape(self, x1, y1, x2, y2):
        shapeFunctions = {
            "line": self.canvas.create_line,
            "rectangle": self.canvas.create_rectangle,
            "oval": self.canvas.create_oval
        }

        if self.selectedShape not in shapeFunctions:
            messagebox.showerror("Error", "Invalid shape selected.")
            return

        draw = shapeFunctions[self.selectedShape]
        draw(x1, y1, x2, y2, fill=self.selectedColour)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimplePaintApp(root)
    root.mainloop()



















