import os
from flask import Blueprint, request, redirect
from controllers.url_controller import (
    createShortening, getUrlMap, deleteShortening, updateShortening, getUrl
)
from dotenv import load_dotenv
from markupsafe import escape

load_dotenv("../.env")
url_blueprint = Blueprint("url", __name__)

@url_blueprint.route("/shorten", methods=["GET"])
def shorten():
    try:
        url = request.args.get("url")  
        if not url:
            return {"error": "Missing 'url' parameter"}, 400

        urlHash = createShortening(url)
        base_url = request.host_url.rstrip("/")
        return {"shortened": f"{base_url}/shortened/{urlHash}"}, 200

    except Exception as Error:
        print("Error In Route /shorten:", Error)
        return {"error": "Internal Server Error"}, 500

@url_blueprint.route("/shortened/<string:urlHash>", methods=["GET"])
def shortened(urlHash):
    try:
        urlHash = escape(urlHash)
        destination = getUrl(urlHash)
        print("Redirection:", destination)
        return redirect(destination)

    except Exception as Error:
        print("Error In Route /shortened:", Error)
        return {"error": "Internal Server Error"}, 500
