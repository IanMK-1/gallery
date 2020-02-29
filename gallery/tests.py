from django.test import TestCase
from .models import Image, Location, Category


# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self) -> None:
        # creating a new location and saving it
        self.new_location = Location(location='Dubai')
        self.new_location.save()

        # creating a new category and saving it
        self.select_category = Category(category='travel')
        self.select_category.save()

        # creating a new image and saving it
        self.first_image = Image(image='color.jpg', image_name='colors image', description='bright colors',
                                 image_location=self.new_location, image_category=self.select_category)
        self.first_image.save_image()

    def tearDown(self) -> None:
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.first_image, Image))
        self.assertTrue(isinstance(self.new_location, Location))
        self.assertTrue(isinstance(self.select_category, Category))

    def test_save_method(self):
        self.first_image.save_image()
        self.new_location.save()
        self.select_category.save()
        locations = Location.objects.all()
        categories = Category.objects.all()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
        self.assertTrue(len(locations) > 0)
        self.assertTrue(len(categories) > 0)

    def test_delete_image(self):
        self.first_image.save_image()
        self.first_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)
