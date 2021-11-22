from django import forms
from myapp.models import Order
from myapp.models import Product
from myapp.models import Client


class OrderForm(forms.Form):
    client = forms.ModelMultipleChoiceField(queryset=Client.objects.all(), widget=forms.RadioSelect(),
                                            label="Client Name")
    num_units = forms.IntegerField(label="Quantity")
    product = forms.ModelMultipleChoiceField(queryset=Product.objects.all())


class InterestForm(forms.Form):
    interested = forms.CharField(widget=forms.RadioSelect())
    quantity = forms.DecimalField(initial=1)
    comments = forms.CharField(widget=forms.Textarea(), label="Additional Comments", required=False)
