from flask import request
from uuid import uuid4 # generates unique id (randomized)

from app import app
from db import directors, movies # from database py file

# Create/Read/Update/Delete for movies
# Remember @app ties in all apps to current route

# Option 2 without methods next to '/post'
# If only one route, replace .route decorator to .post method
# For example, @app.post or @app.get instead of @app.route
# should include status codes if it is not 200

#POST
@app.post('/movie')
def create_movie():
    movie_data = request.get_json() # parses json data into dictionary
    if movie_data['director'] not in directors:
        return {"message": "director does not exist"}, 400 # bad request status code
    movie_id = uuid4().hex # assigning id to uuid, hex - returns hexadecimal string repres
    movies[uuid4().hex] = movie_data # adds post_id as key to the post_data
    return {
        'message': "Movie created",
        'movie-id': movie_id
        }, 201

#GET
@app.get('/movie')
def get_movie():
    try:
        return list(movies.values()), 200
    except:
        return {'message':"Failed to get movies"}, 400

#GET specific/singular movie same as getting ind_user
    
@app.get('/movie/<movie_id>')
def get_ind_movie(movie_id):
    try: 
        return movies[movie_id], 200
    except KeyError:
        return {'message':"invalid movie"}, 400

#PUT/UPDATE 
    
@app.put('/movie')
def update_movie():
    movie_data = request.get_json()

    if movie_data['id'] in movies:
        # Different options below:

        # posts[post_data['id']] = post_data
        # post_id = post_data.pop('id')
        # posts[post_id] |= post_data

        movies[movie_data['id']] = {k:v for k,v in movie_data.items() if k != 'id'} 

        return {'message': f'post: {movie_data["id"]} updated'}, 201 # create request ok
    
    return {'message': "invalid post"}, 400

#DELETE

@app.delete('/movie')
def delete_movie():
    movie_data = request.get_json()
    movie_id = movie_data['id']

    if movie_id not in movies:
        return { 'message' : "Invalid Post"}, 400
    
    movies.pop(movie_id)
    return {'message': f'Post: {movie_id} deleted'}
