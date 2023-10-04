import tkinter as tk
from functools import partial
from PIL import ImageTk, Image  
import re
import wikipedia


#- .... ..- .../.. .../.-/- . .-. -.

# The quiz itself
class MorseInterface:
    def __init__(self, quiz_name, quiz_config, quiz_df):
        self.window = tk.Tk()
        self.window.geometry("1400x530")
        self.window.title(quiz_name)

        self.quiz_name = quiz_name
        self.quiz_config = quiz_config
        self.quiz_df = quiz_df

        self.light_blue = "#34A2FE"
        self.dark_blue = "#3458EB"
        self.gold = "#E6C35C"

        self.index = 0
        self.state = "highlight"



        # put on frame to use pixel widths
        self.frame=tk.Frame(self.window, width=1400, height=530)
        self.frame.pack()

        # header
        tk.Label(master=self.frame, fg="white", bg=self.dark_blue).place(x=0,y=0,width=1400, height=100)
        tk.Label(master=self.frame, text=quiz_name, fg="white", bg=self.light_blue,font=("Times New Roman", 25)).place(x=10,y=10,width=1380, height=80)

        # Question
        self.sentences = ["This is a test", "This is a second sentence for when I need to test that"] #self.get_sentences()
        self.qbox = tk.Text(master=self.frame, font=("Times New Roman", 25), bg=self.light_blue, wrap=tk.WORD)
        self.qbox.insert(tk.INSERT, self.sentences[self.index])
        self.qbox.tag_config("start", foreground="red")
        self.qbox.tag_add("start", "1.0", "1.1") 
        self.qbox.config(state='disabled')
        self.qbox.place(x=10,y=120,width=1380, height=200)

        # Answer
        self.abox = tk.Entry(master=self.frame, bg="white", font=("Times New Roman", 25), justify="left")
        self.abox.place(x=10,y=350,width=1380, height=50)
        self.abox.bind("<Return>", self.handle_enter)
        self.abox.bind("<Key>", self.handle_key)

        self.window.mainloop()

    # pull random sentence from wikipedia
    def get_sentences(self):
        text = wikipedia.page(wikipedia.random()).content
        sentences = text.replace("\n","").split(".")
        # do some more cleaning
        return sentences
    
    # helper method to get question sentence
    def get_qbox(self):
        return self.qbox.get("1.0", tk.END)
    
    def get_a_indexes(self, text, word_seperator="/", char_seperator=" "):
        word_index = text.count(word_seperator)
        text = text[max(0, text.rfind(word_seperator)):]
        letter_index = text.count(char_seperator)
        return word_index, letter_index
    
    def get_q_index(self, text, word_index, letter_index):
        word_indexes = [-1] + [x.start() for x in re.finditer(r" ",text)] + [len(text)]
        word_count = text.split(" ")
        if word_index >= len(word_count):
            return -1
        max_len = len(word_count[word_index])
        answer_index = word_indexes[word_index] + 1 + min(max_len, letter_index)
        return answer_index        
    
    # highlight the letter being typed
    def highlight_letter(self, answer):
        w,l = self.get_a_indexes(answer)
        answer_index = self.get_q_index(self.get_qbox(), w,l)

        self.qbox.tag_remove("start", "1.0", "1."+str(len(self.get_qbox())))
        self.qbox.tag_add("start", "1."+str(answer_index), "1."+str(answer_index+1))   

    # change highlighting as keys pressed
    def handle_key(self, event):
        answer = self.abox.get() + event.char
        self.highlight_letter(answer)

    # switch from showing correct answer or to next question on enter
    def handle_enter(self, event):
        if self.state == "highlight":
            self.highlight_correctness()
            self.state = "next q"
        elif self.state == "next q":
            self.index += 1
            self.qbox.config(state='normal')
            self.qbox.delete('1.0', tk.END)
            self.qbox.insert(tk.INSERT, self.sentences[self.index])
            self.qbox.config(state='disabled')
            self.abox.delete('1.0', tk.END)
            self.state = "highlight"
    
    # translate question into answer for answer key
    def get_morse(self):
        answer = ""
        for letter in self.get_qbox()[:-1]:
            if letter == " ":
                answer += "/"
            else:
                letter = letter.lower()
                code = self.quiz_df[self.quiz_df["Letter"].str.lower() == letter]["Code"]
                if len(code) > 0:
                    answer += code.values[0] + " "
                else:
                    answer += "!"

        return answer
    
    # determine what parts of input are wrong
    def get_tag_regions(self, answer, trial):
        answer_words = " ".join(answer.replace("/", " ").split())
        answer_words = answer_words.split(" ")
        trial_words = " ".join(trial.replace("/", " ").split())
        trial_words = trial_words.split(" ")
        slash_indexes = [0] + [x.start() for x in re.finditer(r" ",answer)] + [len(answer)]
        regions = []
        for i in range(max(len(answer_words), len(trial_words))):
            if i > len(trial_words) or i > len(answer_words) or answer_words[i] != trial_words[i]:
                regions.append([slash_indexes[i], slash_indexes[i+1]])
                print(regions)
                
        return regions

    # highlight incorrect portion of input
    def highlight_correctness(self):
        answer = self.get_morse()
        attempt = self.abox.get()
        regions = self.get_tag_regions(answer, attempt)

        self.answer_label = tk.Text(master=self.frame, bg='#F0F0F0', fg="black", font=("Times New Roman", 25))
        self.answer_label.insert(tk.INSERT, answer)
        self.answer_label.tag_config("start", foreground="red")
        for r in regions:
            self.answer_label.tag_add("start", "1."+str(r[0]), "1."+str(r[1])) 
        self.answer_label.config(state='disabled')
        self.answer_label.place(x=10,y=450,width=1380, height=50)


#- .... ..- .../.. .../.-/- . .-. -.
