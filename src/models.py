from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Location(models.Model):
    refreshment_choices = [('no_restaurant', 'No restaurant'), ('restaurant_on_site', 'Restaurant on site')]
    entrance_choices = [('no_fee', 'No entrance fee'), ('fee', 'Entrance fee')]
    diving_choices = [('not_suitable', 'Not suitable for diving'), ('suitable', 'Suitable for diving')]
    accessibility_parking_choices = [
        ('very_close', 'Very Close'), ('100m', '100 m'), ('250m', '250 m'),
        ('500m', '500 m'), ('1000m', '1000 m'), ('1000m_plus', '1000 m +')
    ]
    dog_swimming_choices = [('suitable', 'Suitable for dogs'), ('not_suitable', 'Not suitable for dogs')]
    nudist_beach_choices = [('not_suitable', 'Not suitable for nudists'), ('suitable', 'Suitable for nudists')]

    mapotic_id = models.CharField(max_length=50, unique=True)
    longitude = models.DecimalField(max_digits=500, decimal_places=18)
    latitude = models.DecimalField(max_digits=500, decimal_places=18)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    rating = models.CharField(max_length=50, blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    import_id = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    web = models.TextField(max_length=1024, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    refreshment = models.CharField(choices=refreshment_choices, max_length=50, blank=True, null=True)
    diving = models.CharField(choices=diving_choices, max_length=50, blank=True, null=True)
    entrance = models.CharField(choices=entrance_choices, max_length=50, blank=True, null=True)
    accessibility_parking = models.CharField(choices=accessibility_parking_choices, max_length=50, blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    video = models.TextField(blank=True, null=True)
    nudist_beach = models.CharField(choices=nudist_beach_choices, max_length=50, blank=True, null=True)
    dog_swimming = models.CharField(choices=dog_swimming_choices, max_length=50, blank=True, null=True)










