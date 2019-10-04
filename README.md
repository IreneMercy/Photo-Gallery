## Photo-Gallery
#### Photo-gallery is a web application that enable users to display their photos for others to see.

## Requirements
#### These are the requirements you need to get the project running locally on your machine:
#### Text Editor
#### Install python
#### Install and activate virtual
#### Setup Database
#### Install Django

## Installing Process
#### Download any text editor of your choice, either Sublime, Visual-Studio-Code or Atom.
#### Install your preferred version of python => ```sudo apt-get install python3.6```.
#### ```python --version``` to confirm that python has been installed.
#### Open the command-line and ```cd your preferred directory```, example => ```cd Desktop```.
#### Git clone the project on your current directory => ```git clone https://github.com/IreneMercy/Photo-Gallery```.
#### Open the project on your terminal =>```atom . or code .``` , according to the type of your text editor.
#### Move to your project directory ```cd Photo-Gallery```.
#### Install virtual environment using python ```python3.6 -m venv virtual```, check your project to confirm you have a folder    called virtual and then activate it by running ```source virtual/bin/activate```
#### ```pip install -r requirements.txt``` to install the packages in the ```requirements.txt file```. That will install all packages including Django.
#### ```python3.6``` to open python shell, then ```import django``` and lastly ```django.get_version()``` to see and confirm the version of django installed. You can then ```ctrl z``` to get out of the shell,
#### After ensuring you have all the above, ```python3 manage.py runserver``` to run the project.Then click the local host link given to open the project on a browser ```http://127.0.0.1:8000/```.
