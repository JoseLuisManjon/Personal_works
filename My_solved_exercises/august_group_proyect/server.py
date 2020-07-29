import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import json


# ----------------------
# $$$$$$$ FLASK $$$$$$$$
# ----------------------

app = Flask(__name__)  # init

@app.route("/")  # Default path
def default():
    return " Hola "

# ----------------------
# $$$$$$$ FLASK GET $$$$$$$$
# ----------------------

@app.route('/get/token', methods=['GET'])
def token():
    group_id= None
    if 'id' in request.args:
        group_id = str(request.args['id'])
    
    if group_id == "D124":
        return "{'json': 'D635154795182'}"
    else:
        return "This is a message of error" + "<br>" + "<br>" + str(request.args)

# A route to return all of the available entries in our catalog.
@app.route('/get/df', methods=['GET'])
def api_df():
    token_id = None
    if 'tok' in request.args:
        token_id = str(request.args['tok'])
    if token_id == 'D635154795182':
        return "el DF del grupo D"
    else:
        return "Invalid Token. This is a message of error" + "<br>" + "<br>" + str(request.args)

# ----------------------
# $$$$$$$ MAIN $$$$$$$$
# ----------------------

def main():

    print("STARTING PROCESS")
    print(os.path.dirname(__file__))
    
    # Get the settings fullpath
    settings_file = os.path.dirname(__file__) + "/settings.json"
    # Load json from file 
    with open(settings_file, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    
    # Load variables from jsons
    SERVER_RUNNING = json_readed["server_running"]
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + "Please, allow it to run it.")
            
if __name__ == "__main__":
    main()