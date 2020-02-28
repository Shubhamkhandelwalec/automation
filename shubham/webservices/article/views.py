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
import json


from article.middleware import Articleadd
from .services import *

from django.utils.decorators import decorator_from_middleware,make_middleware_decorator
# Create your views here.
@api_view(['POST'])
@decorator_from_middleware(Articleadd)
def Addarticle(request,form):

    articleadd.execute({'title':form.cleaned_data.get('title'),'description':form.cleaned_data.get('description'),'username':form.cleaned_data.get('username')},{'image':form.cleaned_data.get('image')})
    data = OrderedDict()
    data['message'] = 'Your data has been successfully added'
    return JsonResponse(data, status=200)


@api_view(['POST'])
@decorator_from_middleware(Articledit)
def Editarticle(request,form,articleid):


    articledit.execute({'title':form.cleaned_data.get('title'),'description':form.cleaned_data.get('description'),'articleid':articleid['id']},{'image':form.cleaned_data.get('image')})
    data = OrderedDict()
    data['message'] = 'Your data has been successfully edited'
    return JsonResponse(data, status=200)

@api_view(['POST'])
@decorator_from_middleware(Articledelete)
def Deletearticle(request,form,articleid):


    articldetete.execute({'articleid':articleid['id']})
    data = OrderedDict()
    data['message'] = 'Your data has been successfully deleted'
    return JsonResponse(data, status=200)


@api_view(['GET'])
@decorator_from_middleware(viewarticle)
def Viewarticle(request,articleid):

    detail= Article.objects.get(id=articleid['id'])
    data = OrderedDict()
    print(("detail image",detail.image))
    data['title'] = detail.title
    data['description'] = detail.description
    # imagefield=json.dumps(str(detail.image))
    data['image'] = json.dumps(str(detail.image))

    return JsonResponse(data)

@api_view(['GET'])
@decorator_from_middleware(Viewallarticle)
def ViewAllArticle(request):
    detail=Article.objects.all()
    print("detail int",detail)
    data = OrderedDict()
    dict={}
    if not Article.objects.filter().exists():
        return JsonResponse({'error':'No data in database'})
    for i in detail:
        dict[i.id] = OrderedDict()
        dict[i.id]['title']= i.title
        dict[i.id]['description'] =i.description
        dict[i.id]['image'] = json.dumps(str(i.image))

    return JsonResponse(dict)
