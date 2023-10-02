import tkinter as tk
from file_helpers import *
from gui_helpers import * 
from gui_morse import *


# chose what to be tested on
# quiz_list = read_quiz_options()
# quiz_name = QuizOptionInterface(quiz_list).selected_quiz_name
quiz_name = "Morse Code Sentences"

# chose settings for given quiz
quiz_config = read_quiz_config(quiz_name)
quiz_config = QuizConfigInterface(quiz_config).quiz_config


# process quiz based on selection screens
if "special" in quiz_config["misc"]["type"]:
    quiz_df = None
else:
    quiz_df = get_quiz(quiz_name, quiz_config)

# run quiz until # of qs == 0
redo = True
while redo:
    if quiz_config["misc"]["type"] == "text":
        finished_quiz_data = TextQuizInterface(quiz_name, quiz_config, quiz_df)
    elif quiz_config["misc"]["type"] == "image":
        finished_quiz_data = ImageQuizInterface(quiz_name, quiz_config, quiz_df)
    elif quiz_config["misc"]["type"] == "special_morse":
        finished_quiz_data = MorseInterface(quiz_name, quiz_config, quiz_df)

    # display results and loop if needed
    results = ResultsInterface(finished_quiz_data)
    quiz_df = quiz_df[quiz_df["Correct"] == False]
    quiz_df = quiz_df.drop(columns="Correct")
    redo = results.redo
