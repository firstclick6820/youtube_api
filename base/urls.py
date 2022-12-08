from django.urls import path

from .views import home, get_video_info,get_full_video_details





urlpatterns = [
    path('', home, name="home"),
    path('api/get_video_info/<str:id>/', get_video_info, name="get_video_info"),
    path('api/get_full_video_details/<str:id>/', get_full_video_details, name='get_full_video_details'),
]