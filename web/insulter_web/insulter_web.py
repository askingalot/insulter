from flask import Flask, render_template, redirect, url_for

from insulter import Insulter

app = Flask(__name__)


@app.route('/')
def index():
    insult = Insulter().random_insult()
    return redirect(url_for('insult', insult_text=insult))


@app.route('/insult/')
@app.route('/insult/<insult_text>')
def insult(insult_text=None):
    if not insult_text:
        return redirect(url_for('index'))

    return render_template('insult.html', insult=insult_text)

