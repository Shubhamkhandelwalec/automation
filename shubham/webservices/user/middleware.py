from django.utils.deprecation import MiddlewareMixin
from .forms import *
from collections import OrderedDict
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from .tokenverification import *

class Usersadd(MiddlewareMixin):
    def process_view(self,request,view_func, view_args, view_kwargs):

        form_is_valid = user_ifvalid(request.POST)
        if form_is_valid.is_valid():
            return (view_func(request,form_is_valid))
        else:
            return JsonResponse(form_is_valid.errors,status=500)

class Edituser(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):
        # print("middleware",view_func,view_args,view_kwargs)


        if not User.objects.filter(id=view_kwargs['id'], username=request.POST.get('username')).exists():
            return JsonResponse({"error":"Username and id does not match"},status=404)

        edit_form = editform_ifvalid(request.POST)
        if edit_form.is_valid():
            return view_func(request,edit_form,view_kwargs)
        else:
            return JsonResponse(editform_ifvalid.errors,status=500)

class Deleteuser(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):
        if not User.objects.filter(id=view_kwargs['id'], username=request.POST.get('username')).exists():
            return JsonResponse({"error":"Username and id does not match"},status=404)
        delete_form = deleteform_ifvalid(request.POST)
        if delete_form.is_valid():
            return(view_func(request,delete_form,view_kwargs))
        else:
            return JsonResponse(deleteform_ifvalid.errors,status=500)




class Viewuser(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):



        if not User.objects.filter(id=view_kwargs['id']).exists():
            return JsonResponse({"error":" id does not match for this user"},status=404)

        return view_func(request,view_kwargs)

class Viewalluser(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):
        return view_func(request)

class userlogin(MiddlewareMixin):
    def process_view(self,request,view_func, view_args, view_kwargs):
        if not User.objects.filter(username=request.POST.get('username')).exists():
            return JsonResponse({"error":"You are not authorised user"})


        form_is_valid = userlogin_ifvalid(request.POST)
        if form_is_valid.is_valid():
            return (view_func(request,form_is_valid))
        else:
            return JsonResponse(form_is_valid.errors,status=500)