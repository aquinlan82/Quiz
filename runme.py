import tkinter as tk
from file_helpers import *
from gui_helpers import * 


quiz_list = read_quiz_options()
quiz_name = QuizOptionInterface(quiz_list).selected_quiz_name

quiz_config = read_quiz_config(quiz_name)
quiz_config = QuizConfigInterface(quiz_config).quiz_config

quiz = get_quiz(quiz_name, quiz_config)