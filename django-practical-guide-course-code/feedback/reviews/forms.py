from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField()
#     review_text = forms.CharField(widget=forms.Textarea)
#     rating = forms.IntegerField(min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'review_text', 'rating']
        labels = {
            'user_name': 'Hello world'
        }
