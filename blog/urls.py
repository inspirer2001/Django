
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
    path('contactus/',views.contactus,name= 'blog-contactus'),
    path('home/',views.home,name= 'blog-home'),
    path('signup/', views.signup, name='blog-signup'),
    path('login/', views.Login, name='blog-login'),
    path('profile/', views.profile, name='blog-profile'),
    path('logout/', views.logout, name='blog-logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)