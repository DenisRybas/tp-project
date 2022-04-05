import datetime

import requests
from flask import request, render_template, abort, redirect, url_for, session
from flask_babel import gettext
from flask_cors import cross_origin
from config import app
from config import app, back_uri


@app.template_filter('dt')
def _jinja2_filter_datetime(date):
    ret = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S').strftime('%d %B %Y %H:%M')
    return ret


@app.route('/change_locale')
def change_locale():
    if 'locale' in session:
        if session['locale'] == 'ru':
            session['locale'] = 'en'
        else:
            session['locale'] = 'ru'
    else:
        session['locale'] = 'ru'
    return redirect(request.referrer)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def index_page():
    return render_template(
        'index.html'
    )


@app.route('/faq')
def faq_page():
    return render_template('faq.html')


@app.route('/login', methods=["GET", "POST"])
def login_page():
    if 'logged_in' in session and session['logged_in']:
        return redirect(url_for('index_page'))
    messages = []
    if request.method == 'POST':
        data = request.form.to_dict(flat=False)
        request_uri = back_uri + 'login'
        response = requests.post(request_uri, json=data).json()

        if response['success']:
            session['logged_in'] = True
            session['token'] = response['token']
            request_uri = back_uri + 'user_profile/' + response['token']
            response = requests.get(request_uri).json()
            if response['success']:
                session['username'] = response['user']['username']
                session['user_photo'] = response['user']['user_photo']

            if request.form.get('remember'):
                session.permanent = True
            return redirect(url_for('index_page'))

        else:
            messages.append(gettext('Incorrect login or password'))

    return render_template(
        'login.html', messages=messages
    )


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index_page'))


@app.route('/registration', methods=["GET", "POST"])
def registration_page():
    if 'logged_in' in session and session['logged_in']:
        return redirect(url_for('index_page'))
    messages = []
    if request.method == 'POST':
        data = request.form.to_dict(flat=False)
        request_uri = back_uri + 'registration'
        response = requests.post(request_uri, json=data)
        res = response.json()

        if res['success']:
            session['logged_in'] = True
            session['token'] = res['token']
            request_uri = back_uri + 'user_short_info/' + res['token']
            response = requests.get(request_uri).json()
            session['g_calendar'] = False
            session['spotify'] = False
            if response['success']:
                session['username'] = response['user']['username']
                session['user_photo'] = response['user']['user_photo']

            if request.form.get('remember'):
                session.permanent = True
            return redirect(url_for('index_page'))

        else:
            if 'email' in res:
                messages.append(gettext('This email already exists'))
            if 'nickname' in res:
                messages.append(gettext('This login already exists'))

    return render_template(
        'registration.html', messages=messages
    )


@app.route('/my_diary')
def my_diary_page():
    # if 'logged_in' not in session or not session['logged_in']:
    #     return redirect(url_for('login_page'))
    my_diary = []
    return render_template(
        'my_diary.html', my_diary=my_diary
    )


@app.route('/diary_of_templates')
def diary_of_templates():
    # if 'logged_in' not in session or not session['logged_in']:
    #     return redirect(url_for('login_page'))

    return render_template(
        'diary_of_templates.html'
    )


@app.route('/diary_of_emotions')
def diary_of_emotions():
    return render_template(
        'diary_of_emotions.html'
    )


@app.route('/diary_of_emotions_actions')
def diary_of_emotions_actions():
    return render_template(
        'diary_of_emotions_actions.html'
    )


@app.route('/diary_of_situations')
def diary_of_situations():
    return render_template(
        'diary_of_situations.html'
    )


@app.route('/habit_tracker')
def habit_tracker():
    return render_template(
        'habit_tracker.html'
    )


@app.route('/settings', methods=["GET", "POST"])
@cross_origin()
def settings_page():
    messages = []
    return render_template(
        'settings.html', messages=messages
    )


@app.route('/about')
def about_page():
    return render_template(
        'about.html'
    )


@app.route('/contacts')
def contacts_page():
    return render_template(
        'contacts.html'
    )


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True, port=1130)
