"""
https://stackoverflow.com/a/7568689:
- helped with the string replacement
"""


class Madlib:
    prompt = []
    story = ""
    user_input = []

    def __init__(self, json_file):
        self.prompt = json_file["prompt"]
        self.story = json_file["story"]

    def get_input(self):
        for p in self.prompt:
            raw_data = input(p + ": ")
            self.user_input.append(raw_data)

    def combine_madlib(self):
        self.story = self.story.format(*self.user_input)
        return self.story
