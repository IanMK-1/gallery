from django.shortcuts import render
from .models import Image


# Create your views here.
def homepage(request):
    all_images = Image.display_all_images()
    return render(request, 'homepage.html', {"all_images": all_images})


def single_image(request, id):
    specific_image = Image.get_image_by_id(id)
    return render(request, 'single_image.html', {"specific_image": specific_image})


def filter_image_by_location(request, location):
    images = Image.filter_by_location(location)
    title = location
    return render(request, 'image_location.html', {"images": images, "title": title})
