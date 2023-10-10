from django.urls import path, include
import APP.views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [ 
               

    path("index2", APP.views.Index, name= 'index') ,
    path("", APP.views.Index2, name= 'index2') ,
    # path("cp-admin/", APP.views.CPadmin, name='CPadminH'),
    # path("cp-admin/home.html", APP.views.CPadmin, name='CPadminH'),

    # path("cp-admin/", APP.views.CheckLogin, name='CheckLogin'),
    # path("Login", APP.views.Login_POST, name='Login_POST'),
    # path("Login", APP.views.Login_POST, name='Login_POST'),
    path("upAnh", APP.views.UpAnh, name='upAnh')
    
    # # truyen
    # path("cp-admin/newTruyen", APP.views.newTruyen, name='newTruyen'),

]