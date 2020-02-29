from django.shortcuts import render
from .models import Image


# Create your views here.
def homepage(request):
    all_images = Image.display_all_images()
    return render(request, 'homepage.html', {"all_images": all_images})
