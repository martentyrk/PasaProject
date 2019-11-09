import tkinter as tk

def userInterface():
    main = tk.Tk()
    main["bg"] = "#FFFFFF"


    rootWidth = main.winfo_width()
    rootHeight = main.winfo_height()
    canvas = tk.Canvas(main,cursor="leftbutton", width=rootWidth + 500, height=rootHeight+300, bg="#9CBEC1", confine=True)
    entry = tk.Entry(main)
    background = tk.PhotoImage(file="UIbackground.png")
    background_label = tk.Label(canvas, image=background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    entry.insert(0, "neti.ee")

    entry.pack()
    canvas.pack(expand=True)
    main.minsize(600, 400)
    main.maxsize(600, 400)
    main.mainloop()

userInterface()

