from flask import Flask, render_template, request, redirect, url_for, flash
from mnemonic import Mnemonic
from datetime import datetime
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY


@app.route('/', methods=['GET', 'POST'])
def index():
    lang = 'english'
    num_words = 5

    if request.method == 'POST':
        try:
            num_words = int(request.form['num_words'])
            if num_words > 12:
                flash('You can only generate a maximum of 12 words.')
                flash('Research shows you probably can\'t remember more than 12 words in a row anyways...')
                return redirect(url_for('index'))
        except ValueError as err:
            flash('Expecting an integer, got a {}'.format(err))
            return redirect(url_for('index'))

    mn = Mnemonic(lang)
    pass_list = mn.generate().split(' ')[:int(num_words)]

    return render_template(
        'index.html',
        pass_list=pass_list,
        today=datetime.now().strftime('%x %X')
    )


@app.route('/entropy', methods=['GET', 'POST'])
def entropy():
    return render_template(
        'entropy.html',
        today=datetime.now().strftime('%x %X')
    )


@app.route('/mnemonics', methods=['GET', 'POST'])
def mnemonics():
    return render_template(
        'mnemonics.html',
        today=datetime.now().strftime('%x %X')
    )


@app.route('/nist-passwords', methods=['GET', 'POST'])
def nistpasswords():
    return render_template(
        'nistpasswords.html',
        today=datetime.now().strftime('%x %X')
    )


@app.route('/xkcd-936', methods=['GET', 'POST'])
def xkcd936():
    return render_template(
        'xkcd-936.html',
        today=datetime.now().strftime('%x %X')
    )


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(err):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8585,
        debug=True,
    )
