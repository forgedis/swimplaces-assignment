# Generated by Django 4.2.4 on 2023-08-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='accessibility_parking',
            field=models.CharField(blank=True, choices=[('very_close', 'Very Close'), ('100m', '100 m'), ('250m', '250 m'), ('500m', '500 m'), ('1000m', '1000 m'), ('1000m_plus', '1000 m +')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='diving',
            field=models.CharField(blank=True, choices=[('not_suitable', 'Not suitable for diving'), ('suitable', 'Suitable for diving')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='dog_swimming',
            field=models.CharField(blank=True, choices=[('suitable', 'Suitable for dogs'), ('not_suitable', 'Not suitable for dogs')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='entrance',
            field=models.CharField(blank=True, choices=[('no_fee', 'No entrance fee'), ('fee', 'Entrance fee')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='image_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='import_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=18, max_digits=500),
        ),
        migrations.AlterField(
            model_name='location',
            name='link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(decimal_places=18, max_digits=500),
        ),
        migrations.AlterField(
            model_name='location',
            name='mapotic_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='nudist_beach',
            field=models.CharField(blank=True, choices=[('not_suitable', 'Not suitable for nudists'), ('suitable', 'Suitable for nudists')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='rating',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='refreshment',
            field=models.CharField(blank=True, choices=[('no_restaurant', 'No restaurant'), ('restaurant_on_site', 'Restaurant on site')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='video',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='web',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
    ]
