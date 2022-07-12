from django.contrib import admin
from django.urls import path, include
from posts.views import http_response , index, json_response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name = 'index'),
    path('',http_response, name = "http_response"),
    path('json/',json_response, name='json_response'),
    path('todomates/', include('todomates.urls')), 
    # 사실 todomates도 여기다가 다 적어도 되는데 앱이 많아지면 더러워지니까 한 번 더 나뉘는 구간을 만드는거임!
    path('Profiles/', include('Profiles.urls')),
]   
