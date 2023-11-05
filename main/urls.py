from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('guide_sc.urls', namespace='guide_sc')),
    path('', include('games.urls')),
    path('', include('parser_app.urls')),
    path('', include('custom_users.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
               +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
