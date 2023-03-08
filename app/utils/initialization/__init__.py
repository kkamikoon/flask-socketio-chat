from app.utils.user import (
    get_user,
    authed
)


def init_template_globals(app):
    app.jinja_env.globals.update(get_user=get_user)
    app.jinja_env.globals.update(authed=authed)
