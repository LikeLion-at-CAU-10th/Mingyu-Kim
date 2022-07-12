from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import *
import json

# Create your views here.
def create_category(requests):
    if requests.method == "POST":

        body = json.loads(requests.body.decode('utf-8'))

        new_category = Category.objects.create(
            title = body['title'],
            view_auth = body['view_auth'],
            color = body['color']
        )

        new_category_json = {
            "id" : new_category.id,
            "title" : new_category.title,
            "view_auth" : new_category.view_auth,
            "color" : new_category.color,
            "pup_date" : new_category.pup_date,
        }

        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message" : "성공",
            "data" : new_category_json,
        })

    return JsonResponse({
        "status" : 405,
        "success" : False,
        "message" : "method error",
        "data" : None,
    })

def get_category_all(request):
    if request.method == "GET":
        category_all = Category.objects.all()
        category_json_all = []

        for category in category_all:
            category_json = {
                "id" : category.id,
                "title" : category.title,
                "view_auth" : category.view_auth,
                "color" : category.color,
                "pup_date" : category.pup_date,
            }
            category_json_all.append(category_json)
            
        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message":"생성 성공",
            "data" : category_json_all
        })

def get_category(request, id):
    if request.method == "GET":
        category = get_object_or_404(Category, pk = id)
        category_json = {
            "id" : category.id,
            "title" : category.title,
            "view_auth" : category.view_auth,
            "color" : category.color,
            "pup_date" : category.pup_date,
        }
        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message":"생성 성공",
            "data" : category_json
        })