from flask import Blueprint, request
from services.users_service import UserService

user_route = Blueprint('user_route', __name__)

@user_route.route('/user/<int:user_id>', methods=['GET'])
def signup(user_id):
    return UserService.get_user_by_id(user_id)