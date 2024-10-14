from django.contrib import admin
from django.urls import path
from app.views import signup, login_view, home_view, user_logout, about_view, profile_view, deleteUser_View, confirm_deleteUser_View, updateAccount_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
   path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),
    path('logout/', user_logout, name='logout'),
    path('about/', about_view, name='about'),
    path('profile/', profile_view, name='profile'),
    path('deleteUser/', deleteUser_View, name='deleteUser'),
    path('confirm_deleteUser/', confirm_deleteUser_View, name='confirm_deleteUser'),
    path('updateAccount/', updateAccount_view, name='updateAccount'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
