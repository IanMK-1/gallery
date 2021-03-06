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

    def test_get_image_by_id_method(self):
        self.first_image.save_image()
        specific_image = Image.get_image_by_id(self.first_image.id)
        self.assertEqual(self.first_image.image_name, specific_image.image_name)

    def test_search_image_by_category_method(self):
        self.first_image.save_image()
        image_category = Image.search_image_by_category(self.first_image.image_category.category)
        self.assertEqual(image_category.image_category.category, 'travel')

    def test_filter_by_location(self):
        self.first_image.save_image()
        image_by_location = Image.filter_by_location(self.first_image.image_location.location)
        self.assertEqual(image_by_location.image_location.location, 'Dubai')

    def test_update_image_method(self):
        self.first_image.save_image()
        updated_image = Image.update_image(self.first_image.id, 'food.jpg')
        self.assertEqual(updated_image.image, 'food.jpg')


class LocationTestClass(TestCase):

    def setUp(self) -> None:
        self.new_location = Location(location='Thika')
        self.new_location.save_location()

    def tearDown(self) -> None:
        Location.objects.all().delete()

    def test_save_location_method(self):
        self.new_location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_delete_location_method(self):
        self.new_location.save_location()
        self.new_location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def test_update_location_method(self):
        self.new_location.save_location()
        updated_location = Location.update_location(self.new_location.id, 'Egypt')
        self.assertEqual(updated_location.location, 'Egypt')


class CategoryTestClass(TestCase):

    def setUp(self) -> None:
        self.new_category = Category(category='food')
        self.new_category.save_category()

    def tearDown(self) -> None:
        Category.objects.all().delete()

    def test_save_category_method(self):
        self.new_category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_category_method(self):
        self.new_category.save_category()
        self.new_category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    def test_update_category_method(self):
        self.new_category.save_category()
        updated_category = Category.update_category(self.new_category.id, 'sports')
        self.assertEqual(updated_category.category, 'sports')
