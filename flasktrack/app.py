from flask import Flask, request, render_template
import json

from flasktrack.appendbase import Appendbase

app = Flask(__name__)
app.config.from_envvar("FLASKTRACK_CREDENTIAL_LOCATION")
base = Appendbase.from_file("base.json")

@app.route('/<secret>/submit', methods=[ "POST"])
def handle_new_data(secret):
    if secret != app.config["SUBMIT_SECRET"]:
        return ''
    print(request.form)
    base.append(request.form.to_dict())
    base.to_file("base.json")

    return "accepted"

@app.route('/<secret>/view')
def return_monitor_page(secret):
    if secret != app.config["SUBMIT_SECRET"]:
        return ''

    data_js = "let location_data = " + json.dumps(base.stuff) + ";"

    return render_template("base.html", data_js=data_js)
