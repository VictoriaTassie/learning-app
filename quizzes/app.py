from flask import Blueprint, render_template, request, jsonify, flash, session
import random
import json

# define the blueprint
quizzes = Blueprint('quizzes', __name__, template_folder="templates")
quizzes.secret_key = "stringofwordsandsentences"


@quizzes.route('/')
def index():
    if not session.get('total_correct'):
        session['total_correct'] = 0
        session['correct_in_row'] = 0
    return render_template('quizzes/index.html')
	
@quizzes.route('arithmetic/<type>', methods=["POST", "GET"])
def arithmetic(type):
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
        options = random.sample(range(x+y-5, x+y+5), 4)
    elif type == 'subtraction':
        ans = x - y
        options = random.sample(range(x-y-5, x-y+5), 4)
    elif type == 'multiplication':
        ans = x * y
        options = random.sample(range(x*(y-1), x*(y+1)), 4)
    elif type == 'division':
        mult = x * y
        ans = x
        x = mult
        options = random.sample(range(1, 12), 4)


    # random number to be right
    corans = random.randint(0,3)

    # assign right answer to random position
    options[corans] = ans
            
    return render_template('quizzes/arithmetic2.html', x=x, y=y, options=options, type=type, total_correct=session['total_correct'], correct_in_row=session['correct_in_row'])

@quizzes.route('/indices', methods=['GET', 'POST'])
def indices():
    if request.method == "POST":
        x = int(request.form['x'])
        y = int(request.form['y'])
        clientAnswer = int(request.form['clientAnswer'])
        if clientAnswer == x ** y:
            session['total_correct'] += 1
            session['correct_in_row'] += 1
            return jsonify({'res':'Correct', 'ans': x**y, 'total_correct': session['total_correct'], 'correct_in_row': session['correct_in_row']})
        else:
            session['correct_in_row'] = 0
            return jsonify({'res':'Incorrect', 'ans': x**y, 'total_correct': session['total_correct'], 'correct_in_row': session['correct_in_row']})

    # random numbers to use as powers
    x = random.randint(2, 12)
    y = random.randint(0, 5)
    ans = x ** y

    all_options = []
    for i in range(6):
        all_options.append(x ** i)
    all_options.remove(x**y)
    options = random.sample(all_options, 4)

    corans = random.randint(0,3)

    options[corans] = ans

    return render_template('quizzes/indices.html', x=x, y=y, options=options, total_correct=session['total_correct'], correct_in_row=session['correct_in_row'])


@quizzes.route('/simplifying-indices', methods=['GET','POST'])
def simplifying_indices():
    x = random.randint(-15, 15)
    y = random.randint(-15, 15)
    ans = x + y
    options = random.sample(range(x+y-5, x+y+5), 4)

    # random number to be right
    corans = random.randint(0,3)

    # assign right answer to random position
    options[corans] = ans
            
    return render_template('quizzes/simplifying-indices.html', x=x, y=y, options=options, total_correct=session['total_correct'], correct_in_row=session['correct_in_row'])
