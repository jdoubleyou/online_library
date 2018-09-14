from flask import Blueprint, render_template
from hashlib import md5

blueprint = Blueprint('index', __name__, template_folder="../templates")


@blueprint.route("/", methods=["GET"])
def index():
    icon_version = str(md5(load_favicon()).hexdigest())
    icon_link = "favicon.ico?version={}".format(icon_version)
    return render_template("index.html", icon=icon_link)


@blueprint.route("/favicon.ico", methods=["GET"])
def favicon():
    return load_favicon()


def load_favicon():
    with open("favicon.ico", "rb") as icon:
        return icon.read()
