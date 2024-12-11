from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from app.serializers import RegisterSerializer,LoginSerializer
from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from app.utils.email import send_registration_email

class RegisterView(APIView):
    @swagger_auto_schema(
        request_body=RegisterSerializer,  
        responses={201: "User registered successfully", 400: "Invalid data"}
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_registration_email(user.email)
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    @swagger_auto_schema(
        request_body=LoginSerializer,  
        responses={201: "User registered successfully", 400: "Invalid data"}
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            # Генерируем JWT токен
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)