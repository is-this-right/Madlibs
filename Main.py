'''
For opening a Json file:
https://www.freecodecamp.org/news/loading-a-json-file-in-python-how-to-read-and-parse-json/
'''
import json
import templates

from Madlib import Madlib
from Template import Template

import os
import tkinter
from tkinter import *


def openJson(json_file):
    json_file = open(json_file)
    json_data = json.load(json_file)
    return json_data


def use_template(json_file):
    data = openJson(json_file)
    madlib = Madlib(data)
    madlib.get_input()
    output = madlib.combine_madlib()
    print(output)


def create_template():
    prompt = []
    story = ""
    # use_template("test.json")
    title = input("Title: ")
    # title = "Test"
    next_line = input("Prompt, Story, or End?: ")
    number = 0
    while next_line != "End":
        match next_line:
            case "Prompt":
                prompt.append(input("Enter Prompt: "))
                story = story + "{" + str(number) + "}"
                number += 1
            case "Story":
                story = story + str(input("Enter Story: "))
        next_line = input("Prompt, Story, or End?: ")
    template = Template(title, prompt, story)
    return template


def export_template(template: Template, filename):
    template.export_template(filename)


def template_creator():
    template_output = create_template()
    export_template(template_output, template_output.get_title() + ".json")


if __name__ == "__main__":
    action = input("(C)reate new template or (U)se existing template?")
    if action == "C":
        template_creator()
    elif action == "U":
        path = "./templates/"
        all_files = os.listdir(path)
        for file in all_files:
            file = file.strip(".json")
            print(file)
        template_name = path + input("Which template do you want to use?") + ".json"
        use_template(template_name)
