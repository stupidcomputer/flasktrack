from flask import Flask, request, render_template, abort
import json
from datetime import datetime

from flasktrack.appendbase import Appendbase

app = Flask(__name__)
app.config.from_prefixed_env()
app.config.from_envvar("FLASKTRACK_CREDENTIAL_LOCATION")
# configure via FLASK_DATABASE_LOCATION
base = Appendbase.from_file(app.config["DATABASE_LOCATION"])

@app.route('/<secret>/submit', methods=[ "POST" ])
def handle_new_data(secret):
    if secret != app.config["SUBMIT_SECRET"]:
        return ''
    print(request.form)
    base.append(request.form.to_dict())
    base.to_file(app.config["DATABASE_LOCATION"])

    return "accepted"

@app.route('/<secret>/view')
def return_monitor_page(secret):
    if secret != app.config["SUBMIT_SECRET"]:
        return ''

    data_js = "let location_data = " + json.dumps(base.stuff) + ";"

    return render_template("base.html", data_js=data_js)

@app.route('/public')
def public_current_location():
    # Check if public view is enabled and within allowed date range
    if not app.config.get("PUBLIC_VIEW_ENABLED", True):
        abort(404)
    
    public_start = app.config.get("PUBLIC_VIEW_START_DATE")
    public_end = app.config.get("PUBLIC_VIEW_END_DATE")
    
    if public_start or public_end:
        now = datetime.now()
        
        if public_start:
            start = datetime.fromisoformat(public_start)
            if now < start:
                abort(404)
        
        if public_end:
            end = datetime.fromisoformat(public_end)
            if now > end:
                abort(404)
    
    if not base.stuff:
        abort(404)
    
    latest = base.stuff[-1]
    return render_template("public_location.html", location=latest)
