# phonecalc


## Description
Phonecalc is a basic application that demonstrates user registration and authentication using Django and Django rest framework. The app also demosntrates caching, background tasks and django async

#### Requirements
1. [Python3.9](https://www.python.org/downloads/)
2. [Postgres](https://www.postgresql.org/download/)
3. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
4. [Pip](https://pip.pypa.io/en/stable/installing/)



#### Deliverables
    - Queue log running tasks
    - Cache operation results
    - Generate reports
    - Work with Django's internal authentication & authorization module
    - Work with Django Async
    - Schedule tasks
    - Deploy Django applications
    - Work with files



#### Technologies used
    - Celery
    - Redis
    - Python 3.9
    - Django
    - Django Rest Framework
    - A managed Postgresql instance on elephantsql.com
    - Django Rest Swagger

#### Clone the Repo and enter the project folder.
```bash
git clone https://github.com/ianbwana/phonecalc.git && cd phonecalc
```
#### Create and activate the virtual environment
```bash
python3 -m venv env
```

```bash
source env/bin/activate
```
### Install PostgreSQL requirements
```bash
sudo apt-get install python-dev libpq-dev
```
#### Create Database
You can install postgres and create a database on your local machine then configure it with the instructions[here](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04) or can choose to use the 
SQLite3 database that comes with Django

#### Install dependencies
Install environmental dependencies that will enable the app to run
```bash
pip install -r requirements.txt
```

#### Make and run migrations
```bash
python manage.py makemigrations && python3.6 manage.py migrate
```

#### Run the app
```bash
python manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)



A hosted LIVE DEMO of this app can be found [here](http://138.68.89.212:8000/)


#### ENDPOINTS
These are the main endpoints to demonstrate the requirements of this application. None require auth token authorization
The format is "http://138.68.89.212:8000" + endpoint

| Endpoint  | method |Summary|             
| ------------- | ------------- |------------|
| /api/v1/docs/  | GET          |  Show the main application endpoints on a Swagger UI
| /api/v1/users  | GET  | Show all the registered users. Currently just limited to main admin            |
| /admin/  | GET, POST, PUT, DELETE          |  Admin dasboard
| /api/v1/users  | GET  | Show all the registered users. Currently just limited to main admin            |
| api/v1/auth/register  | POST  | Allows user registration          |
| api/v1/auth/login   | POST  | Allow user login by returning user details and auth token           |
| api/v1/password-reset/  | POST  | Allows a user to reset their password which is sent to their mail           |


### Assumptions
1. There is no need to store the csv file in the database, It is merely a guideline on costs
2. The hosted version of the application is not running on Debug mode but is not optimised for production either so some environmental variables are still visible.
3. No need to configure nginx. Gunicorn is sufficient for demo purposes

