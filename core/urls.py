from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
   path('', views.home, name='home'),
   path('next/', views.next, name='next')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)