"""
WSGI config for automation project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automation.settings')

application = get_wsgi_application()

import os
import glob
from PIL import Image
l=[]
ts = 0
found = None

for file_name in glob.glob('C:/Users/shubham.khandelwal/Documents/Python Scripts/demo images/*'):
    fts = os.path.getmtime(file_name)

    if fts > ts:
        ts = fts
        found = file_name

print("file name is",found)
c = found.split("_")
print(c[2])
latest_file= int(c[2])
l.append(latest_file)
for i in range (3):
    decrement = latest_file-1
    l.append(decrement)
    latest_file=decrement
print(l)

for i in range(len(l)):
    img_number = str(l[i])
    # creating a object
    im = Image.open(r"C:/Users/shubham.khandelwal/Documents/Python Scripts/demo images/2019628_image_00"+img_number+"_orig.jpg")
    im.show()

