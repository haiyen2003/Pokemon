from flask import (Flask, render_template)
from .config import Configuration
import os
from .routes import tracker

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(tracker.bp)
