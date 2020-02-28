from django.shortcuts import render
from django.utils.decorators import decorator_from_middleware
from rest_framework.decorators import api_view
from .services import *
from .middleware import *
import json

# Create your views here.
@api_view(['POST'])
@decorator_from_middleware(adduser)
def Adduser(request,form):

    useradd.execute({'username':form.cleaned_data.get('username'),'firstname':form.cleaned_data.get('firstname'),'lastname':form.cleaned_data.get('lastname'),
                   'mobile':form.cleaned_data.get('mobile'),'email':form.cleaned_data.get('email'),'dob':form.cleaned_data.get('dob'),
                   },{'image':form.cleaned_data.get('image')})
    print(">>>>>>>",form.cleaned_data.get('firstname'))


    data = OrderedDict()
    data['message'] = 'Your data has been successfully added'
    return JsonResponse(data,status=200)

@api_view(['POST'])
@decorator_from_middleware(useredit)
def Edituser(request,form,id):
    print(id,type(id))
    useredit_service.execute({'username': form.cleaned_data.get('username'),'firstname': form.cleaned_data.get('firstname'), 'lastname': form.cleaned_data.get('lastname'),
                     'mobile': form.cleaned_data.get('mobile'), 'email': form.cleaned_data.get('email'),
                     'dob': form.cleaned_data.get('dob'),'id':id['id'],
                     }, {'image': form.cleaned_data.get('image')})
    print(">>>>>>>",form.cleaned_data.get('firstname'))

    data = OrderedDict()
    data['message'] = 'Your data has been successfully edited'
    return JsonResponse(data,status=200)
#
#
# @api_view(['POST'])
# @decorator_from_middleware(cmsdelete)
# def Deletecms(request,form):
#     deletecms.execute({'username':form.cleaned_data.get('username'),'title':form.cleaned_data.get('title'),'meta_title':form.cleaned_data.get('meta_title'),'sub_title':form.cleaned_data.get('sub_title'),
#                    'meta_keyword':form.cleaned_data.get('meta_keyword'),'slug':form.cleaned_data.get('slug'),'meta_description':form.cleaned_data.get('meta_description'),'short_description':form.cleaned_data.get('short_description'),
#                    'description':form.cleaned_data.get('description'),'uniqueid':form.cleaned_data.get('uniqueid')},{'image':form.cleaned_data.get('image')})
#     data = OrderedDict()
#     data['message'] = 'Your data has been successfully deleted'
#     return JsonResponse(data, status=200)
#
# @api_view(['GET'])
# @decorator_from_middleware(Viewsingleuser)
# def Viewuser(request,userid):
#     detail= Cmspages.objects.get(id=userid['id'])
#     data = OrderedDict()
#     data['title'] = detail.title
#     data['meta_title'] = detail.meta_title
#     data['sub_title'] = detail.sub_title
#     data['meta_keyword'] = detail.meta_keyword
#
#     data['slug'] = detail.slug
#     data['meta_description'] = detail.meta_description
#     data['short_description'] = detail.short_description
#     data['image'] = json.dumps(str(detail.image))
#
#     data['description'] = detail.description
#     data['uniqueid'] = detail.uniqueid
#
#     return JsonResponse(data)
#
#
# @api_view(['GET'])
# @decorator_from_middleware(Viewalluser)
# def ViewAllusers(request):
#     detail=Cmspages.objects.all()
#     print("detail int",detail)
#     data = OrderedDict()
#     dict={}
#     if not Cmspages.objects.filter().exists():
#         return JsonResponse({'error':'No data in database'})
#     for i in detail:
#         dict[i.id] = OrderedDict()
#         print("i.title",i.title)
#         data['title'] = i.title
#         data['meta_title'] = i.meta_title
#         data['sub_title'] = i.sub_title
#         data['meta_keyword'] = i.meta_keyword
#
#         data['slug'] = i.slug
#         data['meta_description'] = i.meta_description
#         data['short_description'] = i.short_description
#         data['image'] = json.dumps(str(i.image))
#
#         data['description'] = i.description
#         data['uniqueid'] = i.uniqueid
#     return JsonResponse(data)
#
