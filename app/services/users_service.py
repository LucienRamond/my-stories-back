from model.user import User
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import os
from datetime import datetime, timezone, timedelta
from flask import make_response

class UserService():
    def get_user_by_id(user_id):
        try:
            user = User.query.filter_by(id=user_id).first()
        except Exception as e:
            return (f'{e}')
        return (f'{user.username}')
    
    def login(user_data):
        try:

            user = User.query.filter_by(username=user_data['username']).first()

            if not user or not check_password_hash(user.password_hash, user_data['password']):
                return ("Nom d'utilisateur ou mot de passe incorrect !"), 401
                 
            token = jwt.encode({"username":user.username, "exp": datetime.now(timezone.utc) + timedelta(hours=1)}, os.environ.get('SECRET_KEY'), algorithm="HS256")
            response = make_response({"name": user.username})
            response.set_cookie("jwt_token", token)

            return response
          
        except Exception as e:
            return (f'{e}')
        
    def is_logged():
        return make_response({"islogged":True})
