"""Zoomin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from .decorators import staff_required
from accounts import views

admin.site.login = staff_required(admin.site.login)

urlpatterns = [

    url('admin/', admin.site.urls),

    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^blog/$',views.AboutView.as_view(),name='blog'),
    url(r'^account/',include('accounts.urls',namespace='accounts')),
    url(r'^accounts/',include("django.contrib.auth.urls")),
    url(r'posts/',include('posts.urls',namespace='posts')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
