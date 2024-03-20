from flask import request

from app import app # see: app folder
from db import directors

@app.route('/') # home page
def home():
    return{
        "This is the Home Page": "Get comfy."
    }


# access users from simulated database above

@app.route('/directors')
def get_directors():
    return {
        'directors' : list(directors.values())
    }


# dynamically retrieve a director's id below:
@app.route('/director/<int:id>', methods=["GET"]) # string contained in <> is also the parameter in function below
def get_ind_director(id):
    if id in directors: # check if director exists
        return {
            'director' : directors[id]
        }
    return {
        'ERROR' : 'INVALID DIRECTOR_ID'
    }

# specify what request method the route can use below (can create another route with same name
# but with a different method later on)
# has to be retrieved through json; cannot be done via browser
# think: Postman ext in VS code and Insomnia on the web

# POST method, create director - Postman

@app.route('/director', methods=["POST"])  
def create_director():
    #ANALYZE REQUEST below
    data = request.get_json() 
    # REQUEST PACKAGE from FLASK: must include at the top import Flask, request; then, get json()
    print(data)
    directors[data['id']] = data
    return {
        'DIRECTOR CREATED SUCCESSFULLY': directors[data['id']]
    }

# open Postman ext, create POST method using local address
# body, raw, json() to communicate with APIs
# input request data in body (see info added for "id":3)
# must us double quotes
# check if input is added through GET /users and local host/users


# PUT Method below: UPDATE Route - Postman

@app.route('/director', methods=["PUT"]) 
def update_director():
    #ANALYZE REQUEST below
    data = request.get_json() 
    if data['id'] in directors:
        directors[data['id']] = data
        return {
            'USER updated': directors[data['id']]
        }
    return {
        'error': 'no user found with that id'
    }

# DELETE method - Postman

@app.route('/director', methods=["DELETE"]) 
def delete_director():
    #ANALYZE REQUEST below
    data = request.get_json() 
    if data['id'] in directors:
        del directors[data['id']]
        return {
            'DIRECTOR deleted': f"{data['username']} erased."
        }
    return {
        'error': 'no user found with that id'
    }
