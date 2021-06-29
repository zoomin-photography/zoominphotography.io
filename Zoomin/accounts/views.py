from django.contrib.auth import login,logout
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import Http404
from functools import wraps
from django.views.generic import TemplateView,CreateView
from . import forms

class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'blog.html'

class Signup(CreateView):
    form_class = forms.UserCreateform
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'

def staff_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            return func(request, *args, **kwargs)
        raise Http404()
    return wrapper
