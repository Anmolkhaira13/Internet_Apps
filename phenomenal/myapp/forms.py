from django import forms
from myapp.models import Order
from myapp.models import Product
from myapp.models import Client
from django.contrib.auth.models import User


class OrderForm(forms.Form):
    client = forms.ModelMultipleChoiceField(queryset=Client.objects.all(), widget=forms.RadioSelect(),
                                            label="Client Name")
    num_units = forms.IntegerField(label="Quantity")
    product = forms.ModelMultipleChoiceField(queryset=Product.objects.all())


class InterestForm(forms.Form):
    interested = forms.CharField(widget=forms.RadioSelect())
    quantity = forms.DecimalField(initial=1)
    comments = forms.CharField(widget=forms.Textarea(), label="Additional Comments", required=False)

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model =User
        fields =('username', 'email', 'password')
