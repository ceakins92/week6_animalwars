from flask import render_template

from . import bp

@bp.route('/contact')
def contact():
    return render_template('contact.jinja')

@bp.route('/commission')
def commission():
    return render_template('commission.jinja')