from flask import render_template, abort
from . import public_bp
from app.models import Post
from werkzeug.exceptions import NotFound
@public_bp.route("/")
@public_bp.route("/inicio")
def inicio():
    return render_template("base.html")

@public_bp.route("/p/<string:slug>/")
def show_post(slug):
    post=Post.get_by_slug(slug)
    if post is None:
        raise NotFound(slug)
    return render_template("public/post_view.html", post=post)
@public_bp.route("/error")
def show_error():
    res = 1 / 0
    posts = Post.get_all()
    return render_template("public/pubico.html", posts=posts)