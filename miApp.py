from flask import Flask, render_template, url_for, redirect, request, abort
import os
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from forms import SignupForm, PostForm, LoginForm
from models import Post, User  # Importar modelos desde models.py
from config import db  # Importar db desde config.py

app = Flask(__name__)
app.config['SECRET_KEY'] = "123456"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:adalid123@localhost:5432/miBaseDeDatos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar db con la aplicación
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)


@app.route("/p/<string:slug>/")
def show_post(slug):
    post = Post.get_by_slug(slug)
    if post is None:
        abort(404)
    return render_template("post_view.html", post=post)

@app.route("/")
@app.route("/inicio")
def inicio():
    #posts = Post.get_all()
    return render_template("base.html")

@app.route("/signup/", methods=["GET", "POST"])
def signUp():
    if current_user.is_authenticated:
        return redirect(url_for('post_form'))
    
    form = SignupForm()
    error = None
    
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        
        user = User.get_by_email(email)
        if user is not None:
            error = f'El email {email} ya está siendo utilizado por otro usuario'
        else:
            user = User(name=name, email=email)
            user.set_password(password)
            user.save()
            
            login_user(user, remember=True)
            next_page = request.args.get('next')
            if not next_page or next_page.startswith('/'):
                return redirect(next_page or url_for('inicio'))
    
    return render_template("sign_up.html", form=form, error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('post_form'))
    form = LoginForm()
    if form.validate_on_submit():
         user = User.get_by_email(form.email.data)
         if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('seccion'))
    return render_template('login_form.html', form=form)

@app.route("/post", methods=['GET', 'POST'], defaults={'post_id': None})
@app.route("/post/<int:post_id>/", methods=['GET', 'POST'])
@login_required
def post_form(post_id):
    form = PostForm()
    if post_id:
        post = Post.get_by_id(post_id)
        if not post:
            abort(404)
        form.title.data = post.title
        form.content.data = post.content

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        if post_id:
            post.title = title
            post.content = content
        else:
            post = Post(user_id=current_user.id, title=title, content=content)
        post.save()
        return redirect(url_for('seccion'))
    return render_template("post_form.html", form=form)

@app.route("/seccion")
@login_required  
def seccion():
    posts = Post.query.filter_by(user_id=current_user.id).all()
    return render_template("misPosts.html", posts=posts)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('inicio'))

if __name__ == "__main__":
    os.environ['FLASK_DEBUG'] = "development"
    app.run(debug=True)