from django import forms


class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    zipcode = forms.CharField(max_length=100)
    place = forms.CharField(max_length=100)
    stripe_token = forms.CharField(max_length=255)
