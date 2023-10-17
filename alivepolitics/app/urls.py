from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
#from app.views import PostDetailView,home
#from .views import post_detail



app_name = 'app'


urlpatterns = [
    path('base/',views.base, name='base'),
    path('',views.home, name='home'),
    path('404',views.page_not_found, name='404'),
    #path('posts/',views.detail, name='detail'),
    #path('posts/<slug:slug>/',views.detail, name='detail'),
    #path('<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    #path('post/<str:slug>-<int:pk>/',views.detail , name='detail'),
    path('post/<slug:slug>/',views.post_details, name='post_details'),
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
