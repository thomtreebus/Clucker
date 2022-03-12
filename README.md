# Clucker
Chicken-themes microblogging application built with Django

Follow these steps to setup the project for development:
## Installing dependencies*

It is recommended to install this in a virtual environment. To do this after you have clone the repository (and have ran `cd` to go into it) run:

`virtualenv venv` 

In the event that this does not work do the command below instead of the one above: 

`python3 -m virtualenv venv` 

Next activate the virtual environment:

`source venv/bin/activate`

To install the dependencies for this project do:

`pip3 install -r requirements.txt`

**Note: every time you install a new package using pip/pip3 do not forget to the run the command below**:

`pip3 freeze > requirements.txt `

## Applying migrations*

After installing dependencies create database migrations:

`python3 manage.py makemigrations`

Then apply the migrations with:

`python3 manage.py migrate`

## Accessing the admin interface*

Run the following command to create a super user allowing you to manage the database through `/admin` path:

`python3 manage.py createsuperuser`

## Running the development server

Run to start the the development server at: http://127.0.0.1:8000/:

`python3 manage.py runserver`

## Running tests

Run all the tests for the project:

`python3 manage.py test`

Run to run the tests for the a specific file in the project:

`python3 manage.py test example_project.tests.views.test_example_view`

## Running test with coverage (Recommended)

Run all the tests for the project:

`coverage run manage.py test`

Then generate a report to see if there are any missing tests by typing:

`coverage report`

To see the specifics of missing tests ie. the statements not tested yet do:

`coverage html`

Then do open:

 `firefox htmlcov/index.html`
