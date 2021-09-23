from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', user_views.user_register, name = 'users-register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/user_login.html'), name = 'users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/user_logout.html'), name = 'users-logout'),

    path('', include('IMS.urls'))
]