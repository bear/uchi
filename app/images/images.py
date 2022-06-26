from flask import Blueprint


bp_images = Blueprint(
    "bp_images",
    __name__,
    static_folder="static",
    static_url_path="images",
)
