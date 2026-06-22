# Hatua za BAckend

python -m venv aishavenv: Create a Virtual Environment: this command is to create a virtual folder where all project packages will be created in it, to prevent enterference with other projects

aishavenv\Scripts\activate: activate the virtual environment
Important
Every time you open a new terminal, activate the environment before working on the project.

python -m pip install --upgrade pip
Upgrade pip: pip is Python's package manager.It installs libraries such as:

Django
NumPy
Pandas
Requests

pip install -r requirement.txt
Pip reads the file and installs everything automatically.instead of downloading everyhting separately

django-admin startproject mysite . 
this command create a project of django and all configuration are in the settings.py file. include db,language code, installed app etc

python manage.py startapp blog 
this create app in this projects, since a project may contain many app
 to run an app we use this command:
 python manage.py runserver

# Models or Tables
1. ProductName
Description
price
Image


2. Cart
productId
Quantity
totalPrice

3. user
Username
firstName
LastName
phoneNumber
Roles(admin/customer)
picture
email
password





