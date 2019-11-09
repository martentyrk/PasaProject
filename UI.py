import tkinter as tk
from PIL import ImageTk, Image


def userInterface():
    main = tk.Tk()
    main["bg"] = "#FFFFFF"
    main.geometry("600x400")

    canvas = tk.Canvas(main, width=main.winfo_width() * 600, height=main.winfo_height() * 400, bg="#25FE34")
    background = ImageTk.PhotoImage(Image.open("UIbackground.png").resize((600, 450)))
    background_label = tk.Label(canvas, image=background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1.0)

    URLentry = tk.Entry(canvas, width=50, bd=0)
    URLentry.insert(0, "neti.ee")

    URLentry.place(x=150, y=100)
    canvas.place(x=0, y=0)
    main.minsize(600, 400)
    main.maxsize(600, 400)
    main.mainloop()


userInterface()
