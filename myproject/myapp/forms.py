from django import forms
from .models import UserProfile, UserBio, UserPost


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


select_gender = [('male', 'Male'),
                 ('female', 'Female'),
                 ('others', 'Others')]


class UserBioForm(forms.ModelForm):
    dob = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.CharField(widget=forms.RadioSelect(choices=select_gender))

    class Meta:
        model = UserBio
        fields = ['f_name', 'l_name', 'dob', 'phone', 'gender', 'country']


class UserPostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'write something here..'}))

    class Meta:
        model = UserPost
        fields = ['title', 'image']
