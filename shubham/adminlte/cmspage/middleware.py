from django.utils.deprecation import MiddlewareMixin
from .forms import *
from collections import OrderedDict
from django.http import JsonResponse



class cmsadd(MiddlewareMixin):
    def process_view(self,request,view_func, view_args, view_kwargs):
        print("comes in middleware")
        form_is_valid = cms_ifvalid(request.POST,request.FILES)
        if form_is_valid.is_valid():

            return (view_func(request,form_is_valid))
        else:
            return JsonResponse(form_is_valid.errors,status=500)

class cmsedit(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):

        print(">>>>",view_kwargs['id'],request.POST.get('username'))
        print(Cmspages.objects.filter(id= view_kwargs['id'],username=request.POST.get('username')))
        if not Cmspages.objects.filter(id= view_kwargs['id'],username=request.POST.get('username')).exists():
            return JsonResponse({'error':'This username is not valid'},status=500)

        cmspage_form = cmsedit_ifvalid(request.POST,request.FILES)

        if cmspage_form.is_valid():
            return view_func(request,cmspage_form)
        else:
            return JsonResponse(cmspage_form.errors,status=500)


class cmsdelete(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):
        if not Cmspages.objects.filter(id=view_kwargs['id'], username=request.POST.get('username')).exists():
            return JsonResponse({"error":"Username and id does not match"},status=404)
        cmsdelete_form = cmsdelete_ifvalid(request.POST)
        if cmsdelete_form.is_valid():
            return(view_func(request, cmsdelete_form))

        else:
            return JsonResponse(cmsdelete_form.errors,status=500)

class Viewsingleuser(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):



        if not Cmspages.objects.filter(id=view_kwargs['id']).exists():
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