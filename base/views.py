from django.shortcuts import render
from django.http import JsonResponse
import json
import inflect


from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions



# Import Pytube
from pytube import  ( 
                     YouTube,
                     Playlist)



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
        }
    }
    
    
    return JsonResponse(context, safe=False)





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
    
    
    
    # Use intial data param in the playlist to retrive full details about the playlist
    # use the html attribute on the playlist to retrive the html file of the list
    



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




@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_playlist_html_file(request, id):
    
    # Create a Dynamic URL 
    url = "https://www.youtube.com/playlist?list={}".format(id)
    playlist = Playlist(url)
    
    
    context = {
        'Full Details' : playlist.html,
        
    }
    
    return JsonResponse(context, safe=False)
    