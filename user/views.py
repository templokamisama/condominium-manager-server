from rest_framework import status, viewsets
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer
from user.utils import generate_access_token


class UserViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def sign_up(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        user_serializer.save()
        return Response(user_serializer.data, status.HTTP_201_CREATED)

    def sign_in(self, request):
        user = User.objects.filter(username=request.data['username'])

        if not user.exists:
            raise AuthenticationFailed('user not found')
        if (not user[0].check_password(request.data['password'])):
            raise AuthenticationFailed('wrong password')

        token = generate_access_token(user[0])
        return Response({'token': token, 'error': ''}, status.HTTP_200_OK)
