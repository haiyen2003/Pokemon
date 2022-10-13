from flask import Blueprint, redirect, render_template, url_for
from ..models import Item

bp = Blueprint("itemRoute", __name__, url_prefix = "/")

@bp.route("/<int:id>", methods=["POST"])
def updateItem():
    item = Item.query.get(id)
