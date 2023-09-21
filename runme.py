import tkinter as tk
from file_helpers import *
from gui_helpers import * 


quiz_list = read_quiz_options()
quiz_name = QuizOptionInterface(quiz_list).selected_quiz_name

quiz_config = read_quiz_config(quiz_name)
quiz_config = QuizConfigInterface(quiz_config).quiz_config

# quiz_name = "Capitals"
# quiz_config = {'misc': {'type': 'text'}, 'single_check': {'Reversed?': 'False'}, 'grouped_check': {'Continents': {'Africa': 'True', 'Asia': 'True', 'Oceania': 'True', 'Europe': 'True', 'North America': 'True', 'South America': 'True'}}, 'number_value': {'Number of Questions?': '197'}}

quiz_df = get_quiz(quiz_name, quiz_config)
QuizInterface(quiz_name, quiz_config, quiz_df)