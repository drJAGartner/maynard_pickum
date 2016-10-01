#!/usr/bin/env python
from flask import Flask, render_template
import sys, os, flask_login
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/services')
from lines import Lines

_lines = Lines()
_current_week = 3

day_man = LoginManager()
app = Flask(__name__)
day_man.init_app(app)

@day_man.user_loader
def load_user(u_name, u_pass):
    return User.get(user_id)

@app.route('/')
def index():
    str_lines = _lines.print_for_site()
    print("Here:",str_lines)
    return render_template('index.html', lines=str_lines, week=_current_week)


#@app.route('/question/<int:id>')
#def question(id):
#    return render_template('question.html', question=questions[id])


#@app.route('/guess/<int:id>')
#def guess(id):
#    return render_template('guess.html', guess=guesses[id])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)