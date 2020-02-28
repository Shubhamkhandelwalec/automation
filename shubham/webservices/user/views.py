from django.shortcuts import render
from rest_framework.views import APIView
from collections import OrderedDict
from django.http import JsonResponse
from django.utils.decorators import decorator_from_middleware,make_middleware_decorator
from django.contrib.auth.models import User
from .middleware import *
from django.utils.decorators import method_decorator
from .services import *
from rest_framework.decorators import api_view, schema
import jwt,json
import hashlib
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .tokenverification import *

@api_view(['POST'])
@decorator_from_middleware(Usersadd)
def Adduser(request,form):

    Userservice.execute({'username':form.cleaned_data.get('username'),'first_name':form.cleaned_data.get('firstname'),'last_name':form.cleaned_data.get('lastname'),'email':form.cleaned_data.get('email'),'password':form.cleaned_data.get('password'),'is_superuser':'True','is_staff':'True','is_active':'True'})
    print(">>>>>>>",form.cleaned_data.get('firstname'))

    data = OrderedDict()
    data['message'] = 'Your data has been successfully added'
    return JsonResponse(data,status=200)

@api_view(['POST'])
@decorator_from_middleware(Edituser)
def Edituser(request,form,updateid):
    data = OrderedDict()
    token_if_valid = TokenAuthentication
    var = token_if_valid.authenticate(None, request)
    print("var",var,type(var))
    if 'Error' in var:
        print("var.error", var['Error'])
        data['error'] = 'token is not valid'
        return JsonResponse(data)

    Editservice.execute(
        {'username': form.cleaned_data.get('username'), 'first_name': form.cleaned_data.get('firstname'),
         'last_name': form.cleaned_data.get('lastname'), 'email': form.cleaned_data.get('email'),
         'password': form.cleaned_data.get('password'), 'id': updateid['id']})

    data['message'] = 'Your data has been successfully edited'
    return JsonResponse(data, status=200)


@api_view(['POST'])
@decorator_from_middleware(Deleteuser)
def Deleteuser(request,form,deleteid):
    Deleteservice.execute(
        {'username': form.cleaned_data.get('username'), 'first_name': form.cleaned_data.get('firstname'),
         'last_name': form.cleaned_data.get('lastname'), 'email': form.cleaned_data.get('email'),'id':deleteid['id']})
    data = OrderedDict()
    data['message'] = 'Your data has been successfully deleted'
    return JsonResponse(data, status=200)

# class Deleteuser(APIView):
#     def post(self,request):
#         username = request.POST.get('username')
#         if User.objects.filter(username=username).exists():
#             detail = User.objects.get(username=username)
#             detail.delete()
#             data = OrderedDict()
#             data['message'] = 'Your data has been successfully deleted'
#             return JsonResponse(data)
#         else:
#             return JsonResponse({'error':'username does not exist'},status=404)




@api_view(['GET'])
@decorator_from_middleware(Viewuser)
def Viewuser(request,userid):
    detail= User.objects.get(id=userid['id'])
    data = OrderedDict()
    data['username'] = detail.username
    data['firstname'] = detail.first_name
    data['lastname'] = detail.last_name
    data['email'] = detail.email
    return JsonResponse(data)


@api_view(['GET'])
@decorator_from_middleware(Viewalluser)
def ViewAllusers(request):
    detail=User.objects.all()
    print("detail int",detail)
    data = OrderedDict()
    dict={}
    if not User.objects.filter().exists():
        return JsonResponse({'error':'No data in database'})
    for i in detail:
        dict[i.id] = OrderedDict()
        dict[i.id]['username']= i.username
        dict[i.id]['firstname'] = i.first_name
        dict[i.id]['lastname'] = i.last_name
        dict[i.id]['email'] = i.email
    return JsonResponse(dict)

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
