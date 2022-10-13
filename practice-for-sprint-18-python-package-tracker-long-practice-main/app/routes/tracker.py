from flask import Blueprint, redirect, render_template, url_for
bp = Blueprint("tracker", __name__, url_prefix="")

@bp.route('/')
def index():
    return "Package Tracker"
