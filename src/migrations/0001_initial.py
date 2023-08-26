# Generated by Django 4.2.4 on 2023-08-24 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapotic_id', models.CharField(max_length=50)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('name', models.CharField(max_length=200)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('image_url', models.URLField()),
                ('import_id', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=300)),
                ('web', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('refreshment', models.CharField(choices=[('no_restaurant', 'No restaurant'), ('restaurant_on_site', 'Restaurant on site')], max_length=20)),
                ('diving', models.CharField(choices=[('not_suitable', 'Not suitable for diving'), ('suitable', 'Suitable for diving')], max_length=20)),
                ('entrance', models.CharField(choices=[('no_fee', 'No entrance fee'), ('fee', 'Entrance fee')], max_length=20)),
                ('accessibility_parking', models.CharField(choices=[('very_close', 'Very Close'), ('100m', '100 m'), ('250m', '250 m'), ('500m', '500 m'), ('1000m', '1000 m'), ('1000m_plus', '1000 m +')], max_length=20)),
                ('link', models.URLField()),
                ('video', models.URLField()),
                ('nudist_beach', models.CharField(choices=[('not_suitable', 'Not suitable for nudists'), ('suitable', 'Suitable for nudists')], max_length=20)),
                ('dog_swimming', models.CharField(choices=[('suitable', 'Suitable for dogs'), ('not_suitable', 'Not suitable for dogs')], max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='src.category')),
            ],
        ),
    ]
