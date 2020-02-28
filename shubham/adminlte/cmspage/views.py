from django.shortcuts import render
from django.utils.decorators import decorator_from_middleware
from rest_framework.decorators import api_view
from .services import *
from .middleware import *
import json
from django.contrib.auth import authenticate
from rest_framework.response import Response
import jwt
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
@api_view(['POST'])
@decorator_from_middleware(cmsadd)
def Addcms(request,form):
    print("<><><><><><>form", form.cleaned_data['username'])
    addcms.execute({'username':form.cleaned_data.get('username'),'title':form.cleaned_data.get('title'),'meta_title':form.cleaned_data.get('meta_title'),'sub_title':form.cleaned_data.get('sub_title'),
                   'meta_keyword':form.cleaned_data.get('meta_keyword'),'slug':form.cleaned_data.get('slug'),'meta_description':form.cleaned_data.get('meta_description'),'short_description':form.cleaned_data.get('short_description'),
                   'description':form.cleaned_data.get('description'),'uniqueid':form.cleaned_data.get('uniqueid')},{'image':form.cleaned_data.get('image')})
    print(">>>>>>>",form.cleaned_data.get('firstname'))

    data = OrderedDict()
    data['message'] = 'Your data has been successfully added'
    return JsonResponse(data,status=200)

@api_view(['POST'])
@decorator_from_middleware(cmsedit)
def Editcms(request,form):

    editcms.execute({'username':form.cleaned_data.get('username'),'title':form.cleaned_data.get('title'),'meta_title':form.cleaned_data.get('meta_title'),'sub_title':form.cleaned_data.get('sub_title'),
                   'meta_keyword':form.cleaned_data.get('meta_keyword'),'slug':form.cleaned_data.get('slug'),'meta_description':form.cleaned_data.get('meta_description'),'short_description':form.cleaned_data.get('short_description'),
                   'description':form.cleaned_data.get('description'),'uniqueid':form.cleaned_data.get('uniqueid')},{'image':form.cleaned_data.get('image')})
    print(">>>>>>>",form.cleaned_data.get('firstname'))

    data = OrderedDict()
    data['message'] = 'Your data has been successfully edited'
    return JsonResponse(data,status=200)


@api_view(['POST'])
@decorator_from_middleware(cmsdelete)
def Deletecms(request,form):
    deletecms.execute({'username':form.cleaned_data.get('username'),'title':form.cleaned_data.get('title'),'meta_title':form.cleaned_data.get('meta_title'),'sub_title':form.cleaned_data.get('sub_title'),
                   'meta_keyword':form.cleaned_data.get('meta_keyword'),'slug':form.cleaned_data.get('slug'),'meta_description':form.cleaned_data.get('meta_description'),'short_description':form.cleaned_data.get('short_description'),
                   'description':form.cleaned_data.get('description'),'uniqueid':form.cleaned_data.get('uniqueid')},{'image':form.cleaned_data.get('image')})
    data = OrderedDict()
    data['message'] = 'Your data has been successfully deleted'
    return JsonResponse(data, status=200)

@api_view(['GET'])
@decorator_from_middleware(Viewsingleuser)
def Viewuser(request,userid):
    detail= Cmspages.objects.get(id=userid['id'])
    data = OrderedDict()
    data['title'] = detail.title
    data['meta_title'] = detail.meta_title
    data['sub_title'] = detail.sub_title
    data['meta_keyword'] = detail.meta_keyword

    data['slug'] = detail.slug
    data['meta_description'] = detail.meta_description
    data['short_description'] = detail.short_description
    data['image'] = json.dumps(str(detail.image))

    data['description'] = detail.description
    data['uniqueid'] = detail.uniqueid

    return JsonResponse(data)


@api_view(['GET'])
@decorator_from_middleware(Viewalluser)
def ViewAllusers(request):
    detail=Cmspages.objects.all()
    print("detail int",detail)
    data = OrderedDict()
    dict={}
    if not Cmspages.objects.filter().exists():
        return JsonResponse({'error':'No data in database'})
    for i in detail:
        dict[i.id] = OrderedDict()
        print("i.title",i.title)
        data['title'] = i.title
        data['meta_title'] = i.meta_title
        data['sub_title'] = i.sub_title
        data['meta_keyword'] = i.meta_keyword

        data['slug'] = i.slug
        data['meta_description'] = i.meta_description
        data['short_description'] = i.short_description
        data['image'] = json.dumps(str(i.image))

        data['description'] = i.description
        data['uniqueid'] = i.uniqueid
    return JsonResponse(data)


@api_view(['POST'])
@decorator_from_middleware(userlogin)
def Loginuser(request,form):
    # data = OrderedDict()
    print("MMMMMM",form.cleaned_data.get('username'))
    try:
        user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
    except:
        return JsonResponse({'Error': "Invalid username/password"}, status="400")
    if user is not None:
        payload = {
            'id': user.id,
            'email': user.email,
            'username' : user.username,

        }
        jwt_token = {'token': jwt.encode(payload, "SECRET_KEY").decode('utf-8')}
        print("jwt token",jwt_token)
        return HttpResponse(
            jwt_token['token']
        )
    else:
        return Response(
            json.dumps({'Error': "Invalid credentials"}),
            status=400,
            content_type="application/json"
        )

