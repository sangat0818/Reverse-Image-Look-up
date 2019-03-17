#!/usr/bin/env python
import os
import sys
import time
import random
from cloudinary.api import delete_resources_by_tag, resources_by_tag
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import cloudinary
from imagecropper import getImage
cloudinary.config(
  cloud_name = 'syangmay',  
  api_key = '879423429966397',  
  api_secret = 'Z8mtN-b9hzRM1wTVH9hdONAPRT8'  
)

os.chdir(os.path.join(os.path.dirname(sys.argv[0]), '.'))
if os.path.exists('settings.py'):
    exec(open('settings.py').read())

DEFAULT_TAG = "python_sample_basic"


def dump_response(response):
    print("Upload response:")
    for key in sorted(response.keys()):
        print("  %s: %s" % (key, response[key]))
name = str(getImage())
filename = "image.jpg"
link = str(random.randint(1,10000))
name = "image" + link
def upload_files(filename):
    
    print("--- Upload a local file")
    response = upload(filename, tags=DEFAULT_TAG , public_id = name)
    #dump_response(response)
    url, options = cloudinary_url(
        response['public_id'],
        format=response['format'],
        width=250,
        height=250,
        crop="fill"
        
        
    )
    print("completed")
    time.sleep(5)
    
    return (url)
def cleanup():
    response = resources_by_tag(DEFAULT_TAG)
    resources = response.get('resources', [])
    if not resources:
        print("No images found")
        return
    print("Deleting {0:d} images...".format(len(resources)))
    delete_resources_by_tag(DEFAULT_TAG)
    print("Done!")


