from django.contrib import admin
from django.urls import path
from app.views import signup, login_view, home_view, user_logout, about_view, profile_view
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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
