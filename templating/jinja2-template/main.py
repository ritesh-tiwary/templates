from json import load, loads
from jinja2 import Environment, FileSystemLoader


with open("values.json") as f:
    values = load(f)

environment = Environment(loader=FileSystemLoader("."))
template = environment.get_template("template.json")
rendered = template.render(values)
print(loads(rendered))
