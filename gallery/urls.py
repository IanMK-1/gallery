from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.homepage, name='Home_page'),
    re_path('image/(\d+)', views.single_image, name='Single_image'),
    re_path('photos/(\D+)', views.filter_image_by_location, name='Filter_image')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
