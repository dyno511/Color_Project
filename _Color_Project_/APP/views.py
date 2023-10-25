from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
            

        color_categories = ['RED', 'ORANGE', 'YELLOW',
                            'GREEN', 'BLUE', 'INDIGO', 'PURPLE']

        # Loop through the color categories
        for category in color_categories:
            # Check if there are any elements for the current category
            category_data = [i for i in arrs[2] if i[3] == category and i[2] > 0]

            if category_data:
                ListThongtin += '<span class="code"><strong><h3>Energy ' + \
                    category + '</h3></strong></span>'

                # Loop through the energy data and filter by the current category
                for iListColor in category_data:
                    ListThongtin += '<span class="code">Energy ' + \
                        str(iListColor[0]) + ": " + str(iListColor[2]) + '</span><br>'

        # Print or use ListThongtin as needed


# Print or use ListThongtin as needed

        
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

