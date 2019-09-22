from flask import Blueprint, render_template, request, jsonify, flash
import random
import json

# define the blueprint
learning = Blueprint('learning', __name__, template_folder="templates")


@learning.errorhandler(404)
def error_404(e):
    return render_template('error404.html')

@learning.route('/')
def index():
    return render_template('learning/index.html')
	
@learning.route('/addition', methods=["POST", "GET"])
def addition():      
    return render_template('learning/addition.html')
