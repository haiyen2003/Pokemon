from flask import Blueprint, redirect, render_template, url_for
from app.models import db,Item

item_routes = Blueprint("itemRoute", __name__, url_prefix = "/api")

@item_routes.route("/items/<int:id>", methods=["PUT"])
def updateItem():
    item = Item.query.get(id)
    item_dict = item.to_dict()
    return {"item": item_dict}

@item_routes.route("/items/<int:id>", methods=['DELETE'])
def delete_item(id):
    item =Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return {"message": "Item deleted successfully"}
