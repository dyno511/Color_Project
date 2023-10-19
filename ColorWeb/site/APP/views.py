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
        listColor = arrs[1] # nang luong
        listPixel = arrs[3] # list color
        
        # sumEnergy = 0

        ListThongtin = '<ul>'
        ListThongtin += '<span class="code"><strong><h3>Color</h3></strong></span>'
        for iPixel in listPixel:
            ListThongtin += '<span class="code">Color' + \
                str(iPixel) + ' Pixel</span><br>'
            
        ListThongtin += '<span class="code"><strong><h3>Energy</h3></strong></span>'
        for iListColor in list(arrs[2]):
            ListThongtin += '<span class="code">Energy ' + \
                str(iListColor) + '</span><br>'

            # Lấy danh sách các giá trị từ từ điển
            values = list(iListColor.values())

            # Lấy giá trị đầu tiên (trong trường hợp này, giá trị duy nhất)
            value = values[0]
            # sumEnergy += value

        # ListThongtin += '<hr><h2><strong>Sum Energy ' + \
        #     str(sumEnergy) + '</strong></h2>'
        
        ListThongtin += '</ul>'


    
        data = {
                'arr': arr,
                'listIMG': listIMG,
                'path': path,
                'listColor': listColor,
                'ListThongtin': ListThongtin.replace("}", "").replace("{", "")
            }
        return JsonResponse(data)
    

@csrf_exempt
def Index2(request):
    
    return render(request, 'index2.html')

