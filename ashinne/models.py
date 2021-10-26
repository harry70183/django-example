from django.db import models
from django import forms
from django.contrib.auth import authenticate
# Create your models here.
class Category(models.Model):
    product_type = models.CharField(max_length=20)
    
    def __str__(self):
        return self.product_type

class Mission(models.Model):
    module_id = models.CharField(max_length=10)
    answer = models.DecimalField(max_digits=4, decimal_places=0)
    product_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.module_id
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
    
    
    
    
    
    