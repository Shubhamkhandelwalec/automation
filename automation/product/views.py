from django.shortcuts import render


def home_automation_kit(request):
    return render(request, 'home_automation_kit.html')


def home_automation_product_detail(request, id):
    return render(request, 'home_automation_wifi_plug_oakter.html')

def water_level_controller(request):
    return render(request, 'water_level_controller.html')

def solar_products(request):
    return render(request, 'solar_product.html')

def security_and_surveillance(request):
    return render(request, 'security_and_surveillance.html')

