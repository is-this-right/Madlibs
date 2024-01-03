'''
For opening a Json file:
https://www.freecodecamp.org/news/loading-a-json-file-in-python-how-to-read-and-parse-json/
'''
import json

from Madlib import Madlib
from Template import Template


# import tkinter


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


if __name__ == "__main__":
    # use_template("New Year.json")
    template_output = create_template()
    export_template(template_output, template_output.get_title() + ".json")
    # main_window = tkinter.Tk()
    # main_window.title("Mad Libs")
    # main_window.geometry("500x500")
    # main_window.mainloop()
