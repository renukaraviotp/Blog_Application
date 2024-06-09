from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('loginregister/', views.loginregister, name='loginregister'),
    path('userhome/', views.userhome, name='userhome'),
    path('signupaction/', views.signupaction, name='signupaction'),
    path('loginaction/', views.loginaction, name='loginaction'),
    path('logoutt/', views.logoutt, name='logoutt'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_create/', views.post_create, name='post_create'),
    path('post_detail/<int:pk>', views.post_detail, name='post_detail'),
    path('post_edit/<int:pk>', views.post_edit, name='post_edit'),
    path('post_delete/<int:pk>', views.post_delete, name='post_delete'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
