
from django.contrib import admin
from django.urls import path,include
from tickets import views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),  # واجهة المستخدم العادية
    path('api/auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #jwt_auth
    path('api/',include('todo.urls')),
    path('api/auth/',TokenObtainPairView.as_view(),name='token_obatin_pair'),
    path('api/token/refresh',TokenRefreshView.as_view(),name='token_refresh'),

]
