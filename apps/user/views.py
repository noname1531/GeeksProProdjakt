from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.user.serializers import UserSerializer

class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": {
                "username": user.username,
            },
            "message": "User registered successfully",
        })