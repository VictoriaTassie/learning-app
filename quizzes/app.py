from flask import Blueprint, render_template, request, jsonify, flash
import random
import json

# define the blueprint
quizzes = Blueprint('quizzes', __name__, template_folder="templates")


@quizzes.errorhandler(404)
def error_404(e):
    return render_template('error404.html')

@quizzes.route('/')
def index():
    return render_template('quizzes/index.html')
	
@quizzes.route('/addition', methods=["POST", "GET"])
def addition():
    if request.method == "POST":
        x = int(request.form['x'])
        y = int(request.form['y'])
        clientAnswer = int(request.form['clientAnswer'])
        if clientAnswer == x + y:
            return jsonify({'res':'Correct', 'ans': x+y})
        else:
            return jsonify({'res':'Incorrect', 'ans': x+y})


    # random numbers to add together
    x = random.randint(1,50)
    y = random.randint(1,50)
    ans = x + y

    # random wrong answers
    options = [random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)]

    # random number to be right
    corans = random.randint(0,3)

    # assign right answer to random position
    options[corans] = ans
            
    return render_template('quizzes/addition.html', x=x, y=y, options=options)
