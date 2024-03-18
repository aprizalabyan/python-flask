from flask import Blueprint, request, make_response, jsonify, render_template
from .models import user_collection
from datetime import datetime

bp = Blueprint("routes", __name__)


@bp.route("/")
def index():
    return ""
    # return render_template("index.html")


@bp.route("/user", methods=["GET", "POST"])
def user():
    data = []
    message = ""
    if request.method == "GET":
        try:
            list_users = list(user_collection.find({}))
            for u in list_users:
                u["_id"] = str(u["_id"])
                u["createdAt"] = u["createdAt"] if "createdAt" in u else ""
                u["updatedAt"] = u["updatedAt"] if "updatedAt" in u else ""
            data = list_users
            make_response().status = 200
        except:
            make_response().status = 500
    elif request.method == "POST":
        try:
            payload = request.json
            if payload:
                new_user = {
                    "name": payload["name"],
                    "email": payload["email"],
                    "createdAt": datetime.now(),
                    "updatedAt": datetime.now(),
                }
                print("postt", new_user)
                user_collection.insert_one(new_user)
                make_response().status = 200
        except:
            make_response().status = 500

    response = jsonify(
        {"status": make_response().status_code, "message": message, "data": data}
    )
    response.headers["Content-Type"] = "application/json"
    return response
