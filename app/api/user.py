from flask import Blueprint, request
from services.users_service import UserService
from utils.JwtToken import token_required

user_route = Blueprint('user_route', __name__)

@user_route.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return UserService.get_user_by_id(user_id)

@user_route.route('/user/login', methods=['POST'])
def login():
    user_data = request.get_json()
    return UserService.login(user_data)

@user_route.route('/user/update', methods=['PATCH'])
@token_required
def update():
    user_data = request.get_json()
    return UserService.update(user_data)

@user_route.route('/user/logout', methods=['GET'])
def logout():
    return UserService.logout()

@user_route.route('/user/islogged', methods=['GET'])
@token_required
def user_is_logged():
    return UserService.is_logged()

