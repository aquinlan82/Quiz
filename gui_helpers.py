import tkinter as tk
from functools import partial
from PIL import ImageTk, Image  

# Display first screen to select quiz
class QuizOptionInterface:
    def __init__(self, quiz_list):
        self.window = tk.Tk()
        self.window.geometry("720x500")
        self.window.title("Select Quiz")
        self.window.bind("<Return>", self.handle_button)

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
        self.mylist.bind("<Double-1>", self.handle_button)

        self.scroll_bar.config(command = self.mylist.yview )

        # confirm button
        button = tk.Button(master=frame, text="Confirm", fg="white", bg=self.light_blue, font=("Times New Roman", 15))
        button.bind("<Button-1>", self.handle_button)
        button.place(x=310,y=430, width=100, height=50)

        self.window.mainloop()


    def handle_button(self, event):
        self.selected_quiz_name = self.quiz_list[self.mylist.curselection()[0]]
        self.window.destroy()
        
# Display settings for the chosen quiz
class QuizConfigInterface:
    def __init__(self, quiz_config):
        if "special" in quiz_config["misc"]["type"]:
            self.quiz_config = quiz_config
            return

        print("hi")

        self.window = tk.Tk()
        self.window.geometry("720x830")
        self.window.title("Quiz Config Options")
        self.window.bind("<Return>", self.handle_button)

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
        frame=tk.Frame(self.window, width=720, height=830)
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

# The quiz itself
class TextQuizInterface:
    def __init__(self, quiz_name, quiz_config, quiz_df):
        self.window = tk.Tk()
        self.window.geometry("720x530")
        self.window.title(quiz_name)

        self.quiz_name = quiz_name
        self.quiz_config = quiz_config
        self.quiz_df = quiz_df

        self.light_blue = "#34A2FE"
        self.dark_blue = "#3458EB"
        self.gold = "#E6C35C"

        self.index = 0

        self.finished_count = 0
        self.correct_count = 0
        self.incorrect_count = 0

        self.phase = "To Answer"
        self.quiz_df["Correct"] = True


        # put on frame to use pixel widths
        self.frame=tk.Frame(self.window, width=720, height=530)
        self.frame.pack()

        # header
        tk.Label(master=self.frame, fg="white", bg=self.dark_blue).place(x=0,y=0,width=720, height=100)
        tk.Label(master=self.frame, text=quiz_name, fg="white", bg=self.light_blue,font=("Times New Roman", 25)).place(x=10,y=10,width=700, height=80)

        # Q and A
        self.qbox = tk.Label(master=self.frame, text = self.quiz_df.iloc[self.index]["Axis 1"], font=("Times New Roman", 25), anchor="w")
        self.qbox.place(x=10,y=100,width=720, height=100)
        self.abox = tk.Entry(master=self.frame, bg="white", font=("Times New Roman", 25))
        self.abox.place(x=10,y=170,width=700, height=60)
        self.abox.bind("<Return>", self.handle_enter)

        # footer
        tk.Label(master=self.frame, bg=self.dark_blue).place(x=0,y=490,width=720, height=40)
        tk.Label(master=self.frame, bg=self.light_blue).place(x=5,y=495,width=710, height=30)
        self.finished_count_label = tk.Label(master=self.frame, text="0/"+str(len(self.quiz_df)), bg=self.light_blue, fg="white", font=("Times New Roman", 15))
        self.finished_count_label.place(x=10,y=500,width=80, height=20)
        self.correct_count_label = tk.Label(master=self.frame, text="Correct: 0", bg=self.light_blue, fg="white", font=("Times New Roman", 15))
        self.correct_count_label.place(x=300,y=500,width=100, height=20)
        self.incorrect_count_label = tk.Label(master=self.frame, text="Incorrect: 0", bg=self.light_blue, fg="white", font=("Times New Roman", 15))
        self.incorrect_count_label.place(x=590,y=500,width=100, height=20)

        self.window.mainloop()

    # move to next question by deleting feedback widgets and incrementing through df
    def updateQA(self, used_labels):
        self.index += 1
        if self.index == len(self.quiz_df):
            self.window.destroy()
            return
        self.qbox.config(text = self.quiz_df.iloc[self.index]["Axis 1"])
        self.abox.delete(0, tk.END)

        for label in used_labels:
            label.destroy()

        self.finished_count_label.config(text=str(self.finished_count)+"/"+str(len(self.quiz_df)))
        self.correct_count_label.config(text="Correct: "+str(self.correct_count))
        self.incorrect_count_label.config(text="Incorrect: "+str(self.incorrect_count))

    # When question is answered, move to next question OR check if correct and add widgets for feedback
    def handle_answer(self):
        if str.lower(self.abox.get()) == str.lower(str(self.quiz_df.iloc[self.index]["Axis 2"])):
            self.finished_count += 1
            self.correct_count += 1

            correct_label_temp = tk.Label(master=self.frame, text="Correct!", fg="green", font=("Times New Roman", 25), anchor="w", highlightbackground="green", highlightthickness=3)
            correct_label_temp.place(x=50,y=260,width=130, height=80)
            correct_label_temp.after(500, partial(self.updateQA, [correct_label_temp]))
        else:
            self.finished_count += 1
            self.incorrect_count += 1
            self.quiz_df.at[self.index,"Correct"] = False

            self.incorrect_label_temp = tk.Label(master=self.frame, text="Incorrect :(", fg="red", font=("Times New Roman", 25), anchor="w", highlightbackground="red", highlightthickness=3)
            self.incorrect_label_temp.place(x=50,y=260,width=170, height=80)

            self.answer_label_temp = tk.Label(master=self.frame, text=self.quiz_df.iloc[self.index]["Axis 2"], fg="black", font=("Times New Roman", 25), anchor="w")
            self.answer_label_temp.place(x=250,y=260,width=770, height=80)

            self.phase = "To Move On"

    # Enter can be used to trigger two events:
    #   If a question was just answered it should be checked and setup next screen based on correctness
    #   If a previous question was wrong then enter is pressed to move to next question
    def handle_enter(self, event):
        if self.phase == "To Answer":
            self.handle_answer()
        elif self.phase == "To Move On":
            self.phase = "To Answer"
            self.updateQA([self.incorrect_label_temp, self.answer_label_temp])

