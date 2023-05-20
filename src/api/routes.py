from flask import Flask, request, jsonify, url_for, Blueprint, redirect
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from sqlalchemy import extract
import json
import os

api = Blueprint('api', __name__)
@api.route('/signup', methods=["POST"])
def create_user():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    try:
        new_user = User(username = username, password = password)
        db.session.add(new_user)
        db.session.commit()
        data_response =  create_access_token(new_user)
    except Exception as e:
        return jsonify({"message" : f"Error: {str(e)}"}),400
    return jsonify({"message" : "Usuario registrado", "response": data_response}),200