import tkinter as tk
from file_helpers import *
from gui_helpers import * 

quiz_list = read_quiz_options()
quiz_name = QuizOptionInterface(quiz_list).selected_quiz_name

quiz_config = read_quiz_config(quiz_name)
quiz_config = QuizConfigInterface(quiz_config).quiz_config

quiz_df = get_quiz(quiz_name, quiz_config)
if quiz_config["misc"]["type"] == "text":
    finished_quiz_data = TextQuizInterface(quiz_name, quiz_config, quiz_df)
elif quiz_config["misc"]["type"] == "image":
    finished_quiz_data = ImageQuizInterface(quiz_name, quiz_config, quiz_df)

ResultsInterface(finished_quiz_data)