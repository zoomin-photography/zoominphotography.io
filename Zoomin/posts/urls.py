from django.conf.urls import url
from posts import views

app_name = 'posts'

urlpatterns = [
    url(r'^gallery/$',views.display_images,name='display'),
    url(r'^newposts/$',views.NewPost.as_view(),name='post'),
]
