import flask
import time
import json

app = flask.Flask(__name__)

@app.route("/", methods=['GET']) # Maps the home (/) url to the home function
def home():
    sample_data = [i for i in range(10)]
    dict_data = {'timestamp' : time.time(), 'page' : 'home', 'data' : sample_data}
    json_data = json.dumps(dict_data)
    return json_data

if __name__ == "__main__":
    app.run(port=8080)