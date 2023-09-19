import tkinter as tk

"""
Docs: https://tkdocs.com/tutorial/index.html 
Widgets: https://tkdocs.com/tutorial/widgets.html and https://tkdocs.com/tutorial/morewidgets.html 
Colors: https://www.tcl.tk/man/tcl/TkCmd/colors.html 
Events: https://python-course.eu/tkinter/events-and-binds-in-tkinter.php  
Tutorial: https://realpython.com/python-gui-tkinter/#the-grid-geometry-manager 
"""

window = tk.Tk()

# widgets
greeting = tk.Label(text="Hello, Tkinter", fg="white", bg="#34A2FE",width=10,height=10)
button = tk.Button(text="Click me!", width=25, height=5, bg="blue", fg="yellow")
entry = tk.Entry(fg="yellow", bg="blue", width=50)


# interaction
def handle_keypress(event):
    print(event.char)

def handle_buttonpressleft(event):
    print("Left!")

def handle_buttonpressright(event):
    print("Right!")
    
def handle_entertext(event):
    print(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, "Thanks!")

greeting.pack()
button.pack()
entry.pack()
window.bind("<Key>", handle_keypress)
button.bind("<Button-1>", handle_buttonpressleft)
button.bind("<Button-3>", handle_buttonpressright)
window.bind("<Return>", handle_entertext)

window.mainloop()

###################################################################

window = tk.Tk()

# frame effects
border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()


window.mainloop()
######################################################################

window = tk.Tk()

# set width and height
frame1 = tk.Frame(master=window, width=100, height=50, bg="red")
frame1.pack()

# fill window in either direction x or y
frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.Y)

# add from a direction
frame3 = tk.Frame(master=window, width=50, height=50, bg="blue")
frame3.pack(side=tk.RIGHT)

#frame.pack(expand = BOTH) to make responsive

window.mainloop()


######################################################################

window = tk.Tk()

frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)

window.mainloop()

#######################################################################

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=i, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)


    window.rowconfigure(0, minsize=50)
    window.columnconfigure([0, 1, 2, 3], minsize=50)

    label1 = tk.Label(text="1", bg="black", fg="white")
    label2 = tk.Label(text="2", bg="black", fg="white")
    label3 = tk.Label(text="3", bg="black", fg="white")
    label4 = tk.Label(text="4", bg="black", fg="white")

    label1.grid(row=0, column=0)
    label2.grid(row=0, column=1, sticky="ew")
    label3.grid(row=0, column=2, sticky="ns")
    label4.grid(row=0, column=3, sticky="nsew")

window.mainloop()