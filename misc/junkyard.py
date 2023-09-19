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