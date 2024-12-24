# Generated by Django 5.1.4 on 2024-12-19 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzaImage', models.ImageField(upload_to='pizzahut/images/')),
                ('pizzaName', models.CharField(max_length=100)),
                ('pizzaPrice', models.IntegerField()),
                ('pizzaDescription', models.TextField()),
                ('pizzaOffer', models.BooleanField(default=False)),
                ('pizzaOfferPrice', models.IntegerField(default=0)),
                ('pizzaRetting', models.FloatField(default=0)),
                ('SizeList', models.CharField(choices=[('Small', 'Pizza Small'), ('Medium', 'Pizza Medium'), ('Large', 'Pizza Large')], max_length=100)),
                ('pizzaType', models.CharField(choices=[('veg', 'veg'), ('nonveg', 'nonveg')], max_length=10)),
                ('pizzaKcal', models.IntegerField()),
            ],
        ),
    ]
