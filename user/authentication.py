import jwt
from condominium_manager_server.settings import SECRET_JWT
from rest_framework import authentication, status
from rest_framework.exceptions import AuthenticationFailed

from user.models import User


class JWTCustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION', '')
        if not auth:
            return None

        try:
            access_token = auth.split(' ')[1]
            payload = jwt.decode(
                access_token, SECRET_JWT, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('access_token expired')
        except IndexError:
            raise AuthenticationFailed('Token prefix missing')

        user = User.objects.filter(id=payload['user_id']).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.is_active:
            raise AuthenticationFailed('user is inactive')

        return user, None

    def authenticate_header(self, request):
        return status.HTTP_401_UNAUTHORIZED