# The quiz itself

class ImageQuizInterface:
    def __init__(self, quiz_name, quiz_config, quiz_df):
        self.window = tk.Tk()
        self.window.title(quiz_name)
        self.h = 500
        self.w = 720
        if "window_width" in quiz_config["misc"]:
            self.w = quiz_config["misc"]["window_width"]
        if "window_height" in quiz_config["misc"]:
            self.h = quiz_config["misc"]["window_height"]

        self.window.geometry(str(self.w) + "x" + str(self.h))
        self.quiz_name = quiz_name
        self.quiz_config = quiz_config
        self.quiz_df = quiz_df

        self.light_blue = "#34A2FE"
        self.dark_blue = "#3458EB"
        self.gold = "#E6C35C"

        self.index = 0

        self.finished_count = 0
        self.correct_count = 0
        self.incorrect_count = 0

        self.phase = "To Answer"
        self.quiz_df["Correct"] = True


        # put on frame to use pixel widths
        self.frame=tk.Frame(self.window, width=self.w, height=self.h)
        self.frame.pack()

        # header
        tk.Label(master=self.frame, fg="white", bg=self.dark_blue).place(x=0,y=0,width=self.w, height=100)
        tk.Label(master=self.frame, text=quiz_name, fg="white", bg=self.light_blue,font=("Times New Roman", 25)).place(x=10,y=10,width=self.w-20, height=80)

        # Q and A
        flag_img = self.get_image()
        self.qbox = tk.Label(self.frame, image = flag_img)
        self.qbox.place(x=10,y=110,width=self.w-20, height=self.h-300)   #self.h -100 from top -180 from bottom -20 for buffer

        self.abox = tk.Entry(master=self.frame, bg="white", font=("Times New Roman", 25))
        self.abox.place(x=10,y=self.h-180,width=self.w-20, height=60)
        self.abox.bind("<Return>", self.handle_enter)

        # footer
        tk.Label(master=self.frame, bg=self.dark_blue).place(x=0,y=self.h - 40,width=self.w, height=40)
        tk.Label(master=self.frame, bg=self.light_blue).place(x=5,y=self.h - 35,width=self.w-10, height=30)
        self.finished_count_label = tk.Label(master=self.frame, text="0/"+str(len(self.quiz_df)), bg=self.light_blue, fg="white", font=("Times New Roman", 15))
        self.finished_count_label.place(x=self.w*0.014,y=self.h - 30,width=80, height=20)
        self.correct_count_label = tk.Label(master=self.frame, text="Correct: 0", bg=self.light_blue, fg="white", font=("Times New Roman", 15))
        self.correct_count_label.place(x=self.w*0.418,y=self.h - 30,width=100, height=20)
        self.incorrect_count_label = tk.Label(master=self.frame, text="Incorrect: 0", bg=self.light_blue, fg="white", font=("Times New Roman", 15))
        self.incorrect_count_label.place(x=self.w*0.819,y=self.h - 30,width=100, height=20)

        self.window.mainloop()

    # move to next question by deleting feedback widgets and incrementing through df
    def updateQA(self, used_labels):
        self.index += 1
        if self.index == len(self.quiz_df):
            self.window.destroy()
            return
        self.abox.delete(0, tk.END)

        flag_img = self.get_image()
        self.qbox.config(image=flag_img)
        self.qbox.image = flag_img

        for label in used_labels:
            label.destroy()

        self.finished_count_label.config(text=str(self.finished_count)+"/"+str(len(self.quiz_df)))
        self.correct_count_label.config(text="Correct: "+str(self.correct_count))
        self.incorrect_count_label.config(text="Incorrect: "+str(self.incorrect_count))

    # When question is answered, move to next question OR check if correct and add widgets for feedback
    def handle_answer(self):
        if str.lower(self.abox.get()) == str.lower(self.quiz_df.iloc[self.index]["Axis 2"]):
            self.finished_count += 1
            self.correct_count += 1

            correct_label_temp = tk.Label(master=self.frame, text="Correct!", fg="green", font=("Times New Roman", 25), anchor="w", highlightbackground="green", highlightthickness=3)
            correct_label_temp.place(x=50,y=self.h-100,width=130, height=30)
            correct_label_temp.after(500, partial(self.updateQA, [correct_label_temp]))
        else:
            self.finished_count += 1
            self.incorrect_count += 1
            self.quiz_df.at[self.index,"Correct"] = False

            self.incorrect_label_temp = tk.Label(master=self.frame, text="Incorrect :(", fg="red", font=("Times New Roman", 25), anchor="w", highlightbackground="red", highlightthickness=3)
            self.incorrect_label_temp.place(x=30,y=self.h-100,width=130, height=30)

            self.answer_label_temp = tk.Label(master=self.frame, text=self.quiz_df.iloc[self.index]["Axis 2"], fg="black", font=("Times New Roman", 25), anchor="w")
            self.answer_label_temp.place(x=300,y=self.h-100,width=700, height=30)

            self.phase = "To Move On"

            self.override_button = tk.Button(master=self.frame, text="O", fg="white", bg=self.dark_blue, font=("Times New Roman", 15))
            self.override_button.bind("<Button-1>", self.handle_override)
            self.override_button.place(x=self.w - 60,y=self.h-100, width=50, height=50)

    def handle_override(self, event):
        self.quiz_df.at[self.index,"Correct"] = True
        self.incorrect_count -= 1
        self.correct_count += 1

        self.phase = "To Answer"
        self.updateQA([self.incorrect_label_temp, self.answer_label_temp, self.override_button])
        


    # Enter can be used to trigger two events:
    #   If a question was just answered it should be checked and setup next screen based on correctness
    #   If a previous question was wrong then enter is pressed to move to next question
    def handle_enter(self, event):
        if self.phase == "To Answer":
            self.handle_answer()
        elif self.phase == "To Move On":
            self.phase = "To Answer"
            self.updateQA([self.incorrect_label_temp, self.answer_label_temp])


    def get_image(self):
        path = "data/"+self.quiz_name+"/images/"+self.quiz_df.iloc[self.index]["Axis 1"]
        img = Image.open(path)
        cur_size = list(img.size)
        max_size = [self.w-20, self.h-300]
        ratio = min([max_size[0] / cur_size[0], max_size[1] / cur_size[1]])
        new_size = (int(cur_size[0] * ratio), int(cur_size[1] * ratio))
        flag_img = ImageTk.PhotoImage(img.resize(new_size))
        return flag_img

