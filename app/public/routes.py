from flask import render_template, abort, current_app
from . import public_bp
from app.models import Post
from werkzeug.exceptions import NotFound
import logging

logger = logging.getLogger(__name__)

@public_bp.route("/")
@public_bp.route("/inicio")
def inicio():
    current_app.logger.info('Mostrando los posts del blog')
    logger.info('Mostrando los posts del blog')
    posts = Post.get_all()
    return render_template("public/publico.html", posts=posts)

@public_bp.route("/p/<string:slug>/")
def show_post(slug):
    logger.info('Mostrando un post')
    post=Post.get_by_slug(slug)
    if post is None:
        logger.info(f'El post {slug} no existe')
        raise NotFound(slug)
    return render_template("public/post_view.html", post=post)
@public_bp.route("/error")
def show_error():
    res = 1 / 0
    posts = Post.get_all()
    return render_template("public/pubico.html", posts=posts)