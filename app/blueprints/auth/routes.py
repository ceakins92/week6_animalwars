from flask import render_template, flash, redirect, url_for

from app.models import User
from app import db

from . import bp
from app.forms import RegisterForm
from app.forms import SigninForm

@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        username = form.username.data
        password = User.query.filter_by(passw=form.password.data)
        if not username and not password:
            flash(f"No account found. Please retry or register first:")
            return redirect(url_for("auth.register"))
        if username and password:
            flash(f'{username} logged in!')
        else:
            flash(f'Please try again or register first')
            return redirect(url_for('auth.register'))
    return render_template('signin.jinja', form=form)

@bp.route('/register')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter_by(username=username).first()
        email = User.query.filter_by(email=form.email.data)
        if not email and not user:
            u = User(username=username,email=email,password=form.password.data)
            u.commit()
            flash(f"{username} registered!")
            return redirect(url_for("main.home"))
        if user:
            flash(f'{username} is already taken, please try again')
        else:
            flash(f'{email} is already taken, please try again')
    return render_template('register.jinja', form=form)

@bp.route('/contact')
def contact():
    return render_template('contact.jinja')

@bp.route('/commission')
def commission():
    return render_template('commission.jinja')

@bp.route('/purchase')
def purchase():
    return render_template('purchase.jinja')