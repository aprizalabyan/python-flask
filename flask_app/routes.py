from flask import Blueprint, request, make_response, jsonify, render_template
from .models import user_collection

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
        print("postt")

    response = jsonify(
        {"status": make_response().status_code, "message": message, "data": data}
    )
    response.headers["Content-Type"] = "application/json"
    return response
