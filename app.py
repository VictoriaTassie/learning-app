from flask import Flask, render_template, request, jsonify, flash
import random
import json

app = Flask(__name__)

@app.errorhandler(404)
def error_404(e):
    return render_template('error404.html')

@app.route('/')
def index():
    return render_template('index.html')
	
@app.route('/addition', methods=["POST", "GET"])
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
            
    return render_template('addition.html', x=x, y=y, options=options)
	
if __name__ == "__main__":
    app.run(debug=True)