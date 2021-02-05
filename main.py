import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfile
from PIL import Image, ImageFile


current_x, current_y = 0, 0
color = "white"


def locate_xy(location):
    global current_x, current_y
    current_x, current_y = location.x, location.y


def add_line(location):
    global current_x, current_y
    canvas.create_line(
        (current_x, current_y, location.x, location.y), fill=color)
    current_x, current_y = location.x, location.y


def show_color(new_color):
    global color
    color = new_color


def new_canvas():
    canvas.delete("all")
    display_palette()


def rectangle(location):
    global current_x, current_y
    canvas.create_rectangle(current_x, current_y,
                            location.x, location.y, fill=color)
    current_x, current_y = location.x, location.y


def save_as():
    files = [("All Files", "*.*"),
             ("JPG File", "*.jpg"),
             ("Python File", "*.py"),
             ("Text Document", "*.txt"),
             ("PNG File", "*.png")]
    file = asksaveasfile(filetypes=files, defaultextension="*.png")


def display_palette():
    id = canvas.create_rectangle(800, 970, 830, 1000, fill="white")
    canvas.tag_bind(id, "<Button-1>", lambda x: show_color("white"))

    id = canvas.create_rectangle(840, 970, 870, 1000, fill="blue")
    canvas.tag_bind(id, "<Button-1>", lambda x: show_color("blue"))

    id = canvas.create_rectangle(880, 970, 910, 1000, fill="red")
    canvas.tag_bind(id, "<Button-1>", lambda x: show_color("red"))

    id = canvas.create_rectangle(920, 970, 950, 1000, fill="orange")
    canvas.tag_bind(id, "<Button-1>", lambda x: show_color("orange"))

    id = canvas.create_rectangle(960, 970, 990, 1000, fill="yellow")
    canvas.tag_bind(id, "<Button-1>", lambda x: show_color("yellow"))

    id = canvas.create_rectangle(1000, 970, 1030, 1000, fill="green")
    canvas.tag_bind(id, "<Button-1>", lambda x: show_color("green"))


window = tk.Tk()

width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("Black Board")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

menubar = Menu(window)
window.config(menu=menubar)
submenu1 = Menu(menubar, tearoff=0)
submenu2 = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=submenu1)
submenu1.add_command(label="New File", command=new_canvas)
submenu1.add_command(label="Save as", command=save_as)

menubar.add_cascade(label="Shapes", menu=submenu2)
submenu2.add_command(label="Rectangle", command=rectangle)


canvas = Canvas(window, background="black")
canvas.grid(row=0, column=0, sticky="nsew")

canvas.bind("<Button-1>", locate_xy)
canvas.bind("<B1-Motion>", add_line)
display_palette()

window.mainloop()
