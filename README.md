# Task
A Django application with User and ActivityPeriod models, able to populate the database with some dummy data, 
and an API to serve that data in JSON format.

## Steps to install and run in local system:-
* Create a virtual environment
    ```python3 -m venv <env_name>```
* Activate virtual environment
    ```source <env_name>/bin/activate```
* Install requirements in venv
    ```pip install -r requirements.txt```
* Make migrations
    ```python manage.py makemigrations```
* Apply migrations
    ```python manage.py migrate```
* Create a superuser
    ```python manage.py createsuperuser```
* Run the server
    ```python manage.py runserver```
