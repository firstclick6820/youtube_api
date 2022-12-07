from django.shortcuts import render
from django.http import JsonResponse
import json
import inflect


from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions



# Import Pytube
from pytube import YouTube



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def home(request):
    
    context = {
        "Home": "Welcome to the YOUTUBE API - APP",
        "URLs": {
            "GET Video Info": "/api/get_video_info/j6PbonHsqW0/"
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
