
from django.contrib import admin
from django.urls import path,include
from tickets import views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/firsttask/',views.first_task),
    path('api/',include('users.urls',namespace='users')),
    path('api/',include('todo.urls')),
    #jwt_auth
    path('api/auth/',TokenObtainPairView.as_view(),name='token_obatin_pair'),
    path('api/token/refresh',TokenRefreshView.as_view(),name='token_refresh'),

]
