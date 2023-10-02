import tkinter as tk
from functools import partial
from PIL import ImageTk, Image  
import re
import wikipedia

# The quiz itself
class MorseInterface:
    def __init__(self, quiz_name, quiz_config, quiz_df):
        self.window = tk.Tk()
        self.window.geometry("1400x530")
        self.window.title(quiz_name)

        self.quiz_name = quiz_name
        self.quiz_config = quiz_config

        self.light_blue = "#34A2FE"
        self.dark_blue = "#3458EB"
        self.gold = "#E6C35C"

        self.index = 0


        # put on frame to use pixel widths
        self.frame=tk.Frame(self.window, width=1400, height=530)
        self.frame.pack()

        # header
        tk.Label(master=self.frame, fg="white", bg=self.dark_blue).place(x=0,y=0,width=1400, height=100)
        tk.Label(master=self.frame, text=quiz_name, fg="white", bg=self.light_blue,font=("Times New Roman", 25)).place(x=10,y=10,width=1380, height=80)

        # Question
        self.sentences = ["This is a test sentence to make the line go off the edge and wrap around but for that to happen it has to be longer so here are some extra words to make that happen", "This is a second sentence for when I need to test that"] #self.get_sentences()
        self.qbox = tk.Text(master=self.frame, font=("Times New Roman", 25), bg=self.light_blue, wrap=tk.WORD)
        self.qbox.insert(tk.INSERT, self.sentences[self.index])
        self.qbox.tag_config("start", foreground="red")
        self.highlight_word(setup=True)
        self.qbox.config(state='disabled')
        self.qbox.place(x=10,y=120,width=1380, height=250)

        # Answer
        self.abox = tk.Entry(master=self.frame, bg="white", font=("Times New Roman", 25), justify="left")
        self.abox.place(x=10,y=400,width=1380, height=100)
        self.abox.bind("<Return>", self.handle_enter)
        self.abox.bind("<space>", self.handle_space)

        self.window.mainloop()

    def get_sentences(self):
        text = wikipedia.page(wikipedia.random()).content
        sentences = text.replace("\n","").split(".")
        # do some more cleaning
        return sentences
    
    def get_qbox(self):
        return self.qbox.get("1.0", tk.END)
    
    def highlight_word(self, setup=False):
        if setup:
            spaces_before = 0
            space_indexes = [x.start() for x in re.finditer(r" ",self.get_qbox())]
            i1 = space_indexes[spaces_before]
            self.qbox.tag_add("start","1.0", "1."+str(i1))
        else:
            self.qbox.tag_remove("start", "1.0", "1."+str(len(self.get_qbox())))
            spaces_before = self.abox.get().count(" ")
            space_indexes = [x.start() for x in re.finditer(r" ",self.get_qbox())]
            i1 = space_indexes[spaces_before]
            i2 = space_indexes[spaces_before+1]
            self.qbox.tag_add("start", "1."+str(i1), "1."+str(i2))

    def handle_space(self, event):
        self.highlight_word()
    
    def handle_enter(self):
        print("hi")