from django.contrib import admin
from django.urls import path
from app.views import signup_view, login_view, home_view,user_logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),
    path('logout/', user_logout, name='logout'),
]

