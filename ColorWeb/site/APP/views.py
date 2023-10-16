from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
#  from APP.Code.Test import 
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import csv, io, base64, urllib, os, openpyxl, subprocess, datetime
# from APP.Code.SQL_LoadModel import AddLoadModelSql, ShowLoadModel
from django.core.files.storage import FileSystemStorage
from matplotlib import pyplot as plt
import numpy as np

from APP.Code.LiveVideo import stream, save_image, create_color_variations

from django.http import StreamingHttpResponse


@csrf_exempt
def video_feed(request):
    return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')


@csrf_exempt
def saveImg(request):
    data = save_image()
    if data != False:
        path = data
        listIMG = create_color_variations(path)
        from APP.Code.ChucNang import callListColor
        arrs = callListColor(path)
        arr = arrs[0]
        listColor = arrs[1]        
        ListThongtin = ""

        for iListColor in list(arrs[2]):
 
            ListThongtin += str(iListColor) + '\n'
    
        data = {
                'arr': arr,
                'listIMG': listIMG,
                'path': path,
                'listColor': listColor,
                'ListThongtin': ListThongtin
            }
        return JsonResponse(data)
    

@csrf_exempt
def Index2(request):
    
    return render(request, 'index2.html')

