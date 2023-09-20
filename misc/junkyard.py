# To be added to gui_helper.py in the QuizOptionInterface Class
# Changes ui format to use buttons instead of scroll bar
#
buttons_frame.pack(expand=True, fill="Y")
self.window.columnconfigure(0, weight=1, minsize=175)
self.window.columnconfigure(1, weight=1, minsize=175)
for i, quiz_item in enumerate(quiz_list):
    self.window.rowconfigure(i+1, weight=1, minsize=50)
    button = tk.Button(master=buttons_frame, text=quiz_item, width=30, height=5, bg="blue", fg="yellow")
    button.bind("<Button-1>", partial(self.handle_button, quiz_item))
    button.grid(row=int(i/2)+1, column=i%2, padx=5, pady=5)

# To be added to gui_helper.py in the QuizOptionInterface Class
# Changes ui format to use scrollbar instead of button
#

scroll_frame = tk.Frame(master=frame)
scroll_frame.place(x=0,y=100)

self.scroll_bar = tk.Scrollbar(master=scroll_frame)
self.scroll_bar.pack(side=tk.RIGHT)

self.mylist = tk.Listbox(master=scroll_frame, yscrollcommand=self.scroll_bar.set)
for quiz_item in quiz_list:
    self.mylist.insert(tk.END, quiz_item)

self.mylist.pack(side=tk.LEFT, fill=tk.BOTH )
self.scroll_bar.config(command = self.mylist.yview )

button = tk.Button(master=frame, text="Confirm")
button.bind("<Button-1>", self.handle_button)
button.place(x=0,y=300)

def handle_button(self, event):
    self.selected_quiz_name = self.quiz_list[self.mylist.curselection()[0]]
    self.window.destroy()