import bcrypt
from fastapi import HTTPException, status

from app.internal import encode_token
from app.schemas import CreateUser, LoginUser
from app.repository import UserRepository


class UserService:

    user_repository = UserRepository

    def create_user(self, user: CreateUser):
        user.password = bcrypt.hashpw(
            user.password.encode('utf8'),
            bcrypt.gensalt()
        ).decode('utf8')
        try:
            user = self.user_repository.create_user(user)
            token = encode_token({'user_id': user.get_id()})
            return LoginUser(user=user.to_dict(), token=token)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.__str__())

    def login(self, email, password):
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with email {email} not found"
            )
        if bcrypt.checkpw(password.encode('utf8'), user['password'].encode('utf8')):
            token = encode_token({'user_id': user.get_id()})
            return LoginUser(user=user.to_dict(), token=token)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid Password'
            )

    def get_user_by_email(self, email):
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with email {email} not found"
            )
        return user.to_dict()
