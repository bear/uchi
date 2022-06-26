from os import environ
from flask import g
from redis import Redis


def get_db():
    if "db" not in g:
        g.db = Redis.from_url(environ.get("REDIS_URL"))
    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()
