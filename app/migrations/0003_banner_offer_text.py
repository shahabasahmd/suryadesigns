# Generated by Django 5.0.1 on 2024-02-19 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='offer_text',
            field=models.CharField(default='', max_length=100),
        ),
    ]