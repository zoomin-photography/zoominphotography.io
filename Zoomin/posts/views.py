from django.shortcuts import render
from posts.models import Newpost
from posts.forms import Newpostform
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import CreateView
# Create your views here.


class NewPost(CreateView):
    model = Newpost
    fields = ['new_photo']
    def newpost(request):

        registered = False

        if user.is_superuser:

            if request.method == 'POST':
                New_post = Newpostform(data=request.POST)

                if New_post.is_valid():
                    post = New_post.save(commit=False)

                    if 'new_photo' in request.FILES:
                        print('found it')
                        post.New_post = request.FILES['new_photo']

                    New_post.save()

                    registered = True
                else:
                    print(Newpostform.erros)
            else:
                New_post = Newpostform
        return render(request,'posts/newpost_form.html',{'New_post : Newpostform'})


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'registration/login.html', {})

def display_images(request):

    if request.method == 'GET':

        Images = Newpost.objects.all()
        return render(request,'posts/display.html',{'images':Images})
