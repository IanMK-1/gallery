from django.test import TestCase
from .models import Image


# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self) -> None:
        self.first_image = Image(image='color.jpg', image_name='colors image', description='bright colors')

    def tearDown(self) -> None:
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.first_image, Image))


