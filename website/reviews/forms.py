from django import forms


from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Ваш отзыв'}),
            'rating': forms.NumberInput(attrs={'placeholder': 'Ваша оценка'}),
        }