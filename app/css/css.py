from flask import Blueprint


bp_css = Blueprint(
    "bp_css",
    __name__,
    static_folder="static",
    static_url_path="css",
)
