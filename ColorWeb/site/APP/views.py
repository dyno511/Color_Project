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
from APP.Code.ChucNang import callListColor
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
        
        arrs = callListColor(path)
        arr = arrs[0]
        listColor = arrs[1]
        
        print("listColor", listColor)
        
        data = {
                'arr': arr,
                'listIMG': listIMG,
                'path': path,
                'listColor': listColor
            }
        return JsonResponse(data)
    
@csrf_exempt
def Index(request):
    return render(request, 'index.html')

@csrf_exempt
def Index2(request):
    
    return render(request, 'index2.html')
@csrf_exempt
def UpAnh(request):

    myfile = request.FILES['anh']
    fs = FileSystemStorage(
        settings.MEDIA_ROOT + '/image')
    filename = fs.save(myfile.name, myfile)
    myfile = myfile.name
    

    path = settings.MEDIA_ROOT + '/image/'+ myfile
    
    arr = callListColor(path)
    
    data = {
            'arr': arr,
            'path': path
        }
    return JsonResponse(data)



# LoginCheck = False

# def get_random_string(length):
#     import random
#     import string
#     # choose from all lowercase letter
#     letters = string.ascii_lowercase
#     result_str = ''.join(random.choice(letters) for i in range(length))
#     return result_str

# def CheckHetHan(date):
#     expiry_date =  datetime.datetime.strptime(date, '%Y-%m-%d').date()
#     today = datetime.date.today()
#     if expiry_date < today:
#         return False
#     else:
#         return True
    



# @csrf_exempt
# def Login_POST(request):
#     global LoginCheck
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         # doc file csv data
#         with open(settings.MEDIA_ROOT+"dataUser.csv") as csv_file:
#             csv_reader = csv.reader(csv_file, delimiter=',')
#             for row in csv_reader:
#                 print(email, row[0], password, row[1])
#                 if email == row[0] and password == row[1]:
#                     data = {
#                         'id': get_random_string(12),
#                         'thongbao': 'Đăng nhập thành công'
#                     }
#                     LoginCheck = True
#                     return JsonResponse(data)
#         # dang nhap fail
#         data = {
#             'id': 'null',
#             'thongbao': 'Đăng nhập thất thất bại'
#         }
#         return JsonResponse(data)        
        
# @csrf_exempt        
# def CheckLogin(request):
#     global LoginCheck
#     if request.COOKIES.get('id') == '' or request.COOKIES.get('id') == None:
#         return render(request, 'Login.html')
#     else:
#         LoginCheck = True


# def CPadmin(request):
#     global LoginCheck
#     if LoginCheck == True:
#         return render(request, 'CPHome.html')
#     else:
#         return render(request, 'Login.html')


# def newTruyen(request):
#     global LoginCheck
#     if LoginCheck == True:
#         return render(request, 'CPnewTruyen.html')
#     else:
#         return render(request, 'Login.html')



