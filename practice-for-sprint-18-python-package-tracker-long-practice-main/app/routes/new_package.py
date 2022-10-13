from flask import Blueprint, redirect, render_template, url_for
from sqlalchemy.orm import joinedload


bp = Blueprint("orders", __name__, url_prefix="")
