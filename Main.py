'''
For opening a Json file:
https://www.freecodecamp.org/news/loading-a-json-file-in-python-how-to-read-and-parse-json/
'''
import json

from Madlib import Madlib
from MadlibAssembler import MadlibAssembler
# import tkinter


def openJson(json_file):
    json_file = open(json_file)
    json_data = json.load(json_file)
    return json_data


if __name__ == "__main__":
    data = openJson("test.json")
    madlib = Madlib(data)
    madlib.get_input()
    output = madlib.combine_madlib()
    print(output)
    # main_window = tkinter.Tk()
    # main_window.title("Mad Libs")
    # main_window.geometry("500x500")
    # main_window.mainloop()
