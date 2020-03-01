from django.db import models


class Location(models.Model):
    location = models.CharField(max_length=20)
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls, id, location):
        cls.objects.filter(id=id).update(location=location)
        updated_location = cls.objects.get(id=id)
        return updated_location


class Category(models.Model):
    CATEGORY_CHOICES = (
        ('travel', 'Travel'),
        ('food', 'Food'),
        ('sports', 'Sports'),
        ('landscape', 'Landscape')
    )
    category = models.CharField(max_length=9, choices=CATEGORY_CHOICES, default='food')

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id, category):
        cls.objects.filter(id=id).update(category=category)
        updated_category = cls.objects.get(id=id)
        return updated_category


class Image(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    image_name = models.CharField(max_length=30)
    description = models.TextField()
    image_location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def display_all_images(cls):
        all_images = cls.objects.all()
        return all_images

    @classmethod
    def update_image(cls, id, image):
        cls.objects.filter(id=id).update(image=image)
        updated_image = cls.objects.get(id=id)
        return updated_image

    @classmethod
    def get_image_by_id(cls, id):
        specific_image = cls.objects.get(id=id)
        return specific_image

    @classmethod
    def search_image_by_category(cls, image_category):
        search_result = cls.objects.filter(image_category__category=image_category)
        return search_result

    @classmethod
    def filter_by_location(cls, location):
        search_image_by_location = cls.objects.filter(image_location__location=location)
        return search_image_by_location
