# PROJECT DOCUMENTATION

## TASK 0
Cloned the github repo provided in the project page

## TASK 1
Setup and run the unittest, ensure all test pass and add some more test

## TASK 2
Updated the Storage Engines and added a method to retrieve one object ```def get(self, cls, id)```:
- FileStorage: The method returns the object based on the class and its ID, or None if not found
- DBStorage: The method returns the object based on the class and its ID, or None if not found

(wesam): added the 'count' method to DBStorage - it will be needed in task 4

## TASK 3
<<<<<<< Updated upstream
- Made __init__ files inside each folder in api folder
- app file: created a variable app -instance of Flask-
            -imported storage from models & app_views from api.v1.views
            -registered the blueprint app_views to Flask instance app
            -declared a method to handle @app.teardown_appcontext that calls storage.close()
            -run Flask server with:
                host = env variable HBNB_API_HOST or 0.0.0.0 if not defined
                port = env variable HBNB_API_PORT or 5000 if not defined
                threaded=True
- index file: importing app_views from api.v1.views
            -createed  a route /status on the object app_views that returns a JSON: "status": "OK"

## TASK 4
Continued working in index file:
- Createed an endpoint that retrieves the number of each objects by type
=======
- Created __init__ files inside wach folder
- app file:
>>>>>>> Stashed changes

## TASK 6
- Implement the get_states function that retrieves all State objects from storage and returns them in JSON format.

- Implement the get_state function that retrieves a State object by state_id from storage. If not found, return a 404 error.

- Implement the delete_state function that deletes a State object by state_id from storage. If not found, return a 404 error. Return an empty dictionary with status code 200.

-  Implement the create_state function that creates a new State object using data from the request body. If the request body is not valid JSON, return a 400 error with the message "Not a JSON". If the name is missing, return a 400 error with the message "Missing name". Return the new State with status code 201.

- Implement the update_state function that updates a State object using data from the request body. If the request body is not valid JSON, return a 400 error with the message "Not a JSON". Ignore the id, created_at, and updated_at keys during the update. Return the updated State with status code 200.