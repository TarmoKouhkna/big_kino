from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']
        widgets = {
            'review_text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your review...'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 10}),
        }
