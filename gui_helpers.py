import tkinter as tk
from functools import partial

# Display First Screen to Select Which Quiz
class QuizOptionInterface:
    def __init__(self, quiz_list):
        self.window = tk.Tk()
        self.window.geometry("720x500")
        self.window.title("Select Quiz")

        self.quiz_list = quiz_list
        self.selected_quiz_name = None 

        self.light_blue = "#34A2FE"
        self.dark_blue = "#3458EB"
        self.gold = "#E6C35C"

        # put on frame to use pixel widths
        frame=tk.Frame(self.window, width=720, height=500)
        frame.pack()

        # header
        tk.Label(master=frame, fg="white", bg=self.dark_blue).place(x=0,y=0,width=720, height=100)
        tk.Label(master=frame, text="Select a Quiz", fg="white", bg=self.light_blue,font=("Times New Roman", 25)).place(x=10,y=10,width=700, height=80)

        # quiz options
        self.scroll_bar = tk.Scrollbar(master=frame, bg=self.light_blue)
        self.scroll_bar.place(x=660, y=110, width=30, height=300)
        
        self.mylist = tk.Listbox(master=frame, yscrollcommand=self.scroll_bar.set, font=("Times New Roman", 25))
        for quiz_item in quiz_list:
            self.mylist.insert(tk.END, quiz_item)
        self.mylist.place(x=80, y=110, width=580,height=300)

        self.scroll_bar.config(command = self.mylist.yview )

        # confirm button
        button = tk.Button(master=frame, text="Confirm", fg="white", bg=self.light_blue, font=("Times New Roman", 15))
        button.bind("<Button-1>", self.handle_button)
        button.place(x=310,y=430, width=100, height=50)

        self.window.mainloop()


    def handle_button(self, event):
        self.selected_quiz_name = self.quiz_list[self.mylist.curselection()[0]]
        self.window.destroy()
        

class QuizConfigInterface:
    def __init__(self, quiz_config):
        self.window = tk.Tk()
        self.window.geometry("720x800")
        self.window.title("Quiz Config Options")

        self.misc = quiz_config["misc"]
        self.single_checks = quiz_config['single_check']
        self.grouped_checks = quiz_config['grouped_check']
        self.number_inputs = quiz_config['number_value']

        self.light_blue = "#34A2FE"
        self.dark_blue = "#3458EB"
        self.gold = "#E6C35C"

        self.line_counts = []
        self.line_counts.append(len(self.single_checks))
        self.line_counts.append((len([option for group in self.grouped_checks for option in self.grouped_checks[group]]) + len(self.grouped_checks)))
        self.line_counts.append(len(self.number_inputs) * 2)
        self.x = 10
        self.pady = 10

        # put on frame to use pixel widths
        frame=tk.Frame(self.window, width=720, height=800)
        frame.pack()

        # header
        tk.Label(master=frame, fg="white", bg=self.dark_blue).place(x=0,y=0,width=720, height=100)
        tk.Label(master=frame, text="Quiz Config", fg="white", bg=self.light_blue,font=("Times New Roman", 25)).place(x=10,y=10,width=700, height=80)

        # single checks 
        single_frame = tk.Frame(master=frame, highlightbackground=self.dark_blue, highlightthickness=2)
        single_frame.place(x=self.x ,y=100+self.pady,width=720-self.x-self.x, height=self.line_counts[0] * 40)
        y = 0
        for option in self.single_checks:
            self.single_checks[option] = tk.StringVar(value=self.single_checks[option])
            tk.Checkbutton(master=single_frame, text=option, font=("Times New Roman", 15), anchor="w", variable=self.single_checks[option], onvalue="True", offvalue="False").place(x=10, y=y, width=500, height=30)
            y+=40

        # grouped checks
        group_frame = tk.Frame(master=frame, highlightbackground=self.dark_blue, highlightthickness=2)
        group_frame.place(x=self.x,y=100+40*self.line_counts[0]+self.pady*2,width=720-self.x-self.x, height=40*self.line_counts[1])
        y = 0
        for group_name in self.grouped_checks:
            tk.Label(master=group_frame, text=group_name, anchor="w", font=("Times New Roman", 15)).place(x=self.x, y=y, width=500, height=30)
            y+=40
            for option in self.grouped_checks[group_name]:
                self.grouped_checks[group_name][option] = tk.StringVar(value=self.grouped_checks[group_name][option])
                tk.Checkbutton(master=group_frame, text=option, font=("Times New Roman", 15), anchor="w", variable=self.grouped_checks[group_name][option], onvalue="True", offvalue="False").place(x=10, y=y, width=500, height=30)
                y+=40



        # number inputs
        number_frame = tk.Frame(master=frame, highlightbackground=self.dark_blue, highlightthickness=2)
        number_frame.place(x=self.x,y=100+40*(self.line_counts[0] + self.line_counts[1])+self.pady*3,width=720-self.x-self.x, height=self.line_counts[2] * 40)
        y = 0
        self.entries = {}
        for option in self.number_inputs:
            tk.Label(master=number_frame, text=option, anchor="w", font=("Times New Roman", 15)).place(x=self.x, y=y, width=500, height=30)
            y+=40
            self.entries[option] = tk.Entry(master=number_frame, fg="black", width=50)
            self.entries[option].insert(0, self.number_inputs["Number of Questions?"]["default_val"])
            self.entries[option].place(x=self.x, y=y, width=50, height=30)
            y+=40

        # confirm button
        button = tk.Button(master=frame, text="Confirm", fg="white", bg=self.light_blue, font=("Times New Roman", 15))
        button.bind("<Button-1>", self.handle_button)
        button.place(x=310,y=100+40*sum(self.line_counts)+self.pady*4, width=100, height=50)

        self.window.mainloop()

    def handle_button(self, event):
        # since check box results are stored as tkinter variables, go through each dictionary and replace variables with values
        for option in self.single_checks:
            self.single_checks[option] = self.single_checks[option].get()

        for label in self.grouped_checks:
            for option in self.grouped_checks[label]:
                self.grouped_checks[label][option] = self.grouped_checks[label][option].get()

        for option in self.entries:
            self.number_inputs[option] = self.entries[option].get()


        # put in same format as input config
        self.quiz_config = {"misc": self.misc,"single_check":self.single_checks, "grouped_check":self.grouped_checks, "number_value":self.number_inputs}
        self.window.destroy()
