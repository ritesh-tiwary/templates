from json import load, loads
from chameleon import PageTemplateFile


with open("values.json") as f:
    values = load(f)

templete = PageTemplateFile(filename="template.json")
rendered = templete.render(values=values)
print(loads(rendered))
