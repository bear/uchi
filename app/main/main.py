from flask import Blueprint, render_template
from app.db import get_db


bp_main = Blueprint(
    "bp_main",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/",
)


@bp_main.route("/")
def index():
    # db = get_db()
    # print(db.get("adp::poll::TUT::000999"))
    return render_template("main/index.html")


@bp_main.route("/privacypolicy")
def privacypolicy():
    # db = get_db()
    # print(db.get("adp::poll::TUT::000999"))
    return render_template("main/privacypolicy.html")


@bp_main.route("/presentations")
def presentations():
    # db = get_db()
    # print(db.get("adp::poll::TUT::000999"))
    return render_template("main/presentations.jinja")
