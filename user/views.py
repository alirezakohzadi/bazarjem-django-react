from django.contrib.auth import authenticate, get_user_model
from django.middleware.csrf import get_token
from django.http import JsonResponse
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .serializers import RegisterSerializer, LoginSerializer, ChangePasswordSerializer, UserSerializer, ChangeUserRoleSerializer

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "ثبت‌نام با موفقیت انجام شد."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                response = Response({"message": "ورود موفقیت‌آمیز بود"})
                csrftoken = get_token(request)
                response.set_cookie(key='refresh_token', value=str(refresh), httponly=False, secure=True, samesite='None', max_age=360000)
                response.set_cookie(key='access_token', value=str(refresh.access_token), httponly=False, secure=True, samesite='None', max_age=360000)
                response.set_cookie(key="csrftoken", value=csrftoken, httponly=False, secure=True, samesite='None', max_age=360000)
                return response
            return Response({"error": "ایمیل یا رمز عبور اشتباه است."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({"error": "رمز عبور فعلی اشتباه است."}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"message": "رمز عبور با موفقیت تغییر کرد."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangeUserRoleView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "کاربر پیدا نشد."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ChangeUserRoleSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "نقش کاربر با موفقیت تغییر کرد."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckAuthView(APIView):
    authentication_classes = []

    def get(self, request):
        jwt_auth = JWTAuthentication()
        user = None
        auth_header = request.headers.get("Authorization")
        if auth_header:
            try:
                user, _ = jwt_auth.authenticate(request)
            except AuthenticationFailed:
                pass
        if not user:
            access_token = request.COOKIES.get("access_token")
            if access_token:
                try:
                    refresh = RefreshToken(access_token)
                    new_access_token = str(refresh.access_token)
                    validated_token = jwt_auth.get_validated_token(new_access_token)
                    user = jwt_auth.get_user(validated_token)
                    response = JsonResponse({"logged_in": True, "username": user.username})
                    response["Authorization"] = f"Bearer {new_access_token}"
                    return response
                except Exception:
                    pass
        if user:
            return JsonResponse({"logged_in": True, "username": user.username})
        return JsonResponse({"logged_in": False})


class LogoutView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        response = Response({"message": "Logged out successfully"})
        response.delete_cookie("access_token", path="/", samesite="None")
        response.delete_cookie("refresh_token", path="/", samesite="None")
        return response
