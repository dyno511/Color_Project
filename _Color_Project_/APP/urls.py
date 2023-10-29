from django.urls import path, include
import APP.views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [ 
               
    path("", APP.views.Index2, name= 'index2') ,

    path("chupAnh", APP.views.saveImg, name='chupAnh'),
    
    path('video_feed', APP.views.video_feed, name="video-feed"),
    
    path('shutdown/', APP.views.shutdown, name='shutdown'),
    
    path('MoDen/', APP.views.MoDen, name='MoDen'),

    path('TatDen/', APP.views.TatDen, name='TatDen'),

    path('Xoay/', APP.views.Xoay, name='Xoay'),

    path('LenCam/', APP.views.LenCam, name='LenCam'),

    path('XuongCam/', APP.views.XuongCam, name='XuongCam'),
    
    path('Tien/', APP.views.Tien, name='Tien'),
    
    path('Lui/', APP.views.Lui, name='Lui'),
    
    path('Trai/', APP.views.Trai, name='Trai'),
    
    path('Phai/', APP.views.Phai, name='Phai'),
    
    path('TangTC/', APP.views.TangTC, name='TangTC'),
    
    path('GiamTC/', APP.views.GiamTC, name='GiamTC')

    
]