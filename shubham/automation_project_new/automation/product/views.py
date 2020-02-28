from django.shortcuts import render


def home_automation_kit(request):
    return render(request, 'home_automation_kit.html')


def home_automation_product_detail(request, id):
    return render(request, 'home_automation_wifi_plug_oakter.html')

def water_level_controller(request):
    return render(request, 'water_level_controller.html')