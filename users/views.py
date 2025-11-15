# users/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import SignupSerializer, SigninSerializer, UserSerializer
from .models import User

class SignupView(APIView):
    authentication_classes = []        # ❗ no JWT needed here
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        data = {
            'token': str(refresh.access_token),
            'refresh': str(refresh),
            'user': UserSerializer(user).data,
        }
        return Response(data, status=status.HTTP_201_CREATED)


class SigninView(APIView):
    authentication_classes = []        # ❗ no JWT check here
    permission_classes = [AllowAny]

    def post(self, request):
        # simple manual auth using email & password
        user_email = request.data.get('user_email')
        password = request.data.get('password')
        if not user_email or not password:
            return Response({'detail': 'Email and password required'}, status=400)

        try:
            user = User.objects.get(user_email=user_email)
        except User.DoesNotExist:
            return Response({'detail': 'Invalid credentials'}, status=400)

        if not user.check_password(password):
            return Response({'detail': 'Invalid credentials'}, status=400)

        refresh = RefreshToken.for_user(user)
        data = {
            'token': str(refresh.access_token),
            'refresh': str(refresh),
            'user': UserSerializer(user).data,
        }
        return Response(data, status=200)
