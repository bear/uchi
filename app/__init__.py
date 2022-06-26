from os import environ
from flask import Flask
from .db import close_db
from authlib.integrations.flask_client import OAuth
from .main.main import bp_main
from .css.css import bp_css
from .images.images import bp_images


# Note: we are purposefully NOT pulling the client secret into the app config
config_keys = (
    "AUTH0_CLIENT_ID",
    "AUTH0_DOMAIN",
    "AUTH0_CALLBACK_URL",
    "AUTH0_AUDIENCE",
    "SECRET_KEY",
    "PROFILE_KEY",
    "JWT_PAYLOAD",
    "REDIS_URL",
    "BASE_URL",
)


def create_app():
    app = Flask(__name__)

    for key in config_keys:
        app.config[key] = environ.get(key)
    app.config["AUTH0_BASE_URL"] = f'https://{app.config["AUTH0_DOMAIN"]}'
    app.secret_key = app.config["SECRET_KEY"]

    app.oauth = OAuth(app)
    app.auth0 = app.oauth.register(
        "auth0",
        client_id=app.config["AUTH0_CLIENT_ID"],
        client_secret=environ.get("AUTH0_CLIENT_SECRET"),
        api_base_url=app.config["AUTH0_BASE_URL"],
        access_token_url=f'{app.config["AUTH0_BASE_URL"]}/oauth/token',
        authorize_url=f'{app.config["AUTH0_BASE_URL"]}/authorize',
        client_kwargs={
            "scope": "openid profile email",
        },
    )
    app.teardown_appcontext(close_db)

    app.register_blueprint(bp_main, url_prefix="/")
    app.register_blueprint(bp_css, url_prefix="/")
    app.register_blueprint(bp_images, url_prefix="/")

    return app
