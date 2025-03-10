from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models import Post
from . import admin_bp
from .forms import PostForm

@admin_bp.route("/admin/post", methods=['GET','POST'], defaults={'post_id':None})
@admin_bp.route("/admin/post/<post_id>/", methods=['GET','POST'])
@login_required
def post_form(post_id):
    formu=PostForm()
    if formu.validate_on_submit():
        titulo=formu.titulo.data
        contenido=formu.content.data
        post=Post(user_id=current_user.id, titulo=titulo, contenido=contenido)
        post.save()
        return redirect(url_for('public.inicio'))
    return render_template("admin/post_form.html", formu=formu)