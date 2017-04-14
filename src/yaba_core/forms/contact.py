from django import forms
from captcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    error_css_class = 'has-error'
    name = forms.CharField(label='Your Name:', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Your E-mail:', max_length=75,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Your Message:', max_length=800,
                              widget=forms.Textarea(attrs={'class': 'form-control'}))
    captcha = ReCaptchaField()
