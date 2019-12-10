import tkinter as tk
from PIL import ImageTk, Image
import webscraping as web


def get_info():
    try:
        info = web.webscrape(URLentry.get())
        productinfo_string.set('\n'.join(['{0} : {1}'.format(k, v) for k, v in info.items()]))
    except:
        productinfo_string.set("Can't parse this URL")


main = tk.Tk()
main["bg"] = "#FFFFFF"
main.geometry("600x400")
main.title("Price tracker")
productinfo_string = tk.StringVar()
url = tk.StringVar()
canvas = tk.Canvas(main, width=main.winfo_width() * 800, height=main.winfo_height() * 600, bg="#25FE34")
background = ImageTk.PhotoImage(Image.open("UIbackground.png").resize((800, 600)))
background_label = tk.Label(canvas, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1.0)

URLentry = tk.Entry(canvas, width=50, bd=0)

productinfo_label = tk.Label(canvas, bg="#FFFFFF", width=65, height=15, wraplength=400, textvariable=productinfo_string)

URLentry.insert(0, "neti.ee")

get_info_button = tk.Button(canvas, text="Get info", width=10, command=get_info)
track_button = tk.Button(canvas, text="Track", width=10)

productinfo_label.place(x=175, y=300)
track_button.place(x=370, y=250)
get_info_button.place(x=370, y=200)
URLentry.place(x=250, y=150)
canvas.place(x=0, y=0)
main.minsize(800, 600)
main.maxsize(800, 600)
main.mainloop()
