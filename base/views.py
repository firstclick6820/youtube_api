from django.shortcuts import render
from django.core.files import File
from django.http import JsonResponse, HttpResponse, FileResponse


import json
import inflect


from pathlib import Path
import os


from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions



# Import Pytube
from pytube import  ( 
                     YouTube,
                     Playlist,
                     Channel, 
                     Stream
                     )


# Home Page, Provide Useful Information and Routes about the YOUTUBE - API - APP.
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def home(request):
    
    context = {
        "Home": "Welcome to the YOUTUBE API - APP",
        "URLs": {
            "GET Video Info": "/api/get_video_info/j6PbonHsqW0/",
            "GET Full Details":  "/api/get_full_video_details/j6PbonHsqW0/",
            'GET Playlist Details': '/api/get_playlist_details/PLZlA0Gpn_vH8DWL14Wud_m8NeNNbYKOkj/',
            'GET Playlist Complete Details': '/api/get_playlist_full_details/PLZlA0Gpn_vH8DWL14Wud_m8NeNNbYKOkj/',
            'GET Playlist HTML FILE': '/api/get_playlist_html_file/PLZlA0Gpn_vH8DWL14Wud_m8NeNNbYKOkj/',
            'Download A Single Video': '/download/single_video/j6PbonHsqW0/'
        }
    }
    
    
    return JsonResponse(context, safe=False)




# Get basic details of a video
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_video_info(request, id):
    
    # Number Converter to Text
    converter = inflect.engine()

    # create a dynamic url
    url = "https://www.youtube.com/watch?v={}".format(id)    
    video = YouTube(url)


    # Prepare the context to send as resonse
    context = {
        
        "Video ID": video.video_id,
        "Video Watch URL": video.watch_url,
        "Title": video.title,
        "Author": video.author,
        "Views" :  "{} || {}" .format(video.views, converter.number_to_words(video.views)),  
        "Duration": '{} mintues'.format( int(video.length / 60 )),
        "Thumbnail URL": video.thumbnail_url,
        "Channel ID": video.channel_id,
        "Channel URL": video.channel_url,
        "Kewoards": video.keywords,
        "Publish Date": video.publish_date ,
        "Rating": video.rating,
        "Description": video.description,

    }
    
    return JsonResponse(context, safe=False)




# GET FULL Details of a video
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_full_video_details(request, id):
    
    
    # Number Converter to Text
    converter = inflect.engine()

    # create a dynamic url
    url = "https://www.youtube.com/watch?v={}".format(id)    
    video = YouTube(url)
    
    context = {
        "Details": video.vid_info,
    }
    
    
    return JsonResponse(context, safe=False)



# GET Basic Details of Playlist
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_playlist_details(request, id):
    
    converter = inflect.engine()
    
    # Create a Dynamic URL 
    url = "https://www.youtube.com/playlist?list={}".format(id)
    playlist = Playlist(url)
    
    
    context = {
        'ID' : playlist.playlist_id,
        'Playlist URL': playlist.playlist_url,
        'Title':playlist.title ,
        'Total Videos In The List': "{} videos.".format(playlist.length),
        'Views':   "{} || {}" .format(playlist.views, converter.number_to_words(playlist.views)),  
        'Playlist Owner' : playlist.owner,
        'Owner ID' : playlist.owner_id,
        'Owner URL' : playlist.owner_url,
        'Last_updated': playlist.last_updated,
        
        
    }
    
    return JsonResponse(context, safe=False)
    
    
    


# GET FUll Details of playlist
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_playlist_full_details(request, id):

    
    # Create a Dynamic URL 
    url = "https://www.youtube.com/playlist?list={}".format(id)
    playlist = Playlist(url)
    
    
    context = {
        'Full Details' : playlist.initial_data,
        
    }
    
    return JsonResponse(context, safe=False)




# Get Full HTML FILE of playlist
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_playlist_html_file(request, id):
    
    # Create a Dynamic URL 
    url = "https://www.youtube.com/playlist?list={}".format(id)
    playlist = Playlist(url)
    
    
    context = {
        'HTML FILE' : playlist.html,
        
    }
    
    return JsonResponse(context, safe=False)
    
    



# Download a single youtube video
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def download_single_video(request, id):
    
    
    # create a dynamic url
    url = "https://www.youtube.com/watch?v={}".format(id)    
    video = YouTube(url)
    
    
    video_title = video.title

    
    streams = video.streams.filter(only_video=True)
    
 
    # for item in streams:
    #     video_full_name = "{}.{}".format(video_title, item.mime_type[6:])
    #     print(video_full_name)
    
    
    
    # Caution! this method only grap the video in the streams query
    video_ful_name = "{}.{}".format(video_title, streams.first().mime_type[6:])
    
    
    # Caution! this method only grap the video in the streams query
    downloaded_video = streams.first().download()
    
   
    
    
    new_path = "./{}".format(video_ful_name)

    downloaded_video = File(
            file=open(new_path, 'rb'),
            name=Path(new_path))
  
        
    downloaded_video.name = Path(new_path).name
    downloaded_video.size = os.path.getsize(new_path)
    return FileResponse(downloaded_video, as_attachment=True)
  

