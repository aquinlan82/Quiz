
import json
import os
import pandas as pd

def read_quiz_options():
    dir_list = os.listdir("data")
    return dir_list

def read_quiz_config(quiz_name):
    f = open('data/'+ quiz_name + '/config.json')
    config = json.load(f)
    return config

def get_quiz(quiz_name, quiz_config):
    axes  = pd.read_csv("data/" + quiz_name + "/data.csv")
    if "special" in quiz_config["misc"]["type"]:
        axes = axes.sample(n=len(axes)).reset_index()
        return axes
    
    reversed = reverse_axes(quiz_config, axes)
    filtered = filter_axes(quiz_config, reversed)
    random = randomize_axes(quiz_config, filtered)
    return random


def reverse_axes(quiz_config, axes):
    if "Reversed?" in quiz_config["single_check"]:
        if quiz_config["single_check"]["Reversed?"] == "True":
            axes["Temp"] = axes["Axis 2"]
            axes["Axis 2"] = axes["Axis 1"]
            axes["Axis 1"] = axes["Temp"]
            axes.drop(columns="Temp")
            return axes
    return axes

def filter_axes(quiz_config, axes):
    for option in quiz_config["grouped_check"]:
        include = [x for x in quiz_config["grouped_check"][option] if quiz_config["grouped_check"][option][x] == "True"]
        axes = axes[axes[option].isin(include)]
    return axes

def randomize_axes(quiz_config, axes):
    count = quiz_config["number_value"]["Number of Questions?"]
    axes = axes.sample(n=min(int(count), len(axes))).reset_index()
    return axes


