from shop.models import Bikes
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from shop.models import Bikes


# from .models import *
from django import forms

# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

# class AddGroup(ModelForm):
#     class Meta:
#         model = CommodityGroup
#         fields = '__all__'


class AddBikes(ModelForm):
    class Meta:
        model = Bikes
        fields = '__all__'

# class AddPrice(ModelForm):
#     class Meta:
#         model = PriceDetails
#         fields = '__all__'
