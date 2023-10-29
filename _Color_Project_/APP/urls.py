from django.urls import path, include
import APP.views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [ 
               
    path("", APP.views.Index2, name= 'index2') ,


    path("chupAnh", APP.views.saveImg, name='chupAnh'),
    
    path('video_feed', APP.views.video_feed, name="video-feed"),
    
    path('shutdown/', APP.views.shutdown, name='shutdown'),
    
    path('MoDen/', APP.views.MoDen, name='MoDen')

    
]