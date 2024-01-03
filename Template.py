import json


class Template:
    template = {
        "title": "",
        "prompt": [],
        "story": []
    }

    def __init__(self, title: str, prompt, story):
        self.template.update({"title": title})
        self.template.update({"prompt": prompt})
        self.template.update({"story": story})

    def show_template(self):
        return self.template

    def get_title(self):
        return self.template.get("title")

    def export_template(self, filename: str):
        with open(filename, "w") as file:
            json.dump(self.template, file)
