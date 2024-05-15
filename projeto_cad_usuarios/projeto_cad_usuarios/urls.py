

from django.contrib import admin
from django.urls import path
from app_cad_usuarios import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('home/',views.home,name='home'),
   
   path('about/', views.about, name='about'),  # URL para a tela "about"
    path('entrar/', views.entrar, name='entrar'),
    path('cadastro/', views.cadastro, name='cadastro'),
    
    
]

    

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)