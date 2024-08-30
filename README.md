# EventSphere

## Project Description:
This is a Events management API, this project includes, user registration and login using JWT Authentication, an user can create events which othe user can join and the events can be private or public. I also generates tickets for specific event that an user join. 

The API was documented using swagger

# Tecnology user
## Django and django rest framework

### Features

- [x] User registration
- [x] User login
- [x] Create an event
- [X] join an event
- [x] Generate ticket code
- [] Payments

### Requirents

Before starting, you will need to install in your local machine the following tools:
[Python Interpreter]https://python.org/downloads .
Furthemore you need a code editor to work with the code, like [VSCide]https://code.visualstudio.com/ .

# Clone the repository
$ git clone https://github.com/eltonMessiass/EventSphere_API

# Access the project file
$ cd EventSphere_API

# Create a virtual enviroment
$ python -m venv venv

# Activate the virtual enviroment
Linux: $ source venv/bin/activate .
Windows: # .\venv\Scripts\activate .

# install the project dependecies
$ pip install -r requirements.txt 

# run the server
$ python manage.py runserver
# the server will start on port:8000 - access http://localhost:8000/

# Access the API documentation with swagger
http://localhost/8000/swagger/
