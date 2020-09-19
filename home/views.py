from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

from product.models import Category, Product
from .models import Setting, ContactForm, ContactMessage


# Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    page = 'home'
    products_slider = Product.objects.all().order_by('id')[:4]  # slider product
    products_latest = Product.objects.all().order_by('-id')[:4]  # latest product
    products_picked = Product.objects.all().order_by('?')[:4]  # random product

    context = {
        'setting': setting,
        'page': page,
        'category': category,
        'products_slider': products_slider,
        'products_latest': products_latest,
        'products_picked': products_picked,
    }
    return render(request, 'index.html', context)


def about(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {
        'setting': setting,
        'category': category,
    }
    return render(request, 'aboutus.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.subject = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "your message has been submitted")
            return redirect('contact')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactForm
    context = {
        'setting': setting,
        'form': form,
        'category': category,
    }
    return render(request, 'contact.html', context)


def category_products(request, id, slug):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)

    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'category_products.html', context)
