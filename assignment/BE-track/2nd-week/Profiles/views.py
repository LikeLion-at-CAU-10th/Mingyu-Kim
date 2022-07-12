from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import *
import json
# Create your views here.

def create_profile(requests):
    
    if requests.method == "POST":

        body = json.loads(requests.body.decode('utf-8'))

        new_profile = Profile.objects.create(
            name = body['name'],
            age = body['age'],
            school = body['school'],
            major = body['major']
        )

        new_profile_json = {
            "id" : new_profile.id,
            "name" : new_profile.name,
            "age" : new_profile.age,
            "school" : new_profile.school,
            "major" : new_profile.major,
            "pup_date" : new_profile.pup_date,
        }

        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message" : "성공",
            "data" : new_profile_json,
        })

    return JsonResponse({
        "status" : 405,
        "success" : False,
        "message" : "method error",
        "data" : None,
    })

def get_profile(requests,id):
    if requests.method == "GET":

        profile = get_object_or_404(Profile, pk = id)

        profile_json = {
            "id" : profile.id,
            "name" : profile.name,
            "age" : profile.age,
            "school" : profile.school,
            "major" : profile.major,
            "pup_date" : profile.pup_date,
        }

        return JsonResponse({
            'status' : 200,
            'success' : True,
            'message' : "Good job",
            'data' : profile_json
        })

    return JsonResponse({
            'status': 405,
            'success': False,
            'message': 'method error',
            'data': None
        })

def get_profile_all(requests):
    if requests.method == "GET":

        profile_all = Profile.objects.all()
        profile_json_all = []

        for profile in profile_all:
            profile_json ={
                "id" : profile.id,
                "name" : profile.name,
                "age" : profile.age,
                "school" : profile.school,
                "major" : profile.major,
                "pup_date" : profile.pup_date,
            }
            profile_json_all.append(profile_json)

        return JsonResponse({
            'status' : 200,
            'success' : True,
            'message' : "Good job",
            'data' : profile_json_all
        })

    return JsonResponse({
            'status': 405,
            'success': False,
            'message': 'method error',
            'data': None
        })
