import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import json


# ----------------------
# $$$$$$$ FLASK $$$$$$$$
# ----------------------

app = Flask(__name__)  # init

@app.route("/")  # Default path
def default():
    mensaje = " <h1> API </h1> <p>      /get/json/?id=  para obtener json <p> "
    return mensaje

# ----------------------
# $$$$$$$ FLASK GET $$$$$$$$
# ----------------------

@app.route('/get_json', methods=['GET'])
def get_json():
    token_id = None
    # almaceno archivo en una variable dandole la ruta hasta el archivo
    #settings_file = os.path.dirname(__file__) + '\\clima_madrid.json'
    settings_file = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "\\resources\\data\\clima_madrid.json"
    #    settings_file = os.path.dirname(__file__) + '\\others\\projects\\personal_proyect_august\\proyecto_individual\\src\\clima_madrid.json'
    with open(settings_file, 'r') as json_file_readed:
        field = json.load(json_file_readed)
    if 'id' in request.args:
        token_id = str(request.args['id'])
    if token_id == 'Q05192833':           #Si el token es válido
        return field
    else:
        return "Error: clave no valida" + "<br>" + "<br>" + str(request.args)

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