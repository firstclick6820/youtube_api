from django.urls import path

from .views import home, get_video_info





urlpatterns = [
    path('', home, name="home"),
    path('api/get_video_info/<str:id>/', get_video_info, name="get_video_info")   
]