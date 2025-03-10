from flask import render_template, abort
from . import public_bp
from app.models import Post
@public_bp.route("/")
@public_bp.route("/inicio")
def inicio():
    return render_template("base.html")

@public_bp.route("/p/<string:slug>/")
def show_post(slug):
    post=Post.get_by_slug(slug)
    if post is None:
        abort(404)
    return render_template("public/post_view.html", post=post)