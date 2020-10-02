# Generated by Django 3.0.5 on 2020-10-02 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('brand_name', models.CharField(max_length=60)),
                ('regular_price_value', models.IntegerField(default=0)),
                ('offer_price_value', models.IntegerField(default=0)),
                ('currency', models.CharField(max_length=10)),
                ('classification_l1', models.CharField(max_length=20)),
                ('classification_l2', models.CharField(max_length=20)),
                ('classification_l3', models.CharField(max_length=20)),
            ],
        ),
    ]