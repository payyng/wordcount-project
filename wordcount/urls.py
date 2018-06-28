
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('aboutus/',views.aboutus, name = 'aboutus'),
    path('portfolio/',views.portfolio, name ='portfolio')
]
