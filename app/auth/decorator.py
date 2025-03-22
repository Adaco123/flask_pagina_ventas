from functools import wraps
from flask import abort
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        is_admin=getattr(current_user, 'es_admi', False)
        if not is_admin:
            abort(401)
        return f(*args, **kwargs)
    return decorated_function