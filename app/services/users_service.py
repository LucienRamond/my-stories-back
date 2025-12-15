from model.user import User

class UserService():
    def get_user_by_id(user_id):
        try:
            user = User.query.filter_by(id=user_id).first()
        except Exception as e:
            return (f'{e}')
        return (f'{user.username}')
