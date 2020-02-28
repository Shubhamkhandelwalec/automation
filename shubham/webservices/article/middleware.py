from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from .forms import *
from django.contrib.auth.models import User
from .models import *

class Articleadd(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):
        print(">>>>>>>>>>.",request.POST)

        if not User.objects.filter(username= request.POST.get('username')):
            return JsonResponse({'error':'You are not authorised user'},status=500)

        article_form = article_ifvalid(request.POST,request.FILES)

        if article_form.is_valid():
            return view_func(request,article_form)
        else:
            return JsonResponse(article_form.errors,status=500)

class Articledit(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):

        print("id",request.POST.get('userid'))
        print("view",view_kwargs)
        if not Article.objects.filter(id= view_kwargs['id'],userid=request.POST.get('userid')):
            return JsonResponse({'error':'This article id is not valid'},status=500)

        article_form = articledit_ifvalid(request.POST,request.FILES)

        if article_form.is_valid():
            return view_func(request,article_form,view_kwargs)
        else:
            return JsonResponse(article_form.errors,status=500)

class Articledelete(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):


        if not Article.objects.filter(id= view_kwargs['id'],userid=request.POST.get('userid')):
            return JsonResponse({'error':'You cannot delete this article'},status=500)

        article_form = articledelete_ifvalid(request.POST,request.FILES)

        if article_form.is_valid():
            return view_func(request,article_form,view_kwargs)
        else:
            return JsonResponse(article_form.errors,status=500)


class viewarticle(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):



        if not Article.objects.filter(id=view_kwargs['id']).exists():
            return JsonResponse({"error":" id does not match for this article"},status=404)

        return view_func(request,view_kwargs)

class Viewallarticle(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):
        return view_func(request)
