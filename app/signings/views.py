from flask import (Blueprint, render_template, g, redirect,
                   url_for, request, flash, jsonify)
from flask.ext.login import login_required

signings = Blueprint("signings", __name__)
