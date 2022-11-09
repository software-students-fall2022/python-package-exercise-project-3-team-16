[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9088627&assignment_repo_type=AssignmentRepo)

![build badge](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-16/actions/workflows/build.yaml/badge.svg)

# Python Fortune Teller Package

[Andrei Stoica](https://github.com/andreicstoica)
[Brandon Chen](https://github.com/b-chen00)
[Charlie Xiang](https://github.com/xiang-charlie)
[Sanjaya Bhatta](https://github.com/itSanjaya)

[Package Page on PyPi](https://pypi.org/project/fortunetelleracs1029/0.1.0/)

## Functions and their Args
### getLiveAdvice(type, seed=None)
Returns a line of life advice, either focused on learning (learning) or detaching (detach) depending on the argument passed in with an optional seed argument.
**Args:**
_learning_, _detach_, and _seed_
### getCSFortune(question, debug, seed=None)
Receives a question in the form of a String with a boolean value on whether it is for
debugging purposes. An optional seed argument could be given to generate the same
random result. Outputs a fortune on whether you will succeed in doing anything computer
science related or not. If debugging, a random potential error is given or nothing at
all if it is beyond fixing.
**Args:**
_question_, _debug_, and _seed_
### getInspiration(name)
Receives either a famous person's name or an empty string, and returns a random inspirational quote by the specified
person. If the string is empty, returns a random inspirational quote by a random person.
**Args:**
_name_
### funny(name)
Receives the name of a person and return a funny quote if the person is one of the 6 preset. If an empty string is
given, a random quote by any of the 6 figures is given. If an invalid name is given, no quote is given back with a
message.
**Args:**
_name_

## How to Import and Install
* Use `pip install fortunetelleracs1029==0.1.0` to create a pipenv-managed virtual environment and install the latest version of this package.
* Activate the virtual environment using `pipenv shell`.

## How to Contribute, Build and Test
* Install and enter the virtual environment as above.
* Run the tests from the main project directory using `python3 -m pytest`.
* Create a Python program and import this package using `from fortunetelleracs1029 import fortuneteller`
