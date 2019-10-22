from flask import Blueprint, render_template, request, jsonify, flash, session
import random
import json
import ast

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

@quizzes.route('/arithmetic-sequences', methods=['GET','POST'])
def arithmetic_sequences():

    if request.method == 'POST':
        a_1 = int(request.form['x'])
        d = int(request.form['y'])
        clientAnswer = ast.literal_eval(request.form['clientAnswer'])
        
        if clientAnswer['a1'] == a_1 and clientAnswer['d'] == d:
            session['total_correct'] = int(session['total_correct']) + 1
            session['correct_in_row'] = int(session['correct_in_row']) + 1
            return jsonify({'res':'Correct', 'ans': 'a1 = '+ str(a_1) + ' d = ' + str(d), 'total_correct': session['total_correct'], 'correct_in_row': session['correct_in_row']})
        else:
            session['correct_in_row'] = 0
            return jsonify({'res':'Incorrect', 'ans': 'a<sub>1</sub> = '+ str(a_1) + ', d = ' + str(d), 'total_correct': session['total_correct'], 'correct_in_row': session['correct_in_row']})


    a_1 = random.randint(-100, 100)
    d = random.randint(-15, 15)
    ns = random.sample(range(2, 25), 2)

    values = [a_1 + (ns[i] - 1)*d for i in range(2)]
    ans = {'a1': a_1, 'd': d}

    a = random.sample(range(a_1-5, a_1+5), 4)
    ds = random.sample(range(d-5,d+5), 4)

    options = [{'a1': a[0], 'd': ds[0]}, {'a1': a[1], 'd': ds[1]}, {'a1': a[2], 'd': ds[2]}, {'a1': a[3], 'd': ds[3]}]
    # random number to be right
    corans = random.randint(0,3)

    options[corans] = ans

    return render_template('quizzes/arithmetic-sequences.html', x=a_1, y=d, ns=ns, values=values, options=options)