import os
from dotenv import load_dotenv
from app.config import DOWNLOAD_DIR
from app.core.transformer import Transformer
from flask import Flask, render_template, render_template_string, jsonify, send_file


load_dotenv()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/transform")
def transform():
    return render_template_string(str(Transformer().Transform()))

@app.route("/content/<filename>")
def content(filename):
    try:
        filepath = os.path.join(os.path.join(os.pardir, DOWNLOAD_DIR), filename)
        return send_file(filepath, download_name=filename, as_attachment=True)
    except FileNotFoundError as e:
        return jsonify({"status": "error", "message": f"{os.path.basename(e.filename)} - File does not exist."})

# HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def not_found(error):
    return render_template("500.html"), 500
