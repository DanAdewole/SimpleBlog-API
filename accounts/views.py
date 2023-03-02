from django.contrib.auth import authenticate
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from .tokens import create_jwt_pair_for_user
from .serializers import SignUpSerializer


class SignUpView(generics.GenericAPIView):
    """sign up user"""
    
    serializer_class = SignUpSerializer
    permission_classes=[]

    @swagger_auto_schema(
        operation_summary="Create a user account",
        operation_description="This endpoint signs up a user with email, firstname, lastname, and a password",
    )
    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {"message": "User Created Successfully", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogInView(APIView):
    """login and authenticate user"""
    
    @swagger_auto_schema(
        operation_summary="Generates JWT pair",
        operation_description="This endpoint logs in a user with email and password"
    )
    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        user = authenticate(email=email, password=password)
        
        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {
				"message": "Login Successful",
				"token": tokens,
			}
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Invalid email or password"})
        

    @swagger_auto_schema(
        operation_summary="Get request info",
        operation_description="This endpoints shows the request info"
    )
    def get(self, request: Request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth),
        }

        return Response(data=content, status=status.HTTP_200_OK)
