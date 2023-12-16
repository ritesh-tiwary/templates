from typing import List
from xml.etree import ElementTree
from setuptools import find_packages, setup


HYPHEN_E_DOT = "-e ."
README_FILE = "README.md"
REQUIREMENTS_FILE = "requirements.txt"

def get_version() -> str:
	tree = ElementTree.parse("pom.xml")
	root = tree.getroot()
	version_tag = root.find("{http://maven.apache.org/POM/4.0.0}version")
	version_text = version_tag.text
	version = version_text.split("-")[0]
	return version

def get_requirements() -> List[str]:
	with open(REQUIREMENTS_FILE) as file:
		requirements_file = file.readlines()
	
	requirements_file = [package_name.replace("\n", "") for package_name in requirements_file]
	if HYPHEN_E_DOT in requirements_file:
		requirements_file.remove(HYPHEN_E_DOT)

	return requirements_file

setup(
	name = "myapp",
	version = get_version(),
	author = "Ritesh Tiwary",
	author_email = "ritesh.tiwary@rediffmail.com",
	description = "My Application",
	long_desciption = open(README_FILE).read(),
	long_desciption_content_type = "text/markdown",
	url = "https://github.com/ritesh-tiwary/templates/consoleapp",
	packages = find_packages(),
	install_requires = get_requirements(),
	entry_points = {"console_scripts": ["myapp=myapp.app:main"]},
	classifiers = [
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3.12",
		"Operating System :: OS Independent"
	],
	license = "MIT License",
	platforms = ["Linux"],
	python_requires = ">=3.12"
)
