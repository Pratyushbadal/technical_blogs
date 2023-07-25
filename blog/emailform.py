from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=100,
                             widget=forms.EmailInput(attrs={"class": "form-control"}))
    message = forms.CharField(label="Message", max_length=1000,
                              widget=forms.Textarea(attrs={"class": "form-control"}))

