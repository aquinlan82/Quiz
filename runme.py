import tkinter as tk
from file_helpers import *
from gui_helpers import * 


# If True use screens to choose quiz if false use capitals
if False:
    quiz_list = read_quiz_options()
    quiz_name = QuizOptionInterface(quiz_list).selected_quiz_name

    quiz_config = read_quiz_config(quiz_name)
    quiz_config = QuizConfigInterface(quiz_config).quiz_config
else:
    quiz_name = "Capitals"
    quiz_config = {'misc': {'type': 'text'}, 'single_check': {'Reversed?': 'False'}, 'grouped_check': {'Continents': {'Africa': 'True', 'Asia': 'True', 'Oceania': 'True', 'Europe': 'True', 'North America': 'True', 'South America': 'True'}}, 'number_value': {'Number of Questions?': '197'}}

# process quiz based on selection screens
quiz_df = get_quiz(quiz_name, quiz_config)

# run quiz until # of qs == 0
redo = True
while redo:
    if quiz_config["misc"]["type"] == "text":
        finished_quiz_data = TextQuizInterface(quiz_name, quiz_config, quiz_df)
    elif quiz_config["misc"]["type"] == "image":
        finished_quiz_data = ImageQuizInterface(quiz_name, quiz_config, quiz_df)

    results = ResultsInterface(finished_quiz_data)
    redo = results.redo
    quiz_df = quiz_df[quiz_df["Correct"] == False]
    quiz_df = quiz_df.drop(columns="Correct")
