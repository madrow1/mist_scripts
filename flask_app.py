from flask import Flask, render_template, request, jsonify

mist_automation = Flask(__name__)

mist_automation.route("/")
def index():
    return render_template("index.html")

mist_automation.run()