import tkinter as tk

def UserInterface():
    main = tk.Tk()
    main["bg"] = "#FFFFFF"


    rootWidth = main.winfo_width()
    rootHeight = main.winfo_height()
    c = tk.Canvas(main,cursor="leftbutton", width=rootWidth + 500, height=rootHeight+300, bg="#9CBEC1", confine=True)
    entry = tk.Entry(main)

    entry.insert(0, "neti.ee")

    entry.pack()
    c.pack(expand=True)
    main.minsize(600, 400)
    main.maxsize(800, 600)
    main.mainloop()


