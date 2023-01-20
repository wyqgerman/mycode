#!/usr/bin/env python3

from flask import Flask, render_template, redirect, url_for
from trivia import PopTrivia


SECRET_KEY = 'this is a secret key'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET', 'POST'])
def trivia():
    form = PopTrivia()
    if form.validate_on_submit():
        return redirect(url_for('finished'))
    return render_template('trivia.html', form=form)


@app.route('/finished')
def finished():
    return render_template('finished.html')


if __name__ == '__main__':
    app.run(debug=True)
