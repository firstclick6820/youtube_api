from django.urls import path

from .views import ( 
                    home, 
                    get_video_info,
                    get_full_video_details,
                    get_playlist_details,
                    get_playlist_full_details,
                    get_playlist_html_file
                    )





urlpatterns = [
    path('', home, name="home"),
    path('api/get_video_info/<str:id>/', get_video_info, name="get_video_info"),
    path('api/get_full_video_details/<str:id>/', get_full_video_details, name='get_full_video_details'),
    path('api/get_playlist_details/<str:id>/', get_playlist_details, name='get_playlist_details'),
    path('api/get_playlist_full_details/<str:id>/', get_playlist_full_details, name="get_playlist_full_details"),
    path('api/get_playlist_html_file/<str:id>/', get_playlist_html_file, name="get_playlist_html_file")
]