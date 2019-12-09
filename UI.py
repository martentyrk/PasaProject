import tkinter as tk
from PIL import ImageTk, Image
import webscraping as web

info = web.webscrape("https://www.amazon.com/PlayStation-4-Slim-1TB-Console/dp/B071CV8CG2/ref=sr_1_1?keywords=playstation+4&qid=1573324821&sr=8-1")
print(info)


productinfo_string = "Tere"

def userInterface():
    main = tk.Tk()
    main["bg"] = "#FFFFFF"
    main.geometry("600x400")
    main.title("Price tracker")

    canvas = tk.Canvas(main, width=main.winfo_width() * 600, height=main.winfo_height() * 400, bg="#25FE34")
    background = ImageTk.PhotoImage(Image.open("UIbackground.png").resize((600, 450)))
    background_label = tk.Label(canvas, image=background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1.0)

    productinfo_label = tk.Label(canvas, bg="#FFFFFF", width=43, height=10, text=productinfo_string)

    URLentry = tk.Entry(canvas, width=50, bd=0)
    URLentry.insert(0, "neti.ee")

    get_info_button = tk.Button(canvas, text="Get info", width=10)
    track_button = tk.Button(canvas, text="Track", width=10)

    productinfo_label.place(x=150, y=200)
    track_button.place(x=270, y=150)
    get_info_button.place(x=270, y=100)
    URLentry.place(x=150, y=50)
    canvas.place(x=0, y=0)
    main.minsize(600, 400)
    main.maxsize(600, 400)
    main.mainloop()


userInterface()
