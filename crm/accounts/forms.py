from django.forms import ModelForm
from .models import Customer, Order
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
    class Meta:
        model = Customer
        fileds = '__all__'
        exclude = ['user']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        # fields = ['customer', 'product'] if specific fields required

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 