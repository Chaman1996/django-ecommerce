# Generated by Django 3.1 on 2020-09-16 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contactmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='message',
            field=models.TextField(),
        ),
    ]