# Display results
class ResultsInterface:
    def __init__(self, quiz_results):
        self.window = tk.Tk()
        self.window.geometry("720x300")
        self.window.title("Results")

        self.light_blue = "#34A2FE"
        self.dark_blue = "#3458EB"
        self.gold = "#E6C35C"

        self.finished_count = quiz_results.finished_count
        self.correct_count = quiz_results.correct_count

        self.redo = False

        # put on frame to use pixel widths
        frame=tk.Frame(self.window, width=720, height=300)
        frame.pack()

        # header
        tk.Label(master=frame, fg="white", bg=self.dark_blue).place(x=0,y=0,width=720, height=100)
        tk.Label(master=frame, text="Results", fg="white", bg=self.light_blue,font=("Times New Roman", 25)).place(x=10,y=10,width=700, height=80)

        # adaptive message
        if self.finished_count > 0:
            perc = self.correct_count / self.finished_count
            text = "Snarky Message Here"
            if perc == 1:
                "Perfect Score!"
            elif perc > 0.9:
                text = "Nice :)"
            elif perc > 0.5:
                text = "Meh"
            elif perc > 0.3:
                text = "... You Tried"
            else:
                text = "That's rough, buddy"
            tk.Label(master=frame, text=text, fg="black",font=("Times New Roman", 25)).place(x=10,y=100,width=700, height=80)

        # score
        tk.Label(master=frame, text=str(self.correct_count) + "/" + str(self.finished_count), fg="black",font=("Times New Roman", 25)).place(x=10,y=150,width=700, height=80)

        # redo button
        button = tk.Button(master=frame, text="Redo Incorrect Questions", fg="white", bg=self.light_blue, font=("Times New Roman", 15))
        button.bind("<Button-1>", self.handle_button)
        button.place(x=250,y=230, width=250, height=50)

        self.window.mainloop()

    def handle_button(self, event):
        self.redo = True
        self.window.destroy()