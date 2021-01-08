from flask import Flask
from flask import request, jsonify
from flask import render_template
import expertise 
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Expertise', methods=['GET'])

def functionName():
    user = request.args.get('user') 
    expertiseList =  expertise.getExpertise(user)
    response = jsonify(expertiseList)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response