import tkinter as tk

root = tk.Tk()
root.title(" RR  Simple Text on Canvas")

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Draw text on the canvas at coordinates (x=50, y=50)
canvas.create_text(50, 50, text="RRRRRR")

root.mainloop()
