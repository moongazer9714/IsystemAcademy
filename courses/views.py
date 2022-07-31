from django.shortcuts import redirect, render

# Create your views here.

from django.shortcuts import render, HttpResponse
from .models import Contact, Course


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def courses(request):
    posts = Course.objects.filter(is_published=True)
    context = {
        'posts': posts
    }
    return render(request, 'courses.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('contact')

    return render(request, 'contact.html', {})


def courses_detail(request, slug):
    post = Course.objects.get(slug=slug)
    context = {
        'post': post
    }
    return render(request, 'courses_detail.html', context)
