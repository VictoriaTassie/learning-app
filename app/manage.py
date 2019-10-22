from flask import Flask, render_template
from app.learning.app import learning
from app.quizzes.app import quizzes

application = Flask(__name__)
application.register_blueprint(learning, url_prefix="/learning", template_folder="templates")
application.register_blueprint(quizzes, url_prefix="/quizzes", template_folder="templates")

application.secret_key = "stringofwordsandsentences"


@application.errorhandler(404)
def error_404(e):
    return render_template('error404.html')

@application.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    application.run(debug=True)