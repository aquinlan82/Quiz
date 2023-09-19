import tkinter as tk
from functools import partial

# Display First Screen to Select Which Quiz
class QuizOptionInterface:
    def __init__(self, quiz_list):
        self.window = tk.Tk()
        #self.window.geometry("720x200")
        self.window.title("Quiz")

        self.quiz_list = quiz_list
        self.selected_quiz_name = None 

        # header
        label = tk.Label(master=self.window, text="Select a Quiz", fg="white", bg="#34A2FE",width=50,height=5)
        label.grid(row=0, column=0)

        # quiz options
        frame = tk.Frame(master=self.window)
        frame.grid(row=1, column=0)

        self.scroll_bar = tk.Scrollbar(master=frame)
        self.scroll_bar.pack(side=tk.RIGHT)
        
        self.mylist = tk.Listbox(master=frame, yscrollcommand=self.scroll_bar.set)
        for quiz_item in quiz_list:
            self.mylist.insert(tk.END, quiz_item)
        
        self.mylist.pack(side=tk.LEFT, fill=tk.BOTH )
        self.scroll_bar.config(command = self.mylist.yview )

        # confirm button
        button = tk.Button(master=self.window, text="Confirm")
        button.bind("<Button-1>", self.handle_button)
        button.grid(row=2, column=0)

        self.window.mainloop()


    def handle_button(self, event):
        self.selected_quiz_name = self.quiz_list[self.mylist.curselection()[0]]
        self.window.destroy()
        




class QuizConfigInterface:
    def __init__(self, quiz_config):
        self.window = tk.Tk()
        self.single_checks = quiz_config['single_check']
        self.grouped_checks = quiz_config['grouped_check']
        self.number_inputs = quiz_config['number_value']

        # header
        greeting = tk.Label(text="This is a different Screen!", fg="white", bg="#34A2FE",width=10,height=10)
        greeting.pack()

        # single checks 
        for option in self.single_checks:
            self.single_checks[option] = tk.StringVar(value=self.single_checks[option])
            checkbox = tk.Checkbutton(self.window, text='Python',variable=self.single_checks[option], onvalue="True", offvalue="False")
            checkbox.pack()

        # grouped checks
        for group_name in self.grouped_checks:
            tk.Label(master=self.window, text=group_name).pack()
            for option in self.grouped_checks[group_name]:
                self.grouped_checks[group_name][option] = tk.StringVar(value=self.grouped_checks[group_name][option])
                checkbox = tk.Checkbutton(self.window, text='Python',variable=self.grouped_checks[group_name][option], onvalue="True", offvalue="False")
                checkbox.pack()


        # number inputs
        self.entries = {}
        for option in self.number_inputs:
            self.number_inputs[option] = tk.IntVar(value=self.number_inputs[option])
            tk.Label(master=self.window, text=option).pack()
            self.entries[option] = tk.Entry(master=self.window, fg="yellow", bg="blue", width=50)
            self.entries[option].pack()

        # confirm button
        button = tk.Button(text="Dont click me!", width=25, height=5, bg="green", fg="red")
        button.bind("<Button-1>", self.handle_button)
        button.pack()

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
        self.quiz_config = {"single_check":self.single_checks, "grouped_check":self.grouped_checks, "number_value":self.number_inputs}

        self.window.destroy()
