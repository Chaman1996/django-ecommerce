# Generated by Django 3.1 on 2020-09-19 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20200919_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='alt',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
