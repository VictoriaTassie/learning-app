from flask import Blueprint, render_template, request, jsonify, flash, session
import random
import json

# define the blueprint
quizzes = Blueprint('quizzes', __name__, template_folder="templates")
quizzes.secret_key = "stringofwordsandsentences"


@quizzes.errorhandler(404)
def error_404(e):
    return render_template('error404.html')

@quizzes.route('/')
def index():
    return render_template('quizzes/index.html')
	
@quizzes.route('arithmetic/<type>', methods=["POST", "GET"])
def arithmetic(type):
    if not session.get('total_correct'):
        session['total_correct'] = 0
        session['correct_in_row'] = 0

    if request.method == "POST":
        x = int(request.form['x'])
        y = int(request.form['y'])
        clientAnswer = int(request.form['clientAnswer'])
        if type == 'addition':
            if clientAnswer == x + y:
                session['total_correct'] += 1
                session['correct_in_row'] += 1
                return jsonify({'res':'Correct', 'ans': x+y, 'total_correct': session['total_correct'], 'correct_in_row': session['correct_in_row']})
            else:
                session['correct_in_row'] = 0
                return jsonify({'res':'Incorrect', 'ans': x+y, 'total_correct': session['total_correct'], 'correct_in_row': session['correct_in_row']})
        elif type == 'subtraction':
            if clientAnswer == x - y:
                session['total_correct'] += 1
                session['correct_in_row'] += 1
                return jsonify({'res':'Correct', 'ans': x-y, 'total_correct': session['total_correct'], 'correct_in_row': session['correct_in_row']})
            else:
                session['correct_in_row'] = 0
                return jsonify({'res':'Incorrect', 'ans': x-y, 'total_correct': session['total_correct'], 'correct_in_row': session['correct_in_row']})
        elif type == 'multiplication':
            if clientAnswer == x * y:
                session['total_correct'] += 1
                session['correct_in_row'] += 1
                return jsonify({'res':'Correct', 'ans': x*y, 'total_correct': session['total_correct'], 'correct_in_row': session['correct_in_row']})
            else:
                session['correct_in_row'] = 0
                return jsonify({'res':'Incorrect', 'ans': x*y, 'total_correct': session['total_correct'], 'correct_in_row': session['correct_in_row']})
        elif type == 'division':
            if clientAnswer == x / y:
                session['total_correct'] += 1
                session['correct_in_row'] += 1
                return jsonify({'res':'Correct', 'ans': x/y, 'total_correct': session['total_correct'], 'correct_in_row': session['correct_in_row']})
            else:
                session['correct_in_row'] = 0
                return jsonify({'res':'Incorrect', 'ans': x/y, 'total_correct': session['total_correct'], 'correct_in_row': session['correct_in_row']})


    # random numbers to add together
    if type == 'multiplication' or type == 'division':
        x = random.randint(2, 12)
        y = random.randint(2, 12)
    else:
        x = random.randint(1,50)
        y = random.randint(1,50)
    
    if type == 'addition':
        ans = x + y
    elif type == 'subtraction':
        ans = x - y
    elif type == 'multiplication':
        ans = x * y
		
    if type == 'division':
        mult = x * y
        ans = x
        x = mult

    # random wrong answers
    if type == 'addition':
        options = [random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)]
    elif type == 'subtraction':
        options = [random.randint(-49,49), random.randint(-49,49), random.randint(-49,49), random.randint(-49,49)]
    elif type == 'multiplication':
        options = [random.randint(2,144), random.randint(2,144), random.randint(2,144), random.randint(2,144)]
    elif type == 'division':
        options = random.sample(range(1, 12), 4) #[random.randint(1,12), random.randint(1,12), random.randint(1,12), random.randint(1,12)]

    # random number to be right
    corans = random.randint(0,3)

    # assign right answer to random position
    options[corans] = ans
            
    return render_template('quizzes/arithmetic.html', x=x, y=y, options=options, type=type, total_correct=session['total_correct'], correct_in_row=session['correct_in_row'])
