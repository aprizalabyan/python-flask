from flask import Blueprint, request, make_response, jsonify, render_template
from .models import user_collection
from datetime import datetime
from bson import ObjectId

bp = Blueprint("routes", __name__)


@bp.route("/")
def index():
    # return ""
    return render_template("index.html")


@bp.route("/user", methods=["GET", "POST", "PUT", "DELETE"])
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
            message = "Get data success"
        except:
            make_response().status = 500
            message = "Get data failed"
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
                user_collection.insert_one(new_user)
                make_response().status = 200
                message = "Data added successfully"
        except:
            make_response().status = 500
            message = "Failed to add"
    elif request.method == "PUT":
        try:
            payload = request.json
            user_id = request.args.get("id")
            if payload and user_id:
                user_collection.update_one(
                    {"_id": ObjectId(user_id)},
                    {
                        "$set": {
                            "name": payload["name"],
                            "email": payload["email"],
                            "updatedAt": datetime.now(),
                        }
                    },
                )
                make_response().status = 200
                message = "Data updated successfully"
        except:
            make_response().status = 500
            message = "Failed to update"
    elif request.method == "DELETE":
        try:
            user_id = request.args.get("id")
            if user_id:
                user_collection.delete_one({"_id": ObjectId(user_id)})
                make_response().status = 200
                message = "Data deleted successfully"
        except:
            make_response().status = 500
            message = "Failed to delete"

    response = jsonify(
        {"status": make_response().status_code, "message": message, "data": data}
    )
    response.headers["Content-Type"] = "application/json"
    return response
