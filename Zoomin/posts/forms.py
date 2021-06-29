from django import forms
from posts.models import Newpost

class Newpostform(forms.ModelForm):
    class Meta:
        model = Newpost
        fields = '__all__'
