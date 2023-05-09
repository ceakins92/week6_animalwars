from flask import render_template

from . import bp

@bp.route('/')
def home():
    matrix = {
        'instructors': ('sean','dylan'),
        'students':('ray','hamed','gian','ben','christoper','alec')
    }
    return render_template('index.jinja',title='Animal Wars - Home', instructors=matrix['instructors'], students=matrix['students'])

@bp.route('/about')
def about():
    return render_template('about.jinja')