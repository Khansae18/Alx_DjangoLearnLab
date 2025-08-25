from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=200, strip=True)
    author = forms.CharField(max_length=200, strip=True)
    published_date = forms.DateField(
        required=False,
        input_formats=["%Y-%m-%d"],  # YYYY-MM-DD
    )

class SearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=False, strip=True)
