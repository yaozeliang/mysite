from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('resume/', views.resume, name='resume'),
    # path('gallery/', views.gallery, name='gallery'),
    # path('article/', views.article, name='article'),
    # path('contact/', views.contact, name='contact'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



