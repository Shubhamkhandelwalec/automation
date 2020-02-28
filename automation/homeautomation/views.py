from django.shortcuts import render
from ipware import get_client_ip
from rest_framework.decorators import api_view
from .forms import *
from django.http import JsonResponse, HttpResponse
import os
import sys
from automation.admininfo import *


@api_view(['GET', 'POST'])
def contact_us(request):
    try:
        if request.method == 'POST':
            form = ContactUsForm(request.POST, request.FILES)
            if form.is_valid():
                client_browser = request.META['HTTP_USER_AGENT']
                client_ip = get_client_ip(request)[0]
                name = request.POST['name']
                phone_no = request.POST['phone']
                email = request.POST['email']
                city = request.POST['city']
                print(client_browser, client_ip, name, phone_no, email, city)
                ContactUs(name=name, phone_no=phone_no, email=email, city=city, client_ip=client_ip,
                          client_browser=client_browser).save()
                return_json = {'message': 'Thanks for showing interest.\nWe will contact you soon'}
                return JsonResponse(return_json, status=200, safe=False)
            else:
                return JsonResponse({'message': form.errors.as_json()}, status=500, safe=False)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        f_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        logger.error(str((e, exc_type, f_name, exc_tb.tb_lineno)))
        return_json = {'message': f"{e}, {f_name}, {exc_tb.tb_lineno}"}
        return JsonResponse(return_json, status=500, safe=False)
