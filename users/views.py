from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.hashers import make_password
from .serializer import UserSerializer

class RegisterView(APIView):
  permission_classes= [AllowAny]
   
  def post(self,request):
      username= request.data.get('username')
      email =request.data.get('email')
      password=request.data.get('password')

      if not username or not email  or not password :
         return Response({"error":'all fields are requried'},status=status.HTTP_400_BAD_REQUEST)
      if User.objects.filter(username=username).exists():
          return Response({"error":'Uername already exists'},status=status.HTTP_400_BAD_REQUEST)
      
      user=User.objects.create(
         username=username,
         email=email,
         password= make_password(password)
        ) 

      serializer= UserSerializer(user) 

      refresh = RefreshToken.for_user(user) 
      return Response ({
           'message': 'User created successfully',
           'user':serializer.data,
           'refresh':str(refresh),
           'access':str(refresh.access_token),
         },
        status=status.HTTP_201_CREATED)
      


class LogoutView(APIView):
   permission_classes= [IsAuthenticated]

   def post(self,request): 
        
         try:
            
            refresh_token =request.data.get("refresh")
            if not refresh_token:
                return Response({"error":'refresh_token is requried'},status=status.HTTP_400_BAD_REQUEST)
            
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"error:Successfullt logged out"},status=status.HTTP_200_OK)
         except Exception as e:
           return Response({"error":'Invalid Token'},status=status.HTTP_400_BAD_REQUEST)


            