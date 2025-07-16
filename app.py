from flask import Flask, render_template
from routes.url_routes import url_blueprint  
from dotenv import load_dotenv
import os

load_dotenv(".env")

app = Flask(__name__, template_folder="./views")
app.register_blueprint(url_blueprint)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
