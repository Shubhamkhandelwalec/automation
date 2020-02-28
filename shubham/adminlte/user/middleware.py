from django.utils.deprecation import MiddlewareMixin
from .forms import *
from collections import OrderedDict
from django.http import JsonResponse



class adduser(MiddlewareMixin):
    def process_view(self,request,view_func, view_args, view_kwargs):

        form_is_valid = user_ifvalid(request.POST,request.FILES)
        if form_is_valid.is_valid():

            return (view_func(request,form_is_valid))
        else:
            return JsonResponse(form_is_valid.errors,status=500)

class useredit(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):


        print("id type",type(view_kwargs['id']))
        if not User.objects.filter(id= view_kwargs['id']).exists():
            return JsonResponse({'error':'This id is not valid'},status=500)

        edit_form = useredit_ifvalid(request.POST,request.FILES)

        if edit_form.is_valid():
            return view_func(request,edit_form,view_kwargs)
        else:
            return JsonResponse(edit_form.errors,status=500)

#
# class cmsdelete(MiddlewareMixin):
#     def process_view(self,request,view_func,view_args,view_kwargs):
#         if not Cmspages.objects.filter(id=view_kwargs['id'], username=request.POST.get('username')).exists():
#             return JsonResponse({"error":"Username and id does not match"},status=404)
#         cmsdelete_form = cmsdelete_ifvalid(request.POST)
#         if cmsdelete_form.is_valid():
#             return(view_func(request, cmsdelete_form))
#
#         else:
#             return JsonResponse(cmsdelete_form.errors,status=500)
#
# class Viewsingleuser(MiddlewareMixin):
#     def process_view(self,request,view_func,view_args,view_kwargs):
#
#
#
#         if not Cmspages.objects.filter(id=view_kwargs['id']).exists():
#             return JsonResponse({"error":" id does not match for this user"},status=404)
#
#         return view_func(request,view_kwargs)
#
# class Viewalluser(MiddlewareMixin):
#     def process_view(self,request,view_func,view_args,view_kwargs):
#         return view_func(request)