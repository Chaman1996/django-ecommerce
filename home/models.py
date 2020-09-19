from __future__ import unicode_literals
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
from django.forms import ModelForm, TextInput, Textarea


class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )

    title = models.CharField(max_length=100, blank=True)
    keywords = models.TextField(default='-')
    description = RichTextUploadingField()
    schema = models.TextField(default="-")
    company = models.CharField(max_length=220, blank=True)
    address = models.TextField(default="-")
    phone = models.CharField(max_length=12, blank=True)
    fax = models.CharField(max_length=12, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    smtpserver = models.CharField(max_length=100, blank=True)
    smtpemail = models.CharField(max_length=100, blank=True)
    smtppassword = models.CharField(max_length=100, blank=True)
    smtpport = models.CharField(max_length=100, blank=True)
    icon = models.ImageField(upload_to='images/', blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    youtube = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    aboutus = RichTextUploadingField()
    contact = RichTextUploadingField()
    references = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    creat_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed')
    )

    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(max_length=20, blank=True)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Name & surename'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'email'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'subject'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'message'}),
        }
