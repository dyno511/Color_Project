from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from APP.Code.LiveVideo import stream, save_image, create_color_variations
from django.http import StreamingHttpResponse
import time

@csrf_exempt
def video_feed(request):
    return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')


# @csrf_exempt
# def saveImg(request):
#     data = save_image()
#     if data != False:
#         path = data
#         listIMG = create_color_variations(path)
#         from APP.Code.ChucNang import callListColor
#         arrs = callListColor(path)
#         arr = arrs[0]
#         listColor = arrs[1] # nang luong
#         listPixel = arrs[3] # list color
        
#         # sumEnergy = 0

#         ListThongtin = '<ul>'
#         ListThongtin += '<span class="code"><strong><h3>Color</h3></strong></span>'
#         for iPixel in listPixel:
#             ListThongtin += '<span class="code">Color' + \
#                 str(iPixel) + ' Units</span><br>'
            

#         color_categories = ['RED', 'ORANGE', 'YELLOW',
#                             'GREEN', 'BLUE', 'INDIGO', 'PURPLE']

#         # Loop through the color categories
#         for category in color_categories:
#             # Check if there are any elements for the current category
#             category_data = [i for i in arrs[2] if i[3] == category and i[2] > 0]

#             if category_data:
#                 ListThongtin += '<span class="code"><strong><h3>Energy ' + \
#                     category + ' Chanel </h3></strong></span>'

#                 # Loop through the energy data and filter by the current category
#                 for iListColor in category_data:
#                     ListThongtin += '<span class="code">Energy no' + \
#                         str(iListColor[0]+1) + ": " + str(iListColor[2]) + ' units </span><br>'

#         # Print or use ListThongtin as needed


# # Print or use ListThongtin as needed

        
#         ListThongtin += '</ul>'


    
#         data = {
#                 'arr': arr,
#                 'listIMG': listIMG,
#                 'path': path,
#                 'listColor': listColor,
#                 'ListThongtin': ListThongtin.replace("}", "").replace("{", "")
#             }
#         return JsonResponse(data)
    
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

        ListThongtin = '<ul>'
        ListThongtin += '<span class="code"><strong><h3>Color</h3></strong></span>'
        for iPixel in listPixel:
            ListThongtin += '<span class="code">Color' + str(iPixel) + ' Units</span><br>'

        color_categories = ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'INDIGO', 'PURPLE']

        # Loop through the color categories
        for category in color_categories:
            # Check if there are any elements for the current category
            category_data = [i for i in arrs[2] if i[3] == category and i[2] > 0]

            if category_data:
                # Initialize a variable to store the total energy for the current category
                total_energy = 0

                # Loop through the energy data and filter by the current category
                for iListColor in category_data:
                    total_energy += iListColor[2]

                ListThongtin += '<span class="code"><strong><h3>Energy ' + category + ' Chanel: ' + str(total_energy) + ' units</h3></strong></span>'

                # Loop through the energy data and filter by the current category
                for iListColor in category_data:
                    ListThongtin += '<span class="code">Energy no' + str(iListColor[0]+1) + ": " + str(iListColor[2]) + ' units </span><br>'

        ListThongtin += '</ul'

        data = {
            'arr': arr,
            'listIMG': listIMG,
            'path': path,
            'listColor': listColor,
            'ListThongtin': ListThongtin.replace("}", "").replace("{", "")
        }
        return JsonResponse(data)    
import os, platform
from django.http import JsonResponse

@csrf_exempt
def shutdown(request):
    if request.method == 'POST':
        try:
             os.system("systemctl suspend")
           

            
        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'})
    else:
        return JsonResponse({'message': 'Invalid request method.'})



@csrf_exempt
def Index2(request):  
    return render(request, 'index2.html')

import serial
from django.views.decorators.csrf import csrf_exempt
import time
# Define a common function to send commands to the serial device
def send_command(command):
    try:
        data = command
        ser = serial.Serial('/dev/ttyUSB0', 9600)  # Change 'COM7' to the appropriate COM port
        ser.write(data.encode())
        time.sleep(1)
    except:
        pass

@csrf_exempt
def MoDen(request):
    send_command("0003")  # Send the command to open the device
    return JsonResponse({"status": 200})

@csrf_exempt
def TatDen(request):
    send_command("0002")  # Send the command to close the device
    return JsonResponse({"status": 200})

@csrf_exempt
def Xoay(request):
    send_command("0")  # Send the command to rotate
    return JsonResponse({"status": 200})

@csrf_exempt
def LenCam(request):
    send_command("0006")  # Send the command to move up
    return JsonResponse({"status": 200})

@csrf_exempt
def XuongCam(request):
    send_command("0008")  # Send the command to move down
    return JsonResponse({"status": 200})

@csrf_exempt
def Tien(request):
    send_command("0007")  # Send the command to move forward
    return JsonResponse({"status": 200})

@csrf_exempt
def Lui(request):
    send_command("0012")  # Send the command to move backward
    return JsonResponse({"status": 200})

@csrf_exempt
def Trai(request):
    send_command("0009")  # Send the command to move left
    return JsonResponse({"status": 200})

@csrf_exempt
def Phai(request):
    send_command("0010")  # Send the command to move right
    return JsonResponse({"status": 200})

@csrf_exempt
def TangTC(request):
    send_command("0")  # Send the command to increase speed
    return JsonResponse({"status": 200})

@csrf_exempt
def GiamTC(request):
    send_command("0")  # Send the command to decrease speed
    return JsonResponse({"status": 200})

