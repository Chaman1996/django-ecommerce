# Generated by Django 3.1 on 2020-09-16 02:39

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('keywords', models.TextField(default='-')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('company', models.CharField(blank=True, max_length=220)),
                ('address', models.TextField(default='-')),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('fax', models.CharField(blank=True, max_length=12)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('smtpserver', models.CharField(blank=True, max_length=100)),
                ('smtpemail', models.CharField(blank=True, max_length=100)),
                ('smtppassword', models.CharField(blank=True, max_length=100)),
                ('smtpport', models.CharField(blank=True, max_length=100)),
                ('icon', models.ImageField(blank=True, upload_to='images/')),
                ('facebook', models.CharField(blank=True, max_length=100)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('youtube', models.CharField(blank=True, max_length=100)),
                ('twitter', models.CharField(blank=True, max_length=100)),
                ('aboutus', ckeditor_uploader.fields.RichTextUploadingField()),
                ('contact', ckeditor_uploader.fields.RichTextUploadingField()),
                ('references', ckeditor_uploader.fields.RichTextUploadingField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('creat_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
