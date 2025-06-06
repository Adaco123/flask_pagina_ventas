from flask import render_template, abort, current_app, redirect, url_for, request
from . import public_bp
from flask_login import current_user
from .forms import CommentForm
from app.models import Post, Comment
from werkzeug.exceptions import NotFound
import logging

logger = logging.getLogger(__name__)

@public_bp.route("/")
@public_bp.route("/inicio")
def inicio():
    current_app.logger.info('Mostrando los posts del blog')
    logger.info('Mostrando los posts del blog')
    page = int(request.args.get('page', 1))
    per_page=current_app.config['ITEMS_PER_PAGE']
    post_pagination = Post.all_paginated(page, per_page)
    return render_template("public/publico.html", post_pagination=post_pagination)

@public_bp.route("/p/<string:slug>/",methods= ['GET','POST'])
def show_post(slug):
    logger.info('Mostrando un post')
    post=Post.get_by_slug(slug)
    if not post:
        logger.info(f'El post {slug} no existe')
        raise NotFound(slug)
    form=CommentForm()
    if current_user.is_authenticated and form.validate_on_submit():
        content=form.content.data
        comment=Comment(content=content, user_id=current_user.id, user_name=current_user.nombre,
                        post_id=post.id)
        comment.save()
        return redirect(url_for('public.show_post', slug=post.title_slug))
    return render_template("public/post_view.html", post=post, form=form)
@public_bp.route("/error")
def show_error():
    res = 1 / 0
    posts = Post.get_all()
    return render_template("public/pubico.html", posts=posts)