from model.user import User
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import os
from datetime import datetime, timezone, timedelta
from flask import make_response
from server import db

class UserService():
    def get_user_by_id(user_id):
        try:
            user = User.query.filter_by(id=user_id).first()
            response = make_response({
                "id":user.id,
                "name":user.username,
                "avatar_img":user.avatar_img,
            })
        except Exception as e:
            return (f'{e}')
        return response

    def get_all_users():
        try:
            users = User.query.all()

            response = [{"id":user.id,
                "name":user.username,
                "avatar_img":user.avatar_img} for user in users]
            
        except Exception as e:
            return (f'{e}')
        
        return make_response(response)
    
    def login(user_data):
        try:

            user = User.query.filter_by(username=user_data['username']).first()

            if not user or not check_password_hash(user.password_hash, user_data['password']):
                return ("Nom d'utilisateur ou mot de passe incorrect !"), 401
                 
            token = jwt.encode({"username":user.username, "exp": datetime.now(timezone.utc) + timedelta(hours=1)}, os.environ.get('SECRET_KEY'), algorithm="HS256")
            response = make_response({"id":user.id, "name": user.username, "avatar_img": user.avatar_img})
            response.set_cookie("jwt_token", token, httponly=True)

            return response
          
        except Exception as e:
            return (f'{e}')

    def logout():
        response = make_response({'message': 'Successfully logged out'}, 200)
        response.delete_cookie("jwt_token")
        return response
    
    def update(user_data):
        user = User.query.filter_by(id=user_data["user_id"]).first()
        user.avatar_img = user_data['avatar_img']

        db.session.commit()
        
        return make_response({"message":"Avatar successfully updated !"})
            
    def is_logged():
        return make_response({"islogged":True})
