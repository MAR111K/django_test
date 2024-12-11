from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class UserMeView(APIView):
    permission_classes = [IsAuthenticated]  

    @swagger_auto_schema(
        operation_description="Получение информации о текущем пользователе",
        responses={200: openapi.Response(
            description="Информация о пользователе",
            examples={
                "application/json": {
                    "id": 1,
                    "username": "john_doe",
                    "email": "john@example.com"
                }
            }
        )}
    )
    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "phone": user.phone,
            "image_url": request.build_absolute_uri(user.image.url) if user.image else None
        })