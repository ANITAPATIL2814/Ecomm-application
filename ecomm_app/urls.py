from django.contrib import admin
from django.urls import path
from ecomm_app import views

urlpatterns = [
    path('home',views.home),
    path('pdetails/<pid>',views.pdetails), # to access id 
    path('viewcart',views.viewcart),
    path('register',views.register),
    path('login/',views.user_login),
    path('logout/',views.user_logout),
    path('catfilter/<cv>',views.catfilter),#cv will be anything we write cv here becz in function views.py we pass cv
    path('sort/<sv>',views.sort),# for sorted value
    path('range',views.range),
    path('addtocart/<pid>',views.addtocart),
    path('remove/<cid>',views.remove),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('placeorder',views.placeorder),
    path('makepayment',views.makepayment)
]

from django.conf.urls.static import static
from ecomm import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)