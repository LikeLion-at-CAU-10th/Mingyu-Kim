from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

def http_response(request):
    if request.method == "GET":
        return HttpResponse("Hello CAU!")

def json_response(request):
    if request.method == "GET":

        data = {
            "name" : "Gyu",
            "school" : "CAU",
        }
        return JsonResponse(data=data)

def index(request): # request는 사용자가 보내는 요청!
    if request.method == 'POST':
        name = request.POST.get('name') # html태그의 name을 뜻하는 것!

        context = {
            'name' : name,
        }

        return render(request, 'index.html', context = context)

    else:
        return render(request, 'index.html') # 요청과 함께 index.html을 보여줘라!


# Create your views here.
