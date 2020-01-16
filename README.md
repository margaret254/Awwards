# Awwards
#### Application to post projects to be rated by other users.
#### By **Margaret254**&trade;

## Description
This is an app that allows users to post reviews on other peoples projects.
## Features
* User can log in to application and view other peoples posts.
* A user can upload posts and edit their profile.
* Admin can regulate images uploaded by deleting from the admin dashboard as well as completely close a users account.



## Behavior Driven Development
1. When the user loads the page,he/she sees the uploaded sites
2. If the user wants to upload a site, he/she should first register
3. Then click on the upload site and fill in the form.
4. Then, the user should click on the logout to log out from the page.

## Setup/Installation requirements
1.Clone or download and unzip the repository from github,https://github.com/margaret254/Awards

2. Activate virtual environment using python3.6 as default handler virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate

3. Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt
4. Create the Database
- psql
- CREATE DATABASE "Dataase Name";

4. Create .env file and  paste the following filling where appropriate:

1.SECRET_KEY = '<Secret_key>'
2.DBNAME = <DB-Name>
3.USER = '<Username>'
4.PASSWORD = '<password>'
5.DEBUG = True

5. Run initial Migration
-python3.6 manage.py makemigrations
-python3.6 manage.py migrate

6. Run the app
-python3.6 manage.py runserver
-Open terminal on localhost:8000



## Technologies Used
* PYTHON 3.6
* DJANGO FRAMEWORK
* BOOTSTRAP
* CSS
* POSTGRESS

## Prerequisite
* PYTHON 3.6
* DJANGO FRAMEWORK
* PYTHON VIRTULENV
* POSTGRESS
## Support and contact details
contact me @ maggiemwas91@gmail.com
### License
The project is under[MIT license](/blob/master/LICENSE)
Copyright &copy; 2019.All rigths reserved
  