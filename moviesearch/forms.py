from django import forms


class MovieSearchForm(forms.Form):
    query = forms.CharField(label='Search Movie', max_length=100)
