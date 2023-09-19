import tkinter as tk
from file_helpers import *
from gui_helpers import * 


# quiz_list = read_quiz_options()
# chosen_quiz = QuizOptionInterface(quiz_list).selected_quiz_name
chosen_quiz = "capitals"

quiz_config = read_quiz_config(chosen_quiz)
print(quiz_config)
quiz_config = QuizConfigInterface(quiz_config).quiz_config
print("hi")
print(quiz_config["single_check"]["Reversed?"])
