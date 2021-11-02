import flask
from flask import request, jsonify, Flask
from os import environ
import random

app = flask.Flask(__name__)



@app.route('/', methods=['GET'])
def home():
	return """
    <h1>TSP GENETIC API</h1>
    <h2>The purpose of this API is to calculate solutions to the travelling salesman problem
    using evolutionary genetic algorithms</h2>
    
    <h2>Developed By <a href="https://github.com/tracedelange/">Trace DeLange</a></h2>



    <h3>Routes:</h3>
    <ul>
        <li style="font-size: 3vmin;">
            /generate
        </li>
    
    </ul>
    
    """
@app.route('/generate', methods=['GET'])
def generate(count):
    return jsonify(count)

if __name__ == "__main__":
    app.run(debug=True)