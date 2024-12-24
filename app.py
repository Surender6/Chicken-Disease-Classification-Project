from flask import Flask,request,jsonify,render_template
import os
from flask_cors import CORS,cross_origin
from cnnClassifier.pipeline import PredictionPipeline

os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')

app = Flask(__name__)
CORS(app)