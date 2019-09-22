from flask import Flask, render_template
from learning.app import learning
from quizzes.app import quizzes

application = Flask(__name__)
application.register_blueprint(learning, url_prefix="/learning", template_folder="templates")
application.register_blueprint(quizzes, url_prefix="/quizzes", template_folder="templates")

@application.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    application.run(debug=True)