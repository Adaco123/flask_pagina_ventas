from flask import request, url_for, render_template, redirect, current_app
from flask_login import login_user, current_user, logout_user, login_required
from .forms import SignupForm, LoginForm
from . import auth_bp
from .models import User
from app import login_manager
import logging
from app.common.mail import send_email

logger = logging.getLogger(__name__)

@auth_bp.route("/SignUp/", methods=["GET", "POST"])
def sign_up_form():
    if current_user.is_authenticated:
        return redirect(url_for("auth.cuenta"))
    formu=SignupForm()
    error=None
    if formu.validate_on_submit():
        nombre=formu.nombre.data
        email=formu.email.data
        password=formu.password.data

        user=User.get_by_email(email)
        if user is not None:
            error=f"el Email {email} esta siendo utilizado por otra persona"
        else:
            user= User(nombre=nombre, email=email)
            user.set_password(password)
            user.save()
            send_email(subject='Bienvenid@ al miniblog',
                       sender=current_app.config['DONT_REPLY_FROM_EMAIL'],
                       recipients=[email, ],
                       text_body=f'Hola {nombre}, bienvenid@ al miniblog de Flask',
                       html_body=f'<p>Hola <strong>{nombre}</strong>, bienvenid@ al miniblog de Flask</p>')
            login_user(user, remember=True)
            return redirect(url_for("auth.cuenta"))
        
    return render_template("auth/signup_form.html", formu=formu, error=error)

@auth_bp.route("/login", methods=["GET", "POST"])
def login_form():
    if current_user.is_authenticated:
        return redirect(url_for("auth.cuenta"))
    formu=LoginForm()
    if formu.validate_on_submit():
        user=User.get_by_email(formu.email.data)
        if user is not None and user.check_password(formu.password.data):
            login_user(user, remember=formu.remember_me.data)
            logger.info("acceso permitido")
            return redirect(url_for('public.inicio', form=formu))
    return render_template("auth/login_form.html", form=formu)
@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("public.inicio"))
@login_required
@auth_bp.route("/cuenta")
def cuenta():
    return render_template("auth/cuenta.html